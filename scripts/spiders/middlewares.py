class CustomHeadersMiddleware:
    def process_request(self, request, spider):
        request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        request.headers['Accept-Language'] = 'en-US,en;q=0.5'
        return None