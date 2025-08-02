# =============================================================================
# SECTION 1: DEPENDENCIES & SETUP
# =============================================================================
import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import html2text
import re

# This script requires external libraries. Ensure they are installed:
# pip install requests beautifulsoup4 lxml html2text

# --- Custom Logger ---
try:
    from logger import setup_logger
    logger = setup_logger('web_scraper')
except ImportError:
    import logging
    logger = logging.getLogger('web_scraper_fallback')
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# =============================================================================
# SECTION 2: CORE SCRAPING LOGIC & HELPERS
# =============================================================================

def _send_progress(percent, message):
    """Sends a JSON progress update to stdout."""
    progress_data = json.dumps({"progress": {"percent": percent, "message": message}})
    print(progress_data, flush=True)

def _fetch_url(url, stream=False):
    """Fetches content from a URL with appropriate headers."""
    logger.info(f"Fetching URL: {url}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=15, stream=stream)
        response.raise_for_status()
        logger.info(f"Successfully fetched {url} with status {response.status_code}")
        return response, None
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch {url}. Error: {e}")
        return None, str(e)

def _html_to_markdown(html_content):
    """Converts HTML content to clean Markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    return h.handle(html_content)

def _get_valid_filename(url_or_domain, is_domain=False):
    """Creates a valid filename or directory name."""
    name = re.sub(r'^https?://', '', url_or_domain)
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    if not is_domain:
        name += ".md"
    return name

# =============================================================================
# SECTION 3: ADAPTER FUNCTIONS (Called by script_router.py)
# =============================================================================

# --- PREVIOUS ADAPTERS (scrape_page_to_markdown, etc.) ---
# These functions remain the same as the previous version. For brevity, they are omitted here.
# You should keep them in your actual file.

def scrape_page_to_markdown_adapter(payload, output_dir):
    """
    Adapter for scraping a single web page to a Markdown file.
    Payload: {"url": "http://example.com"}
    """
    url = payload.get('url')
    logger.info(f"Starting scrape_page_to_markdown for URL: {url}")
    if not url:
        logger.error("No URL provided in payload.")
        return {"error": "No URL provided in payload.", "coins_used": 0}

    _send_progress(25, f"Fetching content from {url}...")
    response, error = _fetch_url(url)
    if error:
        return {"error": f"Failed to fetch URL: {error}", "coins_used": 0}

    _send_progress(50, "Converting HTML to Markdown...")
    markdown_content = _html_to_markdown(response.text)
    filename = _get_valid_filename(url)
    filepath = os.path.join(output_dir, filename)

    try:
        _send_progress(75, f"Saving file as {filename}...")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        logger.info(f"Successfully saved scraped content to {filepath}")
        _send_progress(100, "Scraping complete!")
        return {"message": f"Successfully scraped '{url}' to '{filename}'", "coins_used": 0}
    except IOError as e:
        logger.error(f"Failed to write file {filepath}. Error: {e}")
        return {"error": f"Failed to write file: {str(e)}", "coins_used": 0}

def scrape_sitemap_to_markdown_adapter(payload, output_dir):
    """
    Adapter for scraping all URLs from a sitemap.xml to Markdown files.
    Payload: {"sitemap_url": "http://example.com/sitemap.xml"}
    """
    sitemap_url = payload.get('sitemap_url')
    logger.info(f"Starting scrape_sitemap_to_markdown for sitemap: {sitemap_url}")
    if not sitemap_url:
        logger.error("No sitemap URL provided.")
        return {"error": "No sitemap URL provided.", "coins_used": 0}

    response, error = _fetch_url(sitemap_url)
    if error:
        return {"error": f"Failed to fetch sitemap: {error}", "coins_used": 0}

    soup = BeautifulSoup(response.text, 'lxml-xml')
    urls = [loc.text for loc in soup.find_all('loc')]
    total_urls = len(urls)
    logger.info(f"Found {total_urls} URLs in sitemap.")

    if not urls:
        return {"error": "No URLs found in the sitemap.", "coins_used": 0}

    scraped_count = 0
    errors = []
    for i, url in enumerate(urls):
        percent_complete = int(((i + 1) / total_urls) * 100)
        _send_progress(percent_complete, f"Scraping {i+1}/{total_urls}: {url}")

        page_response, fetch_error = _fetch_url(url)
        if fetch_error:
            errors.append(f"Failed to fetch {url}: {fetch_error}")
            continue

        markdown_content = _html_to_markdown(page_response.text)
        filename = _get_valid_filename(url)
        filepath = os.path.join(output_dir, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            scraped_count += 1
        except IOError as e:
            logger.error(f"Failed to write file for {url}. Error: {e}")
            errors.append(f"Failed to write file for {url}: {str(e)}")

    logger.info(f"Sitemap processing finished. Scraped {scraped_count}/{total_urls} pages.")
    return {
        "message": f"Sitemap processing complete. Successfully scraped {scraped_count}/{total_urls} pages.",
        "errors": errors,
        "coins_used": 0
    }

def download_files_from_url_adapter(payload, output_dir):
    """
    Adapter for finding and downloading files of a specific type from a page.
    Payload: {"url": "http://example.com", "file_type": "pdf"}
    """
    url = payload.get('url')
    file_type = payload.get('file_type', '').lower()
    logger.info(f"Starting download_files_from_url for page: {url}, file type: {file_type}")
    if not url or not file_type:
        return {"error": "URL and file_type must be provided.", "coins_used": 0}

    response, error = _fetch_url(url)
    if error:
        return {"error": f"Failed to fetch page: {error}", "coins_used": 0}

    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].lower().endswith(f'.{file_type}')]
    total_links = len(links)
    logger.info(f"Found {total_links} links for file type '.{file_type}'")

    if not links:
        return {"message": f"No '.{file_type}' files found on the page.", "coins_used": 0}

    downloaded_count = 0
    errors = []
    for i, link in enumerate(links):
        percent_complete = int(((i + 1) / total_links) * 100)
        file_url = urljoin(url, link)
        _send_progress(percent_complete, f"Downloading {i+1}/{total_links}: {os.path.basename(file_url)}")

        filename = os.path.basename(urlparse(file_url).path)
        filepath = os.path.join(output_dir, filename)
        
        try:
            logger.info(f"Downloading from {file_url} to {filepath}")
            file_response, fetch_error = _fetch_url(file_url, stream=True)
            if fetch_error:
                raise requests.exceptions.RequestException(fetch_error)
            
            with open(filepath, 'wb') as f:
                for chunk in file_response.iter_content(chunk_size=8192):
                    f.write(chunk)
            downloaded_count += 1
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to download {file_url}. Error: {e}")
            errors.append(f"Failed to download {file_url}: {str(e)}")

    logger.info(f"File download finished. Downloaded {downloaded_count}/{total_links} files.")
    return {
        "message": f"File download complete. Successfully downloaded {downloaded_count}/{len(links)} files.",
        "errors": errors,
        "coins_used": 0
    }

def download_website_adapter(payload, output_dir):
    """
    Downloads a single webpage along with its CSS and images for local viewing.
    Payload: {"url": "http://example.com"}
    """
    url = payload.get('url')
    if not url:
        return {"error": "No URL provided.", "coins_used": 0}

    logger.info(f"Starting website download for {url}")
    _send_progress(5, "Creating site directory...")

    # Create a dedicated directory for the site
    site_name = _get_valid_filename(urlparse(url).netloc, is_domain=True)
    site_dir = os.path.join(output_dir, site_name)
    css_dir = os.path.join(site_dir, 'css')
    img_dir = os.path.join(site_dir, 'img')
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(img_dir, exist_ok=True)

    _send_progress(10, "Fetching main HTML page...")
    response, error = _fetch_url(url)
    if error:
        return {"error": f"Failed to fetch main page: {error}", "coins_used": 0}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Download CSS
    _send_progress(30, "Downloading CSS files...")
    for link in soup.find_all('link', rel='stylesheet'):
        css_url = urljoin(url, link['href'])
        css_filename = os.path.basename(urlparse(css_url).path)
        css_filepath = os.path.join(css_dir, css_filename)
        try:
            css_response, _ = _fetch_url(css_url)
            if css_response:
                with open(css_filepath, 'w', encoding='utf-8') as f:
                    f.write(css_response.text)
                # Rewrite link in HTML
                link['href'] = f'css/{css_filename}'
        except Exception as e:
            logger.warn(f"Could not download CSS {css_url}: {e}")

    # Download Images
    _send_progress(60, "Downloading images...")
    for img in soup.find_all('img'):
        img_url = urljoin(url, img['src'])
        img_filename = os.path.basename(urlparse(img_url).path)
        img_filepath = os.path.join(img_dir, img_filename)
        try:
            img_response, _ = _fetch_url(img_url, stream=True)
            if img_response:
                with open(img_filepath, 'wb') as f:
                    for chunk in img_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                # Rewrite src in HTML
                img['src'] = f'img/{img_filename}'
        except Exception as e:
            logger.warn(f"Could not download image {img_url}: {e}")

    # Save the modified HTML
    _send_progress(95, "Saving modified HTML file...")
    index_path = os.path.join(site_dir, 'index.html')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(str(soup.prettify()))

    _send_progress(100, "Website download complete!")
    logger.info(f"Website download finished for {url}. Saved in {site_dir}")
    return {"message": f"Website snapshot saved to folder: {site_name}", "coins_used": 0}
