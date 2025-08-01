Scrapy Documentation
Release 2.13.3
Scrapy developers
Jul 02, 2025



FIRST STEPS
1 Gettinghelp 3
2 Firststeps 5
2.1 Scrapyataglance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Installationguide . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.3 ScrapyTutorial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3 Basicconcepts 23
3.1 Commandlinetool . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.2 Spiders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.3 Selectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.4 Items . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.5 ItemLoaders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
3.6 Scrapyshell. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.7 ItemPipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
3.8 Feedexports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90
3.9 RequestsandResponses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.10 LinkExtractors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
3.11 Settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
3.12 Exceptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
4 Built-inservices 161
4.1 Logging. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 161
4.2 StatsCollection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
4.3 Sendinge-mail . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
4.4 TelnetConsole . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
5 Solvingspecificproblems 175
5.1 FrequentlyAskedQuestions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
5.2 DebuggingSpiders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
5.3 SpidersContracts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
5.4 CommonPractices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
5.5 BroadCrawls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
5.6 Usingyourbrowser’sDeveloperToolsforscraping . . . . . . . . . . . . . . . . . . . . . . . . . . . 194
5.7 Selectingdynamically-loadedcontent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
5.8 Debuggingmemoryleaks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 202
5.9 Downloadingandprocessingfilesandimages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206
5.10 DeployingSpiders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
5.11 AutoThrottleextension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
i

5.12 Benchmarking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
5.13 Jobs: pausingandresumingcrawls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
5.14 Coroutines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
5.15 asyncio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227
6 ExtendingScrapy 233
6.1 Architectureoverview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
6.2 Add-ons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
6.3 DownloaderMiddleware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
6.4 SpiderMiddleware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254
6.5 Extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
6.6 Signals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
6.7 Scheduler . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
6.8 ItemExporters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
6.9 Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
6.10 CoreAPI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287
7 Alltherest 299
7.1 Releasenotes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299
7.2 ContributingtoScrapy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398
7.3 VersioningandAPIstability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 403
PythonModuleIndex 405
Index 407
ii

ScrapyDocumentation,Release2.13.3
Scrapyisafasthigh-levelwebcrawlingandwebscrapingframework,usedtocrawlwebsitesandextractstructureddata
fromtheirpages. Itcanbeusedforawiderangeofpurposes,fromdataminingtomonitoringandautomatedtesting.
FIRSTSTEPS 1

ScrapyDocumentation,Release2.13.3
2 FIRSTSTEPS

CHAPTER
ONE
GETTING HELP
Havingtrouble? We’dliketohelp!
• TrytheFAQ–it’sgotanswerstosomecommonquestions.
• Lookingforspecificinformation? Trythegenindexormodindex.
• AskorsearchquestionsinStackOverflowusingthescrapytag.
• AskorsearchquestionsintheScrapysubreddit.
• Searchforquestionsonthearchivesofthescrapy-usersmailinglist.
• Askaquestioninthe#scrapyIRCchannel,
• ReportbugswithScrapyinourissuetracker.
• JointheDiscordcommunityScrapyDiscord.
3

ScrapyDocumentation,Release2.13.3
4 Chapter1. Gettinghelp

CHAPTER
TWO
FIRST STEPS
2.1 Scrapy at a glance
Scrapy(/skrepa/)isanapplicationframeworkforcrawlingwebsitesandextractingstructureddatawhichcanbeused
forawiderangeofusefulapplications,likedatamining,informationprocessingorhistoricalarchival.
EventhoughScrapywasoriginallydesignedforwebscraping,itcanalsobeusedtoextractdatausingAPIs(suchas
AmazonAssociatesWebServices)orasageneralpurposewebcrawler.
2.1.1 Walk-through of an example spider
InordertoshowyouwhatScrapybringstothetable,we’llwalkyouthroughanexampleofaScrapySpiderusingthe
simplestwaytorunaspider.
Here’sthecodeforaspiderthatscrapesfamousquotesfromwebsitehttps://quotes.toscrape.com,followingthepagi-
nation:
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes"
start_urls = [
"https://quotes.toscrape.com/tag/humor/",
]
def parse(self, response):
for quote in response.css("div.quote"):
yield {
"author": quote.xpath("span/small/text()").get(),
"text": quote.css("span.text::text").get(),
}
next_page = response.css('li.next a::attr("href")').get()
if next_page is not None:
yield response.follow(next_page, self.parse)
Putthisinatextfile,nameitsomethinglikequotes_spider.pyandrunthespiderusingtherunspidercommand:
scrapy runspider quotes_spider.py -o quotes.jsonl
Whenthisfinishesyouwillhaveinthequotes.jsonlfilealistofthequotesinJSONLinesformat,containingthe
textandauthor,whichwilllooklikethis:
5

ScrapyDocumentation,Release2.13.3
{"author": "Jane Austen", "text": "\u201cThe person, be it gentleman or lady, who has␣
not pleasure in a good novel, must be intolerably stupid.\u201d"}
˓→
{"author": "Steve Martin", "text": "\u201cA day without sunshine is like, you know,␣
night.\u201d"}
˓→
{"author": "Garrison Keillor", "text": "\u201cAnyone who thinks sitting in church can␣
make you a Christian must also think that sitting in a garage can make you a car.\u201d
˓→
"}
˓→
...
Whatjusthappened?
Whenyouranthecommandscrapy runspider quotes_spider.py,ScrapylookedforaSpiderdefinitioninside
itandranitthroughitscrawlerengine.
The crawl started by making requests to the URLs defined in the start_urls attribute (in this case, only the URL
for quotes in the humor category) and called the default callback method parse, passing the response object as an
argument. Intheparsecallback,weloopthroughthequoteelementsusingaCSSSelector,yieldaPythondictwith
theextractedquotetextandauthor,lookforalinktothenextpageandscheduleanotherrequestusingthesameparse
methodascallback.
Here you will notice one of the main advantages of Scrapy: requests are scheduled and processed asynchronously.
ThismeansthatScrapydoesn’tneedtowaitforarequesttobefinishedandprocessed,itcansendanotherrequestor
dootherthingsinthemeantime. Thisalsomeansthatotherrequestscankeepgoingevenifarequestfailsoranerror
happenswhilehandlingit.
Whilethisenablesyoutodoveryfastcrawls(sendingmultipleconcurrentrequestsatthesametime,inafault-tolerant
way) Scrapy also gives you control over the politeness of the crawl through a few settings. You can do things like
settingadownloaddelaybetweeneachrequest,limitingtheamountofconcurrentrequestsperdomainorperIP,and
evenusinganauto-throttlingextensionthattriestofigurethesesettingsoutautomatically.
(cid:242) Note
This is using feed exports to generate theJSON file, you can easilychange the export format (XMLor CSV, for
example)orthestoragebackend(FTPorAmazonS3,forexample). Youcanalsowriteanitempipelinetostore
theitemsinadatabase.
2.1.2 What else?
You’veseenhowtoextractandstoreitemsfromawebsiteusingScrapy,butthisisjustthesurface. Scrapyprovidesa
lotofpowerfulfeaturesformakingscrapingeasyandefficient,suchas:
• Built-insupportforselectingandextractingdatafromHTML/XMLsourcesusingextendedCSSselectorsand
XPathexpressions,withhelpermethodsforextractionusingregularexpressions.
• Aninteractiveshellconsole(IPythonaware)fortryingouttheCSSandXPathexpressionstoscrapedata,which
isveryusefulwhenwritingordebuggingyourspiders.
• Built-insupportforgeneratingfeedexportsinmultipleformats(JSON,CSV,XML)andstoringtheminmultiple
backends(FTP,S3,localfilesystem)
• Robustencodingsupportandauto-detection,fordealingwithforeign,non-standardandbrokenencodingdecla-
rations.
• Strongextensibilitysupport,allowingyoutopluginyourownfunctionalityusingsignalsandawell-definedAPI
(middlewares,extensions,andpipelines).
• Awiderangeofbuilt-inextensionsandmiddlewaresforhandling:
6 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
– cookiesandsessionhandling
– HTTPfeatureslikecompression,authentication,caching
– user-agentspoofing
– robots.txt
– crawldepthrestriction
– andmore
• ATelnetconsoleforhookingintoaPythonconsolerunninginsideyourScrapyprocess,tointrospectanddebug
yourcrawler
• Plus other goodies like reusable spiders to crawl sites from Sitemaps and XML/CSV feeds, a media pipeline
forautomaticallydownloadingimages(oranyothermedia)associatedwiththescrapeditems,acachingDNS
resolver,andmuchmore!
2.1.3 What’s next?
ThenextstepsforyouaretoinstallScrapy,followthroughthetutorialtolearnhowtocreateafull-blownScrapyproject
andjointhecommunity. Thanksforyourinterest!
2.2 Installation guide
2.2.1 Supported Python versions
ScrapyrequiresPython3.9+,eithertheCPythonimplementation(default)orthePyPyimplementation(seeAlternate
Implementations).
2.2.2 Installing Scrapy
Ifyou’reusingAnacondaorMiniconda,youcaninstallthepackagefromtheconda-forgechannel,whichhasup-to-date
packagesforLinux,WindowsandmacOS.
ToinstallScrapyusingconda,run:
conda install -c conda-forge scrapy
Alternatively,ifyou’realreadyfamiliarwithinstallationofPythonpackages,youcaninstallScrapyanditsdependencies
fromPyPIwith:
pip install Scrapy
WestronglyrecommendthatyouinstallScrapyinadedicatedvirtualenv,toavoidconflictingwithyoursystempack-
ages.
Note that sometimes this may require solving compilation issues for some Scrapy dependencies depending on your
operatingsystem,sobesuretocheckthePlatformspecificinstallationnotes.
Formoredetailedandplatform-specificinstructions,aswellastroubleshootinginformation,readon.
Thingsthataregoodtoknow
ScrapyiswritteninpurePythonanddependsonafewkeyPythonpackages(amongothers):
• lxml,anefficientXMLandHTMLparser
• parsel,anHTML/XMLdataextractionlibrarywrittenontopoflxml,
2.2. Installationguide 7

ScrapyDocumentation,Release2.13.3
• w3lib,amulti-purposehelperfordealingwithURLsandwebpageencodings
• twisted,anasynchronousnetworkingframework
• cryptographyandpyOpenSSL,todealwithvariousnetwork-levelsecurityneeds
Some of these packages themselves depend on non-Python packages that might require additional installation steps
dependingonyourplatform. Pleasecheckplatform-specificguidesbelow.
Incaseofanytroublerelatedtothesedependencies,pleaserefertotheirrespectiveinstallationinstructions:
• lxmlinstallation
• cryptographyinstallation
Usingavirtualenvironment(recommended)
TL;DR:WerecommendinstallingScrapyinsideavirtualenvironmentonallplatforms.
Pythonpackagescanbeinstalledeitherglobally(a.k.asystemwide),orinuser-space. Wedonotrecommendinstalling
Scrapysystemwide.
Instead,werecommendthatyouinstallScrapywithinaso-called“virtualenvironment”(venv). Virtualenvironments
allowyoutonotconflictwithalready-installedPythonsystempackages(whichcouldbreaksomeofyoursystemtools
andscripts),andstillinstallpackagesnormallywithpip(withoutsudoandthelikes).
SeeVirtualEnvironmentsandPackagesonhowtocreateyourvirtualenvironment.
Once you have created a virtual environment, you can install Scrapy inside it with pip, just like any other Python
package. (Seeplatform-specificguidesbelowfornon-Pythondependenciesthatyoumayneedtoinstallbeforehand).
2.2.3 Platform specific installation notes
Windows
Thoughit’spossibletoinstallScrapyonWindowsusingpip,werecommendyouinstallAnacondaorMinicondaand
usethepackagefromtheconda-forgechannel,whichwillavoidmostinstallationissues.
Onceyou’veinstalledAnacondaorMiniconda,installScrapywith:
conda install -c conda-forge scrapy
ToinstallScrapyonWindowsusingpip:
. Warning
Thisinstallationmethodrequires“MicrosoftVisualC++”forinstallingsomeScrapydependencies,whichdemands
significantlymorediskspacethanAnaconda.
1. DownloadandexecuteMicrosoftC++BuildToolstoinstalltheVisualStudioInstaller.
2. RuntheVisualStudioInstaller.
3. UndertheWorkloadssection,selectC++buildtools.
4. Checktheinstallationdetailsandmakesurefollowingpackagesareselectedasoptionalcomponents:
• MSVC(e.gMSVCv142-VS2019C++x64/x86buildtools(v14.23))
• WindowsSDK(e.gWindows10SDK(10.0.18362.0))
5. InstalltheVisualStudioBuildTools.
8 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
Now,youshouldbeabletoinstallScrapyusingpip.
Ubuntu14.04orabove
Scrapyiscurrentlytestedwithrecent-enoughversionsoflxml,twistedandpyOpenSSL,andiscompatiblewithrecent
Ubuntudistributions. ButitshouldsupportolderversionsofUbuntutoo,likeUbuntu14.04,albeitwithpotentialissues
withTLSconnections.
Don’tusethepython-scrapypackageprovidedbyUbuntu,theyaretypicallytoooldandslowtocatchupwiththe
latestScrapyrelease.
ToinstallScrapyonUbuntu(orUbuntu-based)systems,youneedtoinstallthesedependencies:
sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev␣
libffi-dev libssl-dev
˓→
• python3-dev,zlib1g-dev,libxml2-devandlibxslt1-devarerequiredforlxml
• libssl-devandlibffi-devarerequiredforcryptography
Insideavirtualenv,youcaninstallScrapywithpipafterthat:
pip install scrapy
(cid:242) Note
Thesamenon-PythondependenciescanbeusedtoinstallScrapyinDebianJessie(8.0)andabove.
macOS
Building Scrapy’s dependencies requires the presence of a C compiler and development headers. On macOS this is
typically provided by Apple’s Xcode development tools. To install the Xcode command-line tools, open a terminal
windowandrun:
xcode-select --install
There’s a known issue that prevents pip from updating system packages. This has to be addressed to successfully
installScrapyanditsdependencies. Herearesomeproposedsolutions:
• (Recommended)Don’t usesystemPython. Installanew, updatedversionthatdoesn’tconflictwiththerestof
yoursystem. Here’showtodoitusingthehomebrewpackagemanager:
– Installhomebrewfollowingtheinstructionsinhttps://brew.sh/
– UpdateyourPATHvariabletostatethathomebrewpackagesshouldbeusedbeforesystempackages(Change
.bashrcto.zshrcaccordinglyifyou’reusingzshasdefaultshell):
echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bashrc
– Reload.bashrctoensurethechangeshavetakenplace:
source ~/.bashrc
– Installpython:
brew install python
• (Optional)InstallScrapyinsideaPythonvirtualenvironment.
2.2. Installationguide 9

ScrapyDocumentation,Release2.13.3
ThismethodisaworkaroundfortheabovemacOSissue, butit’sanoverallgoodpracticeformanaging
dependenciesandcancomplementthefirstmethod.
AfteranyoftheseworkaroundsyoushouldbeabletoinstallScrapy:
pip install Scrapy
PyPy
WerecommendusingthelatestPyPyversion. ForPyPy3,onlyLinuxinstallationwastested.
MostScrapydependenciesnowhavebinarywheelsforCPython,butnotforPyPy. Thismeansthatthesedependencies
willbebuiltduringinstallation. OnmacOS,youarelikelytofaceanissuewithbuildingtheCryptographydependency.
The solution to this problem is described here, that is to brew install openssl and then export the flags that
this command recommends (only needed when installing Scrapy). Installing on Linux has no special issues besides
installingbuilddependencies. InstallingScrapywithPyPyonWindowsisnottested.
You can check that Scrapy is installed correctly by running scrapy bench. If this command gives errors such as
TypeError: ... got 2 unexpected keyword arguments, thismeansthatsetuptoolswasunabletopickup
onePyPy-specificdependency. Tofixthisissue,runpip install 'PyPyDispatcher>=2.1.0'.
2.2.4 Troubleshooting
AttributeError: ‘module’objecthasnoattribute‘OP_NO_TLSv1_1’
AfteryouinstallorupgradeScrapy,TwistedorpyOpenSSL,youmaygetanexceptionwiththefollowingtraceback:
[...]
File "[...]/site-packages/twisted/protocols/tls.py", line 63, in <module>
from twisted.internet._sslverify import _setAcceptableProtocols
File "[...]/site-packages/twisted/internet/_sslverify.py", line 38, in <module>
TLSVersion.TLSv1_1: SSL.OP_NO_TLSv1_1,
AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'
The reason you get this exception is that your system or virtual environment has a version of pyOpenSSL that your
versionofTwisteddoesnotsupport.
ToinstallaversionofpyOpenSSLthatyourversionofTwistedsupports,reinstallTwistedwiththetlsextraoption:
pip install twisted[tls]
Fordetails,seeIssue#2473.
2.3 Scrapy Tutorial
In this tutorial, we’ll assume that Scrapy is already installed on your system. If that’s not the case, see Installation
guide.
Wearegoingtoscrapequotes.toscrape.com,awebsitethatlistsquotesfromfamousauthors.
Thistutorialwillwalkyouthroughthesetasks:
1. CreatinganewScrapyproject
2. Writingaspidertocrawlasiteandextractdata
3. Exportingthescrapeddatausingthecommandline
4. Changingspidertorecursivelyfollowlinks
10 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
5. Usingspiderarguments
ScrapyiswritteninPython. ThemoreyoulearnaboutPython,themoreyoucangetoutofScrapy.
Ifyou’realreadyfamiliarwithotherlanguagesandwanttolearnPythonquickly,thePythonTutorialisagoodresource.
Ifyou’renewtoprogrammingandwanttostartwithPython,thefollowingbooksmaybeusefultoyou:
• AutomatetheBoringStuffWithPython
• HowToThinkLikeaComputerScientist
• LearnPython3TheHardWay
YoucanalsotakealookatthislistofPythonresourcesfornon-programmers,aswellasthesuggestedresourcesinthe
learnpython-subreddit.
2.3.1 Creating a project
Beforeyoustartscraping,youwillhavetosetupanewScrapyproject. Enteradirectorywhereyou’dliketostoreyour
codeandrun:
scrapy startproject tutorial
Thiswillcreateatutorialdirectorywiththefollowingcontents:
tutorial/
scrapy.cfg # deploy configuration file
tutorial/ # project's Python module, you'll import your code from here
__init__.py
items.py # project items definition file
middlewares.py # project middlewares file
pipelines.py # project pipelines file
settings.py # project settings file
spiders/ # a directory where you'll later put your spiders
__init__.py
2.3.2 Our first Spider
SpidersareclassesthatyoudefineandthatScrapyusestoscrapeinformationfromawebsite(oragroupofwebsites).
TheymustsubclassSpideranddefinetheinitialrequeststobemade,andoptionally,howtofollowlinksinpagesand
parsethedownloadedpagecontenttoextractdata.
This is the code for our first Spider. Save it in a file named quotes_spider.py under the tutorial/spiders
directoryinyourproject:
from pathlib import Path
import scrapy
class QuotesSpider(scrapy.Spider):
(continuesonnextpage)
2.3. ScrapyTutorial 11

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
name = "quotes"
async def start(self):
urls = [
"https://quotes.toscrape.com/page/1/",
"https://quotes.toscrape.com/page/2/",
]
for url in urls:
yield scrapy.Request(url=url, callback=self.parse)
def parse(self, response):
page = response.url.split("/")[-2]
filename = f"quotes-{page}.html"
Path(filename).write_bytes(response.body)
self.log(f"Saved file {filename}")
Asyoucansee,ourSpidersubclassesscrapy.Spideranddefinessomeattributesandmethods:
• name: identifiestheSpider. Itmustbeuniquewithinaproject,thatis,youcan’tsetthesamenamefordifferent
Spiders.
• start(): mustbeanasynchronousgeneratorthatyieldsrequests(and,optionally,items)forthespidertostart
crawling. Subsequentrequestswillbegeneratedsuccessivelyfromtheseinitialrequests.
• parse(): amethodthatwillbecalledtohandletheresponsedownloadedforeachoftherequestsmade. The
responseparameterisaninstanceofTextResponsethatholdsthepagecontentandhasfurtherhelpfulmethods
tohandleit.
Theparse()methodusuallyparsestheresponse,extractingthescrapeddataasdictsandalsofindingnewURLs
tofollowandcreatingnewrequests(Request)fromthem.
Howtorunourspider
Toputourspidertowork,gototheproject’stopleveldirectoryandrun:
scrapy crawl quotes
This command runs the spider named quotes that we’ve just added, that will send some requests for the quotes.
toscrape.comdomain. Youwillgetanoutputsimilartothis:
... (omitted for brevity)
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Spider opened
2016-12-16 21:24:05 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min),␣
scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:24:05 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.
0.1:6023
˓→
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://quotes.
toscrape.com/robots.txt> (referer: None)
˓→
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.
toscrape.com/page/1/> (referer: None)
˓→
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.
toscrape.com/page/2/> (referer: None)
˓→
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-1.html
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-2.html
(continuesonnextpage)
12 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Closing spider (finished)
...
Now, checkthefilesinthecurrentdirectory. Youshouldnoticethattwonewfileshavebeencreated: quotes-1.html
andquotes-2.html,withthecontentfortherespectiveURLs,asourparsemethodinstructs.
(cid:242) Note
Ifyouarewonderingwhywehaven’tparsedtheHTMLyet,holdon,wewillcoverthatsoon.
Whatjusthappenedunderthehood?
Scrapysendsthefirstscrapy.Request objectsyieldedbythestart()spidermethod. Uponreceivingaresponse
for each one, Scrapy calls the callback method associated with the request (in this case, the parse method) with a
Responseobject.
Ashortcuttothestartmethod
Insteadofimplementingastart()methodthatyieldsRequest objectsfromURLs,youcandefineastart_urls
classattributewithalistofURLs. Thislistwillthenbeusedbythedefaultimplementationofstart()tocreatethe
initialrequestsforyourspider.
from pathlib import Path
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes"
start_urls = [
"https://quotes.toscrape.com/page/1/",
"https://quotes.toscrape.com/page/2/",
]
def parse(self, response):
page = response.url.split("/")[-2]
filename = f"quotes-{page}.html"
Path(filename).write_bytes(response.body)
Theparse()methodwillbecalledtohandleeachoftherequestsforthoseURLs,eventhoughwehaven’texplicitly
toldScrapytodoso. Thishappensbecauseparse()isScrapy’sdefaultcallbackmethod,whichiscalledforrequests
withoutanexplicitlyassignedcallback.
Extractingdata
ThebestwaytolearnhowtoextractdatawithScrapyistryingselectorsusingtheScrapyshell. Run:
scrapy shell 'https://quotes.toscrape.com/page/1/'
(cid:242) Note
2.3. ScrapyTutorial 13

ScrapyDocumentation,Release2.13.3
RemembertoalwaysencloseURLsinquoteswhenrunningScrapyshellfromthecommandline,otherwiseURLs
containingarguments(i.e. &character)willnotwork.
OnWindows,usedoublequotesinstead:
scrapy shell "https://quotes.toscrape.com/page/1/"
Youwillseesomethinglike:
[ ... Scrapy log here ... ]
2016-09-19 12:09:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.
toscrape.com/page/1/> (referer: None)
˓→
[s] Available Scrapy objects:
[s] scrapy scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s] crawler <scrapy.crawler.Crawler object at 0x7fa91d888c90>
[s] item {}
[s] request <GET https://quotes.toscrape.com/page/1/>
[s] response <200 https://quotes.toscrape.com/page/1/>
[s] settings <scrapy.settings.Settings object at 0x7fa91d888c10>
[s] spider <DefaultSpider 'default' at 0x7fa91c8af990>
[s] Useful shortcuts:
[s] shelp() Shell help (print this help)
[s] fetch(req_or_url) Fetch request (or URL) and update local objects
[s] view(response) View response in a browser
Usingtheshell,youcantryselectingelementsusingCSSwiththeresponseobject:
>>> response.css("title")
[<Selector query='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]
Theresultofrunningresponse.css('title')isalist-likeobjectcalledSelectorList,whichrepresentsalistof
SelectorobjectsthatwraparoundXML/HTMLelementsandallowyoutorunfurtherqueriestorefinetheselection
orextractthedata.
Toextractthetextfromthetitleabove,youcando:
>>> response.css("title::text").getall()
['Quotes to Scrape']
Therearetwothingstonotehere: oneisthatwe’veadded::texttotheCSSquery,tomeanwewanttoselectonlythe
textelementsdirectlyinside<title>element. Ifwedon’tspecify::text,we’dgetthefulltitleelement,including
itstags:
>>> response.css("title").getall()
['<title>Quotes to Scrape</title>']
Theotherthingisthattheresultofcalling.getall()isalist: itispossiblethataselectorreturnsmorethanoneresult,
soweextractthemall. Whenyouknowyoujustwantthefirstresult,asinthiscase,youcando:
>>> response.css("title::text").get()
'Quotes to Scrape'
Asanalternative,youcould’vewritten:
14 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
>>> response.css("title::text")[0].get()
'Quotes to Scrape'
AccessinganindexonaSelectorListinstancewillraiseanIndexErrorexceptioniftherearenoresults:
>>> response.css("noelement")[0].get()
Traceback (most recent call last):
...
IndexError: list index out of range
You might want to use .get() directly on the SelectorList instance instead, which returns None if there are no
results:
>>> response.css("noelement").get()
There’salessonhere: formostscrapingcode,youwantittoberesilienttoerrorsduetothingsnotbeingfoundona
page,sothatevenifsomepartsfailtobescraped,youcanatleastgetsomedata.
Besidesthegetall()andget()methods,youcanalsousethere()methodtoextractusingregularexpressions:
>>> response.css("title::text").re(r"Quotes.*")
['Quotes to Scrape']
>>> response.css("title::text").re(r"Q\w+")
['Quotes']
>>> response.css("title::text").re(r"(\w+) to (\w+)")
['Quotes', 'Scrape']
InordertofindtheproperCSSselectorstouse,youmightfinditusefultoopentheresponsepagefromtheshellinyour
webbrowserusingview(response). Youcanuseyourbrowser’sdevelopertoolstoinspecttheHTMLandcomeup
withaselector(seeUsingyourbrowser’sDeveloperToolsforscraping).
SelectorGadgetisalsoanicetooltoquicklyfindCSSselectorforvisuallyselectedelements, whichworksinmany
browsers.
XPath: abriefintro
BesidesCSS,ScrapyselectorsalsosupportusingXPathexpressions:
>>> response.xpath("//title")
[<Selector query='//title' data='<title>Quotes to Scrape</title>'>]
>>> response.xpath("//title/text()").get()
'Quotes to Scrape'
XPathexpressionsareverypowerful,andarethefoundationofScrapySelectors. Infact,CSSselectorsareconverted
toXPathunder-the-hood. Youcanseethatifyoureadthetextrepresentationoftheselectorobjectsintheshellclosely.
While perhaps not as popular as CSS selectors, XPath expressions offer more power because besides navigating the
structure,itcanalsolookatthecontent. UsingXPath,you’reabletoselectthingslike: thelinkthatcontainsthetext
“NextPage”. ThismakesXPathveryfittingtothetaskofscraping,andweencourageyoutolearnXPathevenifyou
alreadyknowhowtoconstructCSSselectors,itwillmakescrapingmucheasier.
Wewon’tcovermuchofXPathhere,butyoucanreadmoreaboutusingXPathwithScrapySelectorshere. Tolearn
moreaboutXPath,werecommendthistutorialtolearnXPaththroughexamples,andthistutorialtolearn“howtothink
inXPath”.
2.3. ScrapyTutorial 15

ScrapyDocumentation,Release2.13.3
Extractingquotesandauthors
Now that you know a bit about selection and extraction, let’s complete our spider by writing the code to extract the
quotesfromthewebpage.
Eachquoteinhttps://quotes.toscrape.comisrepresentedbyHTMLelementsthatlooklikethis:
<div class="quote">
<span class="text">“The world as we have created it is a process of our
thinking. It cannot be changed without changing our thinking.”</span>
<span>
by <small class="author">Albert Einstein</small>
<a href="/author/Albert-Einstein">(about)</a>
</span>
<div class="tags">
Tags:
<a class="tag" href="/tag/change/page/1/">change</a>
<a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
<a class="tag" href="/tag/thinking/page/1/">thinking</a>
<a class="tag" href="/tag/world/page/1/">world</a>
</div>
</div>
Let’sopenupscrapyshellandplayabittofindouthowtoextractthedatawewant:
scrapy shell 'https://quotes.toscrape.com'
WegetalistofselectorsforthequoteHTMLelementswith:
>>> response.css("div.quote")
[<Selector query="descendant-or-self::div[@class and contains(concat(' ', normalize-
space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
˓→
<Selector query="descendant-or-self::div[@class and contains(concat(' ', normalize-
space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
˓→
...]
Eachoftheselectorsreturnedbythequeryaboveallowsustorunfurtherqueriesovertheirsub-elements. Let’sassign
thefirstselectortoavariable,sothatwecanrunourCSSselectorsdirectlyonaparticularquote:
>>> quote = response.css("div.quote")[0]
Now,let’sextractthetext,authorandtagsfromthatquoteusingthequoteobjectwejustcreated:
>>> text = quote.css("span.text::text").get()
>>> text
'“The world as we have created it is a process of our thinking. It cannot be changed␣
without changing our thinking.”'
˓→
>>> author = quote.css("small.author::text").get()
>>> author
'Albert Einstein'
Giventhatthetagsarealistofstrings,wecanusethe.getall()methodtogetallofthem:
>>> tags = quote.css("div.tags a.tag::text").getall()
>>> tags
['change', 'deep-thoughts', 'thinking', 'world']
16 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
Havingfiguredouthowtoextracteachbit,wecannowiterateoverallthequoteelementsandputthemtogetherintoa
Pythondictionary:
>>> for quote in response.css("div.quote"):
... text = quote.css("span.text::text").get()
... author = quote.css("small.author::text").get()
... tags = quote.css("div.tags a.tag::text").getall()
... print(dict(text=text, author=author, tags=tags))
...
{'text': '“The world as we have created it is a process of our thinking. It cannot be␣
changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags': ['change
˓→
', 'deep-thoughts', 'thinking', 'world']}
˓→
{'text': '“It is our choices, Harry, that show what we truly are, far more than our␣
abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
˓→
...
Extractingdatainourspider
Let’sgetbacktoourspider. Untilnow,ithasn’textractedanydatainparticular,justsavingthewholeHTMLpageto
alocalfile. Let’sintegratetheextractionlogicaboveintoourspider.
AScrapyspidertypicallygeneratesmanydictionariescontainingthedataextractedfromthepage. Todothat,weuse
theyieldPythonkeywordinthecallback,asyoucanseebelow:
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes"
start_urls = [
"https://quotes.toscrape.com/page/1/",
"https://quotes.toscrape.com/page/2/",
]
def parse(self, response):
for quote in response.css("div.quote"):
yield {
"text": quote.css("span.text::text").get(),
"author": quote.css("small.author::text").get(),
"tags": quote.css("div.tags a.tag::text").getall(),
}
Torunthisspider,exitthescrapyshellbyentering:
quit()
Then,run:
scrapy crawl quotes
Now,itshouldoutputtheextracteddatawiththelog:
2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.
toscrape.com/page/1/>
˓→
{'tags': ['life', 'love'], 'author': 'André Gide', 'text': '“It is better to be hated␣
(continuesonnextpage)
2.3. ScrapyTutorial 17

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
for what you are than to be loved for what you are not.”'}
˓→
2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 https://quotes.
toscrape.com/page/1/>
˓→
{'tags': ['edison', 'failure', 'inspirational', 'paraphrased'], 'author': 'Thomas A.␣
Edison', 'text': "“I have not failed. I've just found 10,000 ways that won't work.”"}
˓→
2.3.3 Storing the scraped data
ThesimplestwaytostorethescrapeddataisbyusingFeedexports,withthefollowingcommand:
scrapy crawl quotes -O quotes.json
Thatwillgenerateaquotes.jsonfilecontainingallscrapeditems,serializedinJSON.
The -Ocommand-lineswitchoverwritesanyexistingfile; use -oinsteadtoappendnewcontenttoanyexistingfile.
However,appendingtoaJSONfilemakesthefilecontentsinvalidJSON.Whenappendingtoafile,considerusinga
differentserializationformat,suchasJSONLines:
scrapy crawl quotes -o quotes.jsonl
TheJSONLinesformatisusefulbecauseit’sstream-like,soyoucaneasilyappendnewrecordstoit. Itdoesn’thavethe
sameproblemasJSONwhenyouruntwice. Also,aseachrecordisaseparateline,youcanprocessbigfileswithout
havingtofiteverythinginmemory,therearetoolslikeJQtohelpdothatatthecommand-line.
Insmallprojects(liketheoneinthistutorial),thatshouldbeenough. However,ifyouwanttoperformmorecomplex
thingswith thescrapeditems, you canwritean ItemPipeline. Aplaceholder fileforItemPipelines hasbeenset up
for you when the project is created, in tutorial/pipelines.py. Though you don’t need to implement any item
pipelinesifyoujustwanttostorethescrapeditems.
2.3.4 Following links
Let’ssay,insteadofjustscrapingthestufffromthefirsttwopagesfromhttps://quotes.toscrape.com,youwantquotes
fromallthepagesinthewebsite.
Nowthatyouknowhowtoextractdatafrompages,let’sseehowtofollowlinksfromthem.
Thefirstthingtodoisextractthelinktothepagewewanttofollow. Examiningourpage,wecanseethereisalinkto
thenextpagewiththefollowingmarkup:
<ul class="pager">
<li class="next">
<a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
</li>
</ul>
Wecantryextractingitintheshell:
>>> response.css('li.next a').get()
'<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'
Thisgetstheanchorelement,butwewanttheattributehref. Forthat,ScrapysupportsaCSSextensionthatletsyou
selecttheattributecontents,likethis:
>>> response.css("li.next a::attr(href)").get()
'/page/2/'
18 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
Thereisalsoanattribpropertyavailable(seeSelectingelementattributesformore):
>>> response.css("li.next a").attrib["href"]
'/page/2/'
Nowlet’sseeourspider,modifiedtorecursivelyfollowthelinktothenextpage,extractingdatafromit:
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes"
start_urls = [
"https://quotes.toscrape.com/page/1/",
]
def parse(self, response):
for quote in response.css("div.quote"):
yield {
"text": quote.css("span.text::text").get(),
"author": quote.css("small.author::text").get(),
"tags": quote.css("div.tags a.tag::text").getall(),
}
next_page = response.css("li.next a::attr(href)").get()
if next_page is not None:
next_page = response.urljoin(next_page)
yield scrapy.Request(next_page, callback=self.parse)
Now,afterextractingthedata,theparse()methodlooksforthelinktothenextpage,buildsafullabsoluteURLusing
theurljoin()method(sincethelinkscanberelative)andyieldsanewrequesttothenextpage,registeringitselfas
callbacktohandlethedataextractionforthenextpageandtokeepthecrawlinggoingthroughallthepages.
WhatyouseehereisScrapy’smechanismoffollowinglinks: whenyouyieldaRequestinacallbackmethod,Scrapy
willschedulethatrequesttobesentandregisteracallbackmethodtobeexecutedwhenthatrequestfinishes.
Usingthis,youcanbuildcomplexcrawlersthatfollowlinksaccordingtorulesyoudefine,andextractdifferentkinds
ofdatadependingonthepageit’svisiting.
Inourexample, itcreatesasortofloop, followingallthelinkstothenextpageuntilitdoesn’tfindone–handyfor
crawlingblogs,forumsandothersiteswithpagination.
AshortcutforcreatingRequests
AsashortcutforcreatingRequestobjectsyoucanuseresponse.follow:
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes"
start_urls = [
"https://quotes.toscrape.com/page/1/",
]
def parse(self, response):
(continuesonnextpage)
2.3. ScrapyTutorial 19

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
for quote in response.css("div.quote"):
yield {
"text": quote.css("span.text::text").get(),
"author": quote.css("span small::text").get(),
"tags": quote.css("div.tags a.tag::text").getall(),
}
next_page = response.css("li.next a::attr(href)").get()
if next_page is not None:
yield response.follow(next_page, callback=self.parse)
Unlike scrapy.Request, response.follow supports relative URLs directly - no need to call urljoin. Note that
response.followjustreturnsaRequestinstance;youstillhavetoyieldthisRequest.
Youcanalsopassaselectortoresponse.followinsteadofastring;thisselectorshouldextractnecessaryattributes:
for href in response.css("ul.pager a::attr(href)"):
yield response.follow(href, callback=self.parse)
For <a>elementsthereisashortcut: response.followusestheirhrefattributeautomatically. Sothecodecanbe
shortenedfurther:
for a in response.css("ul.pager a"):
yield response.follow(a, callback=self.parse)
Tocreatemultiplerequestsfromaniterable,youcanuseresponse.follow_allinstead:
anchors = response.css("ul.pager a")
yield from response.follow_all(anchors, callback=self.parse)
or,shorteningitfurther:
yield from response.follow_all(css="ul.pager a", callback=self.parse)
Moreexamplesandpatterns
Hereisanotherspiderthatillustratescallbacksandfollowinglinks,thistimeforscrapingauthorinformation:
import scrapy
class AuthorSpider(scrapy.Spider):
name = "author"
start_urls = ["https://quotes.toscrape.com/"]
def parse(self, response):
author_page_links = response.css(".author + a")
yield from response.follow_all(author_page_links, self.parse_author)
pagination_links = response.css("li.next a")
yield from response.follow_all(pagination_links, self.parse)
(continuesonnextpage)
20 Chapter2. Firststeps

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
def parse_author(self, response):
def extract_with_css(query):
return response.css(query).get(default="").strip()
yield {
"name": extract_with_css("h3.author-title::text"),
"birthdate": extract_with_css(".author-born-date::text"),
"bio": extract_with_css(".author-description::text"),
}
Thisspiderwillstartfromthemainpage, itwillfollowallthelinkstotheauthorspagescallingthe parse_author
callbackforeachofthem,andalsothepaginationlinkswiththeparsecallbackaswesawbefore.
Here we’re passing callbacks to response.follow_all as positional arguments to make the code shorter; it also
worksforRequest.
Theparse_authorcallbackdefinesahelperfunctiontoextractandcleanupthedatafromaCSSqueryandyieldsthe
Pythondictwiththeauthordata.
Anotherinterestingthingthisspiderdemonstratesisthat,eveniftherearemanyquotesfromthesameauthor,wedon’t
needtoworryaboutvisitingthesameauthorpagemultipletimes. Bydefault,Scrapyfiltersoutduplicatedrequeststo
URLsalreadyvisited,avoidingtheproblemofhittingserverstoomuchbecauseofaprogrammingmistake. Thiscan
beconfiguredintheDUPEFILTER_CLASS setting.
Hopefullybynowyouhaveagoodunderstandingofhowtousethemechanismoffollowinglinksandcallbackswith
Scrapy.
Asyetanotherexamplespiderthatleveragesthemechanismoffollowinglinks,checkouttheCrawlSpiderclassfor
agenericspiderthatimplementsasmallrulesenginethatyoucanusetowriteyourcrawlersontopofit.
Also,acommonpatternistobuildanitemwithdatafrommorethanonepage,usingatricktopassadditionaldatato
thecallbacks.
2.3.5 Using spider arguments
Youcanprovidecommandlineargumentstoyourspidersbyusingthe-aoptionwhenrunningthem:
scrapy crawl quotes -O quotes-humor.json -a tag=humor
TheseargumentsarepassedtotheSpider’s__init__methodandbecomespiderattributesbydefault.
Inthisexample, thevalueprovidedforthe tagargumentwillbeavailablevia self.tag. Youcanusethistomake
yourspiderfetchonlyquoteswithaspecifictag,buildingtheURLbasedontheargument:
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes"
async def start(self):
url = "https://quotes.toscrape.com/"
tag = getattr(self, "tag", None)
if tag is not None:
url = url + "tag/" + tag
yield scrapy.Request(url, self.parse)
(continuesonnextpage)
2.3. ScrapyTutorial 21

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
def parse(self, response):
for quote in response.css("div.quote"):
yield {
"text": quote.css("span.text::text").get(),
"author": quote.css("small.author::text").get(),
}
next_page = response.css("li.next a::attr(href)").get()
if next_page is not None:
yield response.follow(next_page, self.parse)
Ifyoupassthetag=humorargumenttothisspider,you’llnoticethatitwillonlyvisitURLsfromthehumortag,such
ashttps://quotes.toscrape.com/tag/humor.
Youcanlearnmoreabouthandlingspiderargumentshere.
2.3.6 Next steps
ThistutorialcoveredonlythebasicsofScrapy,butthere’salotofotherfeaturesnotmentionedhere. ChecktheWhat
else? sectionintheScrapyataglancechapterforaquickoverviewofthemostimportantones.
YoucancontinuefromthesectionBasicconceptstoknowmoreaboutthecommand-linetool,spiders,selectorsand
otherthingsthetutorialhasn’tcoveredlikemodelingthescrapeddata. Ifyou’dprefertoplaywithanexampleproject,
checktheExamplessection.
2.4 Examples
The best way to learn is with examples, and Scrapy is no exception. For this reason, there is an example Scrapy
project named quotesbot, that you can use to play and learn more about Scrapy. It contains two spiders for https:
//quotes.toscrape.com,oneusingCSSselectorsandanotheroneusingXPathexpressions.
Thequotesbotprojectisavailableat: https://github.com/scrapy/quotesbot. Youcanfindmoreinformationaboutitin
theproject’sREADME.
Ifyou’refamiliarwithgit,youcancheckoutthecode. Otherwiseyoucandownloadtheprojectasazipfilebyclicking
here.
Scrapyataglance
UnderstandwhatScrapyisandhowitcanhelpyou.
Installationguide
GetScrapyinstalledonyourcomputer.
ScrapyTutorial
WriteyourfirstScrapyproject.
Examples
Learnmorebyplayingwithapre-madeScrapyproject.
22 Chapter2. Firststeps

CHAPTER
THREE
BASIC CONCEPTS
3.1 Command line tool
Scrapyiscontrolledthroughthescrapycommand-linetool,tobereferredtohereasthe“Scrapytool”todifferentiate
itfromthesub-commands,whichwejustcall“commands”or“Scrapycommands”.
TheScrapytoolprovidesseveralcommands,formultiplepurposes,andeachoneacceptsadifferentsetofarguments
andoptions.
(Thescrapy deploycommandhasbeenremovedin1.0infavorofthestandalonescrapyd-deploy. SeeDeploying
yourproject.)
3.1.1 Configuration settings
Scrapywilllookforconfigurationparametersinini-stylescrapy.cfgfilesinstandardlocations:
1. /etc/scrapy.cfgorc:\scrapy\scrapy.cfg(system-wide),
2. ~/.config/scrapy.cfg($XDG_CONFIG_HOME)and~/.scrapy.cfg($HOME)forglobal(user-wide)settings,
and
3. scrapy.cfginsideaScrapyproject’sroot(seenextsection).
Settings from these files are merged in the listed order of preference: user-defined values have higher priority than
system-widedefaultsandproject-widesettingswilloverrideallothers,whendefined.
Scrapyalsounderstands,andcanbeconfiguredthrough,anumberofenvironmentvariables. Currentlytheseare:
• SCRAPY_SETTINGS_MODULE(seeDesignatingthesettings)
• SCRAPY_PROJECT(seeSharingtherootdirectorybetweenprojects)
• SCRAPY_PYTHON_SHELL(seeScrapyshell)
3.1.2 Default structure of Scrapy projects
Before delving into the command-line tool and its sub-commands, let’s first understand the directory structure of a
Scrapyproject.
Thoughitcanbemodified,allScrapyprojectshavethesamefilestructurebydefault,similartothis:
scrapy.cfg
myproject/
__init__.py
items.py
middlewares.py
pipelines.py
(continuesonnextpage)
23

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
settings.py
spiders/
__init__.py
spider1.py
spider2.py
...
Thedirectorywherethescrapy.cfgfileresidesisknownastheprojectrootdirectory. Thatfilecontainsthenameof
thepythonmodulethatdefinestheprojectsettings. Hereisanexample:
[settings]
default = myproject.settings
3.1.3 Sharing the root directory between projects
Aprojectrootdirectory,theonethatcontainsthescrapy.cfg,maybesharedbymultipleScrapyprojects,eachwith
itsownsettingsmodule.
Inthatcase,youmustdefineoneormorealiasesforthosesettingsmodulesunder[settings]inyourscrapy.cfg
file:
[settings]
default = myproject1.settings
project1 = myproject1.settings
project2 = myproject2.settings
By default, the scrapy command-line tool will use the default settings. Use the SCRAPY_PROJECT environment
variabletospecifyadifferentprojectforscrapytouse:
$ scrapy settings --get BOT_NAME
Project 1 Bot
$ export SCRAPY_PROJECT=project2
$ scrapy settings --get BOT_NAME
Project 2 Bot
3.1.4 Using the scrapy tool
YoucanstartbyrunningtheScrapytoolwithnoargumentsanditwillprintsomeusagehelpandtheavailablecom-
mands:
Scrapy X.Y - no active project
Usage:
scrapy <command> [options] [args]
Available commands:
crawl Run a spider
fetch Fetch a URL using the Scrapy downloader
[...]
Thefirstlinewillprintthecurrentlyactiveprojectifyou’reinsideaScrapyproject. Inthisexampleitwasrunfrom
outsideaproject. Ifrunfrominsideaprojectitwouldhaveprintedsomethinglikethis:
24 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Scrapy X.Y - project: myproject
Usage:
scrapy <command> [options] [args]
[...]
Creatingprojects
ThefirstthingyoutypicallydowiththescrapytooliscreateyourScrapyproject:
scrapy startproject myproject [project_dir]
ThatwillcreateaScrapyprojectundertheproject_dirdirectory. If project_dirwasn’tspecified,project_dir
willbethesameasmyproject.
Next,yougoinsidethenewprojectdirectory:
cd project_dir
Andyou’rereadytousethescrapycommandtomanageandcontrolyourprojectfromthere.
Controllingprojects
Youusethescrapytoolfrominsideyourprojectstocontrolandmanagethem.
Forexample,tocreateanewspider:
scrapy genspider mydomain mydomain.com
SomeScrapycommands(likecrawl)mustberunfrominsideaScrapyproject. Seethecommandsreferencebelow
formoreinformationonwhichcommandsmustberunfrominsideprojects,andwhichnot.
Alsokeepinmindthatsomecommandsmayhaveslightlydifferentbehaviourswhenrunningthemfrominsideprojects.
Forexample,thefetchcommandwillusespider-overriddenbehaviours(suchastheuser_agentattributetooverride
theuser-agent)iftheurlbeingfetchedisassociatedwithsomespecificspider. Thisisintentional,asthefetchcom-
mandismeanttobeusedtocheckhowspidersaredownloadingpages.
3.1.5 Available tool commands
Thissectioncontainsalistoftheavailablebuilt-incommandswithadescriptionandsomeusageexamples. Remember,
youcanalwaysgetmoreinfoabouteachcommandbyrunning:
scrapy <command> -h
Andyoucanseeallavailablecommandswith:
scrapy -h
Therearetwokindsofcommands,thosethatonlyworkfrominsideaScrapyproject(Project-specificcommands)and
thosethatalsoworkwithoutanactiveScrapyproject(Globalcommands),thoughtheymaybehaveslightlydifferently
whenrunfrominsideaproject(astheywouldusetheprojectoverriddensettings).
Globalcommands:
• startproject
• genspider
3.1. Commandlinetool 25

ScrapyDocumentation,Release2.13.3
• settings
• runspider
• shell
• fetch
• view
• version
Project-onlycommands:
• crawl
• check
• list
• edit
• parse
• bench
startproject
• Syntax: scrapy startproject <project_name> [project_dir]
• Requiresproject: no
Creates a new Scrapy project named project_name, under the project_dir directory. If project_dir wasn’t
specified,project_dirwillbethesameasproject_name.
Usageexample:
$ scrapy startproject myproject
genspider
• Syntax: scrapy genspider [-t template] <name> <domain or URL>
• Requiresproject: no
Addedinversion2.6.0: TheabilitytopassaURLinsteadofadomain.
Createsanewspiderinthecurrentfolderorinthecurrentproject’sspidersfolder,ifcalledfrominsideaproject. The
<name> parameter is set as the spider’s name, while <domain or URL> is used to generate the allowed_domains
andstart_urlsspider’sattributes.
Usageexample:
$ scrapy genspider -l
Available templates:
basic
crawl
csvfeed
xmlfeed
$ scrapy genspider example example.com
Created spider 'example' using template 'basic'
(continuesonnextpage)
26 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
$ scrapy genspider -t crawl scrapyorg scrapy.org
Created spider 'scrapyorg' using template 'crawl'
Thisisjustaconvenientshortcutcommandforcreatingspidersbasedonpre-definedtemplates,butcertainlynotthe
onlywaytocreatespiders. Youcanjustcreatethespidersourcecodefilesyourself,insteadofusingthiscommand.
crawl
• Syntax: scrapy crawl <spider>
• Requiresproject: yes
Startcrawlingusingaspider.
Supportedoptions:
• -h, --help: showahelpmessageandexit
• -a NAME=VALUE:setaspiderargument(mayberepeated)
• --output FILEor-o FILE:appendscrapeditemstotheendofFILE(use-forstdout). Todefinetheoutput
format,setacolonattheendoftheoutputURI(i.e. -o FILE:FORMAT)
• --overwrite-output FILE or -O FILE: dump scraped items into FILE, overwriting any existing file. To
definetheoutputformat,setacolonattheendoftheoutputURI(i.e. -O FILE:FORMAT)
Usageexamples:
$ scrapy crawl myspider
[ ... myspider starts crawling ... ]
$ scrapy crawl -o myfile:csv myspider
[ ... myspider starts crawling and appends the result to the file myfile in csv format ..
. ]
˓→
$ scrapy crawl -O myfile:json myspider
[ ... myspider starts crawling and saves the result in myfile in json format overwriting␣
the original content... ]
˓→
check
• Syntax: scrapy check [-l] <spider>
• Requiresproject: yes
Runcontractchecks.
Usageexamples:
$ scrapy check -l
first_spider
* parse
* parse_item
second_spider
* parse
* parse_item
$ scrapy check
(continuesonnextpage)
3.1. Commandlinetool 27

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
[FAILED] first_spider:parse_item
>>> 'RetailPricex' field is missing
[FAILED] first_spider:parse
>>> Returned 92 requests, expected 0..4
list
• Syntax: scrapy list
• Requiresproject: yes
Listallavailablespidersinthecurrentproject. Theoutputisonespiderperline.
Usageexample:
$ scrapy list
spider1
spider2
edit
• Syntax: scrapy edit <spider>
• Requiresproject: yes
EditthegivenspiderusingtheeditordefinedintheEDITORenvironmentvariableor(ifunset)theEDITOR setting.
Thiscommandisprovidedonlyasaconvenientshortcutforthemostcommoncase,thedeveloperisofcoursefreeto
chooseanytoolorIDEtowriteanddebugspiders.
Usageexample:
$ scrapy edit spider1
fetch
• Syntax: scrapy fetch <url>
• Requiresproject: no
DownloadsthegivenURLusingtheScrapydownloaderandwritesthecontentstostandardoutput.
Theinterestingthingaboutthiscommandisthatitfetchesthepagethewaythespiderwoulddownloadit. Forexample,
ifthespiderhasaUSER_AGENTattributewhichoverridestheUserAgent,itwillusethatone.
Sothiscommandcanbeusedto“see”howyourspiderwouldfetchacertainpage.
If used outside a project, no particular per-spider behaviour would be applied and it will just use the default Scrapy
downloadersettings.
Supportedoptions:
• --spider=SPIDER:bypassspiderautodetectionandforceuseofspecificspider
• --headers: printtheresponse’sHTTPheadersinsteadoftheresponse’sbody
• --no-redirect: donotfollowHTTP3xxredirects(defaultistofollowthem)
Usageexamples:
28 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
$ scrapy fetch --nolog http://www.example.com/some/page.html
[ ... html content here ... ]
$ scrapy fetch --nolog --headers http://www.example.com/
{'Accept-Ranges': ['bytes'],
'Age': ['1263 '],
'Connection': ['close '],
'Content-Length': ['596'],
'Content-Type': ['text/html; charset=UTF-8'],
'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
'Etag': ['"573c1-254-48c9c87349680"'],
'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
'Server': ['Apache/2.2.3 (CentOS)']}
view
• Syntax: scrapy view <url>
• Requiresproject: no
OpensthegivenURLinabrowser,asyourScrapyspiderwould“see”it. Sometimesspidersseepagesdifferentlyfrom
regularusers,sothiscanbeusedtocheckwhatthespider“sees”andconfirmit’swhatyouexpect.
Supportedoptions:
• --spider=SPIDER:bypassspiderautodetectionandforceuseofspecificspider
• --no-redirect: donotfollowHTTP3xxredirects(defaultistofollowthem)
Usageexample:
$ scrapy view http://www.example.com/some/page.html
[ ... browser starts ... ]
shell
• Syntax: scrapy shell [url]
• Requiresproject: no
StartstheScrapyshellforthegivenURL(ifgiven)oremptyifnoURLisgiven. AlsosupportsUNIX-stylelocalfile
paths,eitherrelativewith./or../prefixesorabsolutefilepaths. SeeScrapyshellformoreinfo.
Supportedoptions:
• --spider=SPIDER:bypassspiderautodetectionandforceuseofspecificspider
• -c code: evaluatethecodeintheshell,printtheresultandexit
• --no-redirect: donotfollowHTTP3xxredirects(defaultistofollowthem);thisonlyaffectstheURLyou
maypassasargumentonthecommandline;onceyouareinsidetheshell,fetch(url)willstillfollowHTTP
redirectsbydefault.
Usageexample:
$ scrapy shell http://www.example.com/some/page.html
[ ... scrapy shell starts ... ]
$ scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'
(continuesonnextpage)
3.1. Commandlinetool 29

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
(200, 'http://www.example.com/')
# shell follows HTTP redirects by default
$ scrapy shell --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c
'(response.status, response.url)'
˓→
(200, 'http://example.com/')
# you can disable this with --no-redirect
# (only for the URL passed as command line argument)
$ scrapy shell --no-redirect --nolog http://httpbin.org/redirect-to?url=http%3A%2F
%2Fexample.com%2F -c '(response.status, response.url)'
˓→
(302, 'http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F')
parse
• Syntax: scrapy parse <url> [options]
• Requiresproject: yes
Fetches the given URL and parses it with the spider that handles it, using the method passed with the --callback
option,orparseifnotgiven.
Supportedoptions:
• --spider=SPIDER:bypassspiderautodetectionandforceuseofspecificspider
• --a NAME=VALUE:setspiderargument(mayberepeated)
• --callbackor-c: spidermethodtouseascallbackforparsingtheresponse
• --meta or -m: additional request meta that will be passed to the callback request. This must be a valid json
string. Example: –meta=’{“foo”: “bar”}’
• --cbkwargs: additionalkeywordargumentsthatwillbepassedtothecallback. Thismustbeavalidjsonstring.
Example: –cbkwargs=’{“foo”: “bar”}’
• --pipelines: processitemsthroughpipelines
• --rules or -r: use CrawlSpider rules to discover the callback (i.e. spider method) to use for parsing the
response
• --noitems: don’tshowscrapeditems
• --nolinks: don’tshowextractedlinks
• --nocolour: avoidusingpygmentstocolorizetheoutput
• --depthor-d: depthlevelforwhichtherequestsshouldbefollowedrecursively(default: 1)
• --verboseor-v: displayinformationforeachdepthlevel
• --outputor-o: dumpscrapeditemstoafile
Addedinversion2.3.
Usageexample:
$ scrapy parse http://www.example.com/ -c parse_item
[ ... scrapy log lines crawling example.com spider ... ]
>>> STATUS DEPTH LEVEL 1 <<<
(continuesonnextpage)
30 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
# Scraped Items ------------------------------------------------------------
[{'name': 'Example item',
'category': 'Furniture',
'length': '12 cm'}]
# Requests -----------------------------------------------------------------
[]
settings
• Syntax: scrapy settings [options]
• Requiresproject: no
GetthevalueofaScrapysetting.
Ifusedinsideaprojectit’llshowtheprojectsettingvalue,otherwiseit’llshowthedefaultScrapyvalueforthatsetting.
Exampleusage:
$ scrapy settings --get BOT_NAME
scrapybot
$ scrapy settings --get DOWNLOAD_DELAY
0
runspider
• Syntax: scrapy runspider <spider_file.py>
• Requiresproject: no
Runaspiderself-containedinaPythonfile,withouthavingtocreateaproject.
Exampleusage:
$ scrapy runspider myspider.py
[ ... spider starts crawling ... ]
version
• Syntax: scrapy version [-v]
• Requiresproject: no
Prints the Scrapy version. If used with -v it also prints Python, Twisted and Platform info, which is useful for bug
reports.
bench
• Syntax: scrapy bench
• Requiresproject: no
Runaquickbenchmarktest. Benchmarking.
3.1. Commandlinetool 31

ScrapyDocumentation,Release2.13.3
3.1.6 Custom project commands
YoucanalsoaddyourcustomprojectcommandsbyusingtheCOMMANDS_MODULE setting. SeetheScrapycommands
inscrapy/commandsforexamplesonhowtoimplementyourcommands.
COMMANDS_MODULE
Default: '' (emptystring)
A module to use for looking up custom Scrapy commands. This is used to add custom commands for your Scrapy
project.
Example:
COMMANDS_MODULE = "mybot.commands"
Registercommandsviasetup.pyentrypoints
YoucanalsoaddScrapycommandsfromanexternallibrarybyaddingascrapy.commandssectionintheentrypoints
ofthelibrarysetup.pyfile.
Thefollowingexampleaddsmy_commandcommand:
from setuptools import setup, find_packages
setup(
name="scrapy-mymodule",
entry_points={
"scrapy.commands": [
"my_command=my_scrapy_module.commands:MyCommand",
],
},
)
3.2 Spiders
Spiders are classes which define how a certain site (or a group of sites) will be scraped, including how to perform
thecrawl(i.e. followlinks)andhowtoextractstructureddatafromtheirpages(i.e. scrapingitems). Inotherwords,
Spidersaretheplacewhereyoudefinethecustombehaviourforcrawlingandparsingpagesforaparticularsite(or,in
somecases,agroupofsites).
Forspiders,thescrapingcyclegoesthroughsomethinglikethis:
1. YoustartbygeneratingtheinitialrequeststocrawlthefirstURLs,andspecifyacallbackfunctiontobecalled
withtheresponsedownloadedfromthoserequests.
Thefirstrequeststoperformareobtainedbyiteratingthestart()method,whichbydefaultyieldsaRequest
objectforeachURLinthestart_urls spiderattribute,withtheparsemethodsetascallback functionto
handleeachResponse.
2. Inthecallbackfunction,youparsetheresponse(webpage)andreturnitemobjects,Requestobjects,oraniter-
ableoftheseobjects. ThoseRequestswillalsocontainacallback(maybethesame)andwillthenbedownloaded
byScrapyandthentheirresponsehandledbythespecifiedcallback.
3. Incallbackfunctions,youparsethepagecontents,typicallyusingSelectors(butyoucanalsouseBeautifulSoup,
lxmlorwhatevermechanismyouprefer)andgenerateitemswiththeparseddata.
32 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
4. Finally, the items returned from the spider will be typically persisted to a database (in some Item Pipeline) or
writtentoafileusingFeedexports.
Eventhoughthiscycleapplies(moreorless)toanykindofspider,therearedifferentkindsofdefaultspidersbundled
intoScrapyfordifferentpurposes. Wewilltalkaboutthosetypeshere.
3.2.1 scrapy.Spider
class scrapy.spiders.Spider
class scrapy.Spider(*args: Any,**kwargs: Any)
Baseclassthatanyspidermustsubclass.
Itprovidesadefaultstart()implementationthatsendsrequestsbasedonthestart_urlsclassattributeand
callstheparse()methodforeachresponse.
name
Astringwhichdefinesthenameforthisspider. Thespidernameishowthespiderislocated(andinstan-
tiated)byScrapy, soitmustbeunique. However, nothingpreventsyoufrominstantiatingmorethanone
instanceofthesamespider. Thisisthemostimportantspiderattributeandit’srequired.
Ifthespiderscrapesasingledomain, acommonpracticeistonamethespiderafterthedomain, withor
withouttheTLD.So,forexample,aspiderthatcrawlsmywebsite.comwouldoftenbecalledmywebsite.
allowed_domains
An optional list of strings containing domains that this spider is allowed to crawl. Requests for URLs
not belonging to the domain names specified in this list (or their subdomains) won’t be followed if
OffsiteMiddlewareisenabled.
Let’ssayyourtargeturlishttps://www.example.com/1.html,thenadd'example.com'tothelist.
start_urls: list[str]
StartURLs. Seestart().
custom_settings
A dictionary of settings that will be overridden from the project wide configuration when running this
spider. Itmustbedefinedasaclassattributesincethesettingsareupdatedbeforeinstantiation.
Foralistofavailablebuilt-insettingssee: Built-insettingsreference.
crawler
This attribute is set by the from_crawler() class method after initializing the class, and links to the
Crawlerobjecttowhichthisspiderinstanceisbound.
Crawlersencapsulatealotofcomponentsintheprojectfortheirsingleentryaccess(suchasextensions,
middlewares,signalsmanagers,etc). SeeCrawlerAPI toknowmoreaboutthem.
settings
Configuration for running this spider. This is a Settings instance, see the Settings topic for a detailed
introductiononthissubject.
logger
PythonloggercreatedwiththeSpider’sname. Youcanuseittosendlogmessagesthroughitasdescribed
onLoggingfromSpiders.
state
A dict you can use to persist some spider state between batches. See Keeping persistent state between
batchestoknowmoreaboutit.
3.2. Spiders 33

ScrapyDocumentation,Release2.13.3
from_crawler(crawler,*args,**kwargs)
ThisistheclassmethodusedbyScrapytocreateyourspiders.
Youprobablywon’tneedtooverridethisdirectlybecausethedefaultimplementationactsasaproxytothe
__init__()method,callingitwiththegivenargumentsargsandnamedargumentskwargs.
Nonetheless, this method sets the crawler and settings attributes in the new instance so they can be
accessedlaterinsidethespider’scode.
Changedinversion2.11: Thesettingsincrawler.settingscannowbemodifiedinthismethod,which
ishandyifyouwanttomodifythembasedonarguments. Asaconsequence,thesesettingsaren’tthefinal
valuesastheycanbemodifiedlaterbye.g. add-ons. Forthesamereason,mostoftheCrawlerattributes
aren’tinitializedatthispoint.
ThefinalsettingsandtheinitializedCrawlerattributesareavailableinthestart()method,handlersof
theengine_started signalandlater.
Parameters
• crawler(Crawlerinstance)–crawlertowhichthespiderwillbebound
• args(list)–argumentspassedtothe__init__()method
• kwargs(dict)–keywordargumentspassedtothe__init__()method
classmethod update_settings(settings)
Theupdate_settings()methodisusedtomodifythespider’ssettingsandiscalledduringinitialization
ofaspiderinstance.
IttakesaSettings objectasaparameterandcanaddorupdatethespider’sconfigurationvalues. This
methodisaclassmethod,meaningthatitiscalledontheSpiderclassandallowsallinstancesofthespider
tosharethesameconfiguration.
While per-spider settings can be set in custom_settings, using update_settings() allows you to
dynamicallyadd,removeorchangesettingsbasedonothersettings,spiderattributesorotherfactorsand
usesettingprioritiesotherthan'spider'. Also,it’seasytoextendupdate_settings()inasubclassby
overridingit,whiledoingthesamewithcustom_settingscanbehard.
Forexample,supposeaspiderneedstomodifyFEEDS:
import scrapy
class MySpider(scrapy.Spider):
name = "myspider"
custom_feed = {
"/home/user/documents/items.json": {
"format": "json",
"indent": 4,
}
}
@classmethod
def update_settings(cls, settings):
super().update_settings(settings)
settings.setdefault("FEEDS", {}).update(cls.custom_feed)
async start()→AsyncIterator[Any]
YieldtheinitialRequestobjectstosend.
34 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Addedinversion2.13.
Forexample:
from scrapy import Request, Spider
class MySpider(Spider):
name = "myspider"
async def start(self):
yield Request("https://toscrape.com/")
The default implementation reads URLs from start_urls and yields a request for each with
dont_filterenabled. Itisfunctionallyequivalentto:
async def start(self):
for url in self.start_urls:
yield Request(url, dont_filter=True)
Youcanalsoyielditems. Forexample:
async def start(self):
yield {"foo": "bar"}
To write spiders that work on Scrapy versions lower than 2.13, define also a synchronous
start_requests()methodthatreturnsaniterable. Forexample:
def start_requests(self):
yield Request("https://toscrape.com/")
ª Seealso
Startrequests
parse(response)
This is the default callback used by Scrapy to process downloaded responses, when their requests don’t
specifyacallback.
Theparsemethodisinchargeofprocessingtheresponseandreturningscrapeddataand/ormoreURLs
tofollow. OtherRequestscallbackshavethesamerequirementsastheSpiderclass.
This method, as well as any other Request callback, must return a Request object, an item object, an
iterableofRequestobjectsand/oritemobjects,orNone.
Parameters
response(Response)–theresponsetoparse
[ ]
log(message ,level,component )
WrapperthatsendsalogmessagethroughtheSpider’slogger,keptforbackwardcompatibility. Formore
informationseeLoggingfromSpiders.
closed(reason)
Called when the spider closes. This method provides a shortcut to signals.connect() for the
spider_closed signal.
3.2. Spiders 35

ScrapyDocumentation,Release2.13.3
Let’sseeanexample:
import scrapy
class MySpider(scrapy.Spider):
name = "example.com"
allowed_domains = ["example.com"]
start_urls = [
"http://www.example.com/1.html",
"http://www.example.com/2.html",
"http://www.example.com/3.html",
]
def parse(self, response):
self.logger.info("A response from %s just arrived!", response.url)
ReturnmultipleRequestsanditemsfromasinglecallback:
import scrapy
class MySpider(scrapy.Spider):
name = "example.com"
allowed_domains = ["example.com"]
start_urls = [
"http://www.example.com/1.html",
"http://www.example.com/2.html",
"http://www.example.com/3.html",
]
def parse(self, response):
for h3 in response.xpath("//h3").getall():
yield {"title": h3}
for href in response.xpath("//a/@href").getall():
yield scrapy.Request(response.urljoin(href), self.parse)
Insteadofstart_urlsyoucanusestart()directly;togivedatamorestructureyoucanuseItem objects:
import scrapy
from myproject.items import MyItem
class MySpider(scrapy.Spider):
name = "example.com"
allowed_domains = ["example.com"]
async def start(self):
yield scrapy.Request("http://www.example.com/1.html", self.parse)
yield scrapy.Request("http://www.example.com/2.html", self.parse)
yield scrapy.Request("http://www.example.com/3.html", self.parse)
def parse(self, response):
(continuesonnextpage)
36 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
for h3 in response.xpath("//h3").getall():
yield MyItem(title=h3)
for href in response.xpath("//a/@href").getall():
yield scrapy.Request(response.urljoin(href), self.parse)
3.2.2 Spider arguments
Spiderscanreceiveargumentsthatmodifytheirbehaviour. Somecommonusesforspiderargumentsaretodefinethe
startURLsortorestrictthecrawltocertainsectionsofthesite,buttheycanbeusedtoconfigureanyfunctionalityof
thespider.
Spiderargumentsarepassedthroughthecrawlcommandusingthe-aoption. Forexample:
scrapy crawl myspider -a category=electronics
Spiderscanaccessargumentsintheir__init__methods:
import scrapy
class MySpider(scrapy.Spider):
name = "myspider"
def __init__(self, category=None, *args, **kwargs):
super(MySpider, self).__init__(*args, **kwargs)
self.start_urls = [f"http://www.example.com/categories/{category}"]
# ...
The default __init__ method will take any spider arguments and copy them to the spider as attributes. The above
examplecanalsobewrittenasfollows:
import scrapy
class MySpider(scrapy.Spider):
name = "myspider"
async def start(self):
yield scrapy.Request(f"http://www.example.com/categories/{self.category}")
IfyouarerunningScrapyfromascript,youcanspecifyspiderargumentswhencallingCrawlerProcess.crawlor
CrawlerRunner.crawl:
process = CrawlerProcess()
process.crawl(MySpider, category="electronics")
Keepinmindthatspiderargumentsareonlystrings. Thespiderwillnotdoanyparsingonitsown. Ifyouweretoset
thestart_urlsattributefromthecommandline,youwouldhavetoparseitonyourownintoalistusingsomething
like ast.literal_eval() or json.loads() and then set it as an attribute. Otherwise, you would cause iteration
overastart_urlsstring(averycommonpythonpitfall)resultingineachcharacterbeingseenasaseparateurl.
A valid use case is to set the http auth credentials used by HttpAuthMiddleware or the user agent used by
UserAgentMiddleware:
3.2. Spiders 37

ScrapyDocumentation,Release2.13.3
scrapy crawl myspider -a http_user=myuser -a http_pass=mypassword -a user_agent=mybot
SpiderargumentscanalsobepassedthroughtheScrapydschedule.jsonAPI.SeeScrapyddocumentation.
3.2.3 Start requests
Start requests are Request objects yielded from the start() method of a spider or from the process_start()
methodofaspidermiddleware.
ª Seealso
Startrequestorder
Delayingstartrequestiteration
Youcanoverridethestart()methodasfollowstopauseitsiterationwhenevertherearescheduledrequests:
async def start(self):
async for item_or_request in super().start():
if self.crawler.engine.needs_backout():
await self.crawler.signals.wait_for(signals.scheduler_empty)
yield item_or_request
Thiscanhelpminimizethenumberofrequestsinthescheduleratanygiventime,tominimizeresourceusage(memory
ordisk,dependingonJOBDIR).
3.2.4 Generic Spiders
Scrapycomeswithsomeusefulgenericspidersthatyoucanusetosubclassyourspidersfrom. Theiraimistoprovide
convenient functionality for a few common scraping cases, like following all links on a site based on certain rules,
crawlingfromSitemaps,orparsinganXML/CSVfeed.
For the examples used in the following spiders, we’ll assume you have a project with a TestItem declared in a
myproject.itemsmodule:
import scrapy
class TestItem(scrapy.Item):
id = scrapy.Field()
name = scrapy.Field()
description = scrapy.Field()
CrawlSpider
class scrapy.spiders.CrawlSpider
Thisisthemostcommonlyusedspiderforcrawlingregularwebsites,asitprovidesaconvenientmechanismfor
followinglinksbydefiningasetofrules. Itmaynotbethebestsuitedforyourparticularwebsitesorproject,
but it’s generic enough for several cases, so you can start from it and override it as needed for more custom
functionality,orjustimplementyourownspider.
ApartfromtheattributesinheritedfromSpider(thatyoumustspecify),thisclasssupportsanewattribute:
38 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
rules
Which is a list of one (or more) Rule objects. Each Rule defines a certain behaviour for crawling the
site. Rulesobjectsaredescribedbelow. Ifmultiplerulesmatchthesamelink, thefirstonewillbeused,
accordingtotheorderthey’redefinedinthisattribute.
Thisspideralsoexposesanoverridablemethod:
parse_start_url(response,**kwargs)
ThismethodiscalledforeachresponseproducedfortheURLsinthespider’sstart_urlsattribute. It
allowstoparsetheinitialresponsesandmustreturneitheranitemobject,aRequestobject,oraniterable
containinganyofthem.
Crawlingrules
class scrapy.spiders.Rule(link_extractor: LinkExtractor|None=None,callback: CallbackT|str|None=
None,cb_kwargs: dict[str,Any]|None=None,follow: bool|None=None,
process_links: ProcessLinksT|str|None=None,process_request:
ProcessRequestT|str|None=None,errback: Callable[[Failure],Any]|str|
None=None)
link_extractorisaLinkExtractorobjectwhichdefineshowlinkswillbeextractedfromeachcrawledpage.
Each produced link will be used to generate a Request object, which will contain the link’s text in its meta
dictionary (under the link_text key). If omitted, a default link extractor created with no arguments will be
used,resultinginalllinksbeingextracted.
callbackisacallableorastring(inwhichcaseamethodfromthespiderobjectwiththatnamewillbeused)
to be called for each link extracted with the specified link extractor. This callback receives a Response as its
firstargumentandmustreturneitherasingleinstanceoraniterableofitemobjectsand/orRequestobjects(or
anysubclassofthem). Asmentionedabove,thereceivedResponseobjectwillcontainthetextofthelinkthat
producedtheRequestinitsmetadictionary(underthelink_textkey)
cb_kwargsisadictcontainingthekeywordargumentstobepassedtothecallbackfunction.
followisabooleanwhichspecifiesiflinksshouldbefollowedfromeachresponseextractedwiththisrule. If
callbackisNonefollowdefaultstoTrue,otherwiseitdefaultstoFalse.
process_links is a callable, or a string (in which case a method from the spider object with that name
will be used) which will be called for each list of links extracted from each response using the specified
link_extractor. Thisismainlyusedforfilteringpurposes.
process_requestisacallable(orastring,inwhichcaseamethodfromthespiderobjectwiththatnamewill
beused)whichwillbecalledforeveryRequest extractedbythisrule. Thiscallableshouldtakesaidrequest
as first argument and the Response from which the request originated as second argument. It must return a
RequestobjectorNone(tofilterouttherequest).
errbackisacallableorastring(inwhichcaseamethodfromthespiderobjectwiththatnamewillbeused)
tobecalledifanyexceptionisraisedwhileprocessingarequestgeneratedbytherule. ItreceivesaTwisted
Failureinstanceasfirstparameter.
. Warning
Because of its internal implementation, you must explicitly set callbacks for new requests when writing
CrawlSpider-basedspiders;unexpectedbehaviourcanoccurotherwise.
Addedinversion2.0: Theerrbackparameter.
3.2. Spiders 39

ScrapyDocumentation,Release2.13.3
CrawlSpiderexample
Let’snowtakealookatanexampleCrawlSpiderwithrules:
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class MySpider(CrawlSpider):
name = "example.com"
allowed_domains = ["example.com"]
start_urls = ["http://www.example.com"]
rules = (
# Extract links matching 'category.php' (but not matching 'subsection.php')
# and follow links from them (since no callback means follow=True by default).
Rule(LinkExtractor(allow=(r"category\.php",), deny=(r"subsection\.php",))),
# Extract links matching 'item.php' and parse them with the spider's method parse_
item
˓→
Rule(LinkExtractor(allow=(r"item\.php",)), callback="parse_item"),
)
def parse_item(self, response):
self.logger.info("Hi, this is an item page! %s", response.url)
item = scrapy.Item()
item["id"] = response.xpath('//td[@id="item_id"]/text()').re(r"ID: (\d+)")
item["name"] = response.xpath('//td[@id="item_name"]/text()').get()
item["description"] = response.xpath(
'//td[@id="item_description"]/text()'
).get()
item["link_text"] = response.meta["link_text"]
url = response.xpath('//td[@id="additional_data"]/@href').get()
return response.follow(
url, self.parse_additional_page, cb_kwargs=dict(item=item)
)
def parse_additional_page(self, response, item):
item["additional_data"] = response.xpath(
'//p[@id="additional_data"]/text()'
).get()
return item
Thisspiderwouldstartcrawlingexample.com’shomepage,collectingcategorylinks,anditemlinks,parsingthelatter
withtheparse_itemmethod. Foreachitemresponse,somedatawillbeextractedfromtheHTMLusingXPath,and
anItem willbefilledwithit.
XMLFeedSpider
class scrapy.spiders.XMLFeedSpider
XMLFeedSpider is designed for parsing XML feeds by iterating through them by a certain node name. The
iteratorcanbechosenfrom: iternodes,xml,andhtml. It’srecommendedtousetheiternodesiteratorfor
performance reasons, since the xml and html iterators generate the whole DOM at once in order to parse it.
However,usinghtmlastheiteratormaybeusefulwhenparsingXMLwithbadmarkup.
40 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Tosettheiteratorandthetagname,youmustdefinethefollowingclassattributes:
iterator
Astringwhichdefinestheiteratortouse. Itcanbeeither:
• 'iternodes'-afastiteratorbasedonregularexpressions
• 'html'-aniteratorwhichusesSelector. KeepinmindthisusesDOMparsingandmustloadall
DOMinmemorywhichcouldbeaproblemforbigfeeds
• 'xml' - an iterator which uses Selector. Keep in mind this uses DOM parsing and must load all
DOMinmemorywhichcouldbeaproblemforbigfeeds
Itdefaultsto: 'iternodes'.
itertag
Astringwiththenameofthenode(orelement)toiteratein. Example:
itertag = 'product'
namespaces
A list of (prefix, uri) tuples which define the namespaces available in that document that will be
processedwiththisspider. Theprefixanduriwillbeusedtoautomaticallyregisternamespacesusing
theregister_namespace()method.
Youcanthenspecifynodeswithnamespacesintheitertagattribute.
Example:
class YourSpider(XMLFeedSpider):
namespaces = [('n', 'http://www.sitemaps.org/schemas/sitemap/0.9')]
itertag = 'n:url'
# ...
Apartfromthesenewattributes,thisspiderhasthefollowingoverridablemethodstoo:
adapt_response(response)
Amethodthatreceivestheresponseassoonasitarrivesfromthespidermiddleware,beforethespiderstarts
parsingit. Itcanbeusedtomodifytheresponsebodybeforeparsingit. Thismethodreceivesaresponse
andalsoreturnsaresponse(itcouldbethesameoranotherone).
parse_node(response,selector)
Thismethodiscalledforthenodesmatchingtheprovidedtagname(itertag). Receivestheresponseand
anSelectorforeachnode. Overridingthismethodismandatory. Otherwise,youspiderwon’twork. This
methodmustreturnanitemobject,aRequestobject,oraniterablecontaininganyofthem.
process_results(response,results)
Thismethodiscalledforeachresult(itemorrequest)returnedbythespider,andit’sintendedtoperform
anylasttimeprocessingrequiredbeforereturningtheresultstotheframeworkcore,forexamplesettingthe
itemIDs. Itreceivesalistofresultsandtheresponsewhichoriginatedthoseresults. Itmustreturnalistof
results(itemsorrequests).
. Warning
Because of its internal implementation, you must explicitly set callbacks for new requests when writing
XMLFeedSpider-basedspiders;unexpectedbehaviourcanoccurotherwise.
3.2. Spiders 41

ScrapyDocumentation,Release2.13.3
XMLFeedSpiderexample
Thesespidersareprettyeasytouse,let’shavealookatoneexample:
from scrapy.spiders import XMLFeedSpider
from myproject.items import TestItem
class MySpider(XMLFeedSpider):
name = "example.com"
allowed_domains = ["example.com"]
start_urls = ["http://www.example.com/feed.xml"]
iterator = "iternodes" # This is actually unnecessary, since it's the default value
itertag = "item"
def parse_node(self, response, node):
self.logger.info(
"Hi, this is a <%s> node!: %s", self.itertag, "".join(node.getall())
)
item = TestItem()
item["id"] = node.xpath("@id").get()
item["name"] = node.xpath("name").get()
item["description"] = node.xpath("description").get()
return item
Basically what we did up there was to create a spider that downloads a feed from the given start_urls, and then
iteratesthrougheachofitsitemtags,printsthemout,andstoressomerandomdatainanItem.
CSVFeedSpider
class scrapy.spiders.CSVFeedSpider
ThisspiderisverysimilartotheXMLFeedSpider,exceptthatititeratesoverrows,insteadofnodes. Themethod
thatgetscalledineachiterationisparse_row().
delimiter
AstringwiththeseparatorcharacterforeachfieldintheCSVfileDefaultsto','(comma).
quotechar
AstringwiththeenclosurecharacterforeachfieldintheCSVfileDefaultsto'"'(quotationmark).
headers
AlistofthecolumnnamesintheCSVfile.
parse_row(response,row)
Receivesaresponseandadict(representingeachrow)withakeyforeachprovided(ordetected)headerof
theCSVfile. Thisspideralsogivestheopportunitytooverrideadapt_responseandprocess_results
methodsforpre-andpost-processingpurposes.
CSVFeedSpiderexample
Let’sseeanexamplesimilartothepreviousone,butusingaCSVFeedSpider:
from scrapy.spiders import CSVFeedSpider
from myproject.items import TestItem
(continuesonnextpage)
42 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class MySpider(CSVFeedSpider):
name = "example.com"
allowed_domains = ["example.com"]
start_urls = ["http://www.example.com/feed.csv"]
delimiter = ";"
quotechar = "'"
headers = ["id", "name", "description"]
def parse_row(self, response, row):
self.logger.info("Hi, this is a row!: %r", row)
item = TestItem()
item["id"] = row["id"]
item["name"] = row["name"]
item["description"] = row["description"]
return item
SitemapSpider
class scrapy.spiders.SitemapSpider
SitemapSpiderallowsyoutocrawlasitebydiscoveringtheURLsusingSitemaps.
Itsupportsnestedsitemapsanddiscoveringsitemapurlsfromrobots.txt.
sitemap_urls
Alistofurlspointingtothesitemapswhoseurlsyouwanttocrawl.
Youcanalsopointtoarobots.txtanditwillbeparsedtoextractsitemapurlsfromit.
sitemap_rules
Alistoftuples(regex, callback)where:
• regex is a regular expression to match urls extracted from sitemaps. regex can be either a str or a
compiledregexobject.
• callbackisthecallbacktouseforprocessingtheurlsthatmatchtheregularexpression. callbackcan
beastring(indicatingthenameofaspidermethod)oracallable.
Forexample:
sitemap_rules = [('/product/', 'parse_product')]
Rulesareappliedinorder,andonlythefirstonethatmatcheswillbeused.
Ifyouomitthisattribute,allurlsfoundinsitemapswillbeprocessedwiththeparsecallback.
sitemap_follow
Alistofregexesofsitemapthatshouldbefollowed. ThisisonlyforsitesthatuseSitemapindexfilesthat
pointtoothersitemapfiles.
Bydefault,allsitemapsarefollowed.
sitemap_alternate_links
Specifiesifalternatelinksforoneurlshouldbefollowed. Thesearelinksforthesamewebsiteinanother
languagepassedwithinthesameurlblock.
3.2. Spiders 43

ScrapyDocumentation,Release2.13.3
Forexample:
<url>
<loc>http://example.com/</loc>
<xhtml:link rel="alternate" hreflang="de" href="http://example.com/de"/>
</url>
With sitemap_alternate_links set, this would retrieve both URLs. With
sitemap_alternate_linksdisabled,onlyhttp://example.com/wouldberetrieved.
Defaultissitemap_alternate_linksdisabled.
sitemap_filter(entries)
Thisisafilterfunctionthatcouldbeoverriddentoselectsitemapentriesbasedontheirattributes.
Forexample:
<url>
<loc>http://example.com/</loc>
<lastmod>2005-01-01</lastmod>
</url>
Wecandefineasitemap_filterfunctiontofilterentriesbydate:
from datetime import datetime
from scrapy.spiders import SitemapSpider
class FilteredSitemapSpider(SitemapSpider):
name = "filtered_sitemap_spider"
allowed_domains = ["example.com"]
sitemap_urls = ["http://example.com/sitemap.xml"]
def sitemap_filter(self, entries):
for entry in entries:
date_time = datetime.strptime(entry["lastmod"], "%Y-%m-%d")
if date_time.year >= 2005:
yield entry
Thiswouldretrieveonlyentriesmodifiedon2005andthefollowingyears.
Entriesaredictobjectsextractedfromthesitemapdocument. Usually,thekeyisthetagnameandthevalue
isthetextinsideit.
It’simportanttonoticethat:
• asthelocattributeisrequired,entrieswithoutthistagarediscarded
• alternatelinksarestoredinalistwiththekeyalternate(seesitemap_alternate_links)
• namespacesareremoved,solxmltagsnamedas{namespace}tagnamebecomeonlytagname
Ifyouomitthismethod,allentriesfoundinsitemapswillbeprocessed,observingotherattributesandtheir
settings.
44 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
SitemapSpiderexamples
Simplestexample: processallurlsdiscoveredthroughsitemapsusingtheparsecallback:
from scrapy.spiders import SitemapSpider
class MySpider(SitemapSpider):
sitemap_urls = ["http://www.example.com/sitemap.xml"]
def parse(self, response):
pass # ... scrape item here ...
Processsomeurlswithcertaincallbackandotherurlswithadifferentcallback:
from scrapy.spiders import SitemapSpider
class MySpider(SitemapSpider):
sitemap_urls = ["http://www.example.com/sitemap.xml"]
sitemap_rules = [
("/product/", "parse_product"),
("/category/", "parse_category"),
]
def parse_product(self, response):
pass # ... scrape product ...
def parse_category(self, response):
pass # ... scrape category ...
Followsitemapsdefinedintherobots.txtfileandonlyfollowsitemapswhoseurlcontains/sitemap_shop:
from scrapy.spiders import SitemapSpider
class MySpider(SitemapSpider):
sitemap_urls = ["http://www.example.com/robots.txt"]
sitemap_rules = [
("/shop/", "parse_shop"),
]
sitemap_follow = ["/sitemap_shops"]
def parse_shop(self, response):
pass # ... scrape shop here ...
CombineSitemapSpiderwithothersourcesofurls:
from scrapy.spiders import SitemapSpider
class MySpider(SitemapSpider):
sitemap_urls = ["http://www.example.com/robots.txt"]
sitemap_rules = [
(continuesonnextpage)
3.2. Spiders 45

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
("/shop/", "parse_shop"),
]
other_urls = ["http://www.example.com/about"]
async def start(self):
async for item_or_request in super().start():
yield item_or_request
for url in self.other_urls:
yield Request(url, self.parse_other)
def parse_shop(self, response):
pass # ... scrape shop here ...
def parse_other(self, response):
pass # ... scrape other here ...
3.3 Selectors
Whenyou’rescrapingwebpages,themostcommontaskyouneedtoperformistoextractdatafromtheHTMLsource.
Thereareseverallibrariesavailabletoachievethis,suchas:
• BeautifulSoup is a very popular web scraping library among Python programmers which constructs a Python
objectbasedonthestructureoftheHTMLcodeandalsodealswithbadmarkupreasonablywell,butithasone
drawback: it’sslow.
• lxmlisanXMLparsinglibrary(whichalsoparsesHTML)withapythonicAPIbasedonElementTree. (lxml
isnotpartofthePythonstandardlibrary.)
Scrapycomeswithitsownmechanismforextractingdata. They’recalledselectorsbecausethey“select”certainparts
oftheHTMLdocumentspecifiedeitherbyXPathorCSSexpressions.
XPathisalanguageforselectingnodesinXMLdocuments,whichcanalsobeusedwithHTML.CSSisalanguage
forapplyingstylestoHTMLdocuments. ItdefinesselectorstoassociatethosestyleswithspecificHTMLelements.
(cid:242) Note
ScrapySelectorsisathinwrapperaroundparsellibrary;thepurposeofthiswrapperistoprovidebetterintegration
withScrapyResponseobjects.
parselisastand-alonewebscrapinglibrarywhichcanbeusedwithoutScrapy. Ituseslxmllibraryunderthehood,
andimplementsaneasyAPIontopoflxmlAPI.ItmeansScrapyselectorsareverysimilarinspeedandparsing
accuracytolxml.
3.3.1 Using selectors
Constructingselectors
ResponseobjectsexposeaSelectorinstanceon.selectorattribute:
>>> response.selector.xpath("//span/text()").get()
'good'
46 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Querying responses using XPath and CSS is so common that responses include two more shortcuts: response.
xpath()andresponse.css():
>>> response.xpath("//span/text()").get()
'good'
>>> response.css("span::text").get()
'good'
ScrapyselectorsareinstancesofSelectorclassconstructedbypassingeitherTextResponseobjectormarkupasa
string(intextargument).
UsuallythereisnoneedtoconstructScrapyselectorsmanually: responseobjectisavailableinSpidercallbacks,so
inmostcasesitismoreconvenienttouseresponse.css()andresponse.xpath()shortcuts. Byusingresponse.
selectororoneoftheseshortcutsyoucanalsoensuretheresponsebodyisparsedonlyonce.
Butifrequired,itispossibletouseSelectordirectly. Constructingfromtext:
>>> from scrapy.selector import Selector
>>> body = "<html><body><span>good</span></body></html>"
>>> Selector(text=body).xpath("//span/text()").get()
'good'
Constructingfromresponse-HtmlResponseisoneofTextResponsesubclasses:
>>> from scrapy.selector import Selector
>>> from scrapy.http import HtmlResponse
>>> response = HtmlResponse(url="http://example.com", body=body, encoding="utf-8")
>>> Selector(response=response).xpath("//span/text()").get()
'good'
Selectorautomaticallychoosesthebestparsingrules(XMLvsHTML)basedoninputtype.
Usingselectors
Toexplainhowtousetheselectorswe’llusetheScrapy shell(whichprovidesinteractivetesting)andanexample
pagelocatedintheScrapydocumentationserver:
https://docs.scrapy.org/en/latest/_static/selectors-sample1.html
Forthesakeofcompleteness,here’sitsfullHTMLcode:
<!DOCTYPE html>
<html>
<head>
<base href='http://example.com/' />
<title>Example website</title>
</head>
<body>
<div id='images'>
<a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' alt=
'image1'/></a>
˓→
<a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' alt=
'image2'/></a>
˓→
<a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' alt=
'image3'/></a>
˓→
(continuesonnextpage)
3.3. Selectors 47

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
<a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' alt=
'image4'/></a>
˓→
<a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' alt=
'image5'/></a>
˓→
</div>
</body>
</html>
First,let’sopentheshell:
scrapy shell https://docs.scrapy.org/en/latest/_static/selectors-sample1.html
Then,aftertheshellloads,you’llhavetheresponseavailableasresponseshellvariable,anditsattachedselectorin
response.selectorattribute.
Sincewe’redealingwithHTML,theselectorwillautomaticallyuseanHTMLparser.
So,bylookingattheHTMLcodeofthatpage,let’sconstructanXPathforselectingthetextinsidethetitletag:
>>> response.xpath("//title/text()")
[<Selector query='//title/text()' data='Example website'>]
Toactuallyextractthetextualdata,youmustcalltheselector.get()or.getall()methods,asfollows:
>>> response.xpath("//title/text()").getall()
['Example website']
>>> response.xpath("//title/text()").get()
'Example website'
.get()alwaysreturnsasingleresult;ifthereareseveralmatches,contentofafirstmatchisreturned;ifthereareno
matches,Noneisreturned. .getall()returnsalistwithallresults.
NoticethatCSSselectorscanselecttextorattributenodesusingCSS3pseudo-elements:
>>> response.css("title::text").get()
'Example website'
As you can see, .xpath() and .css() methods return a SelectorList instance, which is a list of new selectors.
ThisAPIcanbeusedforquicklyselectingnesteddata:
>>> response.css("img").xpath("@src").getall()
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']
Ifyouwanttoextractonlythefirstmatchedelement,youcancalltheselector.get()(oritsalias.extract_first()
commonlyusedinpreviousScrapyversions):
>>> response.xpath('//div[@id="images"]/a/text()').get()
'Name: My image 1 '
ItreturnsNoneifnoelementwasfound:
48 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
>>> response.xpath('//div[@id="not-exists"]/text()').get() is None
True
Adefaultreturnvaluecanbeprovidedasanargument,tobeusedinsteadof None:
>>> response.xpath('//div[@id="not-exists"]/text()').get(default="not-found")
'not-found'
Insteadofusinge.g. '@src'XPathitispossibletoqueryforattributesusing.attribpropertyofaSelector:
>>> [img.attrib["src"] for img in response.css("img")]
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']
Asashortcut,.attribisalsoavailableonSelectorListdirectly;itreturnsattributesforthefirstmatchingelement:
>>> response.css("img").attrib["src"]
'image1_thumb.jpg'
Thisismostusefulwhenonlyasingleresultisexpected,e.g. whenselectingbyid,orselectinguniqueelementsona
webpage:
>>> response.css("base").attrib["href"]
'http://example.com/'
Nowwe’regoingtogetthebaseURLandsomeimagelinks:
>>> response.xpath("//base/@href").get()
'http://example.com/'
>>> response.css("base::attr(href)").get()
'http://example.com/'
>>> response.css("base").attrib["href"]
'http://example.com/'
>>> response.xpath('//a[contains(@href, "image")]/@href').getall()
['image1.html',
'image2.html',
'image3.html',
'image4.html',
'image5.html']
>>> response.css("a[href*=image]::attr(href)").getall()
['image1.html',
'image2.html',
'image3.html',
'image4.html',
'image5.html']
>>> response.xpath('//a[contains(@href, "image")]/img/@src').getall()
(continuesonnextpage)
3.3. Selectors 49

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']
>>> response.css("a[href*=image] img::attr(src)").getall()
['image1_thumb.jpg',
'image2_thumb.jpg',
'image3_thumb.jpg',
'image4_thumb.jpg',
'image5_thumb.jpg']
ExtensionstoCSSSelectors
Per W3C standards, CSS selectors do not support selecting text nodes or attribute values. But selecting these is so
essentialinawebscrapingcontextthatScrapy(parsel)implementsacoupleof non-standardpseudo-elements:
• toselecttextnodes,use::text
• toselectattributevalues,use::attr(name)wherenameisthenameoftheattributethatyouwantthevalueof
. Warning
Thesepseudo-elementsareScrapy-/Parsel-specific. Theywillmostprobablynotworkwithotherlibrarieslikelxml
orPyQuery.
Examples:
• title::textselectschildrentextnodesofadescendant<title>element:
>>> response.css("title::text").get()
'Example website'
• *::textselectsalldescendanttextnodesofthecurrentselectorcontext:
>>> response.css("#images *::text").getall()
['\n ',
'Name: My image 1 ',
'\n ',
'Name: My image 2 ',
'\n ',
'Name: My image 3 ',
'\n ',
'Name: My image 4 ',
'\n ',
'Name: My image 5 ',
'\n ']
• foo::textreturnsnoresultsif fooelementexists,butcontainsnotext(i.e. textisempty):
>>> response.css("img::text").getall()
[]
(continuesonnextpage)
50 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
This means (cid:96)(cid:96).css('foo::text').get()(cid:96)(cid:96) could return None even if an element
exists. Use (cid:96)(cid:96)default=''(cid:96)(cid:96) if you always want a string:
>>> response.css("img::text").get()
>>> response.css("img::text").get(default="")
''
• a::attr(href)selectsthehref attributevalueofdescendantlinks:
>>> response.css("a::attr(href)").getall()
['image1.html',
'image2.html',
'image3.html',
'image4.html',
'image5.html']
(cid:242) Note
Seealso: Selectingelementattributes.
(cid:242) Note
Youcannotchainthesepseudo-elements. Butinpracticeitwouldnotmakemuchsense: textnodesdonothave
attributes,andattributevaluesarestringvaluesalreadyanddonothavechildrennodes.
Nestingselectors
Theselectionmethods(.xpath()or.css())returnalistofselectorsofthesametype,soyoucancalltheselection
methodsforthoseselectorstoo. Here’sanexample:
>>> links = response.xpath('//a[contains(@href, "image")]')
>>> links.getall()
['<a href="image1.html">Name: My image 1 <br><img src="image1_thumb.jpg" alt="image1"></
a>',
˓→
'<a href="image2.html">Name: My image 2 <br><img src="image2_thumb.jpg" alt="image2"></a>
',
˓→
'<a href="image3.html">Name: My image 3 <br><img src="image3_thumb.jpg" alt="image3"></a>
',
˓→
'<a href="image4.html">Name: My image 4 <br><img src="image4_thumb.jpg" alt="image4"></a>
',
˓→
'<a href="image5.html">Name: My image 5 <br><img src="image5_thumb.jpg" alt="image5"></a>
']
˓→
>>> for index, link in enumerate(links):
... href_xpath = link.xpath("@href").get()
... img_xpath = link.xpath("img/@src").get()
... print(f"Link number {index} points to url {href_xpath!r} and image {img_xpath!r}
")
˓→
(continuesonnextpage)
3.3. Selectors 51

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
...
Link number 0 points to url 'image1.html' and image 'image1_thumb.jpg'
Link number 1 points to url 'image2.html' and image 'image2_thumb.jpg'
Link number 2 points to url 'image3.html' and image 'image3_thumb.jpg'
Link number 3 points to url 'image4.html' and image 'image4_thumb.jpg'
Link number 4 points to url 'image5.html' and image 'image5_thumb.jpg'
Selectingelementattributes
Thereareseveralwaystogetavalueofanattribute. First,onecanuseXPathsyntax:
>>> response.xpath("//a/@href").getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
XPathsyntaxhasafewadvantages: itisastandardXPathfeature,and@attributescanbeusedinotherpartsofan
XPathexpression-e.g. itispossibletofilterbyattributevalue.
ScrapyalsoprovidesanextensiontoCSSselectors(::attr(...))whichallowstogetattributevalues:
>>> response.css("a::attr(href)").getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
Inadditiontothat,thereisa.attribpropertyofSelector. YoucanuseitifyouprefertolookupattributesinPython
code,withoutusingXPathsorCSSextensions:
>>> [a.attrib["href"] for a in response.css("a")]
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
This property is also available on SelectorList; it returns a dictionary with attributes of a first matching element. It
isconvenientto usewhenaselectoris expectedtogiveasingle result(e.g. when selectingbyelementID,or when
selectinganuniqueelementonapage):
>>> response.css("base").attrib
{'href': 'http://example.com/'}
>>> response.css("base").attrib["href"]
'http://example.com/'
.attribpropertyofanemptySelectorListisempty:
>>> response.css("foo").attrib
{}
Usingselectorswithregularexpressions
Selector alsohasa .re()methodforextractingdatausingregularexpressions. However,unlikeusing.xpath()
or.css()methods,.re()returnsalistofstrings. Soyoucan’tconstructnested.re()calls.
Here’sanexampleusedtoextractimagenamesfromtheHTMLcodeabove:
>>> response.xpath('//a[contains(@href, "image")]/text()').re(r"Name:\s*(.*)")
['My image 1 ',
'My image 2 ',
'My image 3 ',
(continuesonnextpage)
52 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
'My image 4 ',
'My image 5 ']
There’s an additional helper reciprocating .get() (and its alias .extract_first()) for .re(), named .
re_first(). Useittoextractjustthefirstmatchingstring:
>>> response.xpath('//a[contains(@href, "image")]/text()').re_first(r"Name:\s*(.*)")
'My image 1 '
extract()andextract_first()
Ifyou’realong-timeScrapyuser,you’reprobablyfamiliarwith.extract()and.extract_first()selectormeth-
ods. Manyblogpostsandtutorialsareusingthemaswell. ThesemethodsarestillsupportedbyScrapy,thereareno
planstodeprecatethem.
However,Scrapyusagedocsarenowwrittenusing.get()and.getall()methods. Wefeelthatthesenewmethods
resultinamoreconciseandreadablecode.
Thefollowingexamplesshowhowthesemethodsmaptoeachother.
1. SelectorList.get()isthesameasSelectorList.extract_first():
>>> response.css("a::attr(href)").get()
'image1.html'
>>> response.css("a::attr(href)").extract_first()
'image1.html'
2. SelectorList.getall()isthesameasSelectorList.extract():
>>> response.css("a::attr(href)").getall()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
>>> response.css("a::attr(href)").extract()
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']
3. Selector.get()isthesameasSelector.extract():
>>> response.css("a::attr(href)")[0].get()
'image1.html'
>>> response.css("a::attr(href)")[0].extract()
'image1.html'
4. Forconsistency,thereisalsoSelector.getall(),whichreturnsalist:
>>> response.css("a::attr(href)")[0].getall()
['image1.html']
So,themaindifferenceisthatoutputof .get()and.getall()methodsismorepredictable: .get()alwaysreturns
asingleresult,.getall()alwaysreturnsalistofallextractedresults. With.extract()methoditwasnotalways
obviousifaresultisalistornot;togetasingleresulteither.extract()or.extract_first()shouldbecalled.
3.3.2 Working with XPaths
HerearesometipswhichmayhelpyoutouseXPathwithScrapyselectorseffectively. Ifyouarenotmuchfamiliar
withXPathyet,youmaywanttotakealookfirstatthisXPathtutorial.
3.3. Selectors 53

ScrapyDocumentation,Release2.13.3
(cid:242) Note
SomeofthetipsarebasedonthispostfromZyte’sblog.
WorkingwithrelativeXPaths
KeepinmindthatifyouarenestingselectorsanduseanXPaththatstartswith /,thatXPathwillbeabsolutetothe
documentandnotrelativetotheSelectoryou’recallingitfrom.
For example, suppose you want to extract all <p> elements inside <div> elements. First, you would get all <div>
elements:
>>> divs = response.xpath("//div")
At first, you may be tempted to use the following approach, which is wrong, as it actually extracts all <p> elements
fromthedocument,notonlythoseinside<div>elements:
>>> for p in divs.xpath("//p"): # this is wrong - gets all <p> from the whole document
... print(p.get())
...
Thisistheproperwaytodoit(notethedotprefixingthe.//pXPath):
>>> for p in divs.xpath(".//p"): # extracts all <p> inside
... print(p.get())
...
Anothercommoncasewouldbetoextractalldirect<p>children:
>>> for p in divs.xpath("p"):
... print(p.get())
...
FormoredetailsaboutrelativeXPathsseetheLocationPathssectionintheXPathspecification.
Whenqueryingbyclass,considerusingCSS
BecauseanelementcancontainmultipleCSSclasses,theXPathwaytoselectelementsbyclassistheratherverbose:
*[contains(concat(' ', normalize-space(@class), ' '), ' someclass ')]
If you use @class='someclass' you may end up missing elements that have other classes, and if you just use
contains(@class, 'someclass')tomakeupforthatyoumayendupwithmoreelementsthatyouwant,ifthey
haveadifferentclassnamethatsharesthestringsomeclass.
Asitturnsout,Scrapyselectorsallowyoutochainselectors,somostofthetimeyoucanjustselectbyclassusingCSS
andthenswitchtoXPathwhenneeded:
>>> from scrapy import Selector
>>> sel = Selector(
... text='<div class="hero shout"><time datetime="2014-07-23 19:00">Special date</
time></div>'
˓→
... )
>>> sel.css(".shout").xpath("./time/@datetime").getall()
['2014-07-23 19:00']
54 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
ThisiscleanerthanusingtheverboseXPathtrickshownabove. Justremembertousethe.intheXPathexpressions
thatwillfollow.
Bewareofthedifferencebetween//node[1]and(//node)[1]
//node[1]selectsallthenodesoccurringfirstundertheirrespectiveparents.
(//node)[1]selectsallthenodesinthedocument,andthengetsonlythefirstofthem.
Example:
>>> from scrapy import Selector
>>> sel = Selector(
... text="""
... <ul class="list">
... <li>1</li>
... <li>2</li>
... <li>3</li>
... </ul>
... <ul class="list">
... <li>4</li>
... <li>5</li>
... <li>6</li>
... </ul>"""
... )
>>> xp = lambda x: sel.xpath(x).getall()
Thisgetsallfirst<li>elementsunderwhateveritisitsparent:
>>> xp("//li[1]")
['<li>1</li>', '<li>4</li>']
Andthisgetsthefirst<li>elementinthewholedocument:
>>> xp("(//li)[1]")
['<li>1</li>']
Thisgetsallfirst<li>elementsunderan<ul>parent:
>>> xp("//ul/li[1]")
['<li>1</li>', '<li>4</li>']
Andthisgetsthefirst<li>elementunderan<ul>parentinthewholedocument:
>>> xp("(//ul/li)[1]")
['<li>1</li>']
Usingtextnodesinacondition
WhenyouneedtousethetextcontentasargumenttoanXPathstringfunction,avoidusing.//text()andusejust.
instead.
This is because the expression .//text() yields a collection of text elements – a node-set. And when a node-
set is converted to a string, which happens when it is passed as argument to a string function like contains() or
starts-with(),itresultsinthetextforthefirstelementonly.
Example:
3.3. Selectors 55

ScrapyDocumentation,Release2.13.3
>>> from scrapy import Selector
>>> sel = Selector(
... text='<a href="#">Click here to go to the <strong>Next Page</strong></a>'
... )
Convertinganode-settostring:
>>> sel.xpath("//a//text()").getall() # take a peek at the node-set
['Click here to go to the ', 'Next Page']
>>> sel.xpath("string(//a[1]//text())").getall() # convert it to string
['Click here to go to the ']
Anodeconvertedtoastring,however,putstogetherthetextofitselfplusofallitsdescendants:
>>> sel.xpath("//a[1]").getall() # select the first node
['<a href="#">Click here to go to the <strong>Next Page</strong></a>']
>>> sel.xpath("string(//a[1])").getall() # convert it to string
['Click here to go to the Next Page']
So,usingthe.//text()node-setwon’tselectanythinginthiscase:
>>> sel.xpath("//a[contains(.//text(), 'Next Page')]").getall()
[]
Butusingthe.tomeanthenode,works:
>>> sel.xpath("//a[contains(., 'Next Page')]").getall()
['<a href="#">Click here to go to the <strong>Next Page</strong></a>']
VariablesinXPathexpressions
XPathallowsyoutoreferencevariablesinyourXPathexpressions,usingthe$somevariablesyntax. Thisissomewhat
similartoparameterizedqueriesorpreparedstatementsintheSQLworldwhereyoureplacesomeargumentsinyour
querieswithplaceholderslike?,whicharethensubstitutedwithvaluespassedwiththequery.
Here’s an example to match an element based on its “id” attribute value, without hard-coding it (that was shown
previously):
>>> # `$val` used in the expression, a `val` argument needs to be passed
>>> response.xpath("//div[@id=$val]/a/text()", val="images").get()
'Name: My image 1 '
Here’sanotherexample,tofindthe“id”attributeofa<div>tagcontainingfive<a>children(herewepassthevalue
5asaninteger):
>>> response.xpath("//div[count(a)=$cnt]/@id", cnt=5).get()
'images'
All variable references must have a binding value when calling .xpath() (otherwise you’ll get a ValueError:
XPath error: exception). Thisisdonebypassingasmanynamedargumentsasnecessary.
parsel,thelibrarypoweringScrapyselectors,hasmoredetailsandexamplesonXPathvariables.
56 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Removingnamespaces
When dealing with scraping projects, it is often quite convenient to get rid of namespaces altogether and just work
withelementnames,towritemoresimple/convenientXPaths. YoucanusetheSelector.remove_namespaces()
methodforthat.
Let’sshowanexamplethatillustratesthiswiththePythonInsiderblogatomfeed.
First,weopentheshellwiththeurlwewanttoscrape:
$ scrapy shell https://feeds.feedburner.com/PythonInsider
Thisishowthefilestarts:
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet ...
<feed xmlns="http://www.w3.org/2005/Atom"
xmlns:openSearch="http://a9.com/-/spec/opensearchrss/1.0/"
xmlns:blogger="http://schemas.google.com/blogger/2008"
xmlns:georss="http://www.georss.org/georss"
xmlns:gd="http://schemas.google.com/g/2005"
xmlns:thr="http://purl.org/syndication/thread/1.0"
xmlns:feedburner="http://rssnamespace.org/feedburner/ext/1.0">
...
Youcanseeseveralnamespacedeclarationsincludingadefault"http://www.w3.org/2005/Atom"andanotherone
usingthegd: prefixfor"http://schemas.google.com/g/2005".
Onceintheshellwecantryselectingall<link>objectsandseethatitdoesn’twork(becausetheAtomXMLnamespace
isobfuscatingthosenodes):
>>> response.xpath("//link")
[]
ButoncewecalltheSelector.remove_namespaces()method,allnodescanbeaccesseddirectlybytheirnames:
>>> response.selector.remove_namespaces()
>>> response.xpath("//link")
[<Selector query='//link' data='<link rel="alternate" type="text/html" h'>,
<Selector query='//link' data='<link rel="next" type="application/atom+'>,
...
Ifyouwonderwhythenamespaceremovalprocedureisn’talwayscalledbydefaultinsteadofhavingtocallitmanually,
thisisbecauseoftworeasons,which,inorderofrelevance,are:
1. Removingnamespacesrequirestoiterateandmodifyallnodesinthedocument,whichisareasonablyexpensive
operationtoperformbydefaultforalldocumentscrawledbyScrapy
2. There could be some cases where using namespaces is actually required, in case some element names clash
betweennamespaces. Thesecasesareveryrarethough.
UsingEXSLTextensions
Beingbuiltatoplxml,ScrapyselectorssupportsomeEXSLTextensionsandcomewiththesepre-registerednamespaces
touseinXPathexpressions:
3.3. Selectors 57

ScrapyDocumentation,Release2.13.3
prefix namespace usage
re http://exslt.org/regular-expressions regularexpressions
set http://exslt.org/sets setmanipulation
Regularexpressions
The test() function, for example, can prove quite useful when XPath’s starts-with() or contains() are not
sufficient.
Exampleselectinglinksinlistitemwitha“class”attributeendingwithadigit:
>>> from scrapy import Selector
>>> doc = """
... <div>
... <ul>
... <li class="item-0"><a href="link1.html">first item</a></li>
... <li class="item-1"><a href="link2.html">second item</a></li>
... <li class="item-inactive"><a href="link3.html">third item</a></li>
... <li class="item-1"><a href="link4.html">fourth item</a></li>
... <li class="item-0"><a href="link5.html">fifth item</a></li>
... </ul>
... </div>
... """
>>> sel = Selector(text=doc, type="html")
>>> sel.xpath("//li//@href").getall()
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
>>> sel.xpath('//li[re:test(@class, "item-\d$")]//@href').getall()
['link1.html', 'link2.html', 'link4.html', 'link5.html']
. Warning
C library libxslt doesn’t natively support EXSLT regular expressions so lxml’s implementation uses hooks to
Python’sremodule. Thus,usingregexpfunctionsinyourXPathexpressionsmayaddasmallperformancepenalty.
Setoperations
Thesecanbehandyforexcludingpartsofadocumenttreebeforeextractingtextelementsforexample.
Exampleextractingmicrodata(samplecontenttakenfromhttps://schema.org/Product)withgroupsofitemscopesand
correspondingitemprops:
>>> doc = """
... <div itemscope itemtype="http://schema.org/Product">
... <span itemprop="name">Kenmore White 17" Microwave</span>
... <img src="kenmore-microwave-17in.jpg" alt='Kenmore 17" Microwave' />
... <div itemprop="aggregateRating"
... itemscope itemtype="http://schema.org/AggregateRating">
... Rated <span itemprop="ratingValue">3.5</span>/5
... based on <span itemprop="reviewCount">11</span> customer reviews
... </div>
... <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
(continuesonnextpage)
58 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
... <span itemprop="price">$55.00</span>
... <link itemprop="availability" href="http://schema.org/InStock" />In stock
... </div>
... Product description:
... <span itemprop="description">0.7 cubic feet countertop microwave.
... Has six preset cooking categories and convenience features like
... Add-A-Minute and Child Lock.</span>
... Customer reviews:
... <div itemprop="review" itemscope itemtype="http://schema.org/Review">
... <span itemprop="name">Not a happy camper</span> -
... by <span itemprop="author">Ellie</span>,
... <meta itemprop="datePublished" content="2011-04-01">April 1, 2011
... <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
... <meta itemprop="worstRating" content = "1">
... <span itemprop="ratingValue">1</span>/
... <span itemprop="bestRating">5</span>stars
... </div>
... <span itemprop="description">The lamp burned out and now I have to replace
... it. </span>
... </div>
... <div itemprop="review" itemscope itemtype="http://schema.org/Review">
... <span itemprop="name">Value purchase</span> -
... by <span itemprop="author">Lucas</span>,
... <meta itemprop="datePublished" content="2011-03-25">March 25, 2011
... <div itemprop="reviewRating" itemscope itemtype="http://schema.org/Rating">
... <meta itemprop="worstRating" content = "1"/>
... <span itemprop="ratingValue">4</span>/
... <span itemprop="bestRating">5</span>stars
... </div>
... <span itemprop="description">Great microwave for the price. It is small and
... fits in my apartment.</span>
... </div>
... ...
... </div>
... """
>>> sel = Selector(text=doc, type="html")
>>> for scope in sel.xpath("//div[@itemscope]"):
... print("current scope:", scope.xpath("@itemtype").getall())
... props = scope.xpath(
... """
... set:difference(./descendant::*/@itemprop,
... .//*[@itemscope]/*/@itemprop)"""
... )
... print(f" properties: {props.getall()}")
... print("")
...
current scope: ['http://schema.org/Product']
properties: ['name', 'aggregateRating', 'offers', 'description', 'review', 'review']
current scope: ['http://schema.org/AggregateRating']
properties: ['ratingValue', 'reviewCount']
(continuesonnextpage)
3.3. Selectors 59

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
current scope: ['http://schema.org/Offer']
properties: ['price', 'availability']
current scope: ['http://schema.org/Review']
properties: ['name', 'author', 'datePublished', 'reviewRating', 'description']
current scope: ['http://schema.org/Rating']
properties: ['worstRating', 'ratingValue', 'bestRating']
current scope: ['http://schema.org/Review']
properties: ['name', 'author', 'datePublished', 'reviewRating', 'description']
current scope: ['http://schema.org/Rating']
properties: ['worstRating', 'ratingValue', 'bestRating']
Here we first iterate over itemscope elements, and for each one, we look for all itemprops elements and exclude
thosethatarethemselvesinsideanotheritemscope.
OtherXPathextensions
ScrapyselectorsalsoprovideasorelymissedXPathextensionfunction has-classthatreturnsTruefornodesthat
haveallofthespecifiedHTMLclasses.
ForthefollowingHTML:
>>> from scrapy.http import HtmlResponse
>>> response = HtmlResponse(
... url="http://example.com",
... body="""
... <html>
... <body>
... <p class="foo bar-baz">First</p>
... <p class="foo">Second</p>
... <p class="bar">Third</p>
... <p>Fourth</p>
... </body>
... </html>
... """,
... encoding="utf-8",
... )
Youcanuseitlikethis:
>>> response.xpath('//p[has-class("foo")]')
[<Selector query='//p[has-class("foo")]' data='<p class="foo bar-baz">First</p>'>,
<Selector query='//p[has-class("foo")]' data='<p class="foo">Second</p>'>]
>>> response.xpath('//p[has-class("foo", "bar-baz")]')
[<Selector query='//p[has-class("foo", "bar-baz")]' data='<p class="foo bar-baz">First</
p>'>]
˓→
>>> response.xpath('//p[has-class("foo", "bar")]')
[]
SoXPath//p[has-class("foo", "bar-baz")]isroughlyequivalenttoCSSp.foo.bar-baz. Pleasenote,that
60 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
itisslowerinmostofthecases,becauseit’sapure-Pythonfunctionthat’sinvokedforeverynodeinquestionwhereas
the CSS lookup is translated into XPath and thus runs more efficiently, so performance-wise its uses are limited to
situationsthatarenoteasilydescribedwithCSSselectors.
ParselalsosimplifiesaddingyourownXPathextensionswithset_xpathfunc().
3.3.3 Built-in Selectors reference
Selectorobjects
class scrapy.Selector(*args: Any,**kwargs: Any)
AninstanceofSelectorisawrapperoverresponsetoselectcertainpartsofitscontent.
responseisanHtmlResponseoranXmlResponseobjectthatwillbeusedforselectingandextractingdata.
text is a unicode string or utf-8 encoded text for cases when a response isn’t available. Using text and
responsetogetherisundefinedbehavior.
typedefinestheselectortype,itcanbe"html","xml","json"orNone(default).
IftypeisNone,theselectorautomaticallychoosesthebesttypebasedonresponsetype(seebelow),ordefaults
to"html"incaseitisusedtogetherwithtext.
If typeisNoneandaresponseispassed,theselectortypeisinferredfromtheresponsetypeasfollows:
• "html"forHtmlResponsetype
• "xml"forXmlResponsetype
• "json"forTextResponsetype
• "html"foranythingelse
Otherwise,if typeisset,theselectortypewillbeforcedandnodetectionwilloccur.
xpath(query: str,namespaces: Mapping[str,str]|None=None,**kwargs: Any)→
SelectorList[_SelectorType]
FindnodesmatchingthexpathqueryandreturntheresultasaSelectorListinstancewithallelements
flattened. ListelementsimplementSelectorinterfacetoo.
queryisastringcontainingtheXPATHquerytoapply.
namespacesisanoptionalprefix: namespace-urimapping(dict)foradditionalprefixestothosereg-
istered with register_namespace(prefix, uri). Contrary to register_namespace(), these pre-
fixesarenotsavedforfuturecalls.
AnyadditionalnamedargumentscanbeusedtopassvaluesforXPathvariablesintheXPathexpression,
e.g.:
selector.xpath('//a[href=$url]', url="http://www.example.com")
(cid:242) Note
Forconvenience,thismethodcanbecalledasresponse.xpath()
css(query: str)→SelectorList[_SelectorType]
ApplythegivenCSSselectorandreturnaSelectorListinstance.
queryisastringcontainingtheCSSselectortoapply.
3.3. Selectors 61

ScrapyDocumentation,Release2.13.3
Inthebackground,CSSqueriesaretranslatedintoXPathqueriesusingcssselectlibraryandrun.xpath()
method.
(cid:242) Note
Forconvenience,thismethodcanbecalledasresponse.css()
jmespath(query: str,**kwargs: Any)→SelectorList[_SelectorType]
Find objects matching the JMESPath query and return the result as a SelectorList instance with all
elementsflattened. ListelementsimplementSelectorinterfacetoo.
queryisastringcontainingtheJMESPathquerytoapply.
Anyadditionalnamedargumentsarepassedtotheunderlyingjmespath.searchcall,e.g.:
selector.jmespath('author.name', options=jmespath.Options(dict_cls=collections.
OrderedDict))
˓→
(cid:242) Note
Forconvenience,thismethodcanbecalledasresponse.jmespath()
get()→Any
Serializeandreturnthematchednodes.
ForHTMLandXML,theresultisalwaysastring,andpercent-encodedcontentisunquoted.
Seealso: extract()andextract_first()
attrib
Returntheattributesdictionaryforunderlyingelement.
Seealso: Selectingelementattributes.
re(regex: str|Pattern[str],replace_entities: bool=True)→List[str]
Applythegivenregexandreturnalistofstringswiththematches.
regexcanbeeitheracompiledregularexpressionorastringwhichwillbecompiledtoaregularexpression
usingre.compile(regex).
Bydefault,characterentityreferencesarereplacedbytheircorrespondingcharacter(exceptfor&amp;and
&lt;). Passingreplace_entitiesasFalseswitchesoffthesereplacements.
re_first(regex: str|Pattern[str],default: None=None,replace_entities: bool=True)→str|None
re_first(regex: str|Pattern[str],default: str,replace_entities: bool=True)→str
Apply the given regex and return the first string which matches. If there is no match, return the default
value(Noneiftheargumentisnotprovided).
Bydefault,characterentityreferencesarereplacedbytheircorrespondingcharacter(exceptfor&amp;and
&lt;). Passingreplace_entitiesasFalseswitchesoffthesereplacements.
register_namespace(prefix: str,uri: str)→None
RegisterthegivennamespacetobeusedinthisSelector. Withoutregisteringnamespacesyoucan’tselect
orextractdatafromnon-standardnamespaces. SeeSelectorexamplesonXMLresponse.
62 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
remove_namespaces()→None
Remove all namespaces, allowing to traverse the document using namespace-less xpaths. See Removing
namespaces.
__bool__()→bool
ReturnTrueifthereisanyrealcontentselectedorFalseotherwise. Inotherwords,thebooleanvalueof
aSelectorisgivenbythecontentsitselects.
getall()→List[str]
Serializeandreturnthematchednodeina1-elementlistofstrings.
ThismethodisaddedtoSelectorforconsistency; itismoreusefulwithSelectorList. Seealso: extract()
andextract_first()
SelectorListobjects
class scrapy.selector.SelectorList(iterable=(),/)
TheSelectorListclassisasubclassofthebuiltinlistclass,whichprovidesafewadditionalmethods.
xpath(xpath: str,namespaces: Mapping[str,str]|None=None,**kwargs: Any)→
SelectorList[_SelectorType]
Call the .xpath() method for each element in this list and return their results flattened as another
SelectorList.
xpathisthesameargumentastheoneinSelector.xpath()
namespacesisanoptionalprefix: namespace-urimapping(dict)foradditionalprefixestothosereg-
istered with register_namespace(prefix, uri). Contrary to register_namespace(), these pre-
fixesarenotsavedforfuturecalls.
AnyadditionalnamedargumentscanbeusedtopassvaluesforXPathvariablesintheXPathexpression,
e.g.:
selector.xpath('//a[href=$url]', url="http://www.example.com")
css(query: str)→SelectorList[_SelectorType]
Call the .css() method for each element in this list and return their results flattened as another
SelectorList.
queryisthesameargumentastheoneinSelector.css()
jmespath(query: str,**kwargs: Any)→SelectorList[_SelectorType]
Call the .jmespath() method for each element in this list and return their results flattened as another
SelectorList.
queryisthesameargumentastheoneinSelector.jmespath().
Anyadditionalnamedargumentsarepassedtotheunderlyingjmespath.searchcall,e.g.:
selector.jmespath('author.name', options=jmespath.Options(dict_cls=collections.
OrderedDict))
˓→
getall()→List[str]
Callthe.get()methodforeachelementisthislistandreturntheirresultsflattened,asalistofstrings.
Seealso: extract()andextract_first()
get(default: None=None)→str|None
3.3. Selectors 63

ScrapyDocumentation,Release2.13.3
get(default: str)→str
Returntheresultof .get()forthefirstelementinthislist. Ifthelistisempty,returnthedefaultvalue.
Seealso: extract()andextract_first()
re(regex: str|Pattern[str],replace_entities: bool=True)→List[str]
Callthe.re()methodforeachelementinthislistandreturntheirresultsflattened,asalistofstrings.
Bydefault,characterentityreferencesarereplacedbytheircorrespondingcharacter(exceptfor&amp;and
&lt;. Passingreplace_entitiesasFalseswitchesoffthesereplacements.
re_first(regex: str|Pattern[str],default: None=None,replace_entities: bool=True)→str|None
re_first(regex: str|Pattern[str],default: str,replace_entities: bool=True)→str
Callthe.re()methodforthefirstelementinthislistandreturntheresultinanstring. Ifthelistisempty
ortheregexdoesn’tmatchanything,returnthedefaultvalue(Noneiftheargumentisnotprovided).
Bydefault,characterentityreferencesarereplacedbytheircorrespondingcharacter(exceptfor&amp;and
&lt;. Passingreplace_entitiesasFalseswitchesoffthesereplacements.
attrib
Returntheattributesdictionaryforthefirstelement. Ifthelistisempty,returnanemptydict.
Seealso: Selectingelementattributes.
3.3.4 Examples
SelectorexamplesonHTMLresponse
HerearesomeSelectorexamplestoillustrateseveralconcepts. Inallcases,weassumethereisalreadyaSelector
instantiatedwithaHtmlResponseobjectlikethis:
sel = Selector(html_response)
1. Select all <h1> elements from an HTML response body, returning a list of Selector objects (i.e. a
SelectorListobject):
sel.xpath("//h1")
2. Extractthetextofall<h1>elementsfromanHTMLresponsebody,returningalistofstrings:
sel.xpath("//h1").getall() # this includes the h1 tag
sel.xpath("//h1/text()").getall() # this excludes the h1 tag
3. Iterateoverall<p>tagsandprinttheirclassattribute:
for node in sel.xpath("//p"):
print(node.attrib["class"])
SelectorexamplesonXMLresponse
HerearesomeexamplestoillustrateconceptsforSelectorobjectsinstantiatedwithanXmlResponseobject:
sel = Selector(xml_response)
1. Select all <product> elements from an XML response body, returning a list of Selector objects (i.e. a
SelectorListobject):
64 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
sel.xpath("//product")
2. ExtractallpricesfromaGoogleBaseXMLfeedwhichrequiresregisteringanamespace:
sel.register_namespace("g", "http://base.google.com/ns/1.0")
sel.xpath("//g:price").getall()
3.4 Items
Themaingoalinscrapingistoextractstructureddatafromunstructuredsources,typically,webpages. Spidersmay
returntheextracteddataasitems,Pythonobjectsthatdefinekey-valuepairs.
Scrapysupportsmultipletypesofitems. Whenyoucreateanitem,youmayusewhichevertypeofitemyouwant. When
youwritecodethatreceivesanitem,yourcodeshouldworkforanyitemtype.
3.4.1 Item Types
Scrapysupportsthefollowingtypesofitems,viatheitemadapterlibrary: dictionaries,Itemobjects,dataclassobjects,
andattrsobjects.
Dictionaries
Asanitemtype,dictisconvenientandfamiliar.
Itemobjects
Item providesadict-likeAPIplusadditionalfeaturesthatmakeitthemostfeature-completeitemtype:
class scrapy.Item(*args: Any,**kwargs: Any)
Baseclassforscrapeditems.
InScrapy,anobjectisconsideredanitemifit’ssupportedbytheitemadapterlibrary. Forexample,whenthe
outputofaspidercallbackisevaluated,onlysuchobjectsarepassedtoitempipelines. Itemisoneoftheclasses
supportedbyitemadapterbydefault.
ItemsmustdeclareField attributes,whichareprocessedandstoredinthefieldsattribute. Thisrestrictsthe
setofallowedfieldnamesandpreventstypos,raisingKeyErrorwhenreferringtoundefinedfields. Addition-
ally, fieldscanbeusedtodefinemetadataandcontrolthewaydataisprocessedinternally. Pleaserefertothe
documentationaboutfieldsforadditionalinformation.
Unlikeinstancesofdict,instancesofItem maybetracked todebugmemoryleaks.
copy()→Self
deepcopy()→Self
Returnadeepcopy()ofthisitem.
fields: dict[str, Field] = {}
AdictionarycontainingalldeclaredfieldsforthisItem,notonlythosepopulated. Thekeysarethefield
namesandthevaluesaretheField objectsusedintheItemdeclaration.
Item objectsreplicatethestandarddictAPI,includingits__init__method.
Item allowsthedefiningoffieldnames,sothat:
• KeyErrorisraisedwhenusingundefinedfieldnames(i.e. preventstyposgoingunnoticed)
• Itemexporterscanexportallfieldsbydefaultevenifthefirstscrapedobjectdoesnothavevaluesforallofthem
3.4. Items 65

ScrapyDocumentation,Release2.13.3
Item alsoallowsthedefiningoffieldmetadata,whichcanbeusedtocustomizeserialization.
trackreftracksItem objectstohelpfindmemoryleaks(seeDebuggingmemoryleakswithtrackref).
Example:
from scrapy.item import Item, Field
class CustomItem(Item):
one_field = Field()
another_field = Field()
Dataclassobjects
Addedinversion2.2.
dataclass()allowsthedefiningofitemclasseswithfieldnames,sothatitemexporterscanexportallfieldsbydefault
evenifthefirstscrapedobjectdoesnothavevaluesforallofthem.
Additionally,dataclassitemsalsoallowyouto:
• definethetypeanddefaultvalueofeachdefinedfield.
• definecustomfieldmetadatathroughdataclasses.field(),whichcanbeusedtocustomizeserialization.
Example:
from dataclasses import dataclass
@dataclass
class CustomItem:
one_field: str
another_field: int
(cid:242) Note
Fieldtypesarenotenforcedatruntime.
attr.sobjects
Addedinversion2.2.
attr.s()allowsthedefiningofitemclasseswithfieldnames,sothatitemexporterscanexportallfieldsbydefault
evenifthefirstscrapedobjectdoesnothavevaluesforallofthem.
Additionally,attr.sitemsalsoallowto:
• definethetypeanddefaultvalueofeachdefinedfield.
• definecustomfieldmetadata,whichcanbeusedtocustomizeserialization.
Inordertousethistype,theattrspackageneedstobeinstalled.
Example:
66 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
import attr
@attr.s
class CustomItem:
one_field = attr.ib()
another_field = attr.ib()
3.4.2 Working with Item objects
DeclaringItemsubclasses
ItemsubclassesaredeclaredusingasimpleclassdefinitionsyntaxandField objects. Hereisanexample:
import scrapy
class Product(scrapy.Item):
name = scrapy.Field()
price = scrapy.Field()
stock = scrapy.Field()
tags = scrapy.Field()
last_updated = scrapy.Field(serializer=str)
(cid:242) Note
ThosefamiliarwithDjangowillnoticethatScrapyItemsaredeclaredsimilartoDjangoModels,exceptthatScrapy
Itemsaremuchsimplerasthereisnoconceptofdifferentfieldtypes.
Declaringfields
Field objectsareusedtospecifymetadataforeachfield. Forexample,theserializerfunctionforthelast_updated
fieldillustratedintheexampleabove.
Youcanspecifyanykindofmetadataforeachfield. ThereisnorestrictiononthevaluesacceptedbyField objects.
Forthissamereason,thereisnoreferencelistofallavailablemetadatakeys. EachkeydefinedinField objectscould
beusedbyadifferentcomponent, andonlythosecomponentsknowaboutit. Youcanalsodefineanduseanyother
Field key in your project too, for your own needs. The main goal of Field objects is to provide a way to define
allfieldmetadatainoneplace. Typically,thosecomponentswhosebehaviourdependsoneachfieldusecertainfield
keystoconfigurethatbehaviour. Youmustrefertotheirdocumentationtoseewhichmetadatakeysareusedbyeach
component.
It’simportanttonotethattheField objectsusedtodeclaretheitemdonotstayassignedasclassattributes. Instead,
theycanbeaccessedthroughthefieldsattribute.
class scrapy.Field
Containeroffieldmetadata
TheFieldclassisjustanaliastothebuilt-indictclassanddoesn’tprovideanyextrafunctionalityorattributes.
Inotherwords,Field objectsareplain-oldPythondicts. Aseparateclassisusedtosupporttheitemdeclaration
syntaxbasedonclassattributes.
3.4. Items 67

ScrapyDocumentation,Release2.13.3
(cid:242) Note
Fieldmetadatacanalsobedeclaredfordataclassandattrsitems. Pleaserefertothedocumentationfordata-
classes.fieldandattr.ibforadditionalinformation.
WorkingwithItemobjects
Herearesomeexamplesofcommontasksperformedwithitems, usingthe Productitemdeclaredabove. Youwill
noticetheAPIisverysimilartothedictAPI.
Creatingitems
>>> product = Product(name="Desktop PC", price=1000)
>>> print(product)
Product(name='Desktop PC', price=1000)
Gettingfieldvalues
>>> product["name"]
Desktop PC
>>> product.get("name")
Desktop PC
>>> product["price"]
1000
>>> product["last_updated"]
Traceback (most recent call last):
...
KeyError: 'last_updated'
>>> product.get("last_updated", "not set")
not set
>>> product["lala"] # getting unknown field
Traceback (most recent call last):
...
KeyError: 'lala'
>>> product.get("lala", "unknown field")
'unknown field'
>>> "name" in product # is name field populated?
True
>>> "last_updated" in product # is last_updated populated?
False
>>> "last_updated" in product.fields # is last_updated a declared field?
True
(continuesonnextpage)
68 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
>>> "lala" in product.fields # is lala a declared field?
False
Settingfieldvalues
>>> product["last_updated"] = "today"
>>> product["last_updated"]
today
>>> product["lala"] = "test" # setting unknown field
Traceback (most recent call last):
...
KeyError: 'Product does not support field: lala'
Accessingallpopulatedvalues
Toaccessallpopulatedvalues,justusethetypicaldictAPI:
>>> product.keys()
['price', 'name']
>>> product.items()
[('price', 1000), ('name', 'Desktop PC')]
Copyingitems
Tocopyanitem,youmustfirstdecidewhetheryouwantashallowcopyoradeepcopy.
Ifyouritemcontainsmutablevalueslikelistsordictionaries,ashallowcopywillkeepreferencestothesamemutable
valuesacrossalldifferentcopies.
Forexample,ifyouhaveanitemwithalistoftags,andyoucreateashallowcopyofthatitem,boththeoriginalitem
andthecopyhavethesamelistoftags. Addingatagtothelistofoneoftheitemswilladdthetagtotheotheritemas
well.
Ifthatisnotthedesiredbehavior,useadeepcopyinstead.
Seecopyformoreinformation.
Tocreateashallowcopyofanitem,youcaneithercallcopy()onanexistingitem(product2 = product.copy())
orinstantiateyouritemclassfromanexistingitem(product2 = Product(product)).
Tocreateadeepcopy,calldeepcopy()instead(product2 = product.deepcopy()).
Othercommontasks
Creatingdictsfromitems:
>>> dict(product) # create a dict from all populated values
{'price': 1000, 'name': 'Desktop PC'}
Creating items from dicts:
>>> Product({"name": "Laptop PC", "price": 1500})
(continuesonnextpage)
3.4. Items 69

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
Product(price=1500, name='Laptop PC')
>>> Product({"name": "Laptop PC", "lala": 1500}) # warning: unknown field in dict
Traceback (most recent call last):
...
KeyError: 'Product does not support field: lala'
ExtendingItemsubclasses
YoucanextendItems(toaddmorefieldsortochangesomemetadataforsomefields)bydeclaringasubclassofyour
originalItem.
Forexample:
class DiscountedProduct(Product):
discount_percent = scrapy.Field(serializer=str)
discount_expiration_date = scrapy.Field()
You can also extend field metadata by using the previous field metadata and appending more values, or changing
existingvalues,likethis:
class SpecificProduct(Product):
name = scrapy.Field(Product.fields["name"], serializer=my_serializer)
Thatadds(orreplaces)theserializermetadatakeyforthenamefield,keepingallthepreviouslyexistingmetadata
values.
3.4.3 Supporting All Item Types
Incodethatreceivesanitem,suchasmethodsofitempipelinesorspidermiddlewares,itisagoodpracticetousethe
ItemAdapterclasstowritecodethatworksforanysupporteditemtype.
3.4.4 Other classes related to items
class scrapy.item.ItemMeta(class_name: str,bases: tuple[type,...],attrs: dict[str,Any])
MetaclassofItem thathandlesfielddefinitions.
3.5 Item Loaders
Item Loaders provide a convenient mechanism for populating scraped items. Even though items can be populated
directly,ItemLoadersprovideamuchmoreconvenientAPIforpopulatingthemfromascrapingprocess,byautomating
somecommontaskslikeparsingtherawextracteddatabeforeassigningit.
Inotherwords,itemsprovidethecontainerofscrapeddata,whileItemLoadersprovidethemechanismforpopulating
thatcontainer.
ItemLoadersaredesignedtoprovideaflexible, efficientandeasymechanismforextendingandoverridingdifferent
fieldparsingrules,eitherbyspider,orbysourceformat(HTML,XML,etc)withoutbecominganightmaretomaintain.
(cid:242) Note
ItemLoadersareanextensionoftheitemloaderslibrarythatmakeiteasiertoworkwithScrapybyaddingsupport
forresponses.
70 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
3.5.1 Using Item Loaders to populate items
TouseanItemLoader,youmustfirstinstantiateit. Youcaneitherinstantiateitwithanitemobject orwithoutone,in
whichcaseanitemobjectisautomaticallycreatedintheItemLoader__init__methodusingtheitemclassspecified
intheItemLoader.default_item_classattribute.
Then,youstartcollectingvaluesintotheItemLoader,typicallyusingSelectors. Youcanaddmorethanonevalueto
thesameitemfield;theItemLoaderwillknowhowto“join”thosevalueslaterusingaproperprocessingfunction.
(cid:242) Note
Collecteddataisinternallystoredaslists,allowingtoaddseveralvaluestothesamefield. Ifanitemargumentis
passedwhencreatingaloader,eachoftheitem’svalueswillbestoredas-isifit’salreadyaniterable,orwrapped
withalistifit’sasinglevalue.
HereisatypicalItemLoaderusageinaSpider,usingtheProductitemdeclaredintheItemschapter:
from scrapy.loader import ItemLoader
from myproject.items import Product
def parse(self, response):
l = ItemLoader(item=Product(), response=response)
l.add_xpath("name", '//div[@class="product_name"]')
l.add_xpath("name", '//div[@class="product_title"]')
l.add_xpath("price", '//p[@id="price"]')
l.add_css("stock", "p#stock")
l.add_value("last_updated", "today") # you can also use literal values
return l.load_item()
Byquicklylookingatthatcode,wecanseethenamefieldisbeingextractedfromtwodifferentXPathlocationsinthe
page:
1. //div[@class="product_name"]
2. //div[@class="product_title"]
Inotherwords,dataisbeingcollectedbyextractingitfromtwoXPathlocations,usingtheadd_xpath()method. This
isthedatathatwillbeassignedtothenamefieldlater.
Afterwards, similar calls are used for price and stock fields (the latter using a CSS selector with the add_css()
method),andfinallythelast_updatefieldispopulateddirectlywithaliteralvalue(today)usingadifferentmethod:
add_value().
Finally, whenalldataiscollected, theItemLoader.load_item()methodiscalledwhichactuallyreturnstheitem
populated with the data previously extracted and collected with the add_xpath(), add_css(), and add_value()
calls.
3.5.2 Working with dataclass items
Bydefault,dataclassitemsrequireallfieldstobepassedwhencreated. Thiscouldbeanissuewhenusingdataclass
items with item loaders: unless a pre-populated item is passed to the loader, fields will be populated incrementally
usingtheloader’sadd_xpath(),add_css()andadd_value()methods.
Oneapproachtoovercomethisistodefineitemsusingthefield()function,withadefaultargument:
3.5. ItemLoaders 71

ScrapyDocumentation,Release2.13.3
from dataclasses import dataclass, field
from typing import Optional
@dataclass
class InventoryItem:
name: Optional[str] = field(default=None)
price: Optional[float] = field(default=None)
stock: Optional[int] = field(default=None)
3.5.3 Input and Output processors
An Item Loader contains one input processor and one output processor for each (item) field. The input processor
processestheextracteddataassoonasit’sreceived(throughtheadd_xpath(),add_css()oradd_value()meth-
ods) and the result of the input processor is collected and kept inside the ItemLoader. After collecting all data, the
ItemLoader.load_item()methodiscalledtopopulateandgetthepopulateditemobject. That’swhentheoutput
processoriscalledwiththedatapreviouslycollected(andprocessedusingtheinputprocessor). Theresultoftheoutput
processoristhefinalvaluethatgetsassignedtotheitem.
Let’sseeanexampletoillustratehowtheinputandoutputprocessorsarecalledforaparticularfield(thesameapplies
foranyotherfield):
l = ItemLoader(Product(), some_selector)
l.add_xpath("name", xpath1) # (1)
l.add_xpath("name", xpath2) # (2)
l.add_css("name", css) # (3)
l.add_value("name", "test") # (4)
return l.load_item() # (5)
Sowhathappensis:
1. Datafromxpath1isextracted,andpassedthroughtheinputprocessorofthenamefield. Theresultoftheinput
processoriscollectedandkeptintheItemLoader(butnotyetassignedtotheitem).
2. Datafromxpath2isextracted,andpassedthroughthesameinputprocessorusedin(1). Theresultoftheinput
processorisappendedtothedatacollectedin(1)(ifany).
3. Thiscaseissimilartothepreviousones,exceptthatthedataisextractedfromthecssCSSselector,andpassed
throughthesameinputprocessor usedin(1)and(2). Theresultoftheinputprocessorisappendedtothedata
collectedin(1)and(2)(ifany).
4. Thiscaseisalsosimilartothepreviousones,exceptthatthevaluetobecollectedisassigneddirectly,insteadof
beingextractedfromaXPathexpressionoraCSSselector. However,thevalueisstillpassedthroughtheinput
processors. Inthiscase, sincethevalueisnotiterableitisconvertedtoaniterableofasingleelementbefore
passingittotheinputprocessor,becauseinputprocessoralwaysreceiveiterables.
5. The data collected in steps (1), (2), (3) and (4) is passed through the output processor of the name field. The
resultoftheoutputprocessoristhevalueassignedtothenamefieldintheitem.
It’sworthnoticingthatprocessorsarejustcallableobjects, whicharecalledwiththedatatobeparsed, andreturna
parsedvalue. Soyoucanuseanyfunctionasinputoroutputprocessor. Theonlyrequirementisthattheymustaccept
one(andonlyone)positionalargument,whichwillbeaniterable.
Changedinversion2.0: Processorsnolongerneedtobemethods.
72 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(cid:242) Note
Both input and output processors must receive an iterable as their first argument. The output of those functions
canbeanything. Theresultofinputprocessorswillbeappendedtoaninternallist(intheLoader)containingthe
collectedvalues(forthatfield). Theresultoftheoutputprocessorsisthevaluethatwillbefinallyassignedtothe
item.
The other thing you need to keep in mind is that the values returned by input processors are collected internally (in
lists)andthenpassedtooutputprocessorstopopulatethefields.
Last,butnotleast,itemloaderscomeswithsomecommonlyusedprocessorsbuilt-inforconvenience.
3.5.4 Declaring Item Loaders
ItemLoadersaredeclaredusingaclassdefinitionsyntax. Hereisanexample:
from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader
class ProductLoader(ItemLoader):
default_output_processor = TakeFirst()
name_in = MapCompose(str.title)
name_out = Join()
price_in = MapCompose(str.strip)
# ...
As you can see, input processors are declared using the _in suffix while output processors are declared us-
ing the _out suffix. And you can also declare a default input/output processors using the ItemLoader.
default_input_processorandItemLoader.default_output_processorattributes.
3.5.5 Declaring Input and Output Processors
Asseenintheprevioussection,inputandoutputprocessorscanbedeclaredintheItemLoaderdefinition,andit’svery
commontodeclareinputprocessorsthisway. However,thereisonemoreplacewhereyoucanspecifytheinputand
outputprocessorstouse: intheItemField metadata. Hereisanexample:
import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags
def filter_price(value):
if value.isdigit():
return value
class Product(scrapy.Item):
name = scrapy.Field(
input_processor=MapCompose(remove_tags),
output_processor=Join(),
(continuesonnextpage)
3.5. ItemLoaders 73

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
)
price = scrapy.Field(
input_processor=MapCompose(remove_tags, filter_price),
output_processor=TakeFirst(),
)
>>> from scrapy.loader import ItemLoader
>>> il = ItemLoader(item=Product())
>>> il.add_value("name", ["Welcome to my", "<strong>website</strong>"])
>>> il.add_value("price", ["&euro;", "<span>1000</span>"])
>>> il.load_item()
{'name': 'Welcome to my website', 'price': '1000'}
Theprecedenceorder,forbothinputandoutputprocessors,isasfollows:
1. ItemLoaderfield-specificattributes: field_inandfield_out(mostprecedence)
2. Fieldmetadata(input_processorandoutput_processorkey)
3. Item Loader defaults: ItemLoader.default_input_processor() and ItemLoader.
default_output_processor()(leastprecedence)
Seealso: ReusingandextendingItemLoaders.
3.5.6 Item Loader Context
The Item Loader Context is a dict of arbitrary key/values which is shared among all input and output processors in
the Item Loader. It can be passed when declaring, instantiating or using Item Loader. They are used to modify the
behaviouroftheinput/outputprocessors.
Forexample,supposeyouhaveafunctionparse_lengthwhichreceivesatextvalueandextractsalengthfromit:
def parse_length(text, loader_context):
unit = loader_context.get("unit", "m")
# ... length parsing code goes here ...
return parsed_length
Byacceptingaloader_contextargumentthefunctionisexplicitlytellingtheItemLoaderthatit’sabletoreceivean
ItemLoadercontext,sotheItemLoaderpassesthecurrentlyactivecontextwhencallingit,andtheprocessorfunction
(parse_lengthinthiscase)canthususethem.
ThereareseveralwaystomodifyItemLoadercontextvalues:
1. BymodifyingthecurrentlyactiveItemLoadercontext(contextattribute):
loader = ItemLoader(product)
loader.context["unit"] = "cm"
2. OnItemLoaderinstantiation(thekeywordargumentsofItemLoader__init__methodarestoredintheItem
Loadercontext):
loader = ItemLoader(product, unit="cm")
3. OnItemLoaderdeclaration,forthoseinput/outputprocessorsthatsupportinstantiatingthemwithanItemLoader
context. MapComposeisoneofthem:
74 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
class ProductLoader(ItemLoader):
length_out = MapCompose(parse_length, unit="cm")
3.5.7 ItemLoader objects
class scrapy.loader.ItemLoader(item: Any=None,selector: Selector|None=None,response:
TextResponse|None=None,parent: itemloaders.ItemLoader|None=
None,**context: Any)
A user-friendly abstraction to populate an item with data by applying field processors to scraped data. When
instantiatedwithaselectororaresponseitsupportsdataextractionfromwebpagesusingselectors.
Parameters
• item (scrapy.item.Item) – The item instance to populate using subsequent calls to
add_xpath(),add_css(),oradd_value().
• selector (Selector object) – The selector to extract data from, when using the
add_xpath(),add_css(),replace_xpath(),orreplace_css()method.
• response (Response object) – The response used to construct the selector using the
default_selector_class, unless the selector argument is given, in which case this ar-
gumentisignored.
Ifnoitemisgiven,oneisinstantiatedautomaticallyusingtheclassindefault_item_class.
Theitem, selector, responseandremainingkeywordargumentsareassignedtotheLoadercontext(accessible
throughthecontextattribute).
item
TheitemobjectbeingparsedbythisItemLoader. Thisismostlyusedasapropertyso,whenattempting
tooverridethisvalue,youmaywanttocheckoutdefault_item_classfirst.
context
ThecurrentlyactiveContextofthisItemLoader.
default_item_class
Anitemclass(orfactory),usedtoinstantiateitemswhennotgiveninthe__init__method.
default_input_processor
Thedefaultinputprocessortouseforthosefieldswhichdon’tspecifyone.
default_output_processor
Thedefaultoutputprocessortouseforthosefieldswhichdon’tspecifyone.
default_selector_class
TheclassusedtoconstructtheselectorofthisItemLoader,ifonlyaresponseisgiveninthe__init__
method. Ifaselectorisgiveninthe__init__methodthisattributeisignored. Thisattributeissometimes
overriddeninsubclasses.
selector
TheSelector objecttoextractdatafrom. It’seithertheselectorgiveninthe __init__methodorone
created from the response given in the __init__ method using the default_selector_class. This
attributeismeanttoberead-only.
add_css(field_name: str|None,css: str|Iterable[str],*processors: Callable[...,Any],re: str|Pattern[str]|
None=None,**kw: Any)→Self
Similar to ItemLoader.add_value() but receives a CSS selector instead of a value, which is used to
extractalistofunicodestringsfromtheselectorassociatedwiththisItemLoader.
3.5. ItemLoaders 75

ScrapyDocumentation,Release2.13.3
Seeget_css()forkwargs.
Parameters
css(str)–theCSSselectortoextractdatafrom
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
Examples:
# HTML snippet: <p class="product-name">Color TV</p>
loader.add_css('name', 'p.product-name')
# HTML snippet: <p id="price">the price is $1200</p>
loader.add_css('price', 'p#price', re='the price is (.*)')
add_jmes(field_name: str|None,jmes: str,*processors: Callable[...,Any],re: str|Pattern[str]|None=
None,**kw: Any)→Self
SimilartoItemLoader.add_value()butreceivesaJMESPathselectorinsteadofavalue,whichisused
toextractalistofunicodestringsfromtheselectorassociatedwiththisItemLoader.
Seeget_jmes()forkwargs.
Parameters
jmes(str)–theJMESPathselectortoextractdatafrom
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
Examples:
# HTML snippet: {"name": "Color TV"}
loader.add_jmes('name')
# HTML snippet: {"price": the price is $1200"}
loader.add_jmes('price', TakeFirst(), re='the price is (.*)')
add_value(field_name: str|None,value: Any,*processors: Callable[...,Any],re: str|Pattern[str]|None=
None,**kw: Any)→Self
Processandthenaddthegivenvalueforthegivenfield.
Thevalueisfirstpassedthroughget_value()bygivingtheprocessorsandkwargs,andthenpassed
through the field input processor and its result appended to the data collected for that field. If the field
alreadycontainscollecteddata,thenewdataisadded.
The given field_name can be None, in which case values for multiple fields may be added. And the
processedvalueshouldbeadictwithfield_namemappedtovalues.
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
Examples:
76 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
loader.add_value('name', 'Color TV')
loader.add_value('colours', ['white', 'blue'])
loader.add_value('length', '100')
loader.add_value('name', 'name: foo', TakeFirst(), re='name: (.+)')
loader.add_value(None, {'name': 'foo', 'sex': 'male'})
add_xpath(field_name: str|None,xpath: str|Iterable[str],*processors: Callable[...,Any],re: str|
Pattern[str]|None=None,**kw: Any)→Self
SimilartoItemLoader.add_value()butreceivesanXPathinsteadofavalue,whichisusedtoextracta
listofstringsfromtheselectorassociatedwiththisItemLoader.
Seeget_xpath()forkwargs.
Parameters
xpath(str)–theXPathtoextractdatafrom
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
Examples:
# HTML snippet: <p class="product-name">Color TV</p>
loader.add_xpath('name', '//p[@class="product-name"]')
# HTML snippet: <p id="price">the price is $1200</p>
loader.add_xpath('price', '//p[@id="price"]', re='the price is (.*)')
get_collected_values(field_name: str)→List[Any]
Returnthecollectedvaluesforthegivenfield.
get_css(css: str|Iterable[str],*processors: Callable[[...],Any],re: str|Pattern[str]|None=None,**kw:
Any)→Any
Similar to ItemLoader.get_value() but receives a CSS selector instead of a value, which is used to
extractalistofunicodestringsfromtheselectorassociatedwiththisItemLoader.
Parameters
• css(str)–theCSSselectortoextractdatafrom
• re (str or Pattern[str]) – a regular expression to use for extracting data from the
selectedCSSregion
Examples:
# HTML snippet: <p class="product-name">Color TV</p>
loader.get_css('p.product-name')
# HTML snippet: <p id="price">the price is $1200</p>
loader.get_css('p#price', TakeFirst(), re='the price is (.*)')
get_jmes(jmes: str|Iterable[str],*processors: Callable[[...],Any],re: str|Pattern[str]|None=None,
**kw: Any)→Any
SimilartoItemLoader.get_value()butreceivesaJMESPathselectorinsteadofavalue,whichisused
toextractalistofunicodestringsfromtheselectorassociatedwiththisItemLoader.
Parameters
• jmes(str)–theJMESPathselectortoextractdatafrom
3.5. ItemLoaders 77

ScrapyDocumentation,Release2.13.3
• re(str or Pattern)–aregularexpressiontouseforextractingdatafromtheselected
JMESPath
Examples:
# HTML snippet: {"name": "Color TV"}
loader.get_jmes('name')
# HTML snippet: {"price": the price is $1200"}
loader.get_jmes('price', TakeFirst(), re='the price is (.*)')
get_output_value(field_name: str)→Any
Return the collected values parsed using the output processor, for the given field. This method doesn’t
populateormodifytheitematall.
get_value(value: Any,*processors: Callable[[...],Any],re: str|Pattern[str]|None=None,**kw: Any)→
Any
Processthegivenvaluebythegivenprocessorsandkeywordarguments.
Availablekeywordarguments:
Parameters
re(str or Pattern[str])–aregularexpressiontouseforextractingdatafromthegiven
valueusingextract_regex()method,appliedbeforeprocessors
Examples:
>>> from itemloaders import ItemLoader
>>> from itemloaders.processors import TakeFirst
>>> loader = ItemLoader()
>>> loader.get_value('name: foo', TakeFirst(), str.upper, re='name: (.+)')
'FOO'
get_xpath(xpath: str|Iterable[str],*processors: Callable[[...],Any],re: str|Pattern[str]|None=None,
**kw: Any)→Any
SimilartoItemLoader.get_value()butreceivesanXPathinsteadofavalue,whichisusedtoextracta
listofunicodestringsfromtheselectorassociatedwiththisItemLoader.
Parameters
• xpath(str)–theXPathtoextractdatafrom
• re (str or Pattern[str]) – a regular expression to use for extracting data from the
selectedXPathregion
Examples:
# HTML snippet: <p class="product-name">Color TV</p>
loader.get_xpath('//p[@class="product-name"]')
# HTML snippet: <p id="price">the price is $1200</p>
loader.get_xpath('//p[@id="price"]', TakeFirst(), re='the price is (.*)')
load_item()→Any
Populatetheitemwiththedatacollectedsofar,andreturnit. Thedatacollectedisfirstpassedthroughthe
outputprocessorstogetthefinalvaluetoassigntoeachitemfield.
nested_css(css: str,**context: Any)→Self
Createanestedloaderwithacssselector. Thesuppliedselectorisappliedrelativetoselectorassociatedwith
thisItemLoader. ThenestedloadersharestheitemwiththeparentItemLoadersocallstoadd_xpath(),
add_value(),replace_value(),etc. willbehaveasexpected.
78 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
nested_xpath(xpath: str,**context: Any)→Self
Create a nested loader with an xpath selector. The supplied selector is applied relative to selector asso-
ciatedwiththisItemLoader. ThenestedloadersharestheitemwiththeparentItemLoader socallsto
add_xpath(),add_value(),replace_value(),etc. willbehaveasexpected.
replace_css(field_name: str|None,css: str|Iterable[str],*processors: Callable[...,Any],re: str|
Pattern[str]|None=None,**kw: Any)→Self
Similartoadd_css()butreplacescollecteddatainsteadofaddingit.
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
replace_jmes(field_name: str|None,jmes: str|Iterable[str],*processors: Callable[...,Any],re: str|
Pattern[str]|None=None,**kw: Any)→Self
Similartoadd_jmes()butreplacescollecteddatainsteadofaddingit.
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
replace_value(field_name: str|None,value: Any,*processors: Callable[...,Any],re: str|Pattern[str]|
None=None,**kw: Any)→Self
Similartoadd_value()butreplacesthecollecteddatawiththenewvalueinsteadofaddingit.
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
replace_xpath(field_name: str|None,xpath: str|Iterable[str],*processors: Callable[...,Any],re: str|
Pattern[str]|None=None,**kw: Any)→Self
Similartoadd_xpath()butreplacescollecteddatainsteadofaddingit.
Returns
ThecurrentItemLoaderinstanceformethodchaining.
Returntype
ItemLoader
3.5.8 Nested Loaders
Whenparsingrelatedvaluesfromasubsectionofadocument,itcanbeusefultocreatenestedloaders. Imagineyou’re
extractingdetailsfromafooterofapagethatlookssomethinglike:
Example:
<footer>
<a class="social" href="https://facebook.com/whatever">Like Us</a>
<a class="social" href="https://twitter.com/whatever">Follow Us</a>
<a class="email" href="mailto:whatever@example.com">Email Us</a>
</footer>
3.5. ItemLoaders 79

ScrapyDocumentation,Release2.13.3
Withoutnestedloaders,youneedtospecifythefullxpath(orcss)foreachvaluethatyouwishtoextract.
Example:
loader = ItemLoader(item=Item())
# load stuff not in the footer
loader.add_xpath("social", '//footer/a[@class = "social"]/@href')
loader.add_xpath("email", '//footer/a[@class = "email"]/@href')
loader.load_item()
Instead,youcancreateanestedloaderwiththefooterselectorandaddvaluesrelativetothefooter. Thefunctionality
isthesamebutyouavoidrepeatingthefooterselector.
Example:
loader = ItemLoader(item=Item())
# load stuff not in the footer
footer_loader = loader.nested_xpath("//footer")
footer_loader.add_xpath("social", 'a[@class = "social"]/@href')
footer_loader.add_xpath("email", 'a[@class = "email"]/@href')
# no need to call footer_loader.load_item()
loader.load_item()
You can nest loaders arbitrarily and they work with either xpath or css selectors. As a general guideline, use nested
loaderswhentheymakeyourcodesimplerbutdonotgooverboardwithnestingoryourparsercanbecomedifficultto
read.
3.5.9 Reusing and extending Item Loaders
As your project grows bigger and acquires more and more spiders, maintenance becomes a fundamental problem,
especiallywhenyouhavetodealwithmanydifferentparsingrulesforeachspider,havingalotofexceptions,butalso
wantingtoreusethecommonprocessors.
ItemLoadersaredesignedtoeasethemaintenanceburdenofparsingrules,withoutlosingflexibilityand,atthesame
time, providing a convenient mechanism for extending and overriding them. For this reason Item Loaders support
traditionalPythonclassinheritancefordealingwithdifferencesofspecificspiders(orgroupsofspiders).
Suppose,forexample,thatsomeparticularsiteenclosestheirproductnamesinthreedashes(e.g. ---Plasma TV---)
andyoudon’twanttoendupscrapingthosedashesinthefinalproductnames.
Here’showyoucanremovethosedashesbyreusingandextendingthedefaultProductItemLoader(ProductLoader):
from itemloaders.processors import MapCompose
from myproject.ItemLoaders import ProductLoader
def strip_dashes(x):
return x.strip("-")
class SiteSpecificLoader(ProductLoader):
name_in = MapCompose(strip_dashes, ProductLoader.name_in)
AnothercasewhereextendingItemLoaderscanbeveryhelpfuliswhenyouhavemultiplesourceformats,forexample
XMLandHTML.IntheXMLversionyoumaywanttoremoveCDATAoccurrences. Here’sanexampleofhowtodo
it:
80 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
from itemloaders.processors import MapCompose
from myproject.ItemLoaders import ProductLoader
from myproject.utils.xml import remove_cdata
class XmlProductLoader(ProductLoader):
name_in = MapCompose(remove_cdata, ProductLoader.name_in)
Andthat’showyoutypicallyextendinputprocessors.
As for output processors, it is more common to declare them in the field metadata, as they usually depend only on
the field and not on each specific site parsing rule (as input processors do). See also: Declaring Input and Output
Processors.
There are many other possible ways to extend, inherit and override your Item Loaders, and different Item Loaders
hierarchies may fit better for different projects. Scrapy only provides the mechanism; it doesn’t impose any specific
organizationofyourLoaderscollection-that’suptoyouandyourproject’sneeds.
3.6 Scrapy shell
TheScrapyshellisaninteractiveshellwhereyoucantryanddebugyourscrapingcodeveryquickly,withouthaving
torunthespider. It’smeanttobeusedfortestingdataextractioncode,butyoucanactuallyuseitfortestinganykind
ofcodeasitisalsoaregularPythonshell.
The shell is used for testing XPath or CSS expressions and see how they work and what data they extract from the
webpagesyou’retryingtoscrape. Itallowsyoutointeractivelytestyourexpressionswhileyou’rewritingyourspider,
withouthavingtorunthespidertotesteverychange.
OnceyougetfamiliarizedwiththeScrapyshell, you’llseethatit’saninvaluabletoolfordevelopinganddebugging
yourspiders.
3.6.1 Configuring the shell
IfyouhaveIPythoninstalled,theScrapyshellwilluseit(insteadofthestandardPythonconsole). TheIPythonconsole
ismuchmorepowerfulandprovidessmartauto-completionandcolorizedoutput,amongotherthings.
WehighlyrecommendyouinstallIPython,speciallyifyou’reworkingonUnixsystems(whereIPythonexcels). See
theIPythoninstallationguideformoreinfo.
Scrapyalsohassupportforbpython,andwilltrytouseitwhereIPythonisunavailable.
Through Scrapy’s settings you can configure it to use any one of ipython, bpython or the standard python shell,
regardless of which are installed. This is done by setting the SCRAPY_PYTHON_SHELL environment variable; or by
definingitinyourscrapy.cfg:
[settings]
shell = bpython
3.6.2 Launch the shell
TolaunchtheScrapyshellyoucanusetheshellcommandlikethis:
scrapy shell <url>
Wherethe<url>istheURLyouwanttoscrape.
3.6. Scrapyshell 81

ScrapyDocumentation,Release2.13.3
shellalsoworksforlocalfiles. Thiscanbehandyifyouwanttoplayaroundwithalocalcopyofawebpage. shell
understandsthefollowingsyntaxesforlocalfiles:
# UNIX-style
scrapy shell ./path/to/file.html
scrapy shell ../other/path/to/file.html
scrapy shell /absolute/path/to/file.html
# File URI
scrapy shell file:///absolute/path/to/file.html
(cid:242) Note
When using relative file paths, be explicit and prepend them with ./ (or ../ when relevant). scrapy shell
index.htmlwillnotworkasonemightexpect(andthisisbydesign,notabug).
BecauseshellfavorsHTTPURLsoverFileURIs,andindex.htmlbeingsyntacticallysimilartoexample.com,
shellwilltreatindex.htmlasadomainnameandtriggeraDNSlookuperror:
$ scrapy shell index.html
[ ... scrapy shell starts ... ]
[ ... traceback ... ]
twisted.internet.error.DNSLookupError: DNS lookup failed:
address 'index.html' not found: [Errno -5] No address associated with hostname.
shellwillnottestbeforehandifafilecalledindex.htmlexistsinthecurrentdirectory. Again,beexplicit.
3.6.3 Using the shell
The Scrapy shell is just a regular Python console (or IPython console if you have it available) which provides some
additionalshortcutfunctionsforconvenience.
AvailableShortcuts
• shelp()-printahelpwiththelistofavailableobjectsandshortcuts
• fetch(url[, redirect=True]) - fetch a new response from the given URL and update all related objects
accordingly. YoucanoptionallyaskforHTTP3xxredirectionstonotbefollowedbypassingredirect=False
• fetch(request)-fetchanewresponsefromthegivenrequestandupdateallrelatedobjectsaccordingly.
• view(response)-openthegivenresponseinyourlocalwebbrowser,forinspection. Thiswilladda<base>
tagtotheresponsebodyinorderforexternallinks(suchasimagesandstylesheets)todisplayproperly. Note,
however,thatthiswillcreateatemporaryfileinyourcomputer,whichwon’tberemovedautomatically.
AvailableScrapyobjects
TheScrapyshellautomaticallycreatessomeconvenientobjectsfromthedownloadedpage,liketheResponseobject
andtheSelectorobjects(forbothHTMLandXMLcontent).
Thoseobjectsare:
• crawler-thecurrentCrawlerobject.
• spider-theSpiderwhichisknowntohandletheURL,oraSpider objectifthereisnospiderfoundforthe
currentURL
82 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
• request-aRequestobjectofthelastfetchedpage. Youcanmodifythisrequestusingreplace()orfetcha
newrequest(withoutleavingtheshell)usingthefetchshortcut.
• response-aResponseobjectcontainingthelastfetchedpage
• settings-thecurrentScrapysettings
3.6.4 Example of shell session
Here’sanexampleofatypicalshellsessionwherewestartbyscrapingthehttps://scrapy.orgpage,andthenproceedto
scrapethehttps://old.reddit.com/page. Finally,wemodifythe(Reddit)requestmethodtoPOSTandre-fetchitgetting
anerror. WeendthesessionbytypingCtrl-D(inUnixsystems)orCtrl-ZinWindows.
Keepinmindthatthedataextractedheremaynotbethesamewhenyoutryit,asthosepagesarenotstaticandcould
havechangedbythetimeyoutestthis. TheonlypurposeofthisexampleistogetyoufamiliarizedwithhowtheScrapy
shellworks.
First,welaunchtheshell:
scrapy shell 'https://scrapy.org' --nolog
(cid:242) Note
Remember to always enclose URLs in quotes when running the Scrapy shell from the command line, otherwise
URLscontainingarguments(i.e. the&character)willnotwork.
OnWindows,usedoublequotesinstead:
scrapy shell "https://scrapy.org" --nolog
Then, the shell fetches the URL (using the Scrapy downloader) and prints the list of available objects and useful
shortcuts(you’llnoticethattheselinesallstartwiththe[s]prefix):
[s] Available Scrapy objects:
[s] scrapy scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s] crawler <scrapy.crawler.Crawler object at 0x7f07395dd690>
[s] item {}
[s] request <GET https://scrapy.org>
[s] response <200 https://scrapy.org/>
[s] settings <scrapy.settings.Settings object at 0x7f07395dd710>
[s] spider <DefaultSpider 'default' at 0x7f0735891690>
[s] Useful shortcuts:
[s] fetch(url[, redirect=True]) Fetch URL and update local objects (by default,␣
redirects are followed)
˓→
[s] fetch(req) Fetch a scrapy.Request and update local objects
[s] shelp() Shell help (print this help)
[s] view(response) View response in a browser
>>>
Afterthat,wecanstartplayingwiththeobjects:
>>> response.xpath("//title/text()").get()
'Scrapy | A Fast and Powerful Scraping and Web Crawling Framework'
(continuesonnextpage)
3.6. Scrapyshell 83

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
>>> fetch("https://old.reddit.com/")
>>> response.xpath("//title/text()").get()
'reddit: the front page of the internet'
>>> request = request.replace(method="POST")
>>> fetch(request)
>>> response.status
404
>>> from pprint import pprint
>>> pprint(response.headers)
{'Accept-Ranges': ['bytes'],
'Cache-Control': ['max-age=0, must-revalidate'],
'Content-Type': ['text/html; charset=UTF-8'],
'Date': ['Thu, 08 Dec 2016 16:21:19 GMT'],
'Server': ['snooserv'],
'Set-Cookie': ['loid=KqNLou0V9SKMX4qb4n; Domain=reddit.com; Max-Age=63071999; Path=/;␣
expires=Sat, 08-Dec-2018 16:21:19 GMT; secure',
˓→
'loidcreated=2016-12-08T16%3A21%3A19.445Z; Domain=reddit.com; Max-
Age=63071999; Path=/; expires=Sat, 08-Dec-2018 16:21:19 GMT; secure',
˓→
'loid=vi0ZVe4NkxNWdlH7r7; Domain=reddit.com; Max-Age=63071999; Path=/;␣
expires=Sat, 08-Dec-2018 16:21:19 GMT; secure',
˓→
'loidcreated=2016-12-08T16%3A21%3A19.459Z; Domain=reddit.com; Max-
Age=63071999; Path=/; expires=Sat, 08-Dec-2018 16:21:19 GMT; secure'],
˓→
'Vary': ['accept-encoding'],
'Via': ['1.1 varnish'],
'X-Cache': ['MISS'],
'X-Cache-Hits': ['0'],
'X-Content-Type-Options': ['nosniff'],
'X-Frame-Options': ['SAMEORIGIN'],
'X-Moose': ['majestic'],
'X-Served-By': ['cache-cdg8730-CDG'],
'X-Timer': ['S1481214079.394283,VS0,VE159'],
'X-Ua-Compatible': ['IE=edge'],
'X-Xss-Protection': ['1; mode=block']}
3.6.5 Invoking the shell from spiders to inspect responses
Sometimesyouwanttoinspecttheresponsesthatarebeingprocessedinacertainpointofyourspider,ifonlytocheck
thatresponseyouexpectisgettingthere.
Thiscanbeachievedbyusingthescrapy.shell.inspect_responsefunction.
Here’sanexampleofhowyouwouldcallitfromyourspider:
import scrapy
class MySpider(scrapy.Spider):
(continuesonnextpage)
84 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
name = "myspider"
start_urls = [
"http://example.com",
"http://example.org",
"http://example.net",
]
def parse(self, response):
# We want to inspect one specific response.
if ".org" in response.url:
from scrapy.shell import inspect_response
inspect_response(response, self)
# Rest of parsing code.
Whenyourunthespider,youwillgetsomethingsimilartothis:
2014-01-23 17:48:31-0400 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://example.
com> (referer: None)
˓→
2014-01-23 17:48:31-0400 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://example.
org> (referer: None)
˓→
[s] Available Scrapy objects:
[s] crawler <scrapy.crawler.Crawler object at 0x1e16b50>
...
>>> response.url
'http://example.org'
Then,youcancheckiftheextractioncodeisworking:
>>> response.xpath('//h1[@class="fn"]')
[]
Nope,itdoesn’t. Soyoucanopentheresponseinyourwebbrowserandseeifit’stheresponseyouwereexpecting:
>>> view(response)
True
FinallyyouhitCtrl-D(orCtrl-ZinWindows)toexittheshellandresumethecrawling:
>>> ^D
2014-01-23 17:50:03-0400 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://example.
net> (referer: None)
˓→
...
Notethatyoucan’tusethe fetchshortcutheresincetheScrapyengineisblockedbytheshell. However, afteryou
leavetheshell,thespiderwillcontinuecrawlingwhereitstopped,asshownabove.
3.6. Scrapyshell 85

ScrapyDocumentation,Release2.13.3
3.7 Item Pipeline
Afteranitemhasbeenscrapedbyaspider,itissenttotheItemPipelinewhichprocessesitthroughseveralcomponents
thatareexecutedsequentially.
Eachitempipelinecomponent(sometimesreferredasjust“ItemPipeline”)isaPythonclassthatimplementsasimple
method. They receive an item and perform an action over it, also deciding if the item should continue through the
pipelineorbedroppedandnolongerprocessed.
Typicalusesofitempipelinesare:
• cleansingHTMLdata
• validatingscrapeddata(checkingthattheitemscontaincertainfields)
• checkingforduplicates(anddroppingthem)
• storingthescrapediteminadatabase
3.7.1 Writing your own item pipeline
Eachitempipelineisacomponentthatmustimplementthefollowingmethod:
process_item(self,item,spider)
Thismethodiscalledforeveryitempipelinecomponent.
itemisanitemobject,seeSupportingAllItemTypes.
process_item()musteither: returnanitemobject,returnaDeferredorraiseaDropItem exception.
Droppeditemsarenolongerprocessedbyfurtherpipelinecomponents.
Parameters
• item(itemobject)–thescrapeditem
• spider(Spiderobject)–thespiderwhichscrapedtheitem
Additionally,theymayalsoimplementthefollowingmethods:
open_spider(self,spider)
Thismethodiscalledwhenthespiderisopened.
Parameters
spider(Spiderobject)–thespiderwhichwasopened
close_spider(self,spider)
Thismethodiscalledwhenthespiderisclosed.
Parameters
spider(Spiderobject)–thespiderwhichwasclosed
3.7.2 Item pipeline example
Pricevalidationanddroppingitemswithnoprices
Let’s take a look at the following hypothetical pipeline that adjusts the price attribute for those items that do not
includeVAT(price_excludes_vatattribute),anddropsthoseitemswhichdon’tcontainaprice:
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
(continuesonnextpage)
86 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class PricePipeline:
vat_factor = 1.15
def process_item(self, item, spider):
adapter = ItemAdapter(item)
if adapter.get("price"):
if adapter.get("price_excludes_vat"):
adapter["price"] = adapter["price"] * self.vat_factor
return item
else:
raise DropItem("Missing price")
WriteitemstoaJSONlinesfile
Thefollowingpipelinestoresallscrapeditems(fromallspiders)intoasingleitems.jsonlfile,containingoneitem
perlineserializedinJSONformat:
import json
from itemadapter import ItemAdapter
class JsonWriterPipeline:
def open_spider(self, spider):
self.file = open("items.jsonl", "w")
def close_spider(self, spider):
self.file.close()
def process_item(self, item, spider):
line = json.dumps(ItemAdapter(item).asdict()) + "\n"
self.file.write(line)
return item
(cid:242) Note
ThepurposeofJsonWriterPipelineisjusttointroducehowtowriteitempipelines. Ifyoureallywanttostoreall
scrapeditemsintoaJSONfileyoushouldusetheFeedexports.
WriteitemstoMongoDB
Inthisexamplewe’llwriteitemstoMongoDBusingpymongo. MongoDBaddressanddatabasenamearespecifiedin
Scrapysettings;MongoDBcollectionisnamedafteritemclass.
Themainpointofthisexampleistoshowhowtogetthecrawlerandhowtocleanuptheresourcesproperly.
import pymongo
from itemadapter import ItemAdapter
(continuesonnextpage)
3.7. ItemPipeline 87

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class MongoPipeline:
collection_name = "scrapy_items"
def __init__(self, mongo_uri, mongo_db):
self.mongo_uri = mongo_uri
self.mongo_db = mongo_db
@classmethod
def from_crawler(cls, crawler):
return cls(
mongo_uri=crawler.settings.get("MONGO_URI"),
mongo_db=crawler.settings.get("MONGO_DATABASE", "items"),
)
def open_spider(self, spider):
self.client = pymongo.MongoClient(self.mongo_uri)
self.db = self.client[self.mongo_db]
def close_spider(self, spider):
self.client.close()
def process_item(self, item, spider):
self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
return item
Takescreenshotofitem
Thisexampledemonstrateshowtousecoroutinesyntaxintheprocess_item()method.
Thisitempipelinemakesarequesttoalocally-runninginstanceofSplashtorenderascreenshotoftheitemURL.After
therequestresponseisdownloaded,theitempipelinesavesthescreenshottoafileandaddsthefilenametotheitem.
import hashlib
from pathlib import Path
from urllib.parse import quote
import scrapy
from itemadapter import ItemAdapter
from scrapy.http.request import NO_CALLBACK
from scrapy.utils.defer import maybe_deferred_to_future
class ScreenshotPipeline:
"""Pipeline that uses Splash to render screenshot of
every Scrapy item."""
SPLASH_URL = "http://localhost:8050/render.png?url={}"
async def process_item(self, item, spider):
adapter = ItemAdapter(item)
encoded_item_url = quote(adapter["url"])
screenshot_url = self.SPLASH_URL.format(encoded_item_url)
(continuesonnextpage)
88 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
request = scrapy.Request(screenshot_url, callback=NO_CALLBACK)
response = await maybe_deferred_to_future(
spider.crawler.engine.download(request)
)
if response.status != 200:
# Error happened, return item.
return item
# Save screenshot to file, filename will be hash of url.
url = adapter["url"]
url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
filename = f"{url_hash}.png"
Path(filename).write_bytes(response.body)
# Store filename in item.
adapter["screenshot_filename"] = filename
return item
Duplicatesfilter
Afilterthatlooksforduplicateitems,anddropsthoseitemsthatwerealreadyprocessed. Let’ssaythatouritemshave
auniqueid,butourspiderreturnsmultiplesitemswiththesameid:
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
class DuplicatesPipeline:
def __init__(self):
self.ids_seen = set()
def process_item(self, item, spider):
adapter = ItemAdapter(item)
if adapter["id"] in self.ids_seen:
raise DropItem(f"Item ID already seen: {adapter['id']}")
else:
self.ids_seen.add(adapter["id"])
return item
3.7.3 Activating an Item Pipeline component
ToactivateanItemPipelinecomponentyoumustadditsclasstotheITEM_PIPELINES setting,likeinthefollowing
example:
ITEM_PIPELINES = {
"myproject.pipelines.PricePipeline": 300,
"myproject.pipelines.JsonWriterPipeline": 800,
}
Theintegervaluesyouassigntoclassesinthissettingdeterminetheorderinwhichtheyrun: itemsgothroughfrom
lowervaluedtohighervaluedclasses. It’scustomarytodefinethesenumbersinthe0-1000range.
3.7. ItemPipeline 89

ScrapyDocumentation,Release2.13.3
3.8 Feed exports
Oneofthemostfrequentlyrequiredfeatureswhenimplementingscrapersisbeingabletostorethescrapeddataproperly
and,quiteoften,thatmeansgeneratingan“exportfile”withthescrapeddata(commonlycalled“exportfeed”)tobe
consumedbyothersystems.
ScrapyprovidesthisfunctionalityoutoftheboxwiththeFeedExports,whichallowsyoutogeneratefeedswiththe
scrapeditems,usingmultipleserializationformatsandstoragebackends.
This page provides detailed documentation for all feed export features. If you are looking for a step-by-step guide,
checkoutZyte’sexportguides.
3.8.1 Serialization formats
Forserializingthescrapeddata,thefeedexportsusetheItemexporters. Theseformatsaresupportedoutofthebox:
• JSON
• JSONlines
• CSV
• XML
ButyoucanalsoextendthesupportedformatthroughtheFEED_EXPORTERS setting.
JSON
• ValuefortheformatkeyintheFEEDS setting: json
• Exporterused: JsonItemExporter
• Seethiswarningifyou’reusingJSONwithlargefeeds.
JSONlines
• ValuefortheformatkeyintheFEEDS setting: jsonlines
• Exporterused: JsonLinesItemExporter
CSV
• ValuefortheformatkeyintheFEEDS setting: csv
• Exporterused: CsvItemExporter
• Tospecifycolumnstoexport,theirorderandtheircolumnnames,useFEED_EXPORT_FIELDS.Otherfeedex-
porterscanalsousethisoption,butitisimportantforCSVbecauseunlikemanyotherexportformatsCSVuses
afixedheader.
XML
• ValuefortheformatkeyintheFEEDS setting: xml
• Exporterused: XmlItemExporter
Pickle
• ValuefortheformatkeyintheFEEDS setting: pickle
• Exporterused: PickleItemExporter
90 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Marshal
• ValuefortheformatkeyintheFEEDS setting: marshal
• Exporterused: MarshalItemExporter
3.8.2 Storages
WhenusingthefeedexportsyoudefinewheretostorethefeedusingoneormultipleURIs(throughtheFEEDSsetting).
ThefeedexportssupportsmultiplestoragebackendtypeswhicharedefinedbytheURIscheme.
Thestoragesbackendssupportedoutoftheboxare:
• Localfilesystem
• FTP
• S3(requiresboto3)
• GoogleCloudStorage(GCS)(requiresgoogle-cloud-storage)
• Standardoutput
Some storage backends may be unavailable if the required external libraries are not available. For example, the S3
backendisonlyavailableiftheboto3libraryisinstalled.
3.8.3 Storage URI parameters
ThestorageURIcanalsocontainparametersthatgetreplacedwhenthefeedisbeingcreated. Theseparametersare:
• %(time)s-getsreplacedbyatimestampwhenthefeedisbeingcreated
• %(name)s-getsreplacedbythespidername
Anyothernamedparametergetsreplacedbythespiderattributeofthesamename. Forexample,%(site_id)swould
getreplacedbythespider.site_idattributethemomentthefeedisbeingcreated.
Herearesomeexamplestoillustrate:
• StoreinFTPusingonedirectoryperspider:
– ftp://user:password@ftp.example.com/scraping/feeds/%(name)s/%(time)s.json
• StoreinS3usingonedirectoryperspider:
– s3://mybucket/scraping/feeds/%(name)s/%(time)s.json
(cid:242) Note
Spiderargumentsbecomespiderattributes,hencetheycanalsobeusedasstorageURIparameters.
3.8.4 Storage backends
Localfilesystem
Thefeedsarestoredinthelocalfilesystem.
• URIscheme: file
• ExampleURI:file:///tmp/export.csv
• Requiredexternallibraries: none
3.8. Feedexports 91

ScrapyDocumentation,Release2.13.3
Notethatforthelocalfilesystemstorage(only)youcanomittheschemeifyouspecifyanabsolutepathlike /tmp/
export.csv(Unixsystemsonly). Alternativelyyoucanalsouseapathlib.Pathobject.
FTP
ThefeedsarestoredinaFTPserver.
• URIscheme: ftp
• ExampleURI:ftp://user:pass@ftp.example.com/path/to/export.csv
• Requiredexternallibraries: none
FTPsupportstwodifferentconnectionmodes: activeorpassive. Scrapyusesthepassiveconnectionmodebydefault.
Tousetheactiveconnectionmodeinstead,settheFEED_STORAGE_FTP_ACTIVE settingtoTrue.
ThedefaultvaluefortheoverwritekeyintheFEEDS forthisstoragebackendis: True.
‡ Caution
ThevalueTrueinoverwritewillcauseyoutolosethepreviousversionofyourdata.
Thisstoragebackendusesdelayedfiledelivery.
S3
ThefeedsarestoredonAmazonS3.
• URIscheme: s3
• ExampleURIs:
– s3://mybucket/path/to/export.csv
– s3://aws_key:aws_secret@mybucket/path/to/export.csv
• Requiredexternallibraries: boto3>=1.20.0
TheAWScredentialscanbepassedasuser/passwordintheURI,ortheycanbepassedthroughthefollowingsettings:
• AWS_ACCESS_KEY_ID
• AWS_SECRET_ACCESS_KEY
• AWS_SESSION_TOKEN (onlyneededfortemporarysecuritycredentials)
YoucanalsodefineacustomACL,customendpoint,andregionnameforexportedfeedsusingthesesettings:
• FEED_STORAGE_S3_ACL
• AWS_ENDPOINT_URL
• AWS_REGION_NAME
ThedefaultvaluefortheoverwritekeyintheFEEDS forthisstoragebackendis: True.
‡ Caution
ThevalueTrueinoverwritewillcauseyoutolosethepreviousversionofyourdata.
Thisstoragebackendusesdelayedfiledelivery.
92 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
GoogleCloudStorage(GCS)
Addedinversion2.3.
ThefeedsarestoredonGoogleCloudStorage.
• URIscheme: gs
• ExampleURIs:
– gs://mybucket/path/to/export.csv
• Requiredexternallibraries: google-cloud-storage.
Formoreinformationaboutauthentication,pleaserefertoGoogleClouddocumentation.
YoucansetaProjectIDandAccessControlList(ACL)throughthefollowingsettings:
• FEED_STORAGE_GCS_ACL
• GCS_PROJECT_ID
ThedefaultvaluefortheoverwritekeyintheFEEDS forthisstoragebackendis: True.
‡ Caution
ThevalueTrueinoverwritewillcauseyoutolosethepreviousversionofyourdata.
Thisstoragebackendusesdelayedfiledelivery.
Standardoutput
ThefeedsarewrittentothestandardoutputoftheScrapyprocess.
• URIscheme: stdout
• ExampleURI:stdout:
• Requiredexternallibraries: none
Delayedfiledelivery
Asindicatedabove,someofthedescribedstoragebackendsusedelayedfiledelivery.
ThesestoragebackendsdonotuploaditemstothefeedURIasthoseitemsarescraped. Instead,Scrapywritesitems
intoatemporarylocalfile,andonlyonceallthefilecontentshavebeenwritten(i.e. attheendofthecrawl)isthatfile
uploadedtothefeedURI.
If you want item delivery to start earlier when using one of these storage backends, use
FEED_EXPORT_BATCH_ITEM_COUNT to split the output items in multiple files, with the specified maximum
itemcountperfile. Thatway,assoonasafilereachesthemaximumitemcount,thatfileisdeliveredtothefeedURI,
allowingitemdeliverytostartwaybeforetheendofthecrawl.
3.8.5 Item filtering
Addedinversion2.6.0.
Youcanfilteritemsthatyouwanttoallowforaparticularfeedbyusingtheitem_classesoptioninfeedsoptions.
Onlyitemsofthespecifiedtypeswillbeaddedtothefeed.
Theitem_classesoptionisimplementedbytheItemFilterclass,whichisthedefaultvalueoftheitem_filter
feedoption.
3.8. Feedexports 93

ScrapyDocumentation,Release2.13.3
You can create your own custom filtering class by implementing ItemFilter’s method accepts and taking
feed_optionsasanargument.
Forinstance:
class MyCustomFilter:
def __init__(self, feed_options):
self.feed_options = feed_options
def accepts(self, item):
if "field1" in item and item["field1"] == "expected_data":
return True
return False
Youcanassignyourcustomfilteringclasstotheitem_filteroptionofafeed. SeeFEEDS forexamples.
ItemFilter
class scrapy.extensions.feedexport.ItemFilter(feed_options: dict[str,Any]|None)
ThiswillbeusedbyFeedExportertodecideifanitemshouldbeallowedtobeexportedtoaparticularfeed.
Parameters
feed_options(dict)–feedspecificoptionspassedfromFeedExporter
accepts(item: Any)→bool
ReturnTrueifitemshouldbeexportedorFalseotherwise.
Parameters
item(Scrapyitems)–scrapeditemwhichuserwantstocheckifisacceptable
Returns
Trueifaccepted,Falseotherwise
Returntype
bool
3.8.6 Post-Processing
Addedinversion2.6.0.
Scrapyprovidesanoptiontoactivatepluginstopost-processfeedsbeforetheyareexportedtofeedstorages. Inaddition
tousingbuiltinplugins,youcancreateyourownplugins.
These plugins can be activated through the postprocessing option of a feed. The option must be passed a list of
post-processing plugins in the order you want the feed to be processed. These plugins can be declared either as an
importstringorwiththeimportedclassoftheplugin. Parameterstopluginscanbepassedthroughthefeedoptions.
Seefeedoptionsforexamples.
Built-inPlugins
class scrapy.extensions.postprocessing.GzipPlugin(file: BinaryIO,feed_options: dict[str,Any])
Compressesreceiveddatausinggzip.
Acceptedfeed_optionsparameters:
• gzip_compresslevel
• gzip_mtime
• gzip_filename
94 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Seegzip.GzipFileformoreinfoaboutparameters.
class scrapy.extensions.postprocessing.LZMAPlugin(file: BinaryIO,feed_options: dict[str,Any])
Compressesreceiveddatausinglzma.
Acceptedfeed_optionsparameters:
• lzma_format
• lzma_check
• lzma_preset
• lzma_filters
(cid:242) Note
lzma_filterscannotbeusedinpypyversion7.3.1andolder.
Seelzma.LZMAFileformoreinfoaboutparameters.
class scrapy.extensions.postprocessing.Bz2Plugin(file: BinaryIO,feed_options: dict[str,Any])
Compressesreceiveddatausingbz2.
Acceptedfeed_optionsparameters:
• bz2_compresslevel
Seebz2.BZ2Fileformoreinfoaboutparameters.
CustomPlugins
Eachpluginisaclassthatmustimplementthefollowingmethods:
__init__(self,file,feed_options)
Initializetheplugin.
Parameters
• file–file-likeobjecthavingatleastthewrite,tellandclosemethodsimplemented
• feed_options(dict)–feed-specificoptions
write(self,data)
Process and write data (bytes or memoryview) into the plugin’s target file. It must return number of bytes
written.
close(self)
Cleanuptheplugin.
Forexample,youmightwanttocloseafilewrapperthatyoumighthaveusedtocompressdatawrittenintothe
filereceivedinthe__init__method.
. Warning
Donotclosethefilefromthe__init__method.
Topassaparametertoyourplugin,usefeedoptions. Youcanthenaccessthoseparametersfromthe__init__method
ofyourplugin.
3.8. Feedexports 95

ScrapyDocumentation,Release2.13.3
3.8.7 Settings
Thesearethesettingsusedforconfiguringthefeedexports:
• FEEDS (mandatory)
• FEED_EXPORT_ENCODING
• FEED_STORE_EMPTY
• FEED_EXPORT_FIELDS
• FEED_EXPORT_INDENT
• FEED_STORAGES
• FEED_STORAGE_FTP_ACTIVE
• FEED_STORAGE_S3_ACL
• FEED_EXPORTERS
• FEED_EXPORT_BATCH_ITEM_COUNT
FEEDS
Addedinversion2.1.
Default: {}
A dictionary in which every key is a feed URI (or a pathlib.Path object) and each value is a nested dictionary
containingconfigurationparametersforthespecificfeed.
Thissettingisrequiredforenablingthefeedexportfeature.
SeeStoragebackendsforsupportedURIschemes.
Forinstance:
{
'items.json': {
'format': 'json',
'encoding': 'utf8',
'store_empty': False,
'item_classes': [MyItemClass1, 'myproject.items.MyItemClass2'],
'fields': None,
'indent': 4,
'item_export_kwargs': {
'export_empty_fields': True,
},
},
'/home/user/documents/items.xml': {
'format': 'xml',
'fields': ['name', 'price'],
'item_filter': MyCustomFilter1,
'encoding': 'latin1',
'indent': 8,
},
pathlib.Path('items.csv.gz'): {
'format': 'csv',
'fields': ['price', 'name'],
'item_filter': 'myproject.filters.MyCustomFilter2',
(continuesonnextpage)
96 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
'postprocessing': [MyPlugin1, 'scrapy.extensions.postprocessing.GzipPlugin'],
'gzip_compresslevel': 5,
},
}
Thefollowingisalistoftheacceptedkeysandthesettingthatisusedasafallbackvalueifthatkeyisnotprovidedfor
aspecificfeeddefinition:
• format: theserializationformat.
Thissettingismandatory,thereisnofallbackvalue.
• batch_item_count: fallsbacktoFEED_EXPORT_BATCH_ITEM_COUNT.
Addedinversion2.3.0.
• encoding: fallsbacktoFEED_EXPORT_ENCODING.
• fields: fallsbacktoFEED_EXPORT_FIELDS.
• item_classes: listofitemclassestoexport.
Ifundefinedorempty,allitemsareexported.
Addedinversion2.6.0.
• item_filter: afilterclasstofilteritemstoexport.
ItemFilterisusedbedefault.
Addedinversion2.6.0.
• indent: fallsbacktoFEED_EXPORT_INDENT.
• item_export_kwargs: dictwithkeywordargumentsforthecorrespondingitemexporterclass.
Addedinversion2.4.0.
• overwrite: whethertooverwritethefileifitalreadyexists(True)orappendtoitscontent(False).
Thedefaultvaluedependsonthestoragebackend:
– Localfilesystem: False
– FTP:True
(cid:242) Note
SomeFTPserversmaynotsupportappendingtofiles(theAPPEFTPcommand).
– S3: True(appendingisnotsupported)
– GoogleCloudStorage(GCS):True(appendingisnotsupported)
– Standardoutput: False(overwritingisnotsupported)
Addedinversion2.4.0.
• store_empty: fallsbacktoFEED_STORE_EMPTY.
• uri_params: fallsbacktoFEED_URI_PARAMS.
3.8. Feedexports 97

ScrapyDocumentation,Release2.13.3
• postprocessing: listofpluginstouseforpost-processing.
Thepluginswillbeusedintheorderofthelistpassed.
Addedinversion2.6.0.
FEED_EXPORT_ENCODING
Default: "utf-8"(fallback: None)
Theencodingtobeusedforthefeed.
IfsettoNone,itusesUTF-8foreverythingexceptJSONoutput,whichusessafenumericencoding(\uXXXXsequences)
forhistoricreasons.
Use"utf-8"ifyouwantUTF-8forJSONtoo.
Changedinversion2.8:Thestartprojectcommandnowsetsthissettingto"utf-8"inthegeneratedsettings.py
file.
FEED_EXPORT_FIELDS
Default: None
Use the FEED_EXPORT_FIELDS setting to define the fields to export, their order and their output names. See
BaseItemExporter.fields_to_exportformoreinformation.
FEED_EXPORT_INDENT
Default: 0
Amountofspacesusedtoindenttheoutputoneachlevel. If FEED_EXPORT_INDENTisanon-negativeinteger, then
arrayelementsandobjectmemberswillbepretty-printedwiththatindentlevel. Anindentlevelof 0(thedefault),or
negative,willputeachitemonanewline. Noneselectsthemostcompactrepresentation.
CurrentlyimplementedonlybyJsonItemExporter andXmlItemExporter,i.e. whenyouareexportingto.json
or.xml.
FEED_STORE_EMPTY
Default: True
Whethertoexportemptyfeeds(i.e. feedswithnoitems). If False,andtherearenoitemstoexport,nonewfilesare
createdandexistingfilesarenotmodified,eveniftheoverwritefeedoptionisenabled.
FEED_STORAGES
Default: {}
Adictcontainingadditionalfeedstoragebackendssupportedbyyourproject. ThekeysareURIschemesandthevalues
arepathstostorageclasses.
FEED_STORAGE_FTP_ACTIVE
Default: False
WhethertousetheactiveconnectionmodewhenexportingfeedstoanFTPserver(True)orusethepassiveconnection
modeinstead(False,default).
ForinformationaboutFTPconnectionmodes,seeWhatisthedifferencebetweenactiveandpassiveFTP?.
98 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
FEED_STORAGE_S3_ACL
Default: '' (emptystring)
AstringcontainingacustomACLforfeedsexportedtoAmazonS3byyourproject.
Foracompletelistofavailablevalues,accesstheCannedACLsectiononAmazonS3docs.
FEED_STORAGES_BASE
Default:
{
"": "scrapy.extensions.feedexport.FileFeedStorage",
"file": "scrapy.extensions.feedexport.FileFeedStorage",
"stdout": "scrapy.extensions.feedexport.StdoutFeedStorage",
"s3": "scrapy.extensions.feedexport.S3FeedStorage",
"ftp": "scrapy.extensions.feedexport.FTPFeedStorage",
}
Adictcontainingthebuilt-infeedstoragebackendssupportedbyScrapy. Youcandisableanyofthesebackendsby
assigning None to their URI scheme in FEED_STORAGES. E.g., to disable the built-in FTP storage backend (without
replacement),placethisinyoursettings.py:
FEED_STORAGES = {
"ftp": None,
}
FEED_EXPORTERS
Default: {}
Adictcontainingadditionalexporterssupportedbyyourproject. Thekeysareserializationformatsandthevaluesare
pathstoItemexporterclasses.
FEED_EXPORTERS_BASE
Default:
{
"json": "scrapy.exporters.JsonItemExporter",
"jsonlines": "scrapy.exporters.JsonLinesItemExporter",
"jsonl": "scrapy.exporters.JsonLinesItemExporter",
"jl": "scrapy.exporters.JsonLinesItemExporter",
"csv": "scrapy.exporters.CsvItemExporter",
"xml": "scrapy.exporters.XmlItemExporter",
"marshal": "scrapy.exporters.MarshalItemExporter",
"pickle": "scrapy.exporters.PickleItemExporter",
}
Adictcontainingthebuilt-infeedexporterssupportedbyScrapy. Youcandisableanyoftheseexportersbyassigning
NonetotheirserializationformatinFEED_EXPORTERS.E.g.,todisablethebuilt-inCSVexporter(withoutreplacement),
placethisinyoursettings.py:
FEED_EXPORTERS = {
"csv": None,
}
3.8. Feedexports 99

ScrapyDocumentation,Release2.13.3
FEED_EXPORT_BATCH_ITEM_COUNT
Addedinversion2.3.0.
Default: 0
Ifassignedanintegernumberhigherthan0,Scrapygeneratesmultipleoutputfilesstoringuptothespecifiednumber
ofitemsineachoutputfile.
When generating multiple output files, you must use at least one of the following placeholders in the feed URI to
indicatehowthedifferentoutputfilenamesaregenerated:
• %(batch_time)s-getsreplacedbyatimestampwhenthefeedisbeingcreated(e.g. 2020-03-28T14-45-08.
237134)
• %(batch_id)d-getsreplacedbythe1-basedsequencenumberofthebatch.
Useprintf-stylestringformattingtoalterthenumberformat. Forexample,tomakethebatchIDa5-digitnumber
byintroducingleadingzeroesasneeded,use%(batch_id)05d(e.g. 3becomes00003,123becomes00123).
Forinstance,ifyoursettingsinclude:
FEED_EXPORT_BATCH_ITEM_COUNT = 100
Andyourcrawlcommandlineis:
scrapy crawl spidername -o "dirname/%(batch_id)d-filename%(batch_time)s.json"
Thecommandlineabovecangenerateadirectorytreelike:
->projectname
-->dirname
--->1-filename2020-03-28T14-45-08.237134.json
--->2-filename2020-03-28T14-45-09.148903.json
--->3-filename2020-03-28T14-45-10.046092.json
Wherethefirstandsecondfilescontainexactly100items. Thelastonecontains100itemsorfewer.
FEED_URI_PARAMS
Default: None
Astringwiththeimportpathofafunctiontosettheparameterstoapplywithprintf-stylestringformattingtothefeed
URI.
Thefunctionsignatureshouldbeasfollows:
scrapy.extensions.feedexport.uri_params(params,spider)
Returnadictofkey-valuepairstoapplytothefeedURIusingprintf-stylestringformatting.
Parameters
• params(dict)–defaultkey-valuepairs
Specifically:
– batch_id: IDofthefilebatch. SeeFEED_EXPORT_BATCH_ITEM_COUNT.
IfFEED_EXPORT_BATCH_ITEM_COUNT is0,batch_idisalways1.
Addedinversion2.3.0.
100 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
– batch_time: UTCdateandtime,inISOformatwith: replacedwith-.
SeeFEED_EXPORT_BATCH_ITEM_COUNT.
Addedinversion2.3.0.
– time: batch_time,withmicrosecondssetto0.
• spider(scrapy.Spider)–sourcespiderofthefeeditems
‡ Caution
Thefunctionshouldreturnanewdictionary,modifyingthereceivedparamsin-placeisdeprecated.
Forexample,toincludethenameofthesourcespiderinthefeedURI:
1. Definethefollowingfunctionsomewhereinyourproject:
# myproject/utils.py
def uri_params(params, spider):
return {**params, "spider_name": spider.name}
2. PointFEED_URI_PARAMS tothatfunctioninyoursettings:
# myproject/settings.py
FEED_URI_PARAMS = "myproject.utils.uri_params"
3. Use%(spider_name)sinyourfeedURI:
scrapy crawl <spider_name> -o "%(spider_name)s.jsonl"
3.9 Requests and Responses
ScrapyusesRequestandResponseobjectsforcrawlingwebsites.
Typically, Request objectsaregeneratedinthespidersandpassacrossthesystemuntiltheyreachtheDownloader,
whichexecutestherequestandreturnsaResponseobjectwhichtravelsbacktothespiderthatissuedtherequest.
BothRequestandResponseclasseshavesubclasseswhichaddfunctionalitynotrequiredinthebaseclasses. These
aredescribedbelowinRequestsubclassesandResponsesubclasses.
3.9.1 Request objects
class scrapy.Request(*args: Any,**kwargs: Any)
Represents an HTTP request, which is usually generated in a Spider and executed by the Downloader, thus
generatingaResponse.
Parameters
• url(str)–theURLofthisrequest
IftheURLisinvalid,aValueErrorexceptionisraised.
• callback (Callable[Concatenate[Response, ...], Any] | None) – sets
callback,defaultstoNone.
Changed in version 2.0: The callback parameter is no longer required when the errback
parameterisspecified.
3.9. RequestsandResponses 101

ScrapyDocumentation,Release2.13.3
• method(str)–theHTTPmethodofthisrequest. Defaultsto'GET'.
• meta(dict)–theinitialvaluesfortheRequest.meta attribute. Ifgiven,thedictpassed
inthisparameterwillbeshallowcopied.
• body(bytes or str)–therequestbody. Ifastringispassed,thenit’sencodedasbytes
usingtheencodingpassed(whichdefaultstoutf-8). If bodyisnotgiven,anemptybytes
objectisstored. Regardlessofthetypeofthisargument,thefinalvaluestoredwillbeabytes
object(neverastringorNone).
• headers (dict) – the headers of this request. The dict values can be strings (for single
valued headers) or lists (for multi-valued headers). If None is passed as value, the HTTP
headerwillnotbesentatall.
‡ Caution
CookiessetviatheCookieheaderarenotconsideredbytheCookiesMiddleware. Ifyou
need to set cookies for a request, use the cookies argument. This is a known current
limitationthatisbeingworkedon.
• cookies(dict or list)–therequestcookies. Thesecanbesentintwoforms.
1. Usingadict:
request_with_cookies = Request(
url="http://www.example.com",
cookies={"currency": "USD", "country": "UY"},
)
2. Usingalistofdicts:
request_with_cookies = Request(
url="https://www.example.com",
cookies=[
{
"name": "currency",
"value": "USD",
"domain": "example.com",
"path": "/currency",
"secure": True,
},
],
)
Thelatterformallowsforcustomizingthedomainandpathattributesofthecookie. This
isonlyusefulifthecookiesaresavedforlaterrequests. Whensomesitereturnscookies(in
aresponse)thosearestoredinthecookiesforthatdomainandwillbesentagaininfuture
requests. That’sthetypicalbehaviourofanyregularwebbrowser.
Notethatsettingthedont_merge_cookieskeytoTrueinrequest.meta causescustom
cookiestobeignored.
FormoreinfoseeCookiesMiddleware.
102 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
‡ Caution
CookiessetviatheCookieheaderarenotconsideredbytheCookiesMiddleware. Ifyou
needtosetcookiesforarequest, usethescrapy.Request.cookies parameter. This
isaknowncurrentlimitationthatisbeingworkedon.
Addedinversion2.6.0: Cookievaluesthatarebool,floatorintarecastedtostr.
• encoding(str)–theencodingofthisrequest(defaultsto'utf-8'). Thisencodingwill
beusedtopercent-encodetheURLandtoconvertthebodytobytes(ifgivenasastring).
• priority(int)–setspriority,defaultsto0.
• dont_filter(bool)–setsdont_filter,defaultstoFalse.
• errback(Callable[[Failure], Any] | None)–setserrback,defaultstoNone.
Changed in version 2.0: The callback parameter is no longer required when the errback
parameterisspecified.
• flags(list)–Flagssenttotherequest,canbeusedforloggingorsimilarpurposes.
• cb_kwargs(dict)–Adictwitharbitrarydatathatwillbepassedaskeywordargumentsto
theRequest’scallback.
url
AstringcontainingtheURLofthisrequest. KeepinmindthatthisattributecontainstheescapedURL,so
itcandifferfromtheURLpassedinthe__init__()method.
Thisattributeisread-only. TochangetheURLofaRequestusereplace().
method
A string representing the HTTP method in the request. This is guaranteed to be uppercase. Example:
"GET","POST","PUT",etc
headers
Adictionary-like(scrapy.http.headers.Headers)objectwhichcontainstherequestheaders.
body
Therequestbodyasbytes.
Thisattributeisread-only. TochangethebodyofaRequestusereplace().
callback: CallbackT | None
CallabletoparsetheResponsetothisrequestoncereceived.
Thecallablemustexpecttheresponseasitsfirstparameter,andsupportanyadditionalkeywordarguments
setthroughcb_kwargs.
Inadditiontoanarbitrarycallable,thefollowingvaluesarealsosupported:
• None(default),whichindicatesthattheparse()methodofthespidermustbeused.
• NO_CALLBACK().
If an unhandled exception is raised during request or response processing, i.e. by a spider middleware,
downloadermiddlewareordownloadhandler(DOWNLOAD_HANDLERS),errback iscalledinstead.
3.9. RequestsandResponses 103

ScrapyDocumentation,Release2.13.3
(cid:17) Tip
HttpErrorMiddleware raises exceptions for non-2xx responses by default, sending them to the
errback instead.
ª Seealso
Passingadditionaldatatocallbackfunctions
errback: Callable[[Failure], Any] | None
Callabletohandleexceptionsraisedduringrequestorresponseprocessing.
ThecallablemustexpectaFailureasitsfirstparameter.
ª Seealso
Usingerrbackstocatchexceptionsinrequestprocessing
priority: int
Default: 0
Valuethattheschedulermayuseforrequestprioritization.
Built-inschedulersprioritizerequestswithahigherpriorityvalue.
Negativevaluesareallowed.
cb_kwargs
Adictionarythatcontainsarbitrarymetadataforthisrequest. ItscontentswillbepassedtotheRequest’s
callbackaskeywordarguments. ItisemptyfornewRequests,whichmeansbydefaultcallbacksonlygeta
Responseobjectasargument.
Thisdictisshallowcopiedwhentherequestisclonedusingthecopy()orreplace()methods,andcan
alsobeaccessed,inyourspider,fromtheresponse.cb_kwargsattribute.
Incaseofafailuretoprocesstherequest,thisdictcanbeaccessedasfailure.request.cb_kwargsin
therequest’serrback. Formoreinformation,seeAccessingadditionaldatainerrbackfunctions.
meta = {}
Adictionaryofarbitrarymetadatafortherequest.
Youmayextendrequestmetadataasyouseefit.
Requestmetadatacanalsobeaccessedthroughthemeta attributeofaresponse.
Topassdatafromonespidercallbacktoanother,considerusingcb_kwargs instead. However,
requestmetadatamaybetherightchoiceincertainscenarios,suchastomaintainsomedebugging
dataacrossallfollow-uprequests(e.g. thesourceURL).
A common use of request metadata is to define request-specific parameters for Scrapy com-
ponents (extensions, middlewares, etc.). For example, if you set dont_retry to True,
RetryMiddlewarewillneverretrythatrequest,evenifitfails. SeeRequest.metaspecialkeys.
104 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
You may also use request metadata in your custom Scrapy components, for example, to keep
requeststateinformationrelevanttoyourcomponent. Forexample,RetryMiddlewareusesthe
retry_timesmetadatakeytokeeptrackofhowmanytimesarequesthasbeenretriedsofar.
Copyingallthemetadataofapreviousrequestintoanew,follow-uprequestinaspidercallback
isabadpractice,becauserequestmetadatamayincludemetadatasetbyScrapycomponentsthat
isnotmeanttobecopiedintootherrequests. Forexample,copyingtheretry_timesmetadata
keyintofollow-uprequestscanlowertheamountofretriesallowedforthosefollow-uprequests.
Youshouldonlycopyallrequestmetadatafromonerequesttoanotherifthenewrequestismeant
toreplacetheoldrequest,asisoftenthecasewhenreturningarequestfromadownloadermid-
dlewaremethod.
Alsomindthatthecopy()andreplace()requestmethodsshallow-copyrequestmetadata.
dont_filter: bool
Whetherthisrequestmaybefilteredoutbycomponentsthatsupportfilteringoutrequests(False,default),
orthosecomponentsshouldnotfilteroutthisrequest(True).
ThisattributeiscommonlysettoTruetopreventduplicaterequestsfrombeingfilteredout.
WhendefiningthestartURLsofaspiderthroughstart_urls, thisattributeisenabledbydefault. See
start().
attributes: tuple[str, ...] = ('url', 'callback', 'method', 'headers', 'body',
'cookies', 'meta', 'encoding', 'priority', 'dont_filter', 'errback', 'flags',
'cb_kwargs')
Atupleofstrobjectscontainingthenameofallpublicattributesoftheclassthatarealsokeywordpa-
rametersofthe__init__()method.
CurrentlyusedbyRequest.replace(),Request.to_dict()andrequest_from_dict().
copy()
Return a new Request which is a copy of this Request. See also: Passing additional data to callback
functions.
[
replace( url,method,headers,body,cookies,meta,flags,encoding,priority,dont_filter,callback,errback,
]
cb_kwargs )
ReturnaRequestobjectwiththesamemembers,exceptforthosemembersgivennewvaluesbywhichever
keywordargumentsarespecified. Thecb_kwargsandmetaattributesareshallowcopiedbydefault(unless
newvaluesaregivenasarguments). SeealsoPassingadditionaldatatocallbackfunctions.
classmethod from_curl(curl_command: str,ignore_unknown_options: bool=True,**kwargs: Any)→
Self
CreateaRequestobjectfromastringcontainingacURLcommand. ItpopulatestheHTTPmethod, the
URL,theheaders,thecookiesandthebody. ItacceptsthesameargumentsastheRequest class,taking
preferenceandoverridingthevaluesofthesameargumentscontainedinthecURLcommand.
Unrecognized options are ignored by default. To raise an error when finding unknown options call this
methodbypassingignore_unknown_options=False.
‡ Caution
Using from_curl() from Request subclasses, such as JsonRequest, or XmlRpcRequest,
as well as having downloader middlewares and spider middlewares enabled, such as
DefaultHeadersMiddleware, UserAgentMiddleware, or HttpCompressionMiddleware,
maymodifytheRequestobject.
3.9. RequestsandResponses 105

ScrapyDocumentation,Release2.13.3
TotranslateacURLcommandintoaScrapyrequest,youmayusecurl2scrapy.
to_dict(*,spider: Spider|None=None)→dict[str,Any]
ReturnadictionarycontainingtheRequest’sdata.
Userequest_from_dict()toconvertbackintoaRequestobject.
Ifaspiderisgiven, thismethodwilltrytofindoutthenameofthespidermethodsusedascallbackand
errbackandincludethemintheoutputdict,raisinganexceptioniftheycannotbefound.
Otherfunctionsrelatedtorequests
scrapy.http.request.NO_CALLBACK(*args: Any,**kwargs: Any)→NoReturn
WhenassignedtothecallbackparameterofRequest,itindicatesthattherequestisnotmeanttohaveaspider
callbackatall.
Forexample:
Request("https://example.com", callback=NO_CALLBACK)
Thisvalueshouldbeusedbycomponentsthatcreateandhandletheirownrequests,e.g. throughscrapy.core.
engine.ExecutionEngine.download(), so that downloader middlewares handling such requests can treat
themdifferentlyfromrequestsintendedfortheparse()callback.
scrapy.utils.request.request_from_dict(d: dict[str,Any],*,spider: Spider|None=None)→Request
CreateaRequestobjectfromadict.
Ifaspiderisgiven,itwilltrytoresolvethecallbackslookingatthespiderformethodswiththesamename.
Passingadditionaldatatocallbackfunctions
Thecallbackofarequestisafunctionthatwillbecalledwhentheresponseofthatrequestisdownloaded. Thecallback
functionwillbecalledwiththedownloadedResponseobjectasitsfirstargument.
Example:
def parse_page1(self, response):
return scrapy.Request(
"http://www.example.com/some_page.html", callback=self.parse_page2
)
def parse_page2(self, response):
# this would log http://www.example.com/some_page.html
self.logger.info("Visited %s", response.url)
Insomecasesyoumaybeinterestedinpassingargumentstothosecallbackfunctionssoyoucanreceivethearguments
later, in the second callback. The following example shows how to achieve this by using the Request.cb_kwargs
attribute:
def parse(self, response):
request = scrapy.Request(
"http://www.example.com/index.html",
callback=self.parse_page2,
cb_kwargs=dict(main_url=response.url),
)
request.cb_kwargs["foo"] = "bar" # add more arguments for the callback
(continuesonnextpage)
106 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
yield request
def parse_page2(self, response, main_url, foo):
yield dict(
main_url=main_url,
other_url=response.url,
foo=foo,
)
‡ Caution
Request.cb_kwargs wasintroducedinversion1.7. Priortothat,usingRequest.meta wasrecommendedfor
passing information around callbacks. After 1.7, Request.cb_kwargs became the preferred way for handling
userinformation,leavingRequest.meta forcommunicationwithcomponentslikemiddlewaresandextensions.
Usingerrbackstocatchexceptionsinrequestprocessing
Theerrbackofarequestisafunctionthatwillbecalledwhenanexceptionisraisewhileprocessingit.
ItreceivesaFailureasfirstparameterandcanbeusedtotrackconnectionestablishmenttimeouts,DNSerrorsetc.
Here’sanexamplespiderloggingallerrorsandcatchingsomespecificerrorsifneeded:
import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
class ErrbackSpider(scrapy.Spider):
name = "errback_example"
start_urls = [
"http://www.httpbin.org/", # HTTP 200 expected
"http://www.httpbin.org/status/404", # Not found error
"http://www.httpbin.org/status/500", # server issue
"http://www.httpbin.org:12345/", # non-responding host, timeout expected
"https://example.invalid/", # DNS error expected
]
async def start(self):
for u in self.start_urls:
yield scrapy.Request(
u,
callback=self.parse_httpbin,
errback=self.errback_httpbin,
dont_filter=True,
)
def parse_httpbin(self, response):
self.logger.info("Got successful response from {}".format(response.url))
(continuesonnextpage)
3.9. RequestsandResponses 107

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
# do something useful here...
def errback_httpbin(self, failure):
# log all failures
self.logger.error(repr(failure))
# in case you want to do something special for some errors,
# you may need the failure's type:
if failure.check(HttpError):
# these exceptions come from HttpError spider middleware
# you can get the non-200 response
response = failure.value.response
self.logger.error("HttpError on %s", response.url)
elif failure.check(DNSLookupError):
# this is the original request
request = failure.request
self.logger.error("DNSLookupError on %s", request.url)
elif failure.check(TimeoutError, TCPTimedOutError):
request = failure.request
self.logger.error("TimeoutError on %s", request.url)
Accessingadditionaldatainerrbackfunctions
Incaseofafailuretoprocesstherequest,youmaybeinterestedinaccessingargumentstothecallbackfunctionsso
youcanprocessfurtherbasedontheargumentsintheerrback. Thefollowingexampleshowshowtoachievethisby
usingFailure.request.cb_kwargs:
def parse(self, response):
request = scrapy.Request(
"http://www.example.com/index.html",
callback=self.parse_page2,
errback=self.errback_page2,
cb_kwargs=dict(main_url=response.url),
)
yield request
def parse_page2(self, response, main_url):
pass
def errback_page2(self, failure):
yield dict(
main_url=failure.request.cb_kwargs["main_url"],
)
108 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Requestfingerprints
There are some aspects of scraping, such as filtering out duplicate requests (see DUPEFILTER_CLASS) or caching
responses(seeHTTPCACHE_POLICY),whereyouneedtheabilitytogenerateashort,uniqueidentifierfromaRequest
object: arequestfingerprint.
Youoftendonotneedtoworryaboutrequestfingerprints,thedefaultrequestfingerprinterworksformostprojects.
However,thereisnouniversalwaytogenerateauniqueidentifierfromarequest,becausedifferentsituationsrequire
comparingrequestsdifferently. Forexample, sometimesyoumayneedtocompareURLscase-insensitively, include
URLfragments,excludecertainURLqueryparameters,includesomeorallheaders,etc.
Tochangehowrequestfingerprintsarebuiltforyourrequests,usetheREQUEST_FINGERPRINTER_CLASS setting.
REQUEST_FINGERPRINTER_CLASS
Addedinversion2.7.
Default: scrapy.utils.request.RequestFingerprinter
Arequestfingerprinterclassoritsimportpath.
class scrapy.utils.request.RequestFingerprinter(crawler: Crawler|None=None)
Defaultfingerprinter.
Ittakesintoaccountacanonicalversion(w3lib.url.canonicalize_url())ofrequest.urlandthevalues
ofrequest.method andrequest.body. ItthengeneratesanSHA1hash.
Writingyourownrequestfingerprinter
Arequestfingerprinterisacomponentthatmustimplementthefollowingmethod:
fingerprint(self,request: scrapy.Request)
Returnabytesobjectthatuniquelyidentifiesrequest.
SeealsoRequestfingerprintrestrictions.
The fingerprint() method of the default request fingerprinter, scrapy.utils.request.
RequestFingerprinter, uses scrapy.utils.request.fingerprint() with its default parameters. For
some common use cases you can use scrapy.utils.request.fingerprint() as well in your fingerprint()
methodimplementation:
scrapy.utils.request.fingerprint(request: Request,*,include_headers: Iterable[bytes|str]|None=None,
keep_fragments: bool=False)→bytes
Returntherequestfingerprint.
The request fingerprint is a hash that uniquely identifies the resource the request points to. For example, take
thefollowingtwourls: http://www.example.com/query?id=111&cat=222,http://www.example.com/
query?cat=222&id=111.
EventhoughthosearetwodifferentURLsbothpointtothesameresourceandareequivalent(i.e. theyshould
returnthesameresponse).
Anotherexamplearecookiesusedtostoresessionids. Supposethefollowingpageisonlyaccessibletoauthen-
ticatedusers: http://www.example.com/members/offers.html.
Lotsofsitesuseacookietostorethesessionid,whichaddsarandomcomponenttotheHTTPRequestandthus
shouldbeignoredwhencalculatingthefingerprint.
Forthisreason,requestheadersareignoredbydefaultwhencalculatingthefingerprint. Ifyouwanttoinclude
specificheadersusetheinclude_headersargument,whichisalistofRequestheaderstoinclude.
3.9. RequestsandResponses 109

ScrapyDocumentation,Release2.13.3
Also,serversusuallyignorefragmentsinurlswhenhandlingrequests,sotheyarealsoignoredbydefaultwhen
calculatingthefingerprint. Ifyouwanttoincludethem,setthekeep_fragmentsargumenttoTrue(forinstance
whenhandlingrequestswithaheadlessbrowser).
Forexample,totakethevalueofarequestheadernamedX-IDintoaccount:
# my_project/settings.py
REQUEST_FINGERPRINTER_CLASS = "my_project.utils.RequestFingerprinter"
# my_project/utils.py
from scrapy.utils.request import fingerprint
class RequestFingerprinter:
def fingerprint(self, request):
return fingerprint(request, include_headers=["X-ID"])
Youcanalsowriteyourownfingerprintinglogicfromscratch.
However,ifyoudonotusescrapy.utils.request.fingerprint(),makesureyouuseWeakKeyDictionaryto
cacherequestfingerprints:
• CachingsavesCPUbyensuringthatfingerprintsarecalculatedonlyonceperrequest,andnotonceperScrapy
componentthatneedsthefingerprintofarequest.
• UsingWeakKeyDictionarysavesmemorybyensuringthatrequestobjectsdonotstayinmemoryforeverjust
becauseyouhavereferencestotheminyourcachedictionary.
For example, to take into account only the URL of a request, without any prior URL canonicalization or taking the
requestmethodorbodyintoaccount:
from hashlib import sha1
from weakref import WeakKeyDictionary
from scrapy.utils.python import to_bytes
class RequestFingerprinter:
cache = WeakKeyDictionary()
def fingerprint(self, request):
if request not in self.cache:
fp = sha1()
fp.update(to_bytes(request.url))
self.cache[request] = fp.digest()
return self.cache[request]
Ifyouneedtobeabletooverridetherequestfingerprintingforarbitraryrequestsfromyourspidercallbacks,youmay
implementarequestfingerprinterthatreadsfingerprintsfromrequest.meta whenavailable,andthenfallsbackto
scrapy.utils.request.fingerprint(). Forexample:
from scrapy.utils.request import fingerprint
class RequestFingerprinter:
def fingerprint(self, request):
(continuesonnextpage)
110 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
if "fingerprint" in request.meta:
return request.meta["fingerprint"]
return fingerprint(request)
IfyouneedtoreproducethesamefingerprintingalgorithmasScrapy2.6,usethefollowingrequestfingerprinter:
from hashlib import sha1
from weakref import WeakKeyDictionary
from scrapy.utils.python import to_bytes
from w3lib.url import canonicalize_url
class RequestFingerprinter:
cache = WeakKeyDictionary()
def fingerprint(self, request):
if request not in self.cache:
fp = sha1()
fp.update(to_bytes(request.method))
fp.update(to_bytes(canonicalize_url(request.url)))
fp.update(request.body or b"")
self.cache[request] = fp.digest()
return self.cache[request]
Requestfingerprintrestrictions
Scrapycomponentsthatuserequestfingerprintsmayimposeadditionalrestrictionsontheformatofthefingerprints
thatyourrequestfingerprintergenerates.
Thefollowingbuilt-inScrapycomponentshavesuchrestrictions:
• scrapy.extensions.httpcache.FilesystemCacheStorage(defaultvalueofHTTPCACHE_STORAGE)
Requestfingerprintsmustbeatleast1bytelong.
PathandfilenamelengthlimitsofthefilesystemofHTTPCACHE_DIR alsoapply. InsideHTTPCACHE_DIR,the
followingdirectorystructureiscreated:
– Spider.name
∗ firstbyteofarequestfingerprintashexadecimal
· fingerprintashexadecimal
· filenamesupto16characterslong
Forexample,ifarequestfingerprintismadeof20bytes(default),HTTPCACHE_DIRis'/home/user/project/
.scrapy/httpcache',andthenameofyourspideris'my_spider'yourfilesystemmustsupportafilepath
like:
/home/user/project/.scrapy/httpcache/my_spider/01/
0123456789abcdef0123456789abcdef01234567/response_headers
˓→
• scrapy.extensions.httpcache.DbmCacheStorage
3.9. RequestsandResponses 111

ScrapyDocumentation,Release2.13.3
TheunderlyingDBMimplementationmustsupportkeysaslongastwicethenumberofbytesofarequestfin-
gerprint,plus5. Forexample,ifarequestfingerprintismadeof20bytes(default),45-character-longkeysmust
besupported.
3.9.2 Request.meta special keys
TheRequest.metaattributecancontainanyarbitrarydata,buttherearesomespecialkeysrecognizedbyScrapyand
itsbuilt-inextensions.
Thoseare:
• allow_offsite
• autothrottle_dont_adjust_delay
• bindaddress
• cookiejar
• dont_cache
• dont_merge_cookies
• dont_obey_robotstxt
• dont_redirect
• dont_retry
• download_fail_on_dataloss
• download_latency
• download_maxsize
• download_warnsize
• download_timeout
• ftp_password(SeeFTP_PASSWORD formoreinfo)
• ftp_user(SeeFTP_USER formoreinfo)
• handle_httpstatus_all
• handle_httpstatus_list
• is_start_request
• max_retry_times
• proxy
• redirect_reasons
• redirect_urls
• referrer_policy
bindaddress
TheIPoftheoutgoingIPaddresstousefortheperformingtherequest.
112 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
download_timeout
Theamountoftime(insecs)thatthedownloaderwillwaitbeforetimingout. Seealso: DOWNLOAD_TIMEOUT.
download_latency
Theamountoftimespenttofetchtheresponse, sincetherequesthasbeenstarted, i.e. HTTPmessagesentoverthe
network. Thismetakeyonlybecomesavailablewhentheresponsehasbeendownloaded. Whilemostothermetakeys
areusedtocontrolScrapybehavior,thisoneissupposedtoberead-only.
download_fail_on_dataloss
Whetherornottofailonbrokenresponses. See: DOWNLOAD_FAIL_ON_DATALOSS.
max_retry_times
The meta key is used set retry times per request. When initialized, the max_retry_times meta key takes higher
precedenceovertheRETRY_TIMES setting.
3.9.3 Stopping the download of a Response
RaisingaStopDownloadexceptionfromahandlerforthebytes_receivedorheaders_receivedsignalswillstop
thedownloadofagivenresponse. Seethefollowingexample:
import scrapy
class StopSpider(scrapy.Spider):
name = "stop"
start_urls = ["https://docs.scrapy.org/en/latest/"]
@classmethod
def from_crawler(cls, crawler):
spider = super().from_crawler(crawler)
crawler.signals.connect(
spider.on_bytes_received, signal=scrapy.signals.bytes_received
)
return spider
def parse(self, response):
# 'last_chars' show that the full response was not downloaded
yield {"len": len(response.text), "last_chars": response.text[-40:]}
def on_bytes_received(self, data, request, spider):
raise scrapy.exceptions.StopDownload(fail=False)
whichproducesthefollowingoutput:
2020-05-19 17:26:12 [scrapy.core.engine] INFO: Spider opened
2020-05-19 17:26:12 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min),␣
scraped 0 items (at 0 items/min)
˓→
2020-05-19 17:26:13 [scrapy.core.downloader.handlers.http11] DEBUG: Download stopped for
<GET https://docs.scrapy.org/en/latest/> from signal handler StopSpider.on_bytes_
˓→
received
˓→
2020-05-19 17:26:13 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://docs.scrapy.
(continuesonnextpage)
3.9. RequestsandResponses 113

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
org/en/latest/> (referer: None) ['download_stopped']
˓→
2020-05-19 17:26:13 [scrapy.core.scraper] DEBUG: Scraped from <200 https://docs.scrapy.
org/en/latest/>
˓→
{'len': 279, 'last_chars': 'dth, initial-scale=1.0">\n \n <title>Scr'}
2020-05-19 17:26:13 [scrapy.core.engine] INFO: Closing spider (finished)
Bydefault,resultingresponsesarehandledbytheircorrespondingerrbacks. Tocalltheircallbackinstead,likeinthis
example,passfail=FalsetotheStopDownload exception.
3.9.4 Request subclasses
Hereisthelistofbuilt-inRequestsubclasses. Youcanalsosubclassittoimplementyourowncustomfunctionality.
FormRequestobjects
TheFormRequestclassextendsthebaseRequestwithfunctionalityfordealingwithHTMLforms. Ituseslxml.html
formstopre-populateformfieldswithformdatafromResponseobjects.
[ ]
class scrapy.FormRequest(url ,formdata,... )
TheFormRequestclassaddsanewkeywordparametertothe__init__()method. Theremainingarguments
arethesameasfortheRequestclassandarenotdocumentedhere.
Parameters
formdata (dict or collections.abc.Iterable) – is a dictionary (or iterable of (key,
value) tuples) containing HTML Form data which will be url-encoded and assigned to the
bodyoftherequest.
TheFormRequestobjectssupportthefollowingclassmethodinadditiontothestandardRequestmethods:
[
classmethod from_response(response ,formname=None,formid=None,formnumber=0,
formdata=None,formxpath=None,formcss=None,clickdata=None,
]
dont_click=False,... )
ReturnsanewFormRequestobjectwithitsformfieldvaluespre-populatedwiththosefoundintheHTML
<form>elementcontainedinthegivenresponse. ForanexampleseeUsingFormRequest.from_response()
tosimulateauserlogin.
Thepolicyistoautomaticallysimulateaclick,bydefault,onanyformcontrolthatlooksclickable,likea
<input type="submit">. Eventhoughthisisquiteconvenient,andoftenthedesiredbehaviour,some-
timesitcancauseproblemswhichcouldbehardtodebug. Forexample,whenworkingwithformsthat
arefilledand/orsubmittedusingjavascript,thedefaultfrom_response()behaviourmaynotbethemost
appropriate. Todisablethisbehaviouryoucansetthedont_clickargumenttoTrue. Also,ifyouwant
tochangethecontrolclicked(insteadofdisablingit)youcanalsousetheclickdataargument.
‡ Caution
Usingthismethodwithselectelementswhichhaveleadingortrailingwhitespaceintheoptionvalues
willnotworkduetoabuginlxml,whichshouldbefixedinlxml3.8andabove.
Parameters
• response(Responseobject)–theresponsecontainingaHTMLformwhichwillbe
usedtopre-populatetheformfields
• formname(str)–ifgiven,theformwithnameattributesettothisvaluewillbeused.
114 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
• formid(str)–ifgiven,theformwithidattributesettothisvaluewillbeused.
• formxpath(str)–ifgiven,thefirstformthatmatchesthexpathwillbeused.
• formcss(str)–ifgiven,thefirstformthatmatchesthecssselectorwillbeused.
• formnumber(int)–thenumberofformtouse,whentheresponsecontainsmultiple
forms. Thefirstone(andalsothedefault)is0.
• formdata(dict)–fieldstooverrideintheformdata. Ifafieldwasalreadypresent
intheresponse<form>element,itsvalueisoverriddenbytheonepassedinthispa-
rameter. IfavaluepassedinthisparameterisNone,thefieldwillnotbeincludedin
therequest,evenifitwaspresentintheresponse<form>element.
• clickdata(dict)–attributestolookupthecontrolclicked. Ifit’snotgiven,theform
datawillbesubmittedsimulatingaclickonthefirstclickableelement. Inadditionto
htmlattributes,thecontrolcanbeidentifiedbyitszero-basedindexrelativetoother
submittableinputsinsidetheform,viathenrattribute.
• dont_click(bool)–IfTrue,theformdatawillbesubmittedwithoutclickinginany
element.
TheotherparametersofthisclassmethodarepasseddirectlytotheFormRequest__init__()method.
Requestusageexamples
UsingFormRequesttosenddataviaHTTPPOST
If you want to simulate a HTML Form POST in your spider and send a couple of key-value fields, you can return a
FormRequestobject(fromyourspider)likethis:
return [
FormRequest(
url="http://www.example.com/post/action",
formdata={"name": "John Doe", "age": "27"},
callback=self.after_post,
)
]
UsingFormRequest.from_response()tosimulateauserlogin
It is usual for web sites to provide pre-populated form fields through <input type="hidden"> elements, such as
session related data or authentication tokens (for login pages). When scraping, you’ll want these fields to be auto-
matically pre-populated and only override a couple of them, such as the user name and password. You can use the
FormRequest.from_response()methodforthisjob. Here’sanexamplespiderwhichusesit:
import scrapy
def authentication_failed(response):
# TODO: Check the contents of the response and return True if it failed
# or False if it succeeded.
pass
class LoginSpider(scrapy.Spider):
name = "example.com"
(continuesonnextpage)
3.9. RequestsandResponses 115

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
start_urls = ["http://www.example.com/users/login.php"]
def parse(self, response):
return scrapy.FormRequest.from_response(
response,
formdata={"username": "john", "password": "secret"},
callback=self.after_login,
)
def after_login(self, response):
if authentication_failed(response):
self.logger.error("Login failed")
return
# continue scraping with authenticated session...
JsonRequest
TheJsonRequestclassextendsthebaseRequestclasswithfunctionalityfordealingwithJSONrequests.
[ ]
class scrapy.http.JsonRequest(url ,... data,dumps_kwargs )
TheJsonRequest classaddstwonewkeywordparameterstothe__init__()method. Theremainingargu-
mentsarethesameasfortheRequestclassandarenotdocumentedhere.
Using the JsonRequest will set the Content-Type header to application/json and Accept header to
application/json, text/javascript, */*; q=0.01
Parameters
• data (object) – is any JSON serializable object that needs to be JSON encoded and
assignedtobody. Ifthebodyargumentisprovidedthisparameterwillbeignored. Ifthe
bodyargumentisnotprovidedandthedataargumentisprovidedthemethod willbeset
to'POST'automatically.
• dumps_kwargs (dict) – Parameters that will be passed to underlying json.dumps()
methodwhichisusedtoserializedataintoJSONformat.
attributes: tuple[str, ...] = ('url', 'callback', 'method', 'headers', 'body',
'cookies', 'meta', 'encoding', 'priority', 'dont_filter', 'errback', 'flags',
'cb_kwargs', 'dumps_kwargs')
A tuple of str objects containing the name of all public attributes of the class that are also keyword
parametersofthe__init__()method.
CurrentlyusedbyRequest.replace(),Request.to_dict()andrequest_from_dict().
JsonRequestusageexample
SendingaJSONPOSTrequestwithaJSONpayload:
data = {
"name1": "value1",
"name2": "value2",
}
yield JsonRequest(url="http://www.example.com/post/action", data=data)
116 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
3.9.5 Response objects
class scrapy.http.Response(*args: Any,**kwargs: Any)
AnobjectthatrepresentsanHTTPresponse,whichisusuallydownloaded(bytheDownloader)andfedtothe
Spidersforprocessing.
Parameters
• url(str)–theURLofthisresponse
• status(int)–theHTTPstatusoftheresponse. Defaultsto200.
• headers(dict)–theheadersofthisresponse. Thedictvaluescanbestrings(forsingle
valuedheaders)orlists(formulti-valuedheaders).
• body(bytes)–theresponsebody. Toaccessthedecodedtextasastring,useresponse.
textfromanencoding-awareResponsesubclass,suchasTextResponse.
• flags(list)–isalistcontainingtheinitialvaluesfortheResponse.flagsattribute.
Ifgiven,thelistwillbeshallowcopied.
• request (scrapy.Request) – the initial value of the Response.request attribute.
ThisrepresentstheRequestthatgeneratedthisresponse.
• certificate (twisted.internet.ssl.Certificate) – an object representing the
server’sSSLcertificate.
• ip_address (ipaddress.IPv4Address or ipaddress.IPv6Address) – The IP ad-
dressoftheserverfromwhichtheResponseoriginated.
• protocol (str) – The protocol that was used to download the response. For instance:
“HTTP/1.0”,“HTTP/1.1”,“h2”
Addedinversion2.0.0: Thecertificateparameter.
Addedinversion2.1.0: Theip_addressparameter.
Addedinversion2.5.0: Theprotocolparameter.
url
AstringcontainingtheURLoftheresponse.
Thisattributeisread-only. TochangetheURLofaResponseusereplace().
status
AnintegerrepresentingtheHTTPstatusoftheresponse. Example: 200,404.
headers
Adictionary-like(scrapy.http.headers.Headers)objectwhichcontainstheresponseheaders. Val-
uescanbeaccessedusingget()toreturnthefirstheadervaluewiththespecifiednameor getlist()
toreturnallheadervalueswiththespecifiedname. Forexample,thiscallwillgiveyouallcookiesinthe
headers:
response.headers.getlist('Set-Cookie')
body
Theresponsebodyasbytes.
If you want the body as a string, use TextResponse.text (only available in TextResponse and sub-
classes).
Thisattributeisread-only. TochangethebodyofaResponseusereplace().
3.9. RequestsandResponses 117

ScrapyDocumentation,Release2.13.3
request
TheRequestobjectthatgeneratedthisresponse. ThisattributeisassignedintheScrapyengine,afterthe
responseandtherequesthavepassedthroughallDownloaderMiddlewares. Inparticular,thismeansthat:
• HTTPredirectionswillcreateanewrequestfromtherequestbeforeredirection. Ithasthemajorityof
thesamemetadataandoriginalrequestattributesandgetsassignedtotheredirectedresponseinstead
ofthepropagationoftheoriginalrequest.
• Response.request.urldoesn’talwaysequalResponse.url
• Thisattributeisonlyavailableinthespidercode,andintheSpiderMiddlewares,butnotinDown-
loaderMiddlewares(althoughyouhavetheRequestavailabletherebyothermeans)andhandlersof
theresponse_downloaded signal.
meta
Ashortcuttothemeta attributeoftheResponse.requestobject(i.e. self.request.meta).
UnliketheResponse.requestattribute,theResponse.metaattributeispropagatedalongredirectsand
retries,soyouwillgettheoriginalRequest.meta sentfromyourspider.
ª Seealso
Request.meta attribute
cb_kwargs
Addedinversion2.0.
A shortcut to the cb_kwargs attribute of the Response.request object (i.e. self.request.
cb_kwargs).
UnliketheResponse.request attribute,theResponse.cb_kwargs attributeispropagatedalongredi-
rectsandretries,soyouwillgettheoriginalRequest.cb_kwargssentfromyourspider.
ª Seealso
Request.cb_kwargsattribute
flags
A list that contains flags for this response. Flags are labels used for tagging Responses. For exam-
ple: 'cached', 'redirected’, etc. And they’re shown on the string representation of the Response
(__str__()method)whichisusedbytheengineforlogging.
certificate
Addedinversion2.0.0.
Atwisted.internet.ssl.Certificateobjectrepresentingtheserver’sSSLcertificate.
Onlypopulatedforhttpsresponses,Noneotherwise.
ip_address
Addedinversion2.1.0.
TheIPaddressoftheserverfromwhichtheResponseoriginated.
ThisattributeiscurrentlyonlypopulatedbytheHTTP1.1downloadhandler,i.e. forhttp(s)responses.
Forotherhandlers,ip_addressisalwaysNone.
118 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
protocol
Addedinversion2.5.0.
Theprotocolthatwasusedtodownloadtheresponse. Forinstance: “HTTP/1.0”,“HTTP/1.1”
This attribute is currently only populated by the HTTP download handlers, i.e. for http(s) responses.
Forotherhandlers,protocolisalwaysNone.
attributes: tuple[str, ...] = ('url', 'status', 'headers', 'body', 'flags',
'request', 'certificate', 'ip_address', 'protocol')
A tuple of str objects containing the name of all public attributes of the class that are also keyword
parametersofthe__init__()method.
CurrentlyusedbyResponse.replace().
copy()
ReturnsanewResponsewhichisacopyofthisResponse.
[ ]
replace( url,status,headers,body,request,flags,cls )
Returns a Response object with the same members, except for those members given new values by
whicheverkeywordargumentsarespecified. TheattributeResponse.meta iscopiedbydefault.
urljoin(url)
ConstructsanabsoluteurlbycombiningtheResponse’surlwithapossiblerelativeurl.
Thisisawrapperoverurljoin(),it’smerelyanaliasformakingthiscall:
urllib.parse.urljoin(response.url, url)
follow(url: str|Link,callback: CallbackT|None=None,method: str='GET',headers: Mapping[AnyStr,
Any]|Iterable[tuple[AnyStr,Any]]|None=None,body: bytes|str|None=None,cookies:
CookiesT|None=None,meta: dict[str,Any]|None=None,encoding: str|None='utf-8',priority:
int=0,dont_filter: bool=False,errback: Callable[[Failure],Any]|None=None,cb_kwargs:
dict[str,Any]|None=None,flags: list[str]|None=None)→Request
ReturnaRequestinstancetofollowalinkurl. ItacceptsthesameargumentsasRequest.__init__()
method,buturlcanbearelativeURLoraLink object,notonlyanabsoluteURL.
TextResponse provides a follow() method which supports selectors in addition to absolute/relative
URLsandLinkobjects.
Addedinversion2.0: Theflagsparameter.
follow_all(urls: Iterable[str|Link],callback: CallbackT|None=None,method: str='GET',headers:
Mapping[AnyStr,Any]|Iterable[tuple[AnyStr,Any]]|None=None,body: bytes|str|None=
None,cookies: CookiesT|None=None,meta: dict[str,Any]|None=None,encoding: str|
None='utf-8',priority: int=0,dont_filter: bool=False,errback: Callable[[Failure],Any]|
None=None,cb_kwargs: dict[str,Any]|None=None,flags: list[str]|None=None)→
Iterable[Request]
Addedinversion2.0.
Return an iterable of Request instances to follow all links in urls. It accepts the same arguments as
Request.__init__() method, but elements of urls can be relative URLs or Link objects, not only
absoluteURLs.
TextResponse provides a follow_all() method which supports selectors in addition to abso-
lute/relativeURLsandLinkobjects.
3.9. RequestsandResponses 119

ScrapyDocumentation,Release2.13.3
3.9.6 Response subclasses
Hereisthelistofavailablebuilt-inResponsesubclasses. YoucanalsosubclasstheResponseclasstoimplementyour
ownfunctionality.
TextResponseobjects
[ [ ]]
class scrapy.http.TextResponse(url ,encoding ,... )
TextResponseobjectsaddsencodingcapabilitiestothebaseResponseclass,whichismeanttobeusedonly
forbinarydata,suchasimages,soundsoranymediafile.
TextResponseobjectssupportanew__init__()methodargument,inadditiontothebaseResponseobjects.
TheremainingfunctionalityisthesameasfortheResponseclassandisnotdocumentedhere.
Parameters
encoding(str)–isastringwhichcontainstheencodingtouseforthisresponse. Ifyoucreate
aTextResponseobjectwithastringasbody,itwillbeconvertedtobytesencodedusingthis
encoding. IfencodingisNone(default),theencodingwillbelookedupintheresponseheaders
andbodyinstead.
TextResponseobjectssupportthefollowingattributesinadditiontothestandardResponseones:
text
Responsebody,asastring.
Thesameasresponse.body.decode(response.encoding),buttheresultiscachedafterthefirstcall,
soyoucanaccessresponse.textmultipletimeswithoutextraoverhead.
(cid:242) Note
str(response.body)isnotacorrectwaytoconverttheresponsebodyintoastring:
>>> str(b"body")
"b'body'"
encoding
Astringwiththeencodingofthisresponse. Theencodingisresolvedbytryingthefollowingmechanisms,
inorder:
1. theencodingpassedinthe__init__()methodencodingargument
2. theencodingdeclaredintheContent-TypeHTTPheader. Ifthisencodingisnotvalid(i.e. unknown),
itisignoredandthenextresolutionmechanismistried.
3. the encoding declared in the response body. The TextResponse class doesn’t provide any special
functionalityforthis. However,theHtmlResponseandXmlResponseclassesdo.
4. theencodinginferredbylookingattheresponsebody. Thisisthemorefragilemethodbutalsothe
lastonetried.
selector
ASelectorinstanceusingtheresponseastarget. Theselectorislazilyinstantiatedonfirstaccess.
attributes: tuple[str, ...] = ('url', 'status', 'headers', 'body', 'flags',
'request', 'certificate', 'ip_address', 'protocol', 'encoding')
A tuple of str objects containing the name of all public attributes of the class that are also keyword
parametersofthe__init__()method.
CurrentlyusedbyResponse.replace().
120 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
TextResponseobjectssupportthefollowingmethodsinadditiontothestandardResponseones:
jmespath(query)
AshortcuttoTextResponse.selector.jmespath(query):
response.jmespath('object.[*]')
xpath(query)
AshortcuttoTextResponse.selector.xpath(query):
response.xpath('//p')
css(query)
AshortcuttoTextResponse.selector.css(query):
response.css('p')
follow(url: str|Link|parsel.Selector,callback: CallbackT|None=None,method: str='GET',headers:
Mapping[AnyStr,Any]|Iterable[tuple[AnyStr,Any]]|None=None,body: bytes|str|None=None,
cookies: CookiesT|None=None,meta: dict[str,Any]|None=None,encoding: str|None=None,
priority: int=0,dont_filter: bool=False,errback: Callable[[Failure],Any]|None=None,
cb_kwargs: dict[str,Any]|None=None,flags: list[str]|None=None)→Request
ReturnaRequestinstancetofollowalinkurl. ItacceptsthesameargumentsasRequest.__init__()
method,buturlcanbenotonlyanabsoluteURL,butalso
• arelativeURL
• aLink object,e.g. theresultofLinkExtractors
• aSelectorobjectfora<link>or<a>element,e.g. response.css('a.my_link')[0]
• an attribute Selector (not SelectorList), e.g. response.css('a::attr(href)')[0] or
response.xpath('//img/@src')[0]
SeeAshortcutforcreatingRequestsforusageexamples.
follow_all(urls: Iterable[str|Link]|parsel.SelectorList|None=None,callback: CallbackT|None=
None,method: str='GET',headers: Mapping[AnyStr,Any]|Iterable[tuple[AnyStr,Any]]|
None=None,body: bytes|str|None=None,cookies: CookiesT|None=None,meta: dict[str,
Any]|None=None,encoding: str|None=None,priority: int=0,dont_filter: bool=False,
errback: Callable[[Failure],Any]|None=None,cb_kwargs: dict[str,Any]|None=None,
flags: list[str]|None=None,css: str|None=None,xpath: str|None=None)→
Iterable[Request]
AgeneratorthatproducesRequest instancestofollowalllinksinurls. Itacceptsthesamearguments
as the Request’s __init__() method, except that each urls element does not need to be an absolute
URL,itcanbeanyofthefollowing:
• arelativeURL
• aLink object,e.g. theresultofLinkExtractors
• aSelectorobjectfora<link>or<a>element,e.g. response.css('a.my_link')[0]
• an attribute Selector (not SelectorList), e.g. response.css('a::attr(href)')[0] or
response.xpath('//img/@src')[0]
In addition, css and xpath arguments are accepted to perform the link extraction within the
follow_all()method(onlyoneof urls,cssandxpathisaccepted).
3.9. RequestsandResponses 121

ScrapyDocumentation,Release2.13.3
NotethatwhenpassingaSelectorListasargumentfortheurlsparameterorusingthecssorxpath
parameters,thismethodwillnotproducerequestsforselectorsfromwhichlinkscannotbeobtained(for
instance,anchortagswithoutanhrefattribute)
json()
Addedinversion2.2.
DeserializeaJSONdocumenttoaPythonobject.
ReturnsaPythonobjectfromdeserializedJSONdocument. Theresultiscachedafterthefirstcall.
urljoin(url)
ConstructsanabsoluteurlbycombiningtheResponse’sbaseurlwithapossiblerelativeurl. Thebaseurl
shallbeextractedfromthe<base>tag,orjustResponse.urlifthereisnosuchtag.
HtmlResponseobjects
[ ]
class scrapy.http.HtmlResponse(url ,... )
The HtmlResponse class is a subclass of TextResponse which adds encoding auto-discovering support by
lookingintotheHTMLmetahttp-equivattribute. SeeTextResponse.encoding.
XmlResponseobjects
[ ]
class scrapy.http.XmlResponse(url ,... )
TheXmlResponseclassisasubclassofTextResponsewhichaddsencodingauto-discoveringsupportbylook-
ingintotheXMLdeclarationline. SeeTextResponse.encoding.
JsonResponseobjects
[ ]
class scrapy.http.JsonResponse(url ,... )
The JsonResponse class is a subclass of TextResponse that is used when the response has a JSON MIME
typeinitsContent-Typeheader.
3.10 Link Extractors
Alinkextractorisanobjectthatextractslinksfromresponses.
The __init__ method of LxmlLinkExtractor takes settings that determine which links may be extracted.
LxmlLinkExtractor.extract_linksreturnsalistofmatchingLink objectsfromaResponseobject.
LinkextractorsareusedinCrawlSpiderspidersthroughasetofRuleobjects.
You can also use link extractors in regular spiders. For example, you can instantiate LinkExtractor into a class
variableinyourspider,anduseitfromyourspidercallbacks:
def parse(self, response):
for link in self.link_extractor.extract_links(response):
yield Request(link.url, callback=self.parse)
3.10.1 Link extractor reference
Thelinkextractorclassisscrapy.linkextractors.lxmlhtml.LxmlLinkExtractor. Forconvenienceitcanalso
beimportedasscrapy.linkextractors.LinkExtractor:
from scrapy.linkextractors import LinkExtractor
122 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
LxmlLinkExtractor
class scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor(allow=(),deny=(),allow_domains=(),
deny_domains=(),deny_extensions=None,
restrict_xpaths=(),restrict_css=(),tags=('a',
'area'),attrs=('href',),canonicalize=False,
unique=True,process_value=None,
strip=True)
LxmlLinkExtractor is the recommended link extractor with handy filtering options. It is implemented using
lxml’srobustHTMLParser.
Parameters
• allow(str or list)–asingleregularexpression(orlistofregularexpressions)that
the (absolute) urls must match in order to be extracted. If not given (or empty), it will
matchalllinks.
• deny(str or list)–asingleregularexpression(orlistofregularexpressions)thatthe
(absolute)urlsmustmatchinordertobeexcluded(i.e. notextracted). Ithasprecedence
overtheallowparameter. Ifnotgiven(orempty)itwon’texcludeanylinks.
• allow_domains(str or list)–asinglevalueoralistofstringcontainingdomains
whichwillbeconsideredforextractingthelinks
• deny_domains(str or list)–asinglevalueoralistofstringscontainingdomains
whichwon’tbeconsideredforextractingthelinks
• deny_extensions (list) – a single value or list of strings containing extensions that
should be ignored when extracting links. If not given, it will default to scrapy.
linkextractors.IGNORED_EXTENSIONS.
Changedinversion2.0: IGNORED_EXTENSIONSnowincludes7z,7zip,apk,bz2,cdr,
dmg,ico,iso,tar,tar.gz,webm,andxz.
• restrict_xpaths(str or list)–isanXPath(orlistofXPath’s)whichdefinesre-
gions inside the response where links should be extracted from. If given, only the text
selectedbythoseXPathwillbescannedforlinks.
• restrict_css(str or list)–aCSSselector(orlistofselectors)whichdefinesre-
gionsinsidetheresponsewherelinksshouldbeextractedfrom. Hasthesamebehaviour
asrestrict_xpaths.
• restrict_text(str or list)–asingleregularexpression(orlistofregularexpres-
sions)thatthelink’stextmustmatchinordertobeextracted. Ifnotgiven(orempty),it
willmatchalllinks. Ifalistofregularexpressionsisgiven,thelinkwillbeextractedifit
matchesatleastone.
• tags(str or list)–atagoralistoftagstoconsiderwhenextractinglinks. Defaults
to('a', 'area').
• attrs(list)–anattributeorlistofattributeswhichshouldbeconsideredwhenlooking
for links to extract (only for those tags specified in the tags parameter). Defaults to
('href',)
• canonicalize (bool) – canonicalize each extracted url (using
w3lib.url.canonicalize_url). Defaults to False. Note that canonicalize_url is meant for
duplicatechecking; itcanchangetheURLvisibleatserverside,sotheresponsecanbe
differentforrequestswithcanonicalizedandrawURLs. Ifyou’reusingLinkExtractorto
followlinksitismorerobusttokeepthedefaultcanonicalize=False.
• unique(bool)–whetherduplicatefilteringshouldbeappliedtoextractedlinks.
3.10. LinkExtractors 123

ScrapyDocumentation,Release2.13.3
• process_value(collections.abc.Callable)–afunctionwhichreceiveseachvalue
extractedfromthetagandattributesscannedandcanmodifythevalueandreturnanew
one,orreturnNonetoignorethelinkaltogether. Ifnotgiven,process_valuedefaults
tolambda x: x.
Forexample,toextractlinksfromthiscode:
<a href="javascript:goToPage('../other/page.html'); return false">
Link text</a>
˓→
Youcanusethefollowingfunctioninprocess_value:
def process_value(value):
m = re.search(r"javascript:goToPage\('(.*?)'", value)
if m:
return m.group(1)
• strip (bool) – whether to strip whitespaces from extracted attributes. According to
HTML5standard,leadingandtrailingwhitespacesmustbestrippedfromhrefattributes
of <a>,<area>andmanyotherelements,srcattributeof <img>,<iframe>elements,
etc.,soLinkExtractorstripsspacecharsbydefault. Setstrip=Falsetoturnitoff(e.g.
ifyou’reextractingurlsfromelementsorattributeswhichallowleading/trailingwhites-
paces).
extract_links(response: TextResponse)→list[Link]
ReturnsalistofLink objectsfromthespecifiedresponse.
Onlylinksthatmatchthesettingspassedtothe__init__methodofthelinkextractorarereturned.
DuplicatelinksareomittediftheuniqueattributeissettoTrue,otherwisetheyarereturned.
Link
class scrapy.link.Link(url: str,text: str='',fragment: str='',nofollow: bool=False)
LinkobjectsrepresentanextractedlinkbytheLinkExtractor.
Usingtheanchortagsamplebelowtoillustratetheparameters:
<a href="https://example.com/nofollow.html#foo" rel="nofollow">Dont follow this one
</a>
˓→
Parameters
• url–theabsoluteurlbeinglinkedtointheanchortag. Fromthesample,thisishttps:/
/example.com/nofollow.html.
• text–thetextintheanchortag. Fromthesample,thisisDont follow this one.
• fragment–thepartoftheurlafterthehashsymbol. Fromthesample,thisisfoo.
• nofollow–anindicationofthepresenceorabsenceofanofollowvalueintherelat-
tributeoftheanchortag.
3.11 Settings
TheScrapysettingsallowsyoutocustomizethebehaviourofallScrapycomponents,includingthecore,extensions,
pipelinesandspidersthemselves.
124 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
The infrastructure of the settings provides a global namespace of key-value mappings that the code can use to pull
configurationvaluesfrom. Thesettingscanbepopulatedthroughdifferentmechanisms,whicharedescribedbelow.
ThesettingsarealsothemechanismforselectingthecurrentlyactiveScrapyproject(incaseyouhavemany).
Foralistofavailablebuilt-insettingssee: Built-insettingsreference.
3.11.1 Designating the settings
WhenyouuseScrapy,youhavetotellitwhichsettingsyou’reusing. Youcandothisbyusinganenvironmentvariable,
SCRAPY_SETTINGS_MODULE.
ThevalueofSCRAPY_SETTINGS_MODULEshouldbeinPythonpathsyntax,e.g. myproject.settings. Notethatthe
settingsmoduleshouldbeonthePythonimportsearchpath.
3.11.2 Populating the settings
Settingscanbepopulatedusingdifferentmechanisms,eachofwhichhasadifferentprecedence:
1. Command-linesettings(highestprecedence)
2. Spidersettings
3. Projectsettings
4. Add-onsettings
5. Command-specificdefaultsettings
6. Globaldefaultsettings(lowestprecedence)
1. Command-linesettings
Settingssetinthecommandlinehavethehighestprecedence,overridinganyothersettings.
Youcanexplicitlyoverrideoneormoresettingsusingthe-s(or--set)command-lineoption.
Example:
scrapy crawl myspider -s LOG_LEVEL=INFO -s LOG_FILE=scrapy.log
2. Spidersettings
Spiderscandefinetheirownsettingsthatwilltakeprecedenceandoverridetheprojectones.
(cid:242) Note
Pre-crawlersettingscannotbedefinedperspider,andreactorsettingsshouldnothaveadifferentvalueperspider
whenrunningmultiplespidersinthesameprocess.
Onewaytodosoisbysettingtheircustom_settingsattribute:
import scrapy
class MySpider(scrapy.Spider):
name = "myspider"
(continuesonnextpage)
3.11. Settings 125

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
custom_settings = {
"SOME_SETTING": "some value",
}
It’softenbettertoimplementupdate_settings()instead,andsettingssetthereshouldusethe"spider"priority
explicitly:
import scrapy
class MySpider(scrapy.Spider):
name = "myspider"
@classmethod
def update_settings(cls, settings):
super().update_settings(settings)
settings.set("SOME_SETTING", "some value", priority="spider")
Addedinversion2.11.
It’salsopossibletomodifythesettingsinthefrom_crawler()method,e.g. basedonspiderargumentsorotherlogic:
import scrapy
class MySpider(scrapy.Spider):
name = "myspider"
@classmethod
def from_crawler(cls, crawler, *args, **kwargs):
spider = super().from_crawler(crawler, *args, **kwargs)
if "some_argument" in kwargs:
spider.settings.set(
"SOME_SETTING", kwargs["some_argument"], priority="spider"
)
return spider
3. Projectsettings
Scrapyprojectsincludeasettingsmodule,usuallyafilecalledsettings.py,whereyoushouldpopulatemostsettings
thatapplytoallyourspiders.
ª Seealso
Designatingthesettings
4. Add-onsettings
Add-onscanmodifysettings. Theyshoulddothiswith"addon"prioritywherepossible.
126 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
5. Command-specificdefaultsettings
EachScrapycommand canhaveitsowndefaultsettings,whichoverridetheglobaldefaultsettings.
Thosecommand-specificdefaultsettingsarespecifiedinthedefault_settingsattributeofeachcommandclass.
6. Defaultglobalsettings
Thescrapy.settings.default_settingsmoduledefinesglobaldefaultvaluesforsomebuilt-insettings.
(cid:242) Note
startprojectgeneratesasettings.pyfilethatsetssomesettingstodifferentvalues.
Thereferencedocumentationofsettingsindicatesthedefaultvalueifoneexists. Ifstartproject setsavalue,
thatvalueisdocumentedasdefault,andthevaluefromscrapy.settings.default_settingsisdocumented
as“fallback”.
3.11.3 Compatibility with pickle
Settingvaluesmustbepicklable.
3.11.4 Import paths and classes
Addedinversion2.4.0.
WhenasettingreferencesacallableobjecttobeimportedbyScrapy,suchasaclassorafunction,therearetwodifferent
waysyoucanspecifythatobject:
• Asastringcontainingtheimportpathofthatobject
• Astheobjectitself
Forexample:
from mybot.pipelines.validate import ValidateMyItem
ITEM_PIPELINES = {
# passing the classname...
ValidateMyItem: 300,
# ...equals passing the class path
"mybot.pipelines.validate.ValidateMyItem": 300,
}
(cid:242) Note
Passingnon-callableobjectsisnotsupported.
3.11.5 How to access settings
Inaspider,settingsareavailablethroughself.settings:
class MySpider(scrapy.Spider):
name = "myspider"
start_urls = ["http://example.com"]
(continuesonnextpage)
3.11. Settings 127

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
def parse(self, response):
print(f"Existing settings: {self.settings.attributes.keys()}")
(cid:242) Note
The settings attribute is set in the base Spider class after the spider is initialized. If you want to use settings
beforetheinitialization(e.g.,inyourspider’s__init__()method),you’llneedtooverridethefrom_crawler()
method.
Componentscanalsoaccesssettings.
The settingsobjectcanbeusedlikeadict(e.g. settings["LOG_ENABLED"]). However, tosupportnon-string
settingvalues,whichmaybepassedfromthecommandlineasstrings,itisrecommendedtouseoneofthemethods
providedbytheSettingsAPI.
3.11.6 Component priority dictionaries
A component priority dictionary is a dict where keys are components and values are component priorities. For
example:
{
"path.to.ComponentA": None,
ComponentB: 100,
}
Acomponentcanbespecifiedeitherasaclassobjectorthroughanimportpath.
. Warning
Componentprioritydictionariesareregulardictobjects. Becarefulnottodefinethesamecomponentmorethan
once,e.g. withdifferentimportpathstringsordefiningbothanimportpathandatypeobject.
AprioritycanbeanintorNone.
A component with priority 1 goes before a component with priority 2. What going before entails, however, de-
pendsonthecorrespondingsetting. Forexample,intheDOWNLOADER_MIDDLEWARES setting,componentshavetheir
process_request()methodexecutedbeforethatoflatercomponents,buthavetheirprocess_response()method
executedafterthatoflatercomponents.
AcomponentwithpriorityNoneisdisabled.
Somecomponentprioritydictionariesgetmergedwithsomebuilt-invalue. Forexample,DOWNLOADER_MIDDLEWARES
is merged with DOWNLOADER_MIDDLEWARES_BASE. This is where None comes in handy, allowing you to disable a
componentfromthebasesettingintheregularsetting:
DOWNLOADER_MIDDLEWARES = {
"scrapy.downloadermiddlewares.offsite.OffsiteMiddleware": None,
}
128 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
3.11.7 Special settings
Thefollowingsettingsworkslightlydifferentlythanallothersettings.
Pre-crawlersettings
Pre-crawlersettingsaresettingsusedbeforetheCrawlerobjectiscreated.
Thesesettingscannotbesetfromaspider.
ThesesettingsareSPIDER_LOADER_CLASSandsettingsusedbythecorrespondingcomponent,e.g. SPIDER_MODULES
andSPIDER_LOADER_WARN_ONLY forthedefaultcomponent.
Reactorsettings
ReactorsettingsaresettingstiedtotheTwistedreactor.
Thesesettingscanbedefinedfromaspider. However,becauseonly1reactorcanbeusedperprocess,thesesettings
cannotuseadifferentvalueperspiderwhenrunningmultiplespidersinthesameprocess.
Ingeneral,ifdifferentspidersdefinedifferentvalues,thefirstdefinedvalueisused. However,iftwospidersrequesta
differentreactor,anexceptionisraised.
Thesesettingsare:
• ASYNCIO_EVENT_LOOP
• DNS_RESOLVERandsettingsusedbythecorrespondingcomponent,e.g. DNSCACHE_ENABLED,DNSCACHE_SIZE
andDNS_TIMEOUT forthedefaultone.
• REACTOR_THREADPOOL_MAXSIZE
• TWISTED_REACTOR
ASYNCIO_EVENT_LOOPandTWISTED_REACTORareuseduponinstallingthereactor. Therestofthesettingsareapplied
whenstartingthereactor.
3.11.8 Built-in settings reference
Here’salistofallavailableScrapysettings,inalphabeticalorder,alongwiththeirdefaultvaluesandthescopewhere
theyapply.
Thescope,whereavailable,showswherethesettingisbeingused,ifit’stiedtoanyparticularcomponent. Inthatcase
the module of that component will be shown, typically an extension, middleware or pipeline. It also means that the
componentmustbeenabledinorderforthesettingtohaveanyeffect.
ADDONS
Default: {}
Adictcontainingpathstotheadd-onsenabledinyourprojectandtheirpriorities. Formoreinformation,seeAdd-ons.
AWS_ACCESS_KEY_ID
Default: None
TheAWSaccesskeyusedbycodethatrequiresaccesstoAmazonWebservices,suchastheS3feedstoragebackend.
3.11. Settings 129

ScrapyDocumentation,Release2.13.3
AWS_SECRET_ACCESS_KEY
Default: None
TheAWSsecretkeyusedbycodethatrequiresaccesstoAmazonWebservices,suchastheS3feedstoragebackend.
AWS_SESSION_TOKEN
Default: None
TheAWSsecuritytokenusedbycodethatrequiresaccesstoAmazonWebservices,suchastheS3feedstoragebackend,
whenusingtemporarysecuritycredentials.
AWS_ENDPOINT_URL
Default: None
EndpointURLusedforS3-likestorage,forexampleMinioors3.scality.
AWS_USE_SSL
Default: None
UsethisoptionifyouwanttodisableSSLconnectionforcommunicationwithS3orS3-likestorage. BydefaultSSL
willbeused.
AWS_VERIFY
Default: None
VerifySSLconnectionbetweenScrapyandS3orS3-likestorage. BydefaultSSLverificationwilloccur.
AWS_REGION_NAME
Default: None
ThenameoftheregionassociatedwiththeAWSclient.
ASYNCIO_EVENT_LOOP
Default: None
Importpathofagivenasyncioeventloopclass.
Iftheasyncioreactorisenabled(seeTWISTED_REACTOR)thissettingcanbeusedtospecifytheasyncioeventloopto
beusedwithit. Setthesettingtotheimportpathofthedesiredasyncioeventloopclass. IfthesettingissettoNone
thedefaultasyncioeventloopwillbeused.
If you are installing the asyncio reactor manually using the install_reactor() function, you can use the
event_loop_pathparametertoindicatetheimportpathoftheeventloopclasstobeused.
Notethattheeventloopclassmustinheritfromasyncio.AbstractEventLoop.
‡ Caution
Pleasebeawarethat,whenusinganon-defaulteventloop(eitherdefinedviaASYNCIO_EVENT_LOOP orinstalled
with install_reactor()), Scrapy will call asyncio.set_event_loop(), which will set the specified event
loopasthecurrentloopforthecurrentOSthread.
130 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
BOT_NAME
Default: <project name>(fallback: 'scrapybot')
ThenameofthebotimplementedbythisScrapyproject(alsoknownastheprojectname). Thisnamewillbeusedfor
theloggingtoo.
It’sautomaticallypopulatedwithyourprojectnamewhenyoucreateyourprojectwiththestartprojectcommand.
CONCURRENT_ITEMS
Default: 100
Maximumnumberofconcurrentitems(perresponse)toprocessinparallelinitempipelines.
CONCURRENT_REQUESTS
Default: 16
Themaximumnumberofconcurrent(i.e. simultaneous)requeststhatwillbeperformedbytheScrapydownloader.
CONCURRENT_REQUESTS_PER_DOMAIN
Default: 1(fallback: 8)
Themaximumnumberofconcurrent(i.e. simultaneous)requeststhatwillbeperformedtoanysingledomain.
Seealso: AutoThrottleextensionanditsAUTOTHROTTLE_TARGET_CONCURRENCY option.
CONCURRENT_REQUESTS_PER_IP
Default: 0
Themaximumnumberofconcurrent(i.e. simultaneous)requeststhatwillbeperformedtoanysingleIP.Ifnon-zero,
theCONCURRENT_REQUESTS_PER_DOMAINsettingisignored,andthisoneisusedinstead. Inotherwords,concurrency
limitswillbeappliedperIP,notperdomain.
This setting also affects DOWNLOAD_DELAY and AutoThrottle extension: if CONCURRENT_REQUESTS_PER_IP is non-
zero,downloaddelayisenforcedperIP,notperdomain.
DEFAULT_DROPITEM_LOG_LEVEL
Default: "WARNING"
Defaultloglevelofmessagesaboutdroppeditems.
Whenanitemisdroppedbyraisingscrapy.exceptions.DropItem fromtheprocess_item()methodofanitem
pipeline,amessageislogged,andbydefaultitsloglevelistheoneconfiguredinthissetting.
Youmayspecifythisloglevelasaninteger(e.g. 20),asaloglevelconstant(e.g. logging.INFO)orasastringwith
thenameofaloglevelconstant(e.g. "INFO").
When writing an item pipeline, you can force a different log level by setting scrapy.exceptions.DropItem.
log_levelinyourscrapy.exceptions.DropItem exception. Forexample:
from scrapy.exceptions import DropItem
class MyPipeline:
def process_item(self, item, spider):
if not item.get("price"):
(continuesonnextpage)
3.11. Settings 131

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
raise DropItem("Missing price data", log_level="INFO")
return item
DEFAULT_ITEM_CLASS
Default: 'scrapy.Item'
ThedefaultclassthatwillbeusedforinstantiatingitemsinthetheScrapyshell.
DEFAULT_REQUEST_HEADERS
Default:
{
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language": "en",
}
ThedefaultheadersusedforScrapyHTTPRequests. They’repopulatedintheDefaultHeadersMiddleware.
‡ Caution
CookiessetviatheCookieheaderarenotconsideredbytheCookiesMiddleware. Ifyouneedtosetcookiesfora
request,usetheRequest.cookiesparameter. Thisisaknowncurrentlimitationthatisbeingworkedon.
DEPTH_LIMIT
Default: 0
Scope: scrapy.spidermiddlewares.depth.DepthMiddleware
Themaximumdepththatwillbeallowedtocrawlforanysite. Ifzero,nolimitwillbeimposed.
DEPTH_PRIORITY
Default: 0
Scope: scrapy.spidermiddlewares.depth.DepthMiddleware
Anintegerthatisusedtoadjustthepriority ofaRequestbasedonitsdepth.
Thepriorityofarequestisadjustedasfollows:
request.priority = request.priority - (depth * DEPTH_PRIORITY)
As depth increases, positive values of DEPTH_PRIORITY decrease request priority (BFO), while negative values in-
creaserequestpriority(DFO).SeealsoDoesScrapycrawlinbreadth-firstordepth-firstorder?.
(cid:242) Note
ThissettingadjustspriorityintheoppositewaycomparedtootherprioritysettingsREDIRECT_PRIORITY_ADJUST
andRETRY_PRIORITY_ADJUST.
132 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
DEPTH_STATS_VERBOSE
Default: False
Scope: scrapy.spidermiddlewares.depth.DepthMiddleware
Whethertocollectverbosedepthstats. Ifthisisenabled,thenumberofrequestsforeachdepthiscollectedinthestats.
DNSCACHE_ENABLED
Default: True
WhethertoenableDNSin-memorycache.
DNSCACHE_SIZE
Default: 10000
DNSin-memorycachesize.
DNS_RESOLVER
Addedinversion2.0.
Default: 'scrapy.resolver.CachingThreadedResolver'
TheclasstobeusedtoresolveDNSnames. Thedefaultscrapy.resolver.CachingThreadedResolversupports
specifyingatimeoutforDNSrequestsviatheDNS_TIMEOUT setting,butworksonlywithIPv4addresses. Scrapypro-
videsanalternativeresolver,scrapy.resolver.CachingHostnameResolver,whichsupportsIPv4/IPv6addresses
butdoesnottaketheDNS_TIMEOUT settingintoaccount.
DNS_TIMEOUT
Default: 60
TimeoutforprocessingofDNSqueriesinseconds. Floatissupported.
DOWNLOADER
Default: 'scrapy.core.downloader.Downloader'
Thedownloadertouseforcrawling.
DOWNLOADER_HTTPCLIENTFACTORY
Default: 'scrapy.core.downloader.webclient.ScrapyHTTPClientFactory'
Defines a Twisted protocol.ClientFactory class to use for HTTP/1.0 connections (for
HTTP10DownloadHandler).
(cid:242) Note
HTTP/1.0israrelyusednowadaysanditsScrapysupportisdeprecated,soyoucansafelyignorethissetting,unless
you really want to use HTTP/1.0 and override DOWNLOAD_HANDLERS for http(s) scheme accordingly, i.e. to
'scrapy.core.downloader.handlers.http.HTTP10DownloadHandler'.
3.11. Settings 133

ScrapyDocumentation,Release2.13.3
DOWNLOADER_CLIENTCONTEXTFACTORY
Default: 'scrapy.core.downloader.contextfactory.ScrapyClientContextFactory'
RepresentstheclasspathtotheContextFactorytouse.
Here,“ContextFactory”isaTwistedtermforSSL/TLScontexts,definingtheTLS/SSLprotocolversiontouse,whether
todocertificateverification,orevenenableclient-sideauthentication(andvariousotherthings).
(cid:242) Note
ScrapydefaultcontextfactorydoesNOTperformremoteservercertificateverification. Thisisusuallyfinefor
webscraping.
If you do need remote server certificate verification enabled, Scrapy also has another context factory class that
youcanset,'scrapy.core.downloader.contextfactory.BrowserLikeContextFactory',whichusesthe
platform’scertificatestovalidateremoteendpoints.
If you do use a custom ContextFactory, make sure its __init__ method accepts a method parameter (this is the
OpenSSL.SSL method mapping DOWNLOADER_CLIENT_TLS_METHOD), a tls_verbose_logging parameter (bool)
andatls_ciphersparameter(seeDOWNLOADER_CLIENT_TLS_CIPHERS).
DOWNLOADER_CLIENT_TLS_CIPHERS
Default: 'DEFAULT'
UsethissettingtocustomizetheTLS/SSLciphersusedbythedefaultHTTP/1.1downloader.
ThesettingshouldcontainastringintheOpenSSLcipherlistformat,thesecipherswillbeusedasclientciphers. Chang-
ingthissettingmaybenecessarytoaccesscertainHTTPSwebsites: forexample,youmayneedtouse'DEFAULT:!DH'
forawebsitewithweakDHparametersorenableaspecificcipherthatisnotincludedinDEFAULTifawebsiterequires
it.
DOWNLOADER_CLIENT_TLS_METHOD
Default: 'TLS'
UsethissettingtocustomizetheTLS/SSLmethodusedbythedefaultHTTP/1.1downloader.
Thissettingmustbeoneofthesestringvalues:
• 'TLS':mapstoOpenSSL’sTLS_method()(a.k.aSSLv23_method()),whichallowsprotocolnegotiation,start-
ingfromthehighestsupportedbytheplatform;default,recommended
• 'TLSv1.0': thisvalueforcesHTTPSconnectionstouseTLSversion1.0;setthisifyouwantthebehaviorof
Scrapy<1.1
• 'TLSv1.1': forcesTLSversion1.1
• 'TLSv1.2': forcesTLSversion1.2
DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING
Default: False
SettingthistoTruewillenableDEBUGlevelmessagesaboutTLSconnectionparametersafterestablishingHTTPS
connections. ThekindofinformationloggeddependsontheversionsofOpenSSLandpyOpenSSL.
ThissettingisonlyusedforthedefaultDOWNLOADER_CLIENTCONTEXTFACTORY.
134 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
DOWNLOADER_MIDDLEWARES
Default:: {}
Adictcontainingthedownloadermiddlewaresenabledinyourproject,andtheirorders. FormoreinfoseeActivating
adownloadermiddleware.
DOWNLOADER_MIDDLEWARES_BASE
Default:
{
"scrapy.downloadermiddlewares.offsite.OffsiteMiddleware": 50,
"scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware": 100,
"scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware": 300,
"scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware": 350,
"scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware": 400,
"scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": 500,
"scrapy.downloadermiddlewares.retry.RetryMiddleware": 550,
"scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware": 560,
"scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware": 580,
"scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 590,
"scrapy.downloadermiddlewares.redirect.RedirectMiddleware": 600,
"scrapy.downloadermiddlewares.cookies.CookiesMiddleware": 700,
"scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 750,
"scrapy.downloadermiddlewares.stats.DownloaderStats": 850,
"scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware": 900,
}
A dict containing the downloader middlewares enabled by default in Scrapy. Low orders are closer to the en-
gine, high orders are closer to the downloader. You should never modify this setting in your project, modify
DOWNLOADER_MIDDLEWARES instead. FormoreinfoseeActivatingadownloadermiddleware.
DOWNLOADER_STATS
Default: True
Whethertoenabledownloaderstatscollection.
DOWNLOAD_DELAY
Default: 1(fallback: 0)
Minimumsecondstowaitbetween2consecutiverequeststothesamedomain.
UseDOWNLOAD_DELAY tothrottleyourcrawlingspeed,toavoidhittingserverstoohard.
Decimalnumbersaresupported. Forexample,tosendamaximumof4requestsevery10seconds:
DOWNLOAD_DELAY = 2.5
ThissettingisalsoaffectedbytheRANDOMIZE_DOWNLOAD_DELAY setting,whichisenabledbydefault.
WhenCONCURRENT_REQUESTS_PER_IP isnon-zero,delaysareenforcedperIPaddressinsteadofperdomain.
Note that DOWNLOAD_DELAY can lower the effective per-domain concurrency below
CONCURRENT_REQUESTS_PER_DOMAIN. If the response time of a domain is lower than DOWNLOAD_DELAY,
the effective concurrency for that domain is 1. When testing throttling configurations, it usually makes
3.11. Settings 135

ScrapyDocumentation,Release2.13.3
sense to lower CONCURRENT_REQUESTS_PER_DOMAIN first, and only increase DOWNLOAD_DELAY once
CONCURRENT_REQUESTS_PER_DOMAIN is1butahigherthrottlingisdesired.
(cid:242) Note
Thisdelaycanbesetperspiderusingdownload_delayspiderattribute.
Itisalsopossibletochangethissettingperdomain,althoughitrequiresnon-trivialcode. Seetheimplementationof
theAutoThrottleextensionforanexample.
DOWNLOAD_HANDLERS
Default: {}
Adictcontainingtherequestdownloaderhandlersenabledinyourproject. SeeDOWNLOAD_HANDLERS_BASE forex-
ampleformat.
DOWNLOAD_HANDLERS_BASE
Default:
{
"data": "scrapy.core.downloader.handlers.datauri.DataURIDownloadHandler",
"file": "scrapy.core.downloader.handlers.file.FileDownloadHandler",
"http": "scrapy.core.downloader.handlers.http.HTTPDownloadHandler",
"https": "scrapy.core.downloader.handlers.http.HTTPDownloadHandler",
"s3": "scrapy.core.downloader.handlers.s3.S3DownloadHandler",
"ftp": "scrapy.core.downloader.handlers.ftp.FTPDownloadHandler",
}
AdictcontainingtherequestdownloadhandlersenabledbydefaultinScrapy. Youshouldnevermodifythissettingin
yourproject,modifyDOWNLOAD_HANDLERS instead.
YoucandisableanyofthesedownloadhandlersbyassigningNonetotheirURIschemeinDOWNLOAD_HANDLERS.E.g.,
todisablethebuilt-inFTPhandler(withoutreplacement),placethisinyoursettings.py:
DOWNLOAD_HANDLERS = {
"ftp": None,
}
ThedefaultHTTPShandlerusesHTTP/1.1. TouseHTTP/2:
1. InstallTwisted[http2]>=17.9.0toinstallthepackagesrequiredtoenableHTTP/2supportinTwisted.
2. UpdateDOWNLOAD_HANDLERS asfollows:
DOWNLOAD_HANDLERS = {
"https": "scrapy.core.downloader.handlers.http2.H2DownloadHandler",
}
. Warning
HTTP/2supportinScrapyisexperimental,andnotyetrecommendedforproductionenvironments. FutureScrapy
versionsmayintroducerelatedchangeswithoutadeprecationperiodorwarning.
136 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(cid:242) Note
KnownlimitationsofthecurrentHTTP/2implementationofScrapyinclude:
• NosupportforHTTP/2Cleartext(h2c),sincenomajorbrowsersupportsHTTP/2unencrypted(referhttp2
faq).
• Nosettingtospecifyamaximumframesizelargerthanthedefaultvalue,16384. Connectionstoserversthat
sendalargerframewillfail.
• Nosupportforserverpushes,whichareignored.
• Nosupportforthebytes_received andheaders_received signals.
DOWNLOAD_SLOTS
Default: {}
Allowstodefineconcurrency/delayparametersonperslot(domain)basis:
DOWNLOAD_SLOTS = {
"quotes.toscrape.com": {"concurrency": 1, "delay": 2, "randomize_delay":␣
False},
˓→
"books.toscrape.com": {"delay": 3, "randomize_delay": False},
}
(cid:242) Note
Forotherdownloaderslotsdefaultsettingsvalueswillbeused:
• DOWNLOAD_DELAY:delay
• CONCURRENT_REQUESTS_PER_DOMAIN:concurrency
• RANDOMIZE_DOWNLOAD_DELAY:randomize_delay
DOWNLOAD_TIMEOUT
Default: 180
Theamountoftime(insecs)thatthedownloaderwillwaitbeforetimingout.
(cid:242) Note
This timeout can be set per spider using download_timeout spider attribute and per-request using
download_timeoutRequest.metakey.
DOWNLOAD_MAXSIZE
Default: 1073741824(1GiB)
Themaximumresponsebodysize(inbytes)allowed. Biggerresponsesareabortedandignored.
This applies both before and after compression. If decompressing a response body would exceed this limit, decom-
pressionisabortedandtheresponseisignored.
3.11. Settings 137

ScrapyDocumentation,Release2.13.3
Use0todisablethislimit.
This limit can be set per spider using the download_maxsize spider attribute and per request using the
download_maxsizeRequest.metakey.
DOWNLOAD_WARNSIZE
Default: 33554432(32MiB)
Ifthesizeofaresponseexceedsthisvalue,beforeoraftercompression,awarningwillbeloggedaboutit.
Use0todisablethislimit.
This limit can be set per spider using the download_warnsize spider attribute and per request using the
download_warnsizeRequest.metakey.
DOWNLOAD_FAIL_ON_DATALOSS
Default: True
Whetherornottofailonbrokenresponses,thatis,declaredContent-Lengthdoesnotmatchcontentsentbytheserver
orchunkedresponsewasnotproperlyfinish. IfTrue,theseresponsesraiseaResponseFailed([_DataLoss])error.
If False,theseresponsesarepassedthroughandtheflagdatalossisaddedtotheresponse,i.e.: 'dataloss' in
response.flagsisTrue.
Optionally,thiscanbesetper-requestbasisbyusingthedownload_fail_on_datalossRequest.metakeytoFalse.
(cid:242) Note
Abroken response, ordatalosserror, mayhappenunderseveral circumstances, fromservermisconfiguration to
network errors to data corruption. It is up to the user to decide if it makes sense to process broken responses
consideringtheymaycontainpartialorincompletecontent. IfRETRY_ENABLED isTrueandthissettingissetto
True,theResponseFailed([_DataLoss])failurewillberetriedasusual.
. Warning
This setting is ignored by the H2DownloadHandler download handler (see DOWNLOAD_HANDLERS). In case of a
datalosserror,thecorrespondingHTTP/2connectionmaybecorrupted,affectingotherrequeststhatusethesame
connection;hence,aResponseFailed([InvalidBodyLengthError])failureisalwaysraisedforeveryrequest
thatwasusingthatconnection.
DUPEFILTER_CLASS
Default: 'scrapy.dupefilters.RFPDupeFilter'
Theclassusedtodetectandfilterduplicaterequests.
Thedefault,RFPDupeFilter,filtersbasedontheREQUEST_FINGERPRINTER_CLASS setting.
Tochangehowduplicatesarechecked,youcanpointDUPEFILTER_CLASS toacustomsubclassofRFPDupeFilter
thatoverridesits__init__methodtouseadifferentrequestfingerprintingclass. Forexample:
from scrapy.dupefilters import RFPDupeFilter
from scrapy.utils.request import fingerprint
(continuesonnextpage)
138 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class CustomRequestFingerprinter:
def fingerprint(self, request):
return fingerprint(request, include_headers=["X-ID"])
class CustomDupeFilter(RFPDupeFilter):
def __init__(self, path=None, debug=False, *, fingerprinter=None):
super().__init__(
path=path, debug=debug, fingerprinter=CustomRequestFingerprinter()
)
TodisableduplicaterequestfilteringsetDUPEFILTER_CLASS to'scrapy.dupefilters.BaseDupeFilter'. Note
thatnotfilteringoutduplicaterequestsmaycausecrawlingloops. Itisusuallybettertosetthedont_filterparameter
toTrueonthe__init__methodofaspecificRequestobjectthatshouldnotbefilteredout.
AclassassignedtoDUPEFILTER_CLASS mustimplementthefollowinginterface:
class MyDupeFilter:
@classmethod
def from_settings(cls, settings):
"""Returns an instance of this duplicate request filtering class
based on the current crawl settings."""
return cls()
def request_seen(self, request):
"""Returns ``True`` if *request* is a duplicate of another request
seen in a previous call to :meth:`request_seen`, or ``False``
otherwise."""
return False
def open(self):
"""Called before the spider opens. It may return a deferred."""
pass
def close(self, reason):
"""Called before the spider closes. It may return a deferred."""
pass
def log(self, request, spider):
"""Logs that a request has been filtered out.
It is called right after a call to :meth:`request_seen` that
returns ``True``.
If :meth:`request_seen` always returns ``False``, such as in the
case of :class:`~scrapy.dupefilters.BaseDupeFilter`, this method
may be omitted.
"""
pass
class scrapy.dupefilters.BaseDupeFilter
3.11. Settings 139

ScrapyDocumentation,Release2.13.3
Dummyduplicaterequestfilteringclass(DUPEFILTER_CLASS)thatdoesnotfilteroutanyrequest.
class scrapy.dupefilters.RFPDupeFilter(path: str|None=None,debug: bool=False,*,fingerprinter:
RequestFingerprinterProtocol|None=None)
Duplicaterequestfilteringclass(DUPEFILTER_CLASS)thatfiltersoutrequestswiththecanonical(w3lib.url.
canonicalize_url())url,methodandbody.
DUPEFILTER_DEBUG
Default: False
Bydefault, RFPDupeFilteronlylogsthefirstduplicaterequest. SettingDUPEFILTER_DEBUG toTruewillmakeit
logallduplicaterequests.
EDITOR
Default: vi(onUnixsystems)ortheIDLEeditor(onWindows)
Theeditortouseforeditingspiderswiththeeditcommand. Additionally,iftheEDITORenvironmentvariableisset,
theeditcommandwillpreferitoverthedefaultsetting.
EXTENSIONS
Default:: {}
Componentprioritydictionaryofenabledextensions. SeeExtensions.
EXTENSIONS_BASE
Default:
{
"scrapy.extensions.corestats.CoreStats": 0,
"scrapy.extensions.telnet.TelnetConsole": 0,
"scrapy.extensions.memusage.MemoryUsage": 0,
"scrapy.extensions.memdebug.MemoryDebugger": 0,
"scrapy.extensions.closespider.CloseSpider": 0,
"scrapy.extensions.feedexport.FeedExporter": 0,
"scrapy.extensions.logstats.LogStats": 0,
"scrapy.extensions.spiderstate.SpiderState": 0,
"scrapy.extensions.throttle.AutoThrottle": 0,
}
AdictcontainingtheextensionsavailablebydefaultinScrapy,andtheirorders. Thissettingcontainsallstablebuilt-in
extensions. Keepinmindthatsomeofthemneedtobeenabledthroughasetting.
FormoreinformationSeetheextensionsuserguideandthelistofavailableextensions.
FEED_TEMPDIR
TheFeedTempdirallowsyoutosetacustomfoldertosavecrawlertemporaryfilesbeforeuploadingwithFTPfeed
storageandAmazonS3.
140 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
FEED_STORAGE_GCS_ACL
TheAccessControlList(ACL)usedwhenstoringitemstoGoogleCloudStorage. Formoreinformationonhowtoset
thisvalue,pleaserefertothecolumnJSONAPI inGoogleClouddocumentation.
FTP_PASSIVE_MODE
Default: True
WhetherornottousepassivemodewheninitiatingFTPtransfers.
FTP_PASSWORD
Default: "guest"
ThepasswordtouseforFTPconnectionswhenthereisno"ftp_password"inRequestmeta.
(cid:242) Note
Paraphrasing RFC 1635, although it is common to use either the password “guest” or one’s e-mail address for
anonymous FTP, some FTP servers explicitly ask for the user’s e-mail address and will not allow login with the
“guest”password.
FTP_USER
Default: "anonymous"
TheusernametouseforFTPconnectionswhenthereisno"ftp_user"inRequestmeta.
GCS_PROJECT_ID
Default: None
TheProjectIDthatwillbeusedwhenstoringdataonGoogleCloudStorage.
ITEM_PIPELINES
Default: {}
Adictcontainingtheitempipelinestouse,andtheirorders. Ordervaluesarearbitrary,butitiscustomarytodefine
theminthe0-1000range. Lowerordersprocessbeforehigherorders.
Example:
ITEM_PIPELINES = {
"mybot.pipelines.validate.ValidateMyItem": 300,
"mybot.pipelines.validate.StoreMyItem": 800,
}
ITEM_PIPELINES_BASE
Default: {}
A dict containing the pipelines enabled by default in Scrapy. You should never modify this setting in your project,
modifyITEM_PIPELINES instead.
3.11. Settings 141

ScrapyDocumentation,Release2.13.3
JOBDIR
Default: None
Astringindicatingthedirectoryforstoringthestateofacrawlwhenpausingandresumingcrawls.
LOG_ENABLED
Default: True
Whethertoenablelogging.
LOG_ENCODING
Default: 'utf-8'
Theencodingtouseforlogging.
LOG_FILE
Default: None
Filenametouseforloggingoutput. If None,standarderrorwillbeused.
LOG_FILE_APPEND
Default: True
If False,thelogfilespecifiedwithLOG_FILE willbeoverwritten(discardingtheoutputfrompreviousruns,ifany).
LOG_FORMAT
Default: '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
Stringforformattinglogmessages. RefertothePythonloggingdocumentationforthewholelistofavailableplace-
holders.
LOG_DATEFORMAT
Default: '%Y-%m-%d %H:%M:%S'
Stringforformattingdate/time,expansionofthe%(asctime)splaceholderinLOG_FORMAT.RefertothePythondate-
timedocumentationforthewholelistofavailabledirectives.
LOG_FORMATTER
Default: scrapy.logformatter.LogFormatter
Theclasstouseforformattinglogmessagesfordifferentactions.
LOG_LEVEL
Default: 'DEBUG'
Minimum level to log. Available levels are: CRITICAL, ERROR, WARNING, INFO, DEBUG. For more info see
Logging.
142 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
LOG_STDOUT
Default: False
If True, all standard output (and error) of your process will be redirected to the log. For example if you
print('hello')itwillappearintheScrapylog.
LOG_SHORT_NAMES
Default: False
If True,thelogswilljustcontaintherootpath. IfitissettoFalsethenitdisplaysthecomponentresponsibleforthe
logoutput
LOG_VERSIONS
Default: ["lxml", "libxml2", "cssselect", "parsel", "w3lib", "Twisted", "Python",
"pyOpenSSL", "cryptography", "Platform"]
Logstheinstalledversionsofthespecifieditems.
AnitemcanbeanyinstalledPythonpackage.
Thefollowingspecialitemsarealsosupported:
• libxml2
• Platform(platform.platform())
• Python
LOGSTATS_INTERVAL
Default: 60.0
Theinterval(inseconds)betweeneachloggingprintoutofthestatsbyLogStats.
MEMDEBUG_ENABLED
Default: False
Whethertoenablememorydebugging.
MEMDEBUG_NOTIFY
Default: []
Whenmemorydebuggingisenabledamemoryreportwillbesenttothespecifiedaddressesifthissettingisnotempty,
otherwisethereportwillbewrittentothelog.
Example:
MEMDEBUG_NOTIFY = ['user@example.com']
MEMUSAGE_ENABLED
Default: True
Scope: scrapy.extensions.memusage
Whether to enable the memory usage extension. This extension keeps track of a peak memory used by the pro-
cess (it writes it to stats). It can also optionally shutdown the Scrapy process when it exceeds a memory limit (see
MEMUSAGE_LIMIT_MB),andnotifybyemailwhenthathappened(seeMEMUSAGE_NOTIFY_MAIL).
3.11. Settings 143

ScrapyDocumentation,Release2.13.3
SeeMemoryusageextension.
MEMUSAGE_LIMIT_MB
Default: 0
Scope: scrapy.extensions.memusage
Themaximumamountofmemorytoallow(inmegabytes)beforeshuttingdownScrapy(ifMEMUSAGE_ENABLED
isTrue). Ifzero,nocheckwillbeperformed.
SeeMemoryusageextension.
MEMUSAGE_CHECK_INTERVAL_SECONDS
Default: 60.0
Scope: scrapy.extensions.memusage
The Memory usage extension checks the current memory usage, versus the limits set by MEMUSAGE_LIMIT_MB and
MEMUSAGE_WARNING_MB,atfixedtimeintervals.
Thissetsthelengthoftheseintervals,inseconds.
SeeMemoryusageextension.
MEMUSAGE_NOTIFY_MAIL
Default: False
Scope: scrapy.extensions.memusage
Alistofemailstonotifyifthememorylimithasbeenreached.
Example:
MEMUSAGE_NOTIFY_MAIL = ['user@example.com']
SeeMemoryusageextension.
MEMUSAGE_WARNING_MB
Default: 0
Scope: scrapy.extensions.memusage
Themaximumamountofmemorytoallow(inmegabytes)beforesendingawarningemailnotifyingaboutit. Ifzero,
nowarningwillbeproduced.
NEWSPIDER_MODULE
Default: "<project name>.spiders"(fallback: "")
Modulewheretocreatenewspidersusingthegenspidercommand.
Example:
NEWSPIDER_MODULE = 'mybot.spiders_dev'
144 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
RANDOMIZE_DOWNLOAD_DELAY
Default: True
Ifenabled,Scrapywillwaitarandomamountoftime(between0.5*DOWNLOAD_DELAY and1.5*DOWNLOAD_DELAY)
whilefetchingrequestsfromthesamewebsite.
This randomization decreases the chance of the crawler being detected (and subsequently blocked) by sites which
analyzerequestslookingforstatisticallysignificantsimilaritiesinthetimebetweentheirrequests.
Therandomizationpolicyisthesameusedbywget--random-waitoption.
IfDOWNLOAD_DELAY iszero(default)thisoptionhasnoeffect.
REACTOR_THREADPOOL_MAXSIZE
Default: 10
ThemaximumlimitforTwistedReactorthreadpoolsize. Thisiscommonmulti-purposethreadpoolusedbyvarious
Scrapy components. Threaded DNS Resolver, BlockingFeedStorage, S3FilesStore just to name a few. Increase this
valueifyou’reexperiencingproblemswithinsufficientblockingIO.
REDIRECT_PRIORITY_ADJUST
Default: +2
Scope: scrapy.downloadermiddlewares.redirect.RedirectMiddleware
Adjustredirectrequestpriorityrelativetooriginalrequest:
• apositivepriorityadjust(default)meanshigherpriority.
• anegativepriorityadjustmeanslowerpriority.
ROBOTSTXT_OBEY
Default: True(fallback: False)
Ifenabled,Scrapywillrespectrobots.txtpolicies. FormoreinformationseeRobotsTxtMiddleware.
(cid:242) Note
WhilethedefaultvalueisFalseforhistoricalreasons,thisoptionisenabledbydefaultinsettings.pyfilegenerated
byscrapy startprojectcommand.
ROBOTSTXT_PARSER
Default: 'scrapy.robotstxt.ProtegoRobotParser'
Theparserbackendtouseforparsingrobots.txtfiles. FormoreinformationseeRobotsTxtMiddleware.
ROBOTSTXT_USER_AGENT
Default: None
Theuseragentstringtouseformatchingintherobots.txtfile. IfNone,theUser-Agentheaderyouaresendingwiththe
requestortheUSER_AGENT setting(inthatorder)willbeusedfordeterminingtheuseragenttouseintherobots.txt
file.
3.11. Settings 145

ScrapyDocumentation,Release2.13.3
SCHEDULER
Default: 'scrapy.core.scheduler.Scheduler'
Theschedulerclasstobeusedforcrawling. SeetheSchedulertopicfordetails.
SCHEDULER_DEBUG
Default: False
SettingtoTruewilllogdebuginformationabouttherequestsscheduler. Thiscurrentlylogs(onlyonce)iftherequests
cannotbeserializedtodisk. Statscounter(scheduler/unserializable)tracksthenumberoftimesthishappens.
Exampleentryinlogs:
1956-01-31 00:00:00+0800 [scrapy.core.scheduler] ERROR: Unable to serialize request:
<GET http://example.com> - reason: cannot serialize <Request at 0x9a7c7ec>
(type Request)> - no more unserializable requests will be logged
(see 'scheduler/unserializable' stats counter)
SCHEDULER_DISK_QUEUE
Default: 'scrapy.squeues.PickleLifoDiskQueue'
Type of disk queue that will be used by the scheduler. Other available types are scrapy.
squeues.PickleFifoDiskQueue, scrapy.squeues.MarshalFifoDiskQueue, scrapy.squeues.
MarshalLifoDiskQueue.
SCHEDULER_MEMORY_QUEUE
Default: 'scrapy.squeues.LifoMemoryQueue'
Typeofin-memoryqueueusedbythescheduler. Otheravailabletypeis: scrapy.squeues.FifoMemoryQueue.
SCHEDULER_PRIORITY_QUEUE
Default: 'scrapy.pqueues.ScrapyPriorityQueue'
Type of priority queue used by the scheduler. Another available type is scrapy.pqueues.
DownloaderAwarePriorityQueue. scrapy.pqueues.DownloaderAwarePriorityQueue works bet-
ter than scrapy.pqueues.ScrapyPriorityQueue when you crawl many different domains in paral-
lel. But currently scrapy.pqueues.DownloaderAwarePriorityQueue does not work together with
CONCURRENT_REQUESTS_PER_IP.
SCHEDULER_START_DISK_QUEUE
Default: 'scrapy.squeues.PickleFifoDiskQueue'
Typeofdiskqueue(seeJOBDIR)thattheschedulerusesforstartrequests.
Foravailablechoices,seeSCHEDULER_DISK_QUEUE.
UseNoneor""todisabletheseseparatequeuesentirely,andinsteadhavestartrequestssharethesamequeuesasother
requests.
(cid:242) Note
Disablingseparatestartrequestqueuesmakesstartrequestorder unintuitive: startrequestswillbesentinorder
onlyuntilCONCURRENT_REQUESTS isreached,thenremainingstartrequestswillbesentinreverseorder.
146 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
SCHEDULER_START_MEMORY_QUEUE
Default: 'scrapy.squeues.FifoMemoryQueue'
Typeofin-memoryqueuethattheschedulerusesforstartrequests.
Foravailablechoices,seeSCHEDULER_MEMORY_QUEUE.
UseNoneor""todisabletheseseparatequeuesentirely,andinsteadhavestartrequestssharethesamequeuesasother
requests.
(cid:242) Note
Disablingseparatestartrequestqueuesmakesstartrequestorder unintuitive: startrequestswillbesentinorder
onlyuntilCONCURRENT_REQUESTS isreached,thenremainingstartrequestswillbesentinreverseorder.
SCRAPER_SLOT_MAX_ACTIVE_SIZE
Addedinversion2.0.
Default: 5_000_000
Softlimit(inbytes)forresponsedatabeingprocessed.
Whilethesumofthesizesofallresponsesbeingprocessedisabovethisvalue,Scrapydoesnotprocessnewrequests.
SPIDER_CONTRACTS
Default:: {}
A dict containing the spider contracts enabled in your project, used for testing spiders. For more info see Spiders
Contracts.
SPIDER_CONTRACTS_BASE
Default:
{
"scrapy.contracts.default.UrlContract": 1,
"scrapy.contracts.default.ReturnsContract": 2,
"scrapy.contracts.default.ScrapesContract": 3,
}
A dict containing the Scrapy contracts enabled by default in Scrapy. You should never modify this setting in your
project,modifySPIDER_CONTRACTS instead. FormoreinfoseeSpidersContracts.
YoucandisableanyofthesecontractsbyassigningNonetotheirclasspathinSPIDER_CONTRACTS.E.g.,todisable
thebuilt-inScrapesContract,placethisinyoursettings.py:
SPIDER_CONTRACTS = {
"scrapy.contracts.default.ScrapesContract": None,
}
3.11. Settings 147

ScrapyDocumentation,Release2.13.3
SPIDER_LOADER_CLASS
Default: 'scrapy.spiderloader.SpiderLoader'
Theclassthatwillbeusedforloadingspiders,whichmustimplementtheSpiderLoaderAPI.
SPIDER_LOADER_WARN_ONLY
Default: False
By default, when Scrapy tries to import spider classes from SPIDER_MODULES, it will fail loudly if there is any
ImportError or SyntaxError exception. But you can choose to silence this exception and turn it into a simple
warningbysettingSPIDER_LOADER_WARN_ONLY = True.
(cid:242) Note
SomescrapycommandsrunwiththissettingtoTruealready(i.e. theywillonlyissueawarningandwillnotfail)
sincetheydonotactuallyneedtoloadspiderclassestowork: scrapy runspider,scrapy settings,scrapy
startproject,scrapy version.
SPIDER_MIDDLEWARES
Default:: {}
A dict containing the spider middlewares enabled in your project, and their orders. For more info see Activating a
spidermiddleware.
SPIDER_MIDDLEWARES_BASE
Default:
{
"scrapy.spidermiddlewares.httperror.HttpErrorMiddleware": 50,
"scrapy.spidermiddlewares.referer.RefererMiddleware": 700,
"scrapy.spidermiddlewares.urllength.UrlLengthMiddleware": 800,
"scrapy.spidermiddlewares.depth.DepthMiddleware": 900,
}
AdictcontainingthespidermiddlewaresenabledbydefaultinScrapy,andtheirorders. Lowordersareclosertothe
engine,highordersareclosertothespider. FormoreinfoseeActivatingaspidermiddleware.
SPIDER_MODULES
Default: ["<project name>.spiders"](fallback: [])
AlistofmoduleswhereScrapywilllookforspiders.
Example:
SPIDER_MODULES = ["mybot.spiders_prod", "mybot.spiders_dev"]
STATS_CLASS
Default: 'scrapy.statscollectors.MemoryStatsCollector'
Theclasstouseforcollectingstats,whomustimplementtheStatsCollectorAPI.
148 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
STATS_DUMP
Default: True
DumptheScrapystats(totheScrapylog)oncethespiderfinishes.
Formoreinfosee: StatsCollection.
STATSMAILER_RCPTS
Default: [](emptylist)
SendScrapystatsafterspidersfinishscraping. SeeStatsMailerformoreinfo.
TELNETCONSOLE_ENABLED
Default: True
Abooleanwhichspecifiesifthetelnetconsolewillbeenabled(provideditsextensionisalsoenabled).
TEMPLATES_DIR
Default: templatesdirinsidescrapymodule
Thedirectorywheretolookfortemplateswhencreatingnewprojectswithstartprojectcommandandnewspiders
withgenspidercommand.
Theprojectnamemustnotconflictwiththenameofcustomfilesordirectoriesintheprojectsubdirectory.
TWISTED_REACTOR
Addedinversion2.0.
Default: "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
Importpathofagivenreactor.
Scrapywillinstallthisreactorifnootherreactorisinstalledyet,suchaswhenthescrapyCLIprogramisinvokedor
whenusingtheCrawlerProcessclass.
IfyouareusingtheCrawlerRunnerclass,youalsoneedtoinstallthecorrectreactormanually. Youcandothatusing
install_reactor():
scrapy.utils.reactor.install_reactor(reactor_path: str,event_loop_path: str|None=None)→None
Installsthereactorwiththespecifiedimportpath. Alsoinstallstheasyncioeventloopwiththespecifiedimport
pathiftheasyncioreactorisenabled
Ifareactorisalreadyinstalled,install_reactor()hasnoeffect.
CrawlerRunner.__init__raisesExceptioniftheinstalledreactordoesnotmatchtheTWISTED_REACTOR setting;
therefore,havingtop-levelreactorimportsinprojectfilesandimportedthird-partylibrarieswillmakeScrapyraise
Exceptionwhenitcheckswhichreactorisinstalled.
InordertousethereactorinstalledbyScrapy:
import scrapy
from twisted.internet import reactor
class QuotesSpider(scrapy.Spider):
name = "quotes"
(continuesonnextpage)
3.11. Settings 149

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
def __init__(self, *args, **kwargs):
self.timeout = int(kwargs.pop("timeout", "60"))
super(QuotesSpider, self).__init__(*args, **kwargs)
async def start(self):
reactor.callLater(self.timeout, self.stop)
urls = ["https://quotes.toscrape.com/page/1"]
for url in urls:
yield scrapy.Request(url=url, callback=self.parse)
def parse(self, response):
for quote in response.css("div.quote"):
yield {"text": quote.css("span.text::text").get()}
def stop(self):
self.crawler.engine.close_spider(self, "timeout")
whichraisesException,becomes:
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes"
def __init__(self, *args, **kwargs):
self.timeout = int(kwargs.pop("timeout", "60"))
super(QuotesSpider, self).__init__(*args, **kwargs)
async def start(self):
from twisted.internet import reactor
reactor.callLater(self.timeout, self.stop)
urls = ["https://quotes.toscrape.com/page/1"]
for url in urls:
yield scrapy.Request(url=url, callback=self.parse)
def parse(self, response):
for quote in response.css("div.quote"):
yield {"text": quote.css("span.text::text").get()}
def stop(self):
self.crawler.engine.close_spider(self, "timeout")
Ifthissettingisset None,Scrapywillusetheexistingreactorifoneisalreadyinstalled,orinstallthedefaultreactor
definedbyTwistedforthecurrentplatform.
Changed in version 2.7: The startproject command now sets this setting to twisted.internet.
asyncioreactor.AsyncioSelectorReactorinthegeneratedsettings.pyfile.
Changed in version 2.13: The default value was changed from None to "twisted.internet.asyncioreactor.
AsyncioSelectorReactor".
150 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
Foradditionalinformation,seeChoosingaReactorandGUIToolkitIntegration.
URLLENGTH_LIMIT
Default: 2083
Scope: spidermiddlewares.urllength
ThemaximumURLlengthtoallowforcrawledURLs.
ThissettingcanactasastoppingconditionincaseofURLsofever-increasinglength,whichmaybecausedforexample
byaprogrammingerroreitherinthetargetserverorinyourcode. SeealsoREDIRECT_MAX_TIMESandDEPTH_LIMIT.
Use0toallowURLsofanylength.
ThedefaultvalueiscopiedfromtheMicrosoftInternetExplorermaximumURLlength,eventhoughthissettingexists
fordifferentreasons.
USER_AGENT
Default: "Scrapy/VERSION (+https://scrapy.org)"
The default User-Agent to use when crawling, unless overridden. This user agent is also used by
RobotsTxtMiddleware if ROBOTSTXT_USER_AGENT setting is None and there is no overriding User-Agent header
specifiedfortherequest.
WARN_ON_GENERATOR_RETURN_VALUE
Default: True
Whenenabled,Scrapywillwarnifgenerator-basedcallbackmethods(likeparse)containreturnstatementswithnon-
Nonevalues. Thishelpsdetectpotentialmistakesinspiderdevelopment.
Disable this setting to prevent syntax errors that may occur when dynamically modifying generator function source
codeduringruntime,skipASTparsingofcallbackfunctions,orimproveperformanceinauto-reloadingdevelopment
environments.
Settingsdocumentedelsewhere:
Thefollowingsettingsaredocumentedelsewhere,pleasecheckeachspecificcasetoseehowtoenableandusethem.
• ADDONS
• ASYNCIO_EVENT_LOOP
• AUTOTHROTTLE_DEBUG
• AUTOTHROTTLE_ENABLED
• AUTOTHROTTLE_MAX_DELAY
• AUTOTHROTTLE_START_DELAY
• AUTOTHROTTLE_TARGET_CONCURRENCY
• AWS_ACCESS_KEY_ID
• AWS_ENDPOINT_URL
• AWS_REGION_NAME
• AWS_SECRET_ACCESS_KEY
• AWS_SESSION_TOKEN
• AWS_USE_SSL
3.11. Settings 151

ScrapyDocumentation,Release2.13.3
• AWS_VERIFY
• BOT_NAME
• CLOSESPIDER_ERRORCOUNT
• CLOSESPIDER_ITEMCOUNT
• CLOSESPIDER_PAGECOUNT
• CLOSESPIDER_PAGECOUNT_NO_ITEM
• CLOSESPIDER_TIMEOUT
• CLOSESPIDER_TIMEOUT_NO_ITEM
• COMMANDS_MODULE
• COMPRESSION_ENABLED
• CONCURRENT_ITEMS
• CONCURRENT_REQUESTS
• CONCURRENT_REQUESTS_PER_DOMAIN
• CONCURRENT_REQUESTS_PER_IP
• COOKIES_DEBUG
• COOKIES_ENABLED
• DEFAULT_DROPITEM_LOG_LEVEL
• DEFAULT_ITEM_CLASS
• DEFAULT_REQUEST_HEADERS
• DEPTH_LIMIT
• DEPTH_PRIORITY
• DEPTH_STATS_VERBOSE
• DNSCACHE_ENABLED
• DNSCACHE_SIZE
• DNS_RESOLVER
• DNS_TIMEOUT
• DOWNLOADER
• DOWNLOADER_CLIENTCONTEXTFACTORY
• DOWNLOADER_CLIENT_TLS_CIPHERS
• DOWNLOADER_CLIENT_TLS_METHOD
• DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING
• DOWNLOADER_HTTPCLIENTFACTORY
• DOWNLOADER_MIDDLEWARES
• DOWNLOADER_MIDDLEWARES_BASE
• DOWNLOADER_STATS
• DOWNLOAD_DELAY
152 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
• DOWNLOAD_FAIL_ON_DATALOSS
• DOWNLOAD_HANDLERS
• DOWNLOAD_HANDLERS_BASE
• DOWNLOAD_MAXSIZE
• DOWNLOAD_SLOTS
• DOWNLOAD_TIMEOUT
• DOWNLOAD_WARNSIZE
• DUPEFILTER_CLASS
• DUPEFILTER_DEBUG
• EDITOR
• EXTENSIONS
• EXTENSIONS_BASE
• FEEDS
• FEED_EXPORTERS
• FEED_EXPORTERS_BASE
• FEED_EXPORT_BATCH_ITEM_COUNT
• FEED_EXPORT_ENCODING
• FEED_EXPORT_FIELDS
• FEED_EXPORT_INDENT
• FEED_STORAGES
• FEED_STORAGES_BASE
• FEED_STORAGE_FTP_ACTIVE
• FEED_STORAGE_GCS_ACL
• FEED_STORAGE_S3_ACL
• FEED_STORE_EMPTY
• FEED_TEMPDIR
• FEED_URI_PARAMS
• FILES_EXPIRES
• FILES_RESULT_FIELD
• FILES_STORE
• FILES_STORE_GCS_ACL
• FILES_STORE_S3_ACL
• FILES_URLS_FIELD
• FTP_PASSIVE_MODE
• FTP_PASSWORD
• FTP_USER
3.11. Settings 153

ScrapyDocumentation,Release2.13.3
• GCS_PROJECT_ID
• HTTPCACHE_ALWAYS_STORE
• HTTPCACHE_DBM_MODULE
• HTTPCACHE_DIR
• HTTPCACHE_ENABLED
• HTTPCACHE_EXPIRATION_SECS
• HTTPCACHE_GZIP
• HTTPCACHE_IGNORE_HTTP_CODES
• HTTPCACHE_IGNORE_MISSING
• HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS
• HTTPCACHE_IGNORE_SCHEMES
• HTTPCACHE_POLICY
• HTTPCACHE_STORAGE
• HTTPERROR_ALLOWED_CODES
• HTTPERROR_ALLOW_ALL
• HTTPPROXY_AUTH_ENCODING
• HTTPPROXY_ENABLED
• IMAGES_EXPIRES
• IMAGES_MIN_HEIGHT
• IMAGES_MIN_WIDTH
• IMAGES_RESULT_FIELD
• IMAGES_STORE
• IMAGES_STORE_GCS_ACL
• IMAGES_STORE_S3_ACL
• IMAGES_THUMBS
• IMAGES_URLS_FIELD
• ITEM_PIPELINES
• ITEM_PIPELINES_BASE
• JOBDIR
• LOGSTATS_INTERVAL
• LOG_DATEFORMAT
• LOG_ENABLED
• LOG_ENCODING
• LOG_FILE
• LOG_FILE_APPEND
• LOG_FORMAT
154 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
• LOG_FORMATTER
• LOG_LEVEL
• LOG_SHORT_NAMES
• LOG_STDOUT
• LOG_VERSIONS
• MAIL_FROM
• MAIL_HOST
• MAIL_PASS
• MAIL_PORT
• MAIL_SSL
• MAIL_TLS
• MAIL_USER
• MEDIA_ALLOW_REDIRECTS
• MEMDEBUG_ENABLED
• MEMDEBUG_NOTIFY
• MEMUSAGE_CHECK_INTERVAL_SECONDS
• MEMUSAGE_ENABLED
• MEMUSAGE_LIMIT_MB
• MEMUSAGE_NOTIFY_MAIL
• MEMUSAGE_WARNING_MB
• METAREFRESH_ENABLED
• METAREFRESH_IGNORE_TAGS
• METAREFRESH_MAXDELAY
• NEWSPIDER_MODULE
• PERIODIC_LOG_DELTA
• PERIODIC_LOG_STATS
• PERIODIC_LOG_TIMING_ENABLED
• RANDOMIZE_DOWNLOAD_DELAY
• REACTOR_THREADPOOL_MAXSIZE
• REDIRECT_ENABLED
• REDIRECT_MAX_TIMES
• REDIRECT_PRIORITY_ADJUST
• REFERER_ENABLED
• REFERRER_POLICY
• REQUEST_FINGERPRINTER_CLASS
• RETRY_ENABLED
3.11. Settings 155

ScrapyDocumentation,Release2.13.3
• RETRY_EXCEPTIONS
• RETRY_HTTP_CODES
• RETRY_PRIORITY_ADJUST
• RETRY_TIMES
• ROBOTSTXT_OBEY
• ROBOTSTXT_PARSER
• ROBOTSTXT_USER_AGENT
• SCHEDULER
• SCHEDULER_DEBUG
• SCHEDULER_DISK_QUEUE
• SCHEDULER_MEMORY_QUEUE
• SCHEDULER_PRIORITY_QUEUE
• SCHEDULER_START_DISK_QUEUE
• SCHEDULER_START_MEMORY_QUEUE
• SCRAPER_SLOT_MAX_ACTIVE_SIZE
• SPIDER_CONTRACTS
• SPIDER_CONTRACTS_BASE
• SPIDER_LOADER_CLASS
• SPIDER_LOADER_WARN_ONLY
• SPIDER_MIDDLEWARES
• SPIDER_MIDDLEWARES_BASE
• SPIDER_MODULES
• STATSMAILER_RCPTS
• STATS_CLASS
• STATS_DUMP
• TELNETCONSOLE_ENABLED
• TELNETCONSOLE_HOST
• TELNETCONSOLE_PASSWORD
• TELNETCONSOLE_PORT
• TELNETCONSOLE_USERNAME
• TEMPLATES_DIR
• TWISTED_REACTOR
• URLLENGTH_LIMIT
• USER_AGENT
• WARN_ON_GENERATOR_RETURN_VALUE
156 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
3.12 Exceptions
3.12.1 Built-in Exceptions reference
Here’salistofallexceptionsincludedinScrapyandtheirusage.
CloseSpider
exception scrapy.exceptions.CloseSpider(reason='cancelled')
Thisexceptioncanberaisedfromaspidercallbacktorequestthespidertobeclosed/stopped. Supportedargu-
ments:
Parameters
reason(str)–thereasonforclosing
Forexample:
def parse_page(self, response):
if "Bandwidth exceeded" in response.body:
raise CloseSpider("bandwidth_exceeded")
DontCloseSpider
exception scrapy.exceptions.DontCloseSpider
Thisexceptioncanberaisedinaspider_idlesignalhandlertopreventthespiderfrombeingclosed.
DropItem
exception scrapy.exceptions.DropItem
TheexceptionthatmustberaisedbyitempipelinestagestostopprocessinganItem. FormoreinformationseeItem
Pipeline.
IgnoreRequest
exception scrapy.exceptions.IgnoreRequest
This exception can be raised by the Scheduler or any downloader middleware to indicate that the request should be
ignored.
NotConfigured
exception scrapy.exceptions.NotConfigured
Thisexceptioncanberaisedbysomecomponentstoindicatethattheywillremaindisabled. Thosecomponentsinclude:
• Extensions
• Itempipelines
• Downloadermiddlewares
• Spidermiddlewares
Theexceptionmustberaisedinthecomponent’s__init__method.
3.12. Exceptions 157

ScrapyDocumentation,Release2.13.3
NotSupported
exception scrapy.exceptions.NotSupported
Thisexceptionisraisedtoindicateanunsupportedfeature.
StopDownload
Addedinversion2.2.
exception scrapy.exceptions.StopDownload(fail=True)
Raised from a bytes_received or headers_received signal handler to indicate that no further bytes should be
downloadedforaresponse.
Thefailbooleanparametercontrolswhichmethodwillhandletheresultingresponse:
• Iffail=True(default),therequesterrbackiscalled. Theresponseobjectisavailableastheresponseattribute
oftheStopDownloadexception,whichisinturnstoredasthevalueattributeofthereceivedFailureobject.
Thismeansthatinanerrbackdefinedasdef errback(self, failure),theresponsecanbeaccessedthough
failure.value.response.
• If fail=False,therequestcallbackiscalledinstead.
Inbothcases,theresponsecouldhaveitsbodytruncated: thebodycontainsallbytesreceivedupuntiltheexceptionis
raised,includingthebytesreceivedinthesignalhandlerthatraisestheexception. Also,theresponseobjectismarked
with"download_stopped"initsflagsattribute.
(cid:242) Note
fail is a keyword-only parameter, i.e. raising StopDownload(False) or StopDownload(True) will raise a
TypeError.
Seethedocumentationforthebytes_received andheaders_received signalsandtheStoppingthedownloadof
aResponsetopicforadditionalinformationandexamples.
Commandlinetool
Learnaboutthecommand-linetoolusedtomanageyourScrapyproject.
Spiders
Writetherulestocrawlyourwebsites.
Selectors
ExtractthedatafromwebpagesusingXPath.
Scrapyshell
Testyourextractioncodeinaninteractiveenvironment.
Items
Definethedatayouwanttoscrape.
ItemLoaders
Populateyouritemswiththeextracteddata.
ItemPipeline
Post-processandstoreyourscrapeddata.
Feedexports
Outputyourscrapeddatausingdifferentformatsandstorages.
158 Chapter3. Basicconcepts

ScrapyDocumentation,Release2.13.3
RequestsandResponses
UnderstandtheclassesusedtorepresentHTTPrequestsandresponses.
LinkExtractors
Convenientclassestoextractlinkstofollowfrompages.
Settings
LearnhowtoconfigureScrapyandseeallavailablesettings.
Exceptions
Seeallavailableexceptionsandtheirmeaning.
3.12. Exceptions 159

ScrapyDocumentation,Release2.13.3
160 Chapter3. Basicconcepts

CHAPTER
FOUR
BUILT-IN SERVICES
4.1 Logging
(cid:242) Note
scrapy.loghasbeendeprecatedalongsideitsfunctionsinfavorofexplicitcallstothePythonstandardlogging.
Keepreadingtolearnmoreaboutthenewloggingsystem.
Scrapyusesloggingforeventlogging. We’llprovidesomesimpleexamplestogetyoustarted,butformoreadvanced
use-casesit’sstronglysuggestedtoreadthoroughlyitsdocumentation.
Loggingworksoutofthebox,andcanbeconfiguredtosomeextentwiththeScrapysettingslistedinLoggingsettings.
Scrapycallsscrapy.utils.log.configure_logging()tosetsomereasonabledefaultsandhandlethosesettings
inLoggingsettingswhenrunningcommands,soit’srecommendedtomanuallycallitifyou’rerunningScrapyfrom
scriptsasdescribedinRunScrapyfromascript.
4.1.1 Log levels
Python’sbuiltinloggingdefines5differentlevelstoindicatetheseverityofagivenlogmessage. Herearethestandard
ones,listedindecreasingorder:
1. logging.CRITICAL-forcriticalerrors(highestseverity)
2. logging.ERROR-forregularerrors
3. logging.WARNING-forwarningmessages
4. logging.INFO-forinformationalmessages
5. logging.DEBUG-fordebuggingmessages(lowestseverity)
4.1.2 How to log messages
Here’saquickexampleofhowtologamessageusingthelogging.WARNINGlevel:
import logging
logging.warning("This is a warning")
Thereareshortcutsforissuinglogmessagesonanyofthestandard5levels,andthere’salsoagenerallogging.log
methodwhichtakesagivenlevelasargument. Ifneeded,thelastexamplecouldberewrittenas:
161

ScrapyDocumentation,Release2.13.3
import logging
logging.log(logging.WARNING, "This is a warning")
On top of that, you can create different “loggers” to encapsulate messages. (For example, a common practice is to
createdifferentloggersforeverymodule). Theseloggerscanbeconfiguredindependently,andtheyallowhierarchical
constructions.
The previous examples use the root logger behind the scenes, which is a top level logger where all messages are
propagated to (unless otherwise specified). Using logging helpers is merely a shortcut for getting the root logger
explicitly,sothisisalsoanequivalentofthelastsnippets:
import logging
logger = logging.getLogger()
logger.warning("This is a warning")
Youcanuseadifferentloggerjustbygettingitsnamewiththelogging.getLoggerfunction:
import logging
logger = logging.getLogger("mycustomlogger")
logger.warning("This is a warning")
Finally, you can ensure having a custom logger for any module you’re working on by using the __name__ variable,
whichispopulatedwithcurrentmodule’spath:
import logging
logger = logging.getLogger(__name__)
logger.warning("This is a warning")
ª Seealso
Modulelogging,HowTo
BasicLoggingTutorial
Modulelogging,Loggers
Furtherdocumentationonloggers
4.1.3 Logging from Spiders
ScrapyprovidesaloggerwithineachSpiderinstance,whichcanbeaccessedandusedlikethis:
import scrapy
class MySpider(scrapy.Spider):
name = "myspider"
start_urls = ["https://scrapy.org"]
def parse(self, response):
self.logger.info("Parse function called on %s", response.url)
162 Chapter4. Built-inservices

ScrapyDocumentation,Release2.13.3
ThatloggeriscreatedusingtheSpider’sname,butyoucanuseanycustomPythonloggeryouwant. Forexample:
import logging
import scrapy
logger = logging.getLogger("mycustomlogger")
class MySpider(scrapy.Spider):
name = "myspider"
start_urls = ["https://scrapy.org"]
def parse(self, response):
logger.info("Parse function called on %s", response.url)
4.1.4 Logging configuration
Loggersontheirowndon’tmanagehowmessagessentthroughthemaredisplayed. Forthistask,different“handlers”
can be attached to any logger instance and they will redirect those messages to appropriate destinations, such as the
standardoutput,files,emails,etc.
Bydefault,Scrapysetsandconfiguresahandlerfortherootlogger,basedonthesettingsbelow.
Loggingsettings
Thesesettingscanbeusedtoconfigurethelogging:
• LOG_FILE
• LOG_FILE_APPEND
• LOG_ENABLED
• LOG_ENCODING
• LOG_LEVEL
• LOG_FORMAT
• LOG_DATEFORMAT
• LOG_STDOUT
• LOG_SHORT_NAMES
Thefirstcoupleofsettingsdefineadestinationforlogmessages. IfLOG_FILE isset,messagessentthroughtheroot
loggerwillberedirectedtoafilenamedLOG_FILEwithencodingLOG_ENCODING.IfunsetandLOG_ENABLEDisTrue,
log messages will be displayed on the standard error. If LOG_FILE is set and LOG_FILE_APPEND is False, the file
willbeoverwritten(discardingtheoutputfrompreviousruns,ifany). Lastly,ifLOG_ENABLED isFalse,therewon’t
beanyvisiblelogoutput.
LOG_LEVEL determinestheminimumlevelofseveritytodisplay, thosemessageswithlowerseveritywillbefiltered
out. ItrangesthroughthepossiblelevelslistedinLoglevels.
LOG_FORMAT and LOG_DATEFORMAT specify formatting strings used as layouts for all messages. Those strings can
contain any placeholders listed in logging’s logrecord attributes docs and datetime’s strftime and strptime directives
respectively.
If LOG_SHORT_NAMES is set, then the logs will not display the Scrapy component that prints the log. It is unset by
default,hencelogscontaintheScrapycomponentresponsibleforthatlogoutput.
4.1. Logging 163

ScrapyDocumentation,Release2.13.3
Command-lineoptions
Therearecommand-linearguments,availableforallcommands,thatyoucanusetooverridesomeoftheScrapysettings
regardinglogging.
• --logfile FILE
OverridesLOG_FILE
• --loglevel/-L LEVEL
OverridesLOG_LEVEL
• --nolog
SetsLOG_ENABLED toFalse
ª Seealso
Modulelogging.handlers
Furtherdocumentationonavailablehandlers
CustomLogFormats
AcustomlogformatcanbesetfordifferentactionsbyextendingLogFormatterclassandmakingLOG_FORMATTER
pointtoyournewclass.
class scrapy.logformatter.LogFormatter
Classforgeneratinglogmessagesfordifferentactions.
Allmethodsmustreturnadictionarylistingtheparameterslevel,msgandargswhicharegoingtobeusedfor
constructingthelogmessagewhencallinglogging.log.
Dictionarykeysforthemethodoutputs:
• levelistheloglevelforthataction,youcanusethosefromthepythonlogginglibrary: logging.DEBUG,
logging.INFO,logging.WARNING,logging.ERRORandlogging.CRITICAL.
• msgshouldbeastringthatcancontaindifferentformattingplaceholders. Thisstring,formattedwiththe
providedargs,isgoingtobethelongmessageforthataction.
• argsshouldbeatupleordictwiththeformattingplaceholdersformsg. Thefinallogmessageiscomputed
asmsg % args.
UserscandefinetheirownLogFormatterclassiftheywanttocustomizehoweachactionisloggedorifthey
wanttoomititentirely. InordertoomitlogginganactionthemethodmustreturnNone.
Hereisanexampleonhowtocreateacustomlogformattertolowertheseveritylevelofthelogmessagewhen
anitemisdroppedfromthepipeline:
class PoliteLogFormatter(logformatter.LogFormatter):
def dropped(self, item, exception, response, spider):
return {
'level': logging.INFO, # lowering the level from logging.WARNING
'msg': "Dropped: %(exception)s" + os.linesep + "%(item)s",
'args': {
'exception': exception,
'item': item,
}
}
164 Chapter4. Built-inservices

ScrapyDocumentation,Release2.13.3
crawled(request: Request,response: Response,spider: Spider)→LogFormatterResult
Logsamessagewhenthecrawlerfindsawebpage.
download_error(failure: Failure,request: Request,spider: Spider,errmsg: str|None=None)→
LogFormatterResult
Logsadownloaderrormessagefromaspider(typicallycomingfromtheengine).
Addedinversion2.0.
dropped(item: Any,exception: BaseException,response: Response|Failure|None,spider: Spider)→
LogFormatterResult
Logsamessagewhenanitemisdroppedwhileitispassingthroughtheitempipeline.
item_error(item: Any,exception: BaseException,response: Response|Failure|None,spider: Spider)→
LogFormatterResult
Logsamessagewhenanitemcausesanerrorwhileitispassingthroughtheitempipeline.
Addedinversion2.0.
scraped(item: Any,response: Response|Failure|None,spider: Spider)→LogFormatterResult
Logsamessagewhenanitemisscrapedbyaspider.
spider_error(failure: Failure,request: Request,response: Response|Failure,spider: Spider)→
LogFormatterResult
Logsanerrormessagefromaspider.
Addedinversion2.0.
Advancedcustomization
BecauseScrapyusesstdlibloggingmodule,youcancustomizeloggingusingallfeaturesofstdliblogging.
Forexample, let’ssayyou’rescrapingawebsitewhichreturnsmanyHTTP404and500responses, andyouwantto
hideallmessageslikethis:
2016-12-16 22:00:06 [scrapy.spidermiddlewares.httperror] INFO: Ignoring
response <500 https://quotes.toscrape.com/page/1-34/>: HTTP status code
is not handled or not allowed
Thefirstthingtonoteisaloggername-itisinbrackets: [scrapy.spidermiddlewares.httperror]. Ifyouget
just[scrapy]thenLOG_SHORT_NAMES islikelysettoTrue;setittoFalseandre-runthecrawl.
Next, we can see that the message has INFO level. To hide it we should set logging level for scrapy.
spidermiddlewares.httperrorhigherthanINFO;nextlevelafterINFOisWARNING.Itcouldbedonee.g. in
thespider’s__init__method:
import logging
import scrapy
class MySpider(scrapy.Spider):
# ...
def __init__(self, *args, **kwargs):
logger = logging.getLogger("scrapy.spidermiddlewares.httperror")
logger.setLevel(logging.WARNING)
super().__init__(*args, **kwargs)
4.1. Logging 165

ScrapyDocumentation,Release2.13.3
IfyourunthisspideragainthenINFOmessagesfromscrapy.spidermiddlewares.httperrorloggerwillbegone.
YoucanalsofilterlogrecordsbyLogRecorddata. Forexample,youcanfilterlogrecordsbymessagecontentusing
asubstringoraregularexpression. Createalogging.Filtersubclassandequipitwitharegularexpressionpattern
tofilteroutunwantedmessages:
import logging
import re
class ContentFilter(logging.Filter):
def filter(self, record):
match = re.search(r"\d{3} [Ee]rror, retrying", record.message)
if match:
return False
Aproject-levelfiltermaybeattachedtotheroothandlercreatedbyScrapy,thisisawieldywaytofilterallloggersin
differentpartsoftheproject(middlewares,spider,etc.):
import logging
import scrapy
class MySpider(scrapy.Spider):
# ...
def __init__(self, *args, **kwargs):
for handler in logging.root.handlers:
handler.addFilter(ContentFilter())
Alternatively,youmaychooseaspecificloggerandhideitwithoutaffectingotherloggers:
import logging
import scrapy
class MySpider(scrapy.Spider):
# ...
def __init__(self, *args, **kwargs):
logger = logging.getLogger("my_logger")
logger.addFilter(ContentFilter())
4.1.5 scrapy.utils.log module
scrapy.utils.log.configure_logging(settings: Settings|dict[bool|float|int|str|None,Any]|None=
None,install_root_handler: bool=True)→None
InitializeloggingdefaultsforScrapy.
Parameters
• settings(dict,SettingsobjectorNone)–settingsusedtocreateandconfigureahan-
dlerfortherootlogger(default: None).
• install_root_handler(bool)–whethertoinstallrootlogginghandler(default:True)
Thisfunctiondoes:
• RoutewarningsandtwistedloggingthroughPythonstandardlogging
166 Chapter4. Built-inservices

ScrapyDocumentation,Release2.13.3
• AssignDEBUGandERRORleveltoScrapyandTwistedloggersrespectively
• RoutestdouttologifLOG_STDOUTsettingisTrue
Wheninstall_root_handlerisTrue(default),thisfunctionalsocreatesahandlerfortherootloggeraccord-
ingtogivensettings(seeLoggingsettings). Youcanoverridedefaultoptionsusingsettingsargument. When
settingsisemptyorNone,defaultsareused.
configure_loggingisautomaticallycalledwhenusingScrapycommandsorCrawlerProcess,butneedsto
becalledexplicitlywhenrunningcustomscriptsusingCrawlerRunner. Inthatcase,itsusageisnotrequired
butit’srecommended.
Another option when running custom scripts is to manually configure the logging. To do this you can use
logging.basicConfig()tosetabasicroothandler.
Note that CrawlerProcess automatically calls configure_logging, so it is recommended to only use
logging.basicConfig()togetherwithCrawlerRunner.
ThisisanexampleonhowtoredirectINFOorhighermessagestoafile:
import logging
logging.basicConfig(
filename="log.txt", format="%(levelname)s: %(message)s", level=logging.INFO
)
RefertoRunScrapyfromascriptformoredetailsaboutusingScrapythisway.
4.2 Stats Collection
Scrapyprovidesaconvenientfacilityforcollectingstatsintheformofkey/values,wherevaluesareoftencounters. The
facilityiscalledtheStatsCollector,andcanbeaccessedthroughthestatsattributeoftheCrawlerAPI,asillustrated
bytheexamplesintheCommonStatsCollectorusessectionbelow.
However, the Stats Collector is always available, so you can always import it in your module and use its API (to
incrementor setnew statkeys), regardlessof whetherthe statscollection isenabled ornot. Ifit’s disabled, the API
willstillworkbutitwon’tcollectanything. Thisisaimedatsimplifyingthestatscollectorusage: youshouldspendno
morethanonelineofcodeforcollectingstatsinyourspider,Scrapyextension,orwhatevercodeyou’reusingtheStats
Collectorfrom.
AnotherfeatureoftheStatsCollectoristhatit’sveryefficient(whenenabled)andextremelyefficient(almostunno-
ticeable)whendisabled.
TheStatsCollectorkeepsastatstableperopenspiderwhichisautomaticallyopenedwhenthespiderisopened,and
closedwhenthespiderisclosed.
4.2.1 Common Stats Collector uses
Accessthestatscollectorthroughthestatsattribute. Hereisanexampleofanextensionthataccessstats:
class ExtensionThatAccessStats:
def __init__(self, stats):
self.stats = stats
@classmethod
def from_crawler(cls, crawler):
return cls(crawler.stats)
4.2. StatsCollection 167

ScrapyDocumentation,Release2.13.3
Setstatvalue:
stats.set_value("hostname", socket.gethostname())
Incrementstatvalue:
stats.inc_value("custom_count")
Setstatvalueonlyifgreaterthanprevious:
stats.max_value("max_items_scraped", value)
Setstatvalueonlyiflowerthanprevious:
stats.min_value("min_free_memory_percent", value)
Getstatvalue:
>>> stats.get_value("custom_count")
1
Getallstats:
>>> stats.get_stats()
{'custom_count': 1, 'start_time': datetime.datetime(2009, 7, 14, 21, 47, 28, 977139)}
4.2.2 Available Stats Collectors
BesidesthebasicStatsCollectorthereareotherStatsCollectorsavailableinScrapywhichextendthebasicStats
Collector. YoucanselectwhichStatsCollectortousethroughtheSTATS_CLASS setting. ThedefaultStatsCollector
usedistheMemoryStatsCollector.
MemoryStatsCollector
class scrapy.statscollectors.MemoryStatsCollector
A simple stats collector that keeps the stats of the last scraping run (for each spider) in memory, after they’re
closed. Thestatscanbeaccessedthroughthespider_statsattribute,whichisadictkeyedbyspiderdomain
name.
ThisisthedefaultStatsCollectorusedinScrapy.
spider_stats
Adictofdicts(keyedbyspidername)containingthestatsofthelastscrapingrunforeachspider.
DummyStatsCollector
class scrapy.statscollectors.DummyStatsCollector
AStatscollectorwhichdoesnothingbutisveryefficient(becauseitdoesnothing). Thisstatscollectorcanbeset
viatheSTATS_CLASSsetting,todisablestatscollectinordertoimproveperformance. However,theperformance
penaltyofstatscollectionisusuallymarginalcomparedtootherScrapyworkloadlikeparsingpages.
4.3 Sending e-mail
AlthoughPythonmakessendinge-mailsrelativelyeasyviathesmtpliblibrary,Scrapyprovidesitsownfacilityfor
sending e-mails which is very easy to use and it’s implemented using Twisted non-blocking IO, to avoid interfering
168 Chapter4. Built-inservices

ScrapyDocumentation,Release2.13.3
withthenon-blockingIOofthecrawler. ItalsoprovidesasimpleAPIforsendingattachmentsandit’sveryeasyto
configure,withafewsettings.
4.3.1 Quick example
Therearetwowaystoinstantiatethemailsender. Youcaninstantiateitusingthestandard__init__method:
from scrapy.mail import MailSender
mailer = MailSender()
Oryoucaninstantiateitpassingascrapy.Crawlerinstance,whichwillrespectthesettings:
mailer = MailSender.from_crawler(crawler)
Andhereishowtouseittosendane-mail(withoutattachments):
mailer.send(
to=["someone@example.com"],
subject="Some subject",
body="Some body",
cc=["another@example.com"],
)
4.3.2 MailSender class reference
TheMailSendercomponentsisthepreferredclasstouseforsendingemailsfromScrapy,asitusesTwistednon-blocking
IO,liketherestoftheframework.
class scrapy.mail.MailSender(smtphost=None,mailfrom=None,smtpuser=None,smtppass=None,
smtpport=None)
Parameters
• smtphost(str or bytes)–theSMTPhosttouseforsendingtheemails. Ifomitted,
theMAIL_HOST settingwillbeused.
• mailfrom(str)–theaddressusedtosendemails(intheFrom: header). Ifomitted,the
MAIL_FROM settingwillbeused.
• smtpuser–theSMTPuser. Ifomitted,theMAIL_USER settingwillbeused. Ifnotgiven,
noSMTPauthenticationwillbeperformed.
• smtppass(str or bytes)–theSMTPpassforauthentication.
• smtpport(int)–theSMTPporttoconnectto
• smtptls(bool)–enforceusingSMTPSTARTTLS
• smtpssl(bool)–enforceusingasecureSSLconnection
send(to,subject,body,cc=None,attachs=(),mimetype='text/plain',charset=None)
Sendemailtothegivenrecipients.
Parameters
• to(str or list)–thee-mailrecipientsasastringorasalistofstrings
• subject(str)–thesubjectofthee-mail
• cc(str or list)–thee-mailstoCCasastringorasalistofstrings
4.3. Sendinge-mail 169

ScrapyDocumentation,Release2.13.3
• body(str)–thee-mailbody
• attachs (collections.abc.Iterable) – an iterable of tuples (attach_name,
mimetype, file_object)whereattach_nameisastringwiththenamethatwill
appearonthee-mail’sattachment,mimetypeisthemimetypeoftheattachmentand
file_objectisareadablefileobjectwiththecontentsoftheattachment
• mimetype(str)–theMIMEtypeofthee-mail
• charset(str)–thecharacterencodingtouseforthee-mailcontents
4.3.3 Mail settings
These settings define the default __init__ method values of the MailSender class, and can be used to configure
e-mailnotificationsinyourprojectwithoutwritinganycode(forthoseextensionsandcodethatusesMailSender).
MAIL_FROM
Default: 'scrapy@localhost'
Senderemailtouse(From: header)forsendingemails.
MAIL_HOST
Default: 'localhost'
SMTPhosttouseforsendingemails.
MAIL_PORT
Default: 25
SMTPporttouseforsendingemails.
MAIL_USER
Default: None
UsertouseforSMTPauthentication. IfdisablednoSMTPauthenticationwillbeperformed.
MAIL_PASS
Default: None
PasswordtouseforSMTPauthentication,alongwithMAIL_USER.
MAIL_TLS
Default: False
Enforce using STARTTLS. STARTTLS is a way to take an existing insecure connection, and upgrade it to a secure
connectionusingSSL/TLS.
MAIL_SSL
Default: False
EnforceconnectingusinganSSLencryptedconnection
170 Chapter4. Built-inservices

ScrapyDocumentation,Release2.13.3
4.4 Telnet Console
Scrapycomeswithabuilt-intelnetconsoleforinspectingandcontrollingaScrapyrunningprocess. Thetelnetconsole
isjustaregularpythonshellrunninginsidetheScrapyprocess,soyoucandoliterallyanythingfromit.
The telnet console is a built-in Scrapy extension which comes enabled by default, but you can also disable it if you
want. FormoreinformationabouttheextensionitselfseeTelnetconsoleextension.
. Warning
It is not secure to use telnet console via public networks, as telnet doesn’t provide any transport-layer security.
Havingusername/passwordauthenticationdoesn’tchangethat.
IntendedusageisconnectingtoarunningScrapyspiderlocally(spiderprocessandtelnetclientareonthesamema-
chine)oroverasecureconnection(VPN,SSHtunnel). Pleaseavoidusingtelnetconsoleoverinsecureconnections,
ordisableitcompletelyusingTELNETCONSOLE_ENABLED option.
4.4.1 How to access the telnet console
ThetelnetconsolelistensintheTCPportdefinedintheTELNETCONSOLE_PORT setting,whichdefaultsto6023. To
accesstheconsoleyouneedtotype:
telnet localhost 6023
Trying localhost...
Connected to localhost.
Escape character is '^]'.
Username:
Password:
>>>
BydefaultUsernameisscrapyandPasswordisautogenerated. TheautogeneratedPasswordcanbeseenonScrapy
logsliketheexamplebelow:
2018-10-16 14:35:21 [scrapy.extensions.telnet] INFO: Telnet Password: 16f92501e8a59326
Default Username and Password can be overridden by the settings TELNETCONSOLE_USERNAME and
TELNETCONSOLE_PASSWORD.
. Warning
Usernameandpasswordprovideonlyalimitedprotection,astelnetisnotusingsecuretransport-bydefaulttraffic
isnotencryptedevenifusernameandpasswordareset.
YouneedthetelnetprogramwhichcomesinstalledbydefaultinWindows,andmostLinuxdistros.
4.4.2 Available variables in the telnet console
The telnet console is like a regular Python shell running inside the Scrapy process, so you can do anything from it
includingimportingnewmodules,etc.
However,thetelnetconsolecomeswithsomedefaultvariablesdefinedforconvenience:
4.4. TelnetConsole 171

ScrapyDocumentation,Release2.13.3
Shortcut Description
crawler theScrapyCrawler(scrapy.crawler.Crawlerobject)
engine Crawler.engineattribute
spider theactivespider
extensions theExtensionManager(Crawler.extensionsattribute)
stats theStatsCollector(Crawler.statsattribute)
settings theScrapysettingsobject(Crawler.settingsattribute)
est printareportoftheenginestatus
prefs formemorydebugging(seeDebuggingmemoryleaks)
p ashortcuttothepprint.pprint()function
hpy formemorydebugging(seeDebuggingmemoryleaks)
4.4.3 Telnet console usage examples
Herearesomeexampletasksyoucandowiththetelnetconsole:
Viewenginestatus
Youcanusetheest()methodoftheScrapyenginetoquicklyshowitsstateusingthetelnetconsole:
telnet localhost 6023
>>> est()
Execution engine status
time()-engine.start_time : 8.62972998619
len(engine.downloader.active) : 16
engine.scraper.is_idle() : False
engine.spider.name : followall
engine.spider_is_idle() : False
engine._slot.closing : False
len(engine._slot.inprogress) : 16
len(engine._slot.scheduler.dqs or []) : 0
len(engine._slot.scheduler.mqs) : 92
len(engine.scraper.slot.queue) : 0
len(engine.scraper.slot.active) : 0
engine.scraper.slot.active_size : 0
engine.scraper.slot.itemproc_size : 0
engine.scraper.slot.needs_backout() : False
Pause,resumeandstoptheScrapyengine
Topause:
telnet localhost 6023
>>> engine.pause()
>>>
Toresume:
telnet localhost 6023
>>> engine.unpause()
>>>
172 Chapter4. Built-inservices

ScrapyDocumentation,Release2.13.3
Tostop:
telnet localhost 6023
>>> engine.stop()
Connection closed by foreign host.
4.4.4 Telnet Console signals
scrapy.extensions.telnet.update_telnet_vars(telnet_vars)
Sentjustbeforethetelnetconsoleisopened. Youcanhookuptothissignaltoadd,removeorupdatethevariables
thatwillbeavailableinthetelnetlocalnamespace. Inordertodothat, youneedtoupdatethe telnet_vars
dictinyourhandler.
Parameters
telnet_vars(dict)–thedictoftelnetvariables
4.4.5 Telnet settings
Thesearethesettingsthatcontrolthetelnetconsole’sbehaviour:
TELNETCONSOLE_PORT
Default: [6023, 6073]
Theportrangetouseforthetelnetconsole. IfsettoNone,adynamicallyassignedportisused.
TELNETCONSOLE_HOST
Default: '127.0.0.1'
Theinterfacethetelnetconsoleshouldlistenon
TELNETCONSOLE_USERNAME
Default: 'scrapy'
Theusernameusedforthetelnetconsole
TELNETCONSOLE_PASSWORD
Default: None
Thepasswordusedforthetelnetconsole,defaultbehaviouristohaveitautogenerated
Logging
LearnhowtousePython’sbuiltinloggingonScrapy.
StatsCollection
Collectstatisticsaboutyourscrapingcrawler.
Sendinge-mail
Sendemailnotificationswhencertaineventsoccur.
TelnetConsole
Inspectarunningcrawlerusingabuilt-inPythonconsole.
4.4. TelnetConsole 173

ScrapyDocumentation,Release2.13.3
174 Chapter4. Built-inservices

CHAPTER
FIVE
SOLVING SPECIFIC PROBLEMS
5.1 Frequently Asked Questions
5.1.1 How does Scrapy compare to BeautifulSoup or lxml?
BeautifulSoupandlxmlarelibrariesforparsingHTMLandXML.Scrapyisanapplicationframeworkforwritingweb
spidersthatcrawlwebsitesandextractdatafromthem.
Scrapy provides a built-in mechanism for extracting data (called selectors) but you can easily use BeautifulSoup (or
lxml)instead, ifyoufeelmorecomfortableworkingwiththem. Afterall, they’rejustparsinglibrarieswhichcanbe
importedandusedfromanyPythoncode.
Inotherwords,comparingBeautifulSoup(orlxml)toScrapyislikecomparingjinja2toDjango.
5.1.2 Can I use Scrapy with BeautifulSoup?
Yes,youcan. Asmentionedabove,BeautifulSoupcanbeusedforparsingHTMLresponsesinScrapycallbacks. You
justhavetofeedtheresponse’sbodyintoaBeautifulSoupobjectandextractwhateverdatayouneedfromit.
Here’sanexamplespiderusingBeautifulSoupAPI,withlxmlastheHTMLparser:
from bs4 import BeautifulSoup
import scrapy
class ExampleSpider(scrapy.Spider):
name = "example"
allowed_domains = ["example.com"]
start_urls = ("http://www.example.com/",)
def parse(self, response):
# use lxml to get decent HTML parsing speed
soup = BeautifulSoup(response.text, "lxml")
yield {"url": response.url, "title": soup.h1.string}
(cid:242) Note
BeautifulSoupsupportsseveralHTML/XMLparsers. SeeBeautifulSoup’sofficialdocumentationonwhichones
areavailable.
175

ScrapyDocumentation,Release2.13.3
5.1.3 Did Scrapy “steal” X from Django?
Probably, but we don’t like that word. We think Django is a great open source project and an example to follow, so
we’veuseditasaninspirationforScrapy.
Webelievethat,ifsomethingisalreadydonewell,there’snoneedtoreinventit. Thisconcept,besidesbeingoneof
thefoundationsforopensourceandfreesoftware,notonlyappliestosoftwarebutalsotodocumentation,procedures,
policies,etc. So,insteadofgoingthrougheachproblemourselves,wechoosetocopyideasfromthoseprojectsthat
havealreadysolvedthemproperly,andfocusontherealproblemsweneedtosolve.
We’dbeproudifScrapyservesasaninspirationforotherprojects. Feelfreetostealfromus!
5.1.4 Does Scrapy work with HTTP proxies?
Yes. SupportforHTTPproxiesisprovided(sinceScrapy0.8)throughtheHTTPProxydownloadermiddleware. See
HttpProxyMiddleware.
5.1.5 How can I scrape an item with attributes in different pages?
SeePassingadditionaldatatocallbackfunctions.
5.1.6 How can I simulate a user login in my spider?
SeeUsingFormRequest.from_response()tosimulateauserlogin.
5.1.7 Does Scrapy crawl in breadth-first or depth-first order?
DFObydefault,butotherordersarepossible.
5.1.8 My Scrapy crawler has memory leaks. What can I do?
SeeDebuggingmemoryleaks.
Also,PythonhasabuiltinmemoryleakissuewhichisdescribedinLeakswithoutleaks.
5.1.9 How can I make Scrapy consume less memory?
Seepreviousquestion.
5.1.10 How can I prevent memory errors due to many allowed domains?
If you have a spider with a long list of allowed_domains (e.g. 50,000+), consider replacing the default
OffsiteMiddlewaredownloadermiddlewarewithacustomdownloadermiddlewarethatrequireslessmemory. For
example:
• If your domain names are similar enough, use your own regular expression instead joining the strings in
allowed_domainsintoacomplexregularexpression.
• If you can meet the installation requirements, use pyre2 instead of Python’s re to compile your URL-filtering
regularexpression. Seeissue1908.
SeealsoothersuggestionsatStackOverflow.
(cid:242) Note
Remember to disable scrapy.downloadermiddlewares.offsite.OffsiteMiddleware when you enable
yourcustomimplementation:
176 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
DOWNLOADER_MIDDLEWARES = {
"scrapy.downloadermiddlewares.offsite.OffsiteMiddleware": None,
"myproject.middlewares.CustomOffsiteMiddleware": 50,
}
5.1.11 Can I use Basic HTTP Authentication in my spiders?
Yes,seeHttpAuthMiddleware.
5.1.12 WhydoesScrapydownloadpagesinEnglishinsteadofmynativelanguage?
TrychangingthedefaultAccept-LanguagerequestheaderbyoverridingtheDEFAULT_REQUEST_HEADERS setting.
5.1.13 Where can I find some example Scrapy projects?
SeeExamples.
5.1.14 Can I run a spider without creating a project?
Yes. Youcanusetherunspider command. Forexample,ifyouhaveaspiderwrittenina my_spider.pyfileyou
canrunitwith:
scrapy runspider my_spider.py
Seerunspidercommandformoreinfo.
5.1.15 I get “Filtered offsite request” messages. How can I fix them?
Thosemessages(loggedwithDEBUGlevel)don’tnecessarilymeanthereisaproblem,soyoumaynotneedtofixthem.
ThosemessagesarethrownbyOffsiteMiddleware,whichisadownloadermiddleware(enabledbydefault)whose
purposeistofilteroutrequeststodomainsoutsidetheonescoveredbythespider.
5.1.16 What is the recommended way to deploy a Scrapy crawler in production?
SeeDeployingSpiders.
5.1.17 Can I use JSON for large exports?
It’lldependonhowlargeyouroutputis. SeethiswarninginJsonItemExporterdocumentation.
5.1.18 Can I return (Twisted) deferreds from signal handlers?
Somesignalssupportreturningdeferredsfromtheirhandlers,othersdon’t. SeetheBuilt-insignalsreferencetoknow
whichones.
5.1.19 What does the response status code 999 mean?
999isacustomresponsestatuscodeusedbyYahoositestothrottlerequests. Tryslowingdownthecrawlingspeedby
usingadownloaddelayof 2(orhigher)inyourspider:
5.1. FrequentlyAskedQuestions 177

ScrapyDocumentation,Release2.13.3
from scrapy.spiders import CrawlSpider
class MySpider(CrawlSpider):
name = "myspider"
download_delay = 2
# [ ... rest of the spider code ... ]
OrbysettingaglobaldownloaddelayinyourprojectwiththeDOWNLOAD_DELAY setting.
5.1.20 Can I call pdb.set_trace() from my spiders to debug them?
Yes,butyoucanalsousetheScrapyshellwhichallowsyoutoquicklyanalyze(andevenmodify)theresponsebeing
processedbyyourspider,whichis,quiteoften,moreusefulthanplainoldpdb.set_trace().
FormoreinfoseeInvokingtheshellfromspiderstoinspectresponses.
5.1.21 Simplest way to dump all my scraped items into a JSON/CSV/XML file?
TodumpintoaJSONfile:
scrapy crawl myspider -O items.json
TodumpintoaCSVfile:
scrapy crawl myspider -O items.csv
TodumpintoanXMLfile:
scrapy crawl myspider -O items.xml
FormoreinformationseeFeedexports
5.1.22 What’s this huge cryptic __VIEWSTATE parameter used in some forms?
The __VIEWSTATE parameter is used in sites built with ASP.NET/VB.NET. For more info on how it works see this
page. Also,here’sanexamplespiderwhichscrapesoneofthesesites.
5.1.23 What’s the best way to parse big XML/CSV data feeds?
Parsing big feeds with XPath selectors can be problematic since they need to build the DOM of the entire feed in
memory,andthiscanbequiteslowandconsumealotofmemory.
In order to avoid parsing all the entire feed at once in memory, you can use the xmliter_lxml() and csviter()
functions. Infact,thisiswhatXMLFeedSpideruses.
scrapy.utils.iterators.xmliter_lxml(obj: Response|str|bytes,nodename: str,namespace: str|None=
None,prefix: str='x')→Iterator[Selector]
scrapy.utils.iterators.csviter(obj: Response|str|bytes,delimiter: str|None=None,headers: list[str]|
None=None,encoding: str|None=None,quotechar: str|None=None)
→Iterator[dict[str,str]]
Returnsaniteratorofdictionariesfromthegivencsvobject
178 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
objcanbe: -aResponseobject-aunicodestring-astringencodedasutf-8
delimiteristhecharacterusedtoseparatefieldsonthegivenobj.
headersisaniterablethatwhenprovidedoffersthekeysforthereturneddictionaries,ifnotthefirstrowisused.
quotecharisthecharacterusedtoenclosurefieldsonthegivenobj.
5.1.24 Does Scrapy manage cookies automatically?
Yes,Scrapyreceivesandkeepstrackofcookiessentbyservers,andsendsthembackonsubsequentrequests,likeany
regularwebbrowserdoes.
FormoreinfoseeRequestsandResponsesandCookiesMiddleware.
5.1.25 How can I see the cookies being sent and received from Scrapy?
EnabletheCOOKIES_DEBUG setting.
5.1.26 How can I instruct a spider to stop itself?
RaisetheCloseSpiderexceptionfromacallback. Formoreinfosee: CloseSpider.
5.1.27 How can I prevent my Scrapy bot from getting banned?
SeeAvoidinggettingbanned.
5.1.28 Should I use spider arguments or settings to configure my spider?
Bothspiderargumentsandsettingscanbeusedtoconfigureyourspider. Thereisnostrictrulethatmandatestouse
oneortheother,butsettingsaremoresuitedforparametersthat,onceset,don’tchangemuch,whilespiderarguments
aremeanttochangemoreoften, evenoneachspiderrunandsometimesarerequiredforthespidertorunatall(for
example,tosetthestarturlofaspider).
Toillustratewithanexample,assumingyouhaveaspiderthatneedstologintoasitetoscrapedata,andyouonlywant
toscrapedatafromacertainsectionofthesite(whichvarieseachtime). Inthatcase,thecredentialstologinwould
besettings,whiletheurlofthesectiontoscrapewouldbeaspiderargument.
5.1.29 I’m scraping a XML document and my XPath selector doesn’t return any
items
Youmayneedtoremovenamespaces. SeeRemovingnamespaces.
5.1.30 How to split an item into multiple items in an item pipeline?
Item pipelines cannot yield multiple items per input item. Create a spider middleware instead, and use its
process_spider_output()methodforthispurpose. Forexample:
from copy import deepcopy
from itemadapter import ItemAdapter
from scrapy import Request
class MultiplyItemsMiddleware:
def process_spider_output(self, response, result, spider):
for item_or_request in result:
(continuesonnextpage)
5.1. FrequentlyAskedQuestions 179

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
if isinstance(item_or_request, Request):
continue
adapter = ItemAdapter(item)
for _ in range(adapter["multiply_by"]):
yield deepcopy(item)
5.1.31 Does Scrapy support IPv6 addresses?
Yes,bysettingDNS_RESOLVER toscrapy.resolver.CachingHostnameResolver. Notethatbydoingso,youlose
theabilitytosetaspecifictimeoutforDNSrequests(thevalueoftheDNS_TIMEOUT settingisignored).
5.1.32 How to deal with <class 'ValueError'>: filedescriptor out of range in
select() exceptions?
This issue has been reported to appear when running broad crawls in macOS, where the default Twisted reactor is
twisted.internet.selectreactor.SelectReactor. Switching to a different reactor is possible by using the
TWISTED_REACTOR setting.
5.1.33 How can I cancel the download of a given response?
In some situations, it might be useful to stop the download of a certain response. For instance, sometimes you can
determinewhetherornotyouneedthefullcontentsofaresponsebyinspectingitsheadersorthefirstbytesofitsbody.
Inthatcase,youcouldsaveresourcesbyattachingahandlertothebytes_received orheaders_received signals
andraisingaStopDownload exception. PleaserefertotheStoppingthedownloadofaResponsetopicforadditional
informationandexamples.
5.1.34 How can I make a blank request?
from scrapy import Request
blank_request = Request("data:,")
In this case, the URL is set to a data URI scheme. Data URLs allow you to include data inline within web pages,
similar to external resources. The “data:” scheme with an empty content (“,”) essentially creates a request to a data
URLwithoutanyspecificcontent.
5.1.35 Running runspider I get error: No spider found in file: <filename>
This may happen if your Scrapy project has a spider module with a name that conflicts with the name of one of the
Pythonstandardlibrarymodules,suchascsv.pyoros.py,oranyPythonpackagethatyouhaveinstalled. Seeissue
2680.
5.2 Debugging Spiders
This document explains the most common techniques for debugging spiders. Consider the following Scrapy spider
below:
import scrapy
from myproject.items import MyItem
(continuesonnextpage)
180 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class MySpider(scrapy.Spider):
name = "myspider"
start_urls = (
"http://example.com/page1",
"http://example.com/page2",
)
def parse(self, response):
# <processing code not shown>
# collect `item_urls`
for item_url in item_urls:
yield scrapy.Request(item_url, self.parse_item)
def parse_item(self, response):
# <processing code not shown>
item = MyItem()
# populate `item` fields
# and extract item_details_url
yield scrapy.Request(
item_details_url, self.parse_details, cb_kwargs={"item": item}
)
def parse_details(self, response, item):
# populate more `item` fields
return item
Basicallythisisasimplespiderwhichparsestwopagesofitems(thestart_urls). Itemsalsohaveadetailspagewith
additionalinformation,soweusethecb_kwargsfunctionalityofRequesttopassapartiallypopulateditem.
5.2.1 Parse Command
Themostbasicwayofcheckingtheoutputofyourspideristousetheparsecommand. Itallowstocheckthebehaviour
ofdifferentpartsofthespideratthemethodlevel. Ithastheadvantageofbeingflexibleandsimpletouse,butdoes
notallowdebuggingcodeinsideamethod.
Inordertoseetheitemscrapedfromaspecificurl:
$ scrapy parse --spider=myspider -c parse_item -d 2 <item_url>
[ ... scrapy log lines crawling example.com spider ... ]
>>> STATUS DEPTH LEVEL 2 <<<
# Scraped Items ------------------------------------------------------------
[{'url': <item_url>}]
# Requests -----------------------------------------------------------------
[]
Usingthe--verboseor-voptionwecanseethestatusateachdepthlevel:
$ scrapy parse --spider=myspider -c parse_item -d 2 -v <item_url>
[ ... scrapy log lines crawling example.com spider ... ]
(continuesonnextpage)
5.2. DebuggingSpiders 181

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
>>> DEPTH LEVEL: 1 <<<
# Scraped Items ------------------------------------------------------------
[]
# Requests -----------------------------------------------------------------
[<GET item_details_url>]
>>> DEPTH LEVEL: 2 <<<
# Scraped Items ------------------------------------------------------------
[{'url': <item_url>}]
# Requests -----------------------------------------------------------------
[]
Checkingitemsscrapedfromasinglestart_url,canalsobeeasilyachievedusing:
$ scrapy parse --spider=myspider -d 3 'http://example.com/page1'
5.2.2 Scrapy Shell
While the parse command is very useful for checking behaviour of a spider, it is of little help to check what hap-
pens inside a callback, besides showing the response received and the output. How to debug the situation when
parse_detailssometimesreceivesnoitem?
Fortunately,theshellisyourbreadandbutterinthiscase(seeInvokingtheshellfromspiderstoinspectresponses):
from scrapy.shell import inspect_response
def parse_details(self, response, item=None):
if item:
# populate more `item` fields
return item
else:
inspect_response(response, self)
Seealso: Invokingtheshellfromspiderstoinspectresponses.
5.2.3 Open in browser
Sometimes you just want to see how a certain response looks in a browser, you can use the open_in_browser()
functionforthat:
scrapy.utils.response.open_in_browser(response: TextResponse,_openfunc: Callable[[str],Any]=
<functionopen>)→Any
Openresponseinalocalwebbrowser,adjustingthebasetagforexternallinkstowork,e.g. sothatimagesand
stylesaredisplayed.
Forexample:
from scrapy.utils.response import open_in_browser
(continuesonnextpage)
182 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
def parse_details(self, response):
if "item name" not in response.body:
open_in_browser(response)
5.2.4 Logging
Loggingisanotherusefuloptionforgettinginformationaboutyourspiderrun. Althoughnotasconvenient,itcomes
withtheadvantagethatthelogswillbeavailableinallfuturerunsshouldtheybenecessaryagain:
def parse_details(self, response, item=None):
if item:
# populate more `item` fields
return item
else:
self.logger.warning("No item received for %s", response.url)
Formoreinformation,checktheLoggingsection.
5.2.5 Visual Studio Code
TodebugspiderswithVisualStudioCodeyoucanusethefollowinglaunch.json:
{
"version": "0.1.0",
"configurations": [
{
"name": "Python: Launch Scrapy Spider",
"type": "python",
"request": "launch",
"module": "scrapy",
"args": [
"runspider",
"${file}"
],
"console": "integratedTerminal"
}
]
}
Also,makesureyouenable“UserUncaughtExceptions”,tocatchexceptionsinyourScrapyspider.
5.3 Spiders Contracts
Testing spiders can get particularly annoying and while nothing prevents you from writing unit tests the task gets
cumbersomequickly. Scrapyoffersanintegratedwayoftestingyourspidersbythemeansofcontracts.
Thisallowsyoutotesteachcallbackofyourspiderbyhardcodingasampleurlandcheckvariousconstraintsforhow
thecallbackprocessestheresponse. Eachcontractisprefixedwithan@andincludedinthedocstring. Seethefollowing
example:
def parse(self, response):
"""
(continuesonnextpage)
5.3. SpidersContracts 183

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
This function parses a sample response. Some contracts are mingled
with this docstring.
@url http://www.example.com/s?field-keywords=selfish+gene
@returns items 1 16
@returns requests 0 0
@scrapes Title Author Year Price
"""
Youcanusethefollowingcontracts:
class scrapy.contracts.default.UrlContract
This contract (@url) sets the sample URL used when checking other contract conditions for this spider. This
contractismandatory. Allcallbackslackingthiscontractareignoredwhenrunningthechecks:
@url url
class scrapy.contracts.default.CallbackKeywordArgumentsContract
This contract (@cb_kwargs) sets the cb_kwargs attribute for the sample request. It must be a valid JSON
dictionary.
@cb_kwargs {"arg1": "value1", "arg2": "value2", ...}
class scrapy.contracts.default.MetadataContract
Thiscontract(@meta)setsthemeta attributeforthesamplerequest. ItmustbeavalidJSONdictionary.
@meta {"arg1": "value1", "arg2": "value2", ...}
class scrapy.contracts.default.ReturnsContract
This contract (@returns) sets lower and upper bounds for the items and requests returned by the spider. The
upperboundisoptional:
@returns item(s)|request(s) [min [max]]
class scrapy.contracts.default.ScrapesContract
Thiscontract(@scrapes)checksthatalltheitemsreturnedbythecallbackhavethespecifiedfields:
@scrapes field_1 field_2 ...
Usethecheck commandtorunthecontractchecks.
5.3.1 Custom Contracts
Ifyoufindyouneedmorepowerthanthebuilt-inScrapycontractsyoucancreateandloadyourowncontractsinthe
projectbyusingtheSPIDER_CONTRACTS setting:
SPIDER_CONTRACTS = {
"myproject.contracts.ResponseCheck": 10,
"myproject.contracts.ItemValidate": 10,
}
EachcontractmustinheritfromContractandcanoverridethreemethods:
184 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
class scrapy.contracts.Contract(method,*args)
Parameters
• method(collections.abc.Callable)–callbackfunctiontowhichthecontractisas-
sociated
• args(list)–listofargumentspassedintothedocstring(whitespaceseparated)
adjust_request_args(args)
Thisreceivesadictasanargumentcontainingdefaultargumentsforrequestobject. Requestisusedby
default,butthiscanbechangedwiththerequest_clsattribute. Ifmultiplecontractsinchainhavethis
attributedefined,thelastoneisused.
Mustreturnthesameoramodifiedversionofit.
pre_process(response)
Thisallowshookinginvariouschecksontheresponsereceivedfromthesamplerequest,beforeit’sbeing
passedtothecallback.
post_process(output)
Thisallowsprocessingtheoutputofthecallback. Iteratorsareconvertedtolistsbeforebeingpassedto
thishook.
RaiseContractFailfrompre_processorpost_processifexpectationsarenotmet:
class scrapy.exceptions.ContractFail
Errorraisedincaseofafailingcontract
Hereisademocontractwhichchecksthepresenceofacustomheaderintheresponsereceived:
from scrapy.contracts import Contract
from scrapy.exceptions import ContractFail
class HasHeaderContract(Contract):
"""
Demo contract which checks the presence of a custom header
@has_header X-CustomHeader
"""
name = "has_header"
def pre_process(self, response):
for header in self.args:
if header not in response.headers:
raise ContractFail("X-CustomHeader not present")
5.3.2 Detecting check runs
When scrapy check is running, the SCRAPY_CHECK environment variable is set to the true string. You can use
os.environtoperformanychangetoyourspidersoryoursettingswhenscrapy checkisused:
import os
import scrapy
(continuesonnextpage)
5.3. SpidersContracts 185

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class ExampleSpider(scrapy.Spider):
name = "example"
def __init__(self):
if os.environ.get("SCRAPY_CHECK"):
pass # Do some scraper adjustments when a check is running
5.4 Common Practices
ThissectiondocumentscommonpracticeswhenusingScrapy. Thesearethingsthatcovermanytopicsanddon’toften
fallintoanyotherspecificsection.
5.4.1 Run Scrapy from a script
YoucanusetheAPI torunScrapyfromascript,insteadofthetypicalwayofrunningScrapyviascrapy crawl.
RememberthatScrapyisbuiltontopoftheTwistedasynchronousnetworkinglibrary,soyouneedtorunitinsidethe
Twistedreactor.
Thefirstutilityyoucanusetorunyourspidersisscrapy.crawler.CrawlerProcess. ThisclasswillstartaTwisted
reactorforyou,configuringtheloggingandsettingshutdownhandlers. ThisclassistheoneusedbyallScrapycom-
mands.
Here’sanexampleshowinghowtorunasinglespiderwithit.
import scrapy
from scrapy.crawler import CrawlerProcess
class MySpider(scrapy.Spider):
# Your spider definition
...
process = CrawlerProcess(
settings={
"FEEDS": {
"items.json": {"format": "json"},
},
}
)
process.crawl(MySpider)
process.start() # the script will block here until the crawling is finished
Define settings within dictionary in CrawlerProcess. Make sure to check CrawlerProcess documentation to get
acquaintedwithitsusagedetails.
If you are inside a Scrapy project there are some additional helpers you can use to import those components
within the project. You can automatically import your spiders passing their name to CrawlerProcess, and use
get_project_settingstogetaSettingsinstancewithyourprojectsettings.
Whatfollowsisaworkingexampleofhowtodothat,usingthetestspidersprojectasexample.
186 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
process = CrawlerProcess(get_project_settings())
# 'followall' is the name of one of the spiders of the project.
process.crawl("followall", domain="scrapy.org")
process.start() # the script will block here until the crawling is finished
There’s another Scrapy utility that provides more control over the crawling process: scrapy.crawler.
CrawlerRunner. This class is a thin wrapper that encapsulates some simple helpers to run multiple crawlers, but
itwon’tstartorinterferewithexistingreactorsinanyway.
Using this class the reactor should be explicitly run after scheduling your spiders. It’s recommended you use
CrawlerRunnerinsteadofCrawlerProcessifyourapplicationisalreadyusingTwistedandyouwanttorunScrapy
inthesamereactor.
NotethatyouwillalsohavetoshutdowntheTwistedreactoryourselfafterthespiderisfinished. Thiscanbeachieved
byaddingcallbackstothedeferredreturnedbytheCrawlerRunner.crawlmethod.
Here’sanexampleofitsusage,alongwithacallbacktomanuallystopthereactorafterMySpiderhasfinishedrunning.
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.reactor import install_reactor
class MySpider(scrapy.Spider):
# Your spider definition
...
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
runner = CrawlerRunner()
d = runner.crawl(MySpider)
from twisted.internet import reactor
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished
Sameexamplebutusingadifferentreactor.
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.reactor import install_reactor
class MySpider(scrapy.Spider):
custom_settings = {
"TWISTED_REACTOR": "twisted.internet.epollreactor.EPollReactor",
(continuesonnextpage)
5.4. CommonPractices 187

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
}
# Your spider definition
...
install_reactor("twisted.internet.epollreactor.EPollReactor")
configure_logging({"LOG_FORMAT": "%(levelname)s: %(message)s"})
runner = CrawlerRunner()
d = runner.crawl(MySpider)
from twisted.internet import reactor
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished
ª Seealso
ReactorOverview
5.4.2 Running multiple spiders in the same process
Bydefault,Scrapyrunsasinglespiderperprocesswhenyourunscrapy crawl. However,Scrapysupportsrunning
multiplespidersperprocessusingtheinternalAPI.
Hereisanexamplethatrunsmultiplespiderssimultaneously:
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
class MySpider1(scrapy.Spider):
# Your first spider definition
...
class MySpider2(scrapy.Spider):
# Your second spider definition
...
settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(MySpider1)
process.crawl(MySpider2)
process.start() # the script will block here until all crawling jobs are finished
SameexampleusingCrawlerRunner:
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
(continuesonnextpage)
188 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
class MySpider1(scrapy.Spider):
# Your first spider definition
...
class MySpider2(scrapy.Spider):
# Your second spider definition
...
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)
runner.crawl(MySpider1)
runner.crawl(MySpider2)
d = runner.join()
from twisted.internet import reactor
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until all crawling jobs are finished
Sameexamplebutrunningthespiderssequentiallybychainingthedeferreds:
from twisted.internet import defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
class MySpider1(scrapy.Spider):
# Your first spider definition
...
class MySpider2(scrapy.Spider):
# Your second spider definition
...
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)
(continuesonnextpage)
5.4. CommonPractices 189

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
@defer.inlineCallbacks
def crawl():
yield runner.crawl(MySpider1)
yield runner.crawl(MySpider2)
reactor.stop()
from twisted.internet import reactor
crawl()
reactor.run() # the script will block here until the last crawl call is finished
(cid:242) Note
Whenrunningmultiplespidersinthesameprocess,reactorsettingsshouldnothaveadifferentvalueperspider.
Also,pre-crawlersettingscannotbedefinedperspider.
ª Seealso
RunScrapyfromascript.
5.4.3 Distributed crawls
Scrapydoesn’tprovideanybuilt-infacilityforrunningcrawlsinadistribute(multi-server)manner. However,thereare
somewaystodistributecrawls,whichvarydependingonhowyouplantodistributethem.
Ifyouhavemanyspiders,theobviouswaytodistributetheloadistosetupmanyScrapydinstancesanddistributespider
runsamongthose.
If you instead want to run a single (big) spider through many machines, what you usually do is partition the urls to
crawlandsendthemtoeachseparatespider. Hereisaconcreteexample:
First,youpreparethelistofurlstocrawlandputthemintoseparatefiles/urls:
http://somedomain.com/urls-to-crawl/spider1/part1.list
http://somedomain.com/urls-to-crawl/spider1/part2.list
http://somedomain.com/urls-to-crawl/spider1/part3.list
Thenyoufireaspiderrunon3differentScrapydservers. Thespiderwouldreceivea(spider)argumentpartwiththe
numberofthepartitiontocrawl:
curl http://scrapy1.mycompany.com:6800/schedule.json -d project=myproject -d␣
spider=spider1 -d part=1
˓→
curl http://scrapy2.mycompany.com:6800/schedule.json -d project=myproject -d␣
spider=spider1 -d part=2
˓→
curl http://scrapy3.mycompany.com:6800/schedule.json -d project=myproject -d␣
spider=spider1 -d part=3
˓→
190 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
5.4.4 Avoiding getting banned
Somewebsitesimplementcertainmeasurestopreventbotsfromcrawlingthem,withvaryingdegreesofsophistication.
Getting around those measures can be difficult and tricky, and may sometimes require special infrastructure. Please
considercontactingcommercialsupportifindoubt.
Herearesometipstokeepinmindwhendealingwiththesekindsofsites:
• rotateyouruseragentfromapoolofwell-knownonesfrombrowsers(googlearoundtogetalistofthem)
• disablecookies(seeCOOKIES_ENABLED)assomesitesmayusecookiestospotbotbehaviour
• usedownloaddelays(2orhigher). SeeDOWNLOAD_DELAY setting.
• ifpossible,useCommonCrawltofetchpages,insteadofhittingthesitesdirectly
• useapoolofrotatingIPs. Forexample,thefreeTorprojectorpaidserviceslikeProxyMesh. Anopensource
alternativeisscrapoxy,asuperproxythatyoucanattachyourownproxiesto.
• useabanavoidanceservice,suchasZyteAPI,whichprovidesaScrapypluginandadditionalfeatures,likeAI
webscraping
Ifyouarestillunabletopreventyourbotgettingbanned,considercontactingcommercialsupport.
5.5 Broad Crawls
Scrapy defaults are optimized for crawling specific sites. These sites are often handled by a single Scrapy spider,
althoughthisisnotnecessaryorrequired(forexample,therearegenericspidersthathandleanygivensitethrownat
them).
In addition to this “focused crawl”, there is another common type of crawling which covers a large (potentially un-
limited)numberofdomains, andisonlylimitedbytimeorotherarbitraryconstraint, ratherthanstoppingwhenthe
domainwascrawledtocompletionorwhentherearenomorerequeststoperform. Thesearecalled“broadcrawls”
andisthetypicalcrawlersemployedbysearchengines.
Thesearesomecommonpropertiesoftenfoundinbroadcrawls:
• theycrawlmanydomains(often,unbounded)insteadofaspecificsetofsites
• they don’t necessarily crawl domains to completion, because it would be impractical (or impossible) to do so,
andinsteadlimitthecrawlbytimeornumberofpagescrawled
• theyaresimplerinlogic(asopposedtoverycomplexspiderswithmanyextractionrules)becausedataisoften
post-processedinaseparatestage
• theycrawlmanydomainsconcurrently, whichallowsthemtoachievefastercrawlspeedsbynotbeinglimited
byanyparticularsiteconstraint(eachsiteiscrawledslowlytorespectpoliteness,butmanysitesarecrawledin
parallel)
Assaidabove, Scrapydefaultsettingsareoptimizedforfocusedcrawls, notbroadcrawls. However, duetoitsasyn-
chronousarchitecture,Scrapyisverywellsuitedforperformingfastbroadcrawls. Thispagesummarizessomethings
youneedtokeepinmindwhenusingScrapyfordoingbroadcrawls,alongwithconcretesuggestionsofScrapysettings
totuneinordertoachieveanefficientbroadcrawl.
5.5.1 Use the right SCHEDULER_PRIORITY_QUEUE
Scrapy’s default scheduler priority queue is 'scrapy.pqueues.ScrapyPriorityQueue'. It works best during
single-domaincrawl. Itdoesnotworkwellwithcrawlingmanydifferentdomainsinparallel
Toapplytherecommendedpriorityqueueuse:
5.5. BroadCrawls 191

ScrapyDocumentation,Release2.13.3
SCHEDULER_PRIORITY_QUEUE = "scrapy.pqueues.DownloaderAwarePriorityQueue"
5.5.2 Increase concurrency
Concurrencyisthenumberofrequeststhatareprocessedinparallel. Thereisagloballimit(CONCURRENT_REQUESTS)
and an additional limit that can be set either per domain (CONCURRENT_REQUESTS_PER_DOMAIN) or per IP
(CONCURRENT_REQUESTS_PER_IP).
(cid:242) Note
TheschedulerpriorityqueuerecommendedforbroadcrawlsdoesnotsupportCONCURRENT_REQUESTS_PER_IP.
ThedefaultglobalconcurrencylimitinScrapyisnotsuitableforcrawlingmanydifferentdomainsinparallel,soyou
willwanttoincreaseit. HowmuchtoincreaseitwilldependonhowmuchCPUandmemoryyourcrawlerwillhave
available.
Agoodstartingpointis100:
CONCURRENT_REQUESTS = 100
ButthebestwaytofindoutisbydoingsometrialsandidentifyingatwhatconcurrencyyourScrapyprocessgetsCPU
bounded. Foroptimumperformance,youshouldpickaconcurrencywhereCPUusageisat80-90%.
Increasing concurrency also increases memory usage. If memory usage is a concern, you might need to lower your
globalconcurrencylimitaccordingly.
5.5.3 Increase Twisted IO thread pool maximum size
CurrentlyScrapydoesDNSresolutioninablockingwaywithusageofthreadpool. Withhigherconcurrencylevelsthe
crawlingcouldbesloworevenfailhittingDNSresolvertimeouts. Possiblesolutiontoincreasethenumberofthreads
handlingDNSqueries. TheDNSqueuewillbeprocessedfasterspeedingupestablishingofconnectionandcrawling
overall.
Toincreasemaximumthreadpoolsizeuse:
REACTOR_THREADPOOL_MAXSIZE = 20
5.5.4 Setup your own DNS
IfyouhavemultiplecrawlingprocessesandsinglecentralDNS,itcanactlikeDoSattackontheDNSserverresulting
toslowdownofentirenetworkorevenblockingyourmachines. ToavoidthissetupyourownDNSserverwithlocal
cacheandupstreamtosomelargeDNSlikeOpenDNSorVerizon.
5.5.5 Reduce log level
Whendoingbroadcrawlsyouareoftenonlyinterestedinthecrawlratesyougetandanyerrorsfound. Thesestatsare
reportedbyScrapywhenusingthe INFOloglevel. InordertosaveCPU(andlogstoragerequirements)youshould
notuseDEBUGloglevelwhenperforminglargebroadcrawlsinproduction. UsingDEBUGlevelwhendevelopingyour
(broad)crawlermaybefinethough.
Tosetthelogleveluse:
LOG_LEVEL = "INFO"
192 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
5.5.6 Disable cookies
Disablecookiesunlessyoureallyneed. Cookiesareoftennotneededwhendoingbroadcrawls(searchenginecrawlers
ignorethem),andtheyimproveperformancebysavingsomeCPUcyclesandreducingthememoryfootprintofyour
Scrapycrawler.
Todisablecookiesuse:
COOKIES_ENABLED = False
5.5.7 Disable retries
RetryingfailedHTTPrequestscanslowdownthecrawlssubstantially, speciallywhensitescausesareveryslow(or
fail)torespond,thuscausingatimeouterrorwhichgetsretriedmanytimes,unnecessarily,preventingcrawlercapacity
tobereusedforotherdomains.
Todisableretriesuse:
RETRY_ENABLED = False
5.5.8 Reduce download timeout
Unlessyouarecrawlingfromaveryslowconnection(whichshouldn’tbethecaseforbroadcrawls)reducethedownload
timeoutsothatstuckrequestsarediscardedquicklyandfreeupcapacitytoprocessthenextones.
Toreducethedownloadtimeoutuse:
DOWNLOAD_TIMEOUT = 15
5.5.9 Disable redirects
Consider disabling redirects, unless you are interested in following them. When doing broad crawls it’s common to
saveredirectsandresolvethemwhenrevisitingthesiteatalatercrawl. Thisalsohelptokeepthenumberofrequest
constantpercrawlbatch,otherwiseredirectloopsmaycausethecrawlertodedicatetoomanyresourcesonanyspecific
domain.
Todisableredirectsuse:
REDIRECT_ENABLED = False
5.5.10 Crawl in BFO order
ScrapycrawlsinDFOorderbydefault.
Inbroadcrawls,however,pagecrawlingtendstobefasterthanpageprocessing. Asaresult,unprocessedearlyrequests
stayinmemoryuntilthefinaldepthisreached,whichcansignificantlyincreasememoryusage.
CrawlinBFOorderinsteadtosavememory.
5.5.11 Be mindful of memory leaks
Ifyourbroadcrawlshowsahighmemoryusage,inadditiontocrawlinginBFOorder andloweringconcurrencyyou
shoulddebugyourmemoryleaks.
5.5. BroadCrawls 193

ScrapyDocumentation,Release2.13.3
5.5.12 Install a specific Twisted reactor
Ifthecrawlisexceedingthesystem’scapabilities,youmightwanttotryinstallingaspecificTwistedreactor,viathe
TWISTED_REACTOR setting.
5.6 Using your browser’s Developer Tools for scraping
Hereisageneralguideonhowtouseyourbrowser’sDeveloperToolstoeasethescrapingprocess. Todayalmostall
browserscomewithbuiltinDeveloperToolsandalthoughwewilluseFirefoxinthisguide,theconceptsareapplicable
toanyotherbrowser.
Inthisguidewe’llintroducethebasictoolstousefromabrowser’sDeveloperToolsbyscrapingquotes.toscrape.com.
5.6.1 Caveats with inspecting the live browser DOM
SinceDeveloperToolsoperateonalivebrowserDOM,whatyou’llactuallyseewheninspectingthepagesourceisnot
theoriginalHTML,butamodifiedoneafterapplyingsomebrowsercleanupandexecutingJavaScriptcode. Firefox,
inparticular,isknownforadding<tbody>elementstotables. Scrapy,ontheotherhand,doesnotmodifytheoriginal
pageHTML,soyouwon’tbeabletoextractanydataifyouuse<tbody>inyourXPathexpressions.
Therefore,youshouldkeepinmindthefollowingthings:
• DisableJavaScriptwhileinspectingtheDOMlookingforXPathstobeusedinScrapy(intheDeveloperTools
settingsclickDisableJavaScript)
• NeverusefullXPathpaths,userelativeandcleveronesbasedonattributes(suchasid,class,width,etc)or
anyidentifyingfeatureslikecontains(@href, 'image').
• Neverinclude<tbody>elementsinyourXPathexpressionsunlessyoureallyknowwhatyou’redoing
5.6.2 Inspecting a website
ByfarthemosthandyfeatureoftheDeveloperToolsistheInspectorfeature,whichallowsyoutoinspecttheunderlying
HTMLcodeofanywebpage. TodemonstratetheInspector,let’slookatthequotes.toscrape.com-site.
Onthesitewehaveatotaloftenquotesfromvariousauthorswithspecifictags,aswellastheTopTenTags. Let’ssay
wewanttoextractallthequotesonthispage,withoutanymeta-informationaboutauthors,tags,etc.
Instead of viewing the whole source code for the page, we can simply right click on a quote and select Inspect
Element (Q),whichopensuptheInspector. Inityoushouldseesomethinglikethis:
194 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
Theinterestingpartforusisthis:
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">(...)</span>
<span>(...)</span>
<div class="tags">(...)</div>
</div>
Ifyouhoveroverthefirstdivdirectlyabovethespantaghighlightedinthescreenshot,you’llseethatthecorresponding
sectionofthewebpagegetshighlightedaswell. Sonowwehaveasection,butwecan’tfindourquotetextanywhere.
TheadvantageoftheInspector isthatitautomaticallyexpandsandcollapsessectionsandtagsofawebpage, which
greatlyimproves readability. You canexpandand collapseatagby clickingonthe arrowinfrontof itorby double
clickingdirectlyonthetag. Ifweexpandthespantagwiththeclass= "text"wewillseethequote-textweclicked
on. TheInspectorletsyoucopyXPathstoselectedelements. Let’stryitout.
FirstopentheScrapyshellathttps://quotes.toscrape.com/inaterminal:
$ scrapy shell "https://quotes.toscrape.com/"
Then,backtoyourwebbrowser,right-clickonthespantag,selectCopy > XPathandpasteitintheScrapyshelllike
so:
>>> response.xpath("/html/body/div/div[2]/div[1]/div[1]/span[1]/text()").getall()
['“The world as we have created it is a process of our thinking. It cannot be changed␣
without changing our thinking.”']
˓→
Addingtext()attheendweareabletoextractthefirstquotewiththisbasicselector. ButthisXPathisnotreallythat
clever. Allitdoesisgodownadesiredpathinthesourcecodestartingfrom html. Solet’sseeifwecanrefineour
XPathabit:
IfwechecktheInspector againwe’llseethatdirectlybeneathourexpandeddivtagwehavenineidenticaldivtags,
5.6. Usingyourbrowser’sDeveloperToolsforscraping 195

ScrapyDocumentation,Release2.13.3
eachwiththesameattributesasourfirst. Ifweexpandanyofthem,we’llseethesamestructureaswithourfirstquote:
Twospantagsandonedivtag. Wecanexpandeachspantagwiththeclass="text"insideour divtagsandsee
eachquote:
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
<span class="text" itemprop="text">
“The world as we have created it is a process of our thinking. It cannot be changed␣
without changing our thinking.”
˓→
</span>
<span>(...)</span>
<div class="tags">(...)</div>
</div>
WiththisknowledgewecanrefineourXPath: Insteadofapathtofollow, we’llsimplyselectallspantagswiththe
class="text"byusingthehas-class-extension:
>>> response.xpath('//span[has-class("text")]/text()').getall()
['“The world as we have created it is a process of our thinking. It cannot be changed␣
without changing our thinking.”',
˓→
'“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
'“There are only two ways to live your life. One is as though nothing is a miracle. The␣
other is as though everything is a miracle.”',
˓→
...]
Andwithonesimple,clevererXPathweareabletoextractallquotesfromthepage. Wecouldhaveconstructedaloop
over our first XPath to increase the number of the last div, but this would have been unnecessarily complex and by
simplyconstructinganXPathwithhas-class("text")wewereabletoextractallquotesinoneline.
TheInspectorhasalotofotherhelpfulfeatures,suchassearchinginthesourcecodeordirectlyscrollingtoanelement
youselected. Let’sdemonstrateausecase:
SayyouwanttofindtheNextbuttononthepage. TypeNextintothesearchbaronthetoprightoftheInspector. You
shouldgettworesults. Thefirstisalitagwiththeclass="next",thesecondthetextofanatag. Rightclickonthe
atagandselectScroll into View. Ifyouhoveroverthetag,you’llseethebuttonhighlighted. Fromherewecould
easilycreateaLinkExtractortofollowthepagination. Onasimplesitesuchasthis,theremaynotbetheneedtofind
anelementvisuallybuttheScroll into Viewfunctioncanbequiteusefuloncomplexsites.
NotethatthesearchbarcanalsobeusedtosearchforandtestCSSselectors. Forexample,youcouldsearchforspan.
texttofindallquotetexts. Insteadofafulltextsearch,thissearchesforexactlythespantagwiththeclass="text"
inthepage.
5.6.3 The Network-tool
Whilescrapingyoumaycomeacrossdynamicwebpageswheresomepartsofthepageareloadeddynamicallythrough
multiplerequests. Whilethiscanbequitetricky,theNetwork-toolintheDeveloperToolsgreatlyfacilitatesthistask.
TodemonstratetheNetwork-tool,let’stakealookatthepagequotes.toscrape.com/scroll.
Thepageisquitesimilartothebasicquotes.toscrape.com-page,butinsteadoftheabove-mentionedNextbutton,the
pageautomaticallyloadsnewquoteswhenyouscrolltothebottom. WecouldgoaheadandtryoutdifferentXPaths
directly,butinsteadwe’llcheckanotherquiteusefulcommandfromtheScrapyshell:
$ scrapy shell "quotes.toscrape.com/scroll"
(...)
>>> view(response)
Abrowserwindowshouldopenwiththewebpagebutwithonecrucialdifference: Insteadofthequoteswejustseea
greenishbarwiththewordLoading....
196 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
Theview(response)commandlet’susviewtheresponseourshellorlaterourspiderreceivesfromtheserver. Here
weseethatsomebasictemplateisloadedwhichincludesthetitle,thelogin-buttonandthefooter,butthequotesare
missing. Thistellsusthatthequotesarebeingloadedfromadifferentrequestthanquotes.toscrape/scroll.
IfyouclickontheNetworktab,youwillprobablyonlyseetwoentries. Thefirstthingwedoisenablepersistentlogs
byclickingonPersist Logs. Ifthisoptionisdisabled,thelogisautomaticallyclearedeachtimeyounavigatetoa
differentpage. Enablingthisoptionisagooddefault,sinceitgivesuscontrolonwhentoclearthelogs.
Ifwereloadthepagenow,you’llseetheloggetpopulatedwithsixnewrequests.
Hereweseeeveryrequestthathasbeenmadewhenreloadingthepageandcaninspecteachrequestanditsresponse.
Solet’sfindoutwhereourquotesarecomingfrom:
Firstclickontherequestwiththenamescroll. Ontherightyoucannowinspecttherequest. InHeadersyou’llfind
detailsabouttherequestheaders,suchastheURL,themethod,theIP-address,andsoon. We’llignoretheothertabs
andclickdirectlyonResponse.
WhatyoushouldseeinthePreviewpaneistherenderedHTML-code,thatisexactlywhatwesawwhenwecalled
view(response)intheshell. Accordinglythetypeoftherequestinthelogishtml. Theotherrequestshavetypes
likecssorjs,butwhatinterestsusistheonerequestcalledquotes?page=1withthetypejson.
Ifweclickonthisrequest,weseethattherequestURLishttps://quotes.toscrape.com/api/quotes?page=1
andtheresponseisaJSON-objectthatcontainsourquotes. Wecanalsoright-clickontherequestandopenOpen in
new tabtogetabetteroverview.
5.6. Usingyourbrowser’sDeveloperToolsforscraping 197

ScrapyDocumentation,Release2.13.3
WiththisresponsewecannoweasilyparsetheJSON-objectandalsorequesteachpagetogeteveryquoteonthesite:
import scrapy
import json
class QuoteSpider(scrapy.Spider):
name = "quote"
allowed_domains = ["quotes.toscrape.com"]
page = 1
start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]
def parse(self, response):
data = json.loads(response.text)
for quote in data["quotes"]:
yield {"quote": quote["text"]}
if data["has_next"]:
self.page += 1
url = f"https://quotes.toscrape.com/api/quotes?page={self.page}"
yield scrapy.Request(url=url, callback=self.parse)
Thisspiderstartsatthefirstpageofthequotes-API.Witheachresponse,weparsetheresponse.textandassignitto
data. ThisletsusoperateontheJSON-objectlikeonaPythondictionary. Weiteratethroughthequotesandprintout
thequote["text"]. Ifthehandyhas_nextelementistrue(tryloadingquotes.toscrape.com/api/quotes?page=10
inyourbrowserorapage-numbergreaterthan10),weincrementthepageattributeandyieldanewrequest,inserting
theincrementedpage-numberintooururl.
Inmorecomplexwebsites,itcouldbedifficulttoeasilyreproducetherequests,aswecouldneedtoaddheadersor
cookies to make it work. In those cases you can export the requests in cURL format, by right-clicking on each of
theminthenetworktoolandusingthefrom_curl()methodtogenerateanequivalentrequest:
from scrapy import Request
request = Request.from_curl(
"curl 'https://quotes.toscrape.com/api/quotes?page=1' -H 'User-Agent: Mozil"
(continuesonnextpage)
198 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
"la/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0' -H 'Acce"
"pt: */*' -H 'Accept-Language: ca,en-US;q=0.7,en;q=0.3' --compressed -H 'X"
"-Requested-With: XMLHttpRequest' -H 'Proxy-Authorization: Basic QFRLLTAzM"
"zEwZTAxLTk5MWUtNDFiNC1iZWRmLTJjNGI4M2ZiNDBmNDpAVEstMDMzMTBlMDEtOTkxZS00MW"
"I0LWJlZGYtMmM0YjgzZmI0MGY0' -H 'Connection: keep-alive' -H 'Referer: http"
"://quotes.toscrape.com/scroll' -H 'Cache-Control: max-age=0'"
)
Alternatively, if you want to know the arguments needed to recreate that request you can use the
curl_to_request_kwargs()functiontogetadictionarywiththeequivalentarguments:
scrapy.utils.curl.curl_to_request_kwargs(curl_command: str,ignore_unknown_options: bool=True)→
dict[str,Any]
ConvertacURLcommandsyntaxtoRequestkwargs.
Parameters
• curl_command(str)–stringcontainingthecurlcommand
• ignore_unknown_options(bool)–Iftrue,onlyawarningisemittedwhencURLop-
tionsareunknown. Otherwiseraisesanerror. (default: True)
Returns
dictionaryofRequestkwargs
NotethattotranslateacURLcommandintoaScrapyrequest,youmayusecurl2scrapy.
Asyoucansee,withafewinspectionsintheNetwork-toolwewereabletoeasilyreplicatethedynamicrequestsofthe
scrollingfunctionalityofthepage. Crawlingdynamicpagescanbequitedauntingandpagescanbeverycomplex,but
it(mostly)boilsdowntoidentifyingthecorrectrequestandreplicatingitinyourspider.
5.7 Selecting dynamically-loaded content
Somewebpagesshowthedesireddatawhenyouloadtheminawebbrowser. However,whenyoudownloadthemusing
Scrapy,youcannotreachthedesireddatausingselectors.
Whenthishappens,therecommendedapproachistofindthedatasourceandextractthedatafromit.
Ifyoufailtodothat,andyoucannonethelessaccessthedesireddatathroughtheDOM fromyourwebbrowser,see
Usingaheadlessbrowser.
5.7.1 Finding the data source
Toextractthedesireddata,youmustfirstfinditssourcelocation.
Ifthedataisinanon-text-basedformat,suchasanimageoraPDFdocument,usethenetworktoolofyourwebbrowser
tofindthecorrespondingrequest,andreproduceit.
Ifyourwebbrowserletsyouselectthedesireddataastext,thedatamaybedefinedinembeddedJavaScriptcode,or
loadedfromanexternalresourceinatext-basedformat.
Inthatcase,youcanuseatoollikewgreptofindtheURLofthatresource.
IfthedataturnsouttocomefromtheoriginalURLitself,youmustinspectthesourcecodeofthewebpagetodetermine
wherethedataislocated.
IfthedatacomesfromadifferentURL,youwillneedtoreproducethecorrespondingrequest.
5.7. Selectingdynamically-loadedcontent 199

ScrapyDocumentation,Release2.13.3
5.7.2 Inspecting the source code of a webpage
Sometimesyouneedtoinspectthesourcecodeofawebpage(nottheDOM)todeterminewheresomedesireddatais
located.
UseScrapy’sfetch commandtodownloadthewebpagecontentsasseenbyScrapy:
scrapy fetch --nolog https://example.com > response.html
IfthedesireddataisinembeddedJavaScriptcodewithina<script/>element,seeParsingJavaScriptcode.
Ifyoucannotfindthedesireddata,firstmakesureit’snotjustScrapy: downloadthewebpagewithanHTTPclientlike
curlorwgetandseeiftheinformationcanbefoundintheresponsetheyget.
Iftheygetaresponsewiththedesireddata,modifyyourScrapyRequesttomatchthatoftheotherHTTPclient. For
example,tryusingthesameuser-agentstring(USER_AGENT)orthesameheaders.
Iftheyalsogetaresponsewithoutthedesireddata,you’llneedtotakestepstomakeyourrequestmoresimilartothat
ofthewebbrowser. SeeReproducingrequests.
5.7.3 Reproducing requests
Sometimesweneedtoreproducearequestthewayourwebbrowserperformsit.
Use the network tool of your web browser to see how your web browser performs the desired request, and try to
reproducethatrequestwithScrapy.
ItmightbeenoughtoyieldaRequestwiththesameHTTPmethodandURL.However,youmayalsoneedtoreproduce
thebody,headersandformparameters(seeFormRequest)ofthatrequest.
As all major browsers allow to export the requests in curl format, Scrapy incorporates the method from_curl() to
generateanequivalentRequest fromacURLcommand. Togetmoreinformationvisitrequestfromcurl insidethe
networktoolsection.
Onceyougettheexpectedresponse,youcanextractthedesireddatafromit.
YoucanreproduceanyrequestwithScrapy. However, sometimesreproducingallnecessaryrequestsmaynotseem
efficientindevelopertime. Ifthatisyourcase,andcrawlingspeedisnotamajorconcernforyou,youcanalternatively
considerusingaheadlessbrowser.
Ifyougettheexpectedresponsesometimes,butnotalways,theissueisprobablynotyourrequest,butthetargetserver.
Thetargetservermightbebuggy,overloaded,orbanningsomeofyourrequests.
NotethattotranslateacURLcommandintoaScrapyrequest,youmayusecurl2scrapy.
5.7.4 Handling different response formats
Onceyouhavearesponsewiththedesireddata,howyouextractthedesireddatafromitdependsonthetypeofresponse:
• IftheresponseisHTML,XMLorJSON,useselectorsasusual.
• IftheresponseisJSON,useresponse.json()toloadthedesireddata:
data = response.json()
IfthedesireddataisinsideHTMLorXMLcodeembeddedwithinJSONdata,youcanloadthatHTMLorXML
codeintoaSelectorandthenuseitasusual:
selector = Selector(data["html"])
• If the response is JavaScript, or HTML with a <script/> element containing the desired data, see Parsing
JavaScriptcode.
200 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
• IftheresponseisCSS,usearegularexpressiontoextractthedesireddatafromresponse.text.
• If the response is an image or another format based on images (e.g. PDF), read the response as bytes from
response.body anduseanOCRsolutiontoextractthedesireddataastext.
Forexample,youcanusepytesseract. ToreadatablefromaPDF,tabula-pymaybeabetterchoice.
• IftheresponseisSVG,orHTMLwithembeddedSVGcontainingthedesireddata,youmaybeabletoextract
thedesireddatausingselectors,sinceSVGisbasedonXML.
Otherwise,youmightneedtoconverttheSVGcodeintoarasterimage,andhandlethatrasterimage.
5.7.5 Parsing JavaScript code
IfthedesireddataishardcodedinJavaScript,youfirstneedtogettheJavaScriptcode:
• IftheJavaScriptcodeisinaJavaScriptfile,simplyreadresponse.text.
• IftheJavaScriptcodeiswithina<script/>elementofanHTMLpage,useselectorstoextractthetextwithin
that<script/>element.
OnceyouhaveastringwiththeJavaScriptcode,youcanextractthedesireddatafromit:
• YoumightbeabletousearegularexpressiontoextractthedesireddatainJSONformat, whichyoucanthen
parsewithjson.loads().
For example, if the JavaScript code contains a separate line like var data = {"field": "value"}; you
canextractthatdataasfollows:
>>> pattern = r"\bvar\s+data\s*=\s*(\{.*?\})\s*;\s*\n"
>>> json_data = response.css("script::text").re_first(pattern)
>>> json.loads(json_data)
{'field': 'value'}
• chompjsprovidesanAPItoparseJavaScriptobjectsintoadict.
Forexample, iftheJavaScriptcodecontainsvar data = {field: "value", secondField: "second
value"};youcanextractthatdataasfollows:
>>> import chompjs
>>> javascript = response.css("script::text").get()
>>> data = chompjs.parse_js_object(javascript)
>>> data
{'field': 'value', 'secondField': 'second value'}
• Otherwise,usejs2xmltoconverttheJavaScriptcodeintoanXMLdocumentthatyoucanparseusingselectors.
Forexample,iftheJavaScriptcodecontainsvar data = {field: "value"};youcanextractthatdataas
follows:
>>> import js2xml
>>> import lxml.etree
>>> from parsel import Selector
>>> javascript = response.css("script::text").get()
>>> xml = lxml.etree.tostring(js2xml.parse(javascript), encoding="unicode")
>>> selector = Selector(text=xml)
>>> selector.css('var[name="data"]').get()
'<var name="data"><object><property name="field"><string>value</string></property></
object></var>'
˓→
5.7. Selectingdynamically-loadedcontent 201

ScrapyDocumentation,Release2.13.3
5.7.6 Using a headless browser
Onwebpagesthatfetchdatafromadditionalrequests, reproducingthoserequeststhatcontainthedesireddataisthe
preferred approach. The effort is often worth the result: structured, complete data with minimum parsing time and
networktransfer.
However,sometimesitcanbereallyhardtoreproducecertainrequests. Oryoumayneedsomethingthatnorequest
cangiveyou,suchasascreenshotofawebpageasseeninawebbrowser. Inthiscaseusingaheadlessbrowserwill
help.
AheadlessbrowserisaspecialwebbrowserthatprovidesanAPIforautomation. Byinstallingtheasyncioreactor,it
ispossibletointegrateasyncio-basedlibrarieswhichhandleheadlessbrowsers.
One such library is playwright-python (an official Python port of playwright). The following is a simple snippet to
illustrateitsusagewithinaScrapyspider:
import scrapy
from playwright.async_api import async_playwright
class PlaywrightSpider(scrapy.Spider):
name = "playwright"
start_urls = ["data:,"] # avoid using the default Scrapy downloader
async def parse(self, response):
async with async_playwright() as pw:
browser = await pw.chromium.launch()
page = await browser.new_page()
await page.goto("https://example.org")
title = await page.title()
return {"title": title}
However,usingplaywright-pythondirectlyasintheaboveexamplecircumventsmostoftheScrapycomponents(mid-
dlewares,dupefilter,etc). Werecommendusingscrapy-playwrightforabetterintegration.
5.8 Debugging memory leaks
InScrapy,objectssuchasrequests,responsesanditemshaveafinitelifetime: theyarecreated,usedforawhile,and
finallydestroyed.
Fromallthoseobjects, theRequestisprobablytheonewiththelongestlifetime, asitstayswaitingintheScheduler
queueuntilit’stimetoprocessit. FormoreinfoseeArchitectureoverview.
AstheseScrapyobjectshavea(ratherlong)lifetime,thereisalwaystheriskofaccumulatingtheminmemorywithout
releasingthemproperlyandthuscausingwhatisknownasa“memoryleak”.
Tohelpdebuggingmemoryleaks,Scrapyprovidesabuilt-inmechanismfortrackingobjectsreferencescalledtrackref,
and you can also use a third-party library called muppy for more advanced memory debugging (see below for more
info). BothmechanismsmustbeusedfromtheTelnetConsole.
5.8.1 Common causes of memory leaks
It happens quite often (sometimes by accident, sometimes on purpose) that the Scrapy developer passes objects ref-
erencedinRequests(forexample,usingthecb_kwargs ormeta attributesortherequestcallbackfunction)andthat
effectively bounds the lifetime of those referenced objects to the lifetime of the Request. This is, by far, the most
commoncauseofmemoryleaksinScrapyprojects,andaquitedifficultonetodebugfornewcomers.
202 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
Inbigprojects,thespidersaretypicallywrittenbydifferentpeopleandsomeofthosespiderscouldbe“leaking”and
thusaffectingtherestoftheother(well-written)spiderswhentheygettorunconcurrently,which,inturn,affectsthe
wholecrawlingprocess.
Theleakcouldalsocomefromacustommiddleware,pipelineorextensionthatyouhavewritten,ifyouarenotreleasing
the(previouslyallocated)resourcesproperly. Forexample,allocatingresourcesonspider_opened butnotreleasing
themonspider_closed maycauseproblemsifyou’rerunningmultiplespidersperprocess.
TooManyRequests?
BydefaultScrapykeepstherequestqueueinmemory;itincludesRequestobjectsandallobjectsreferencedinRequest
attributes (e.g. in cb_kwargs and meta). While not necessarily a leak, this can take a lot of memory. Enabling
persistentjobqueuecouldhelpkeepingmemoryusageincontrol.
5.8.2 Debugging memory leaks with trackref
trackrefisamoduleprovidedbyScrapytodebugthemostcommoncasesofmemoryleaks. Itbasicallytracksthe
referencestoallliveRequest,Response,Item,SpiderandSelectorobjects.
You can enter the telnet console and inspect how many objects (of the classes mentioned above) are currently alive
usingtheprefs()functionwhichisanaliastotheprint_live_refs()function:
telnet localhost 6023
.. code-block:: pycon
>>> prefs()
Live References
ExampleSpider 1 oldest: 15s ago
HtmlResponse 10 oldest: 1s ago
Selector 2 oldest: 0s ago
FormRequest 878 oldest: 7s ago
Asyoucansee,thatreportalsoshowsthe“age”oftheoldestobjectineachclass. Ifyou’rerunningmultiplespiders
perprocesschancesareyoucanfigureoutwhichspiderisleakingbylookingattheoldestrequestorresponse. You
cangettheoldestobjectofeachclassusingtheget_oldest()function(fromthetelnetconsole).
Whichobjectsaretracked?
Theobjectstrackedbytrackrefsareallfromtheseclasses(andallitssubclasses):
• scrapy.Request
• scrapy.http.Response
• scrapy.Item
• scrapy.Selector
• scrapy.Spider
Arealexample
Let’sseeaconcreteexampleofahypotheticalcaseofmemoryleaks. Supposewehavesomespiderwithalinesimilar
tothisone:
return Request(f"http://www.somenastyspider.com/product.php?pid={product_id}",
callback=self.parse, cb_kwargs={'referer': response})
5.8. Debuggingmemoryleaks 203

ScrapyDocumentation,Release2.13.3
Thatlineispassingaresponsereferenceinsidearequestwhicheffectivelytiestheresponselifetimetotherequests’
one,andthatwoulddefinitelycausememoryleaks.
Let’sseehowwecandiscoverthecause(withoutknowingitapriori,ofcourse)byusingthetrackreftool.
Afterthecrawlerisrunningforafewminutesandwenoticeitsmemoryusagehasgrownalot,wecanenteritstelnet
consoleandcheckthelivereferences:
>>> prefs()
Live References
SomenastySpider 1 oldest: 15s ago
HtmlResponse 3890 oldest: 265s ago
Selector 2 oldest: 0s ago
Request 3878 oldest: 250s ago
Thefactthattherearesomanyliveresponses(andthatthey’resoold)isdefinitelysuspicious,asresponsesshouldhave
arelativelyshortlifetimecomparedtoRequests. Thenumberofresponsesissimilartothenumberofrequests,soit
looksliketheyaretiedinasomeway. Wecannowgoandcheckthecodeofthespidertodiscoverthenastylinethat
isgeneratingtheleaks(passingresponsereferencesinsiderequests).
Sometimesextrainformationaboutliveobjectscanbehelpful. Let’schecktheoldestresponse:
>>> from scrapy.utils.trackref import get_oldest
>>> r = get_oldest("HtmlResponse")
>>> r.url
'http://www.somenastyspider.com/product.php?pid=123'
Ifyouwanttoiterateoverallobjects,insteadofgettingtheoldestone,youcanusethescrapy.utils.trackref.
iter_all()function:
>>> from scrapy.utils.trackref import iter_all
>>> [r.url for r in iter_all("HtmlResponse")]
['http://www.somenastyspider.com/product.php?pid=123',
'http://www.somenastyspider.com/product.php?pid=584',
...]
Toomanyspiders?
If your project has too many spiders executed in parallel, the output of prefs() can be difficult to read. For this
reason,thatfunctionhasaignoreargumentwhichcanbeusedtoignoreaparticularclass(andallitssubclasses). For
example,thiswon’tshowanylivereferencestospiders:
>>> from scrapy.spiders import Spider
>>> prefs(ignore=Spider)
scrapy.utils.trackrefmodule
Herearethefunctionsavailableinthetrackref module.
class scrapy.utils.trackref.object_ref
Inheritfromthisclassifyouwanttotrackliveinstanceswiththetrackrefmodule.
scrapy.utils.trackref.print_live_refs(class_name,ignore=NoneType)
Printareportoflivereferences,groupedbyclassname.
204 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
Parameters
ignore(type or tuple)–ifgiven,allobjectsfromthespecifiedclass(ortupleofclasses)
willbeignored.
scrapy.utils.trackref.get_oldest(class_name)
Returntheoldestobjectalivewiththegivenclassname,or Noneifnoneisfound. Useprint_live_refs()
firsttogetalistofalltrackedliveobjectsperclassname.
scrapy.utils.trackref.iter_all(class_name)
Return an iterator over all objects alive with the given class name, or None if none is found. Use
print_live_refs()firsttogetalistofalltrackedliveobjectsperclassname.
5.8.3 Debugging memory leaks with muppy
trackrefprovidesaveryconvenientmechanismfortrackingdownmemoryleaks,butitonlykeepstrackoftheobjects
thataremorelikelytocausememoryleaks. However,thereareothercaseswherethememoryleakscouldcomefrom
other(moreorlessobscure)objects. Ifthisisyourcase,andyoucan’tfindyourleaksusingtrackref,youstillhave
anotherresource: themuppylibrary.
YoucanusemuppyfromPympler.
Ifyouusepip,youcaninstallmuppywiththefollowingcommand:
pip install Pympler
Here’sanexampletoviewallPythonobjectsavailableintheheapusingmuppy:
>>> from pympler import muppy
>>> all_objects = muppy.get_objects()
>>> len(all_objects)
28667
>>> from pympler import summary
>>> suml = summary.summarize(all_objects)
>>> summary.print_(suml)
types | # objects | total size
==================================== | =========== | ============
<class 'str | 9822 | 1.10 MB
<class 'dict | 1658 | 856.62 KB
<class 'type | 436 | 443.60 KB
<class 'code | 2974 | 419.56 KB
<class '_io.BufferedWriter | 2 | 256.34 KB
<class 'set | 420 | 159.88 KB
<class '_io.BufferedReader | 1 | 128.17 KB
<class 'wrapper_descriptor | 1130 | 88.28 KB
<class 'tuple | 1304 | 86.57 KB
<class 'weakref | 1013 | 79.14 KB
<class 'builtin_function_or_method | 958 | 67.36 KB
<class 'method_descriptor | 865 | 60.82 KB
<class 'abc.ABCMeta | 62 | 59.96 KB
<class 'list | 446 | 58.52 KB
<class 'int | 1425 | 43.20 KB
Formoreinfoaboutmuppy,refertothemuppydocumentation.
5.8. Debuggingmemoryleaks 205

ScrapyDocumentation,Release2.13.3
5.8.4 Leaks without leaks
Sometimes, you may notice that the memory usage of your Scrapy process will only increase, but never decrease.
Unfortunately,thiscouldhappeneventhoughneitherScrapynoryourprojectareleakingmemory. Thisisduetoa(not
sowell)knownproblemofPython,whichmaynotreturnreleasedmemorytotheoperatingsysteminsomecases. For
moreinformationonthisissuesee:
• PythonMemoryManagement
• PythonMemoryManagementPart2
• PythonMemoryManagementPart3
TheimprovementsproposedbyEvanJones,whicharedetailedinthispaper,gotmergedinPython2.5,butthisonly
reducestheproblem,itdoesn’tfixitcompletely. Toquotethepaper:
Unfortunately,thispatchcanonlyfreeanarenaiftherearenomoreobjectsallocatedinitanymore. This
means that fragmentation is a large issue. An application could have many megabytes of free memory,
scatteredthroughoutallthearenas,butitwillbeunabletofreeanyofit. Thisisaproblemexperienced
byallmemoryallocators. Theonlywaytosolveitistomovetoacompactinggarbagecollector,whichis
abletomoveobjectsinmemory. ThiswouldrequiresignificantchangestothePythoninterpreter.
Tokeepmemoryconsumptionreasonableyoucansplitthejobintoseveralsmallerjobsorenablepersistentjobqueue
andstop/startspiderfromtimetotime.
5.9 Downloading and processing files and images
Scrapy provides reusable item pipelines for downloading files attached to a particular item (for example, when you
scrape products and also want to download their images locally). These pipelines share a bit of functionality and
structure(werefertothemasmediapipelines),buttypicallyyou’lleitherusetheFilesPipelineortheImagesPipeline.
Bothpipelinesimplementthesefeatures:
• Avoidre-downloadingmediathatwasdownloadedrecently
• Specifyingwheretostorethemedia(filesystemdirectory,FTPserver,AmazonS3bucket,GoogleCloudStorage
bucket)
TheImagesPipelinehasafewextrafunctionsforprocessingimages:
• Convertalldownloadedimagestoacommonformat(JPG)andmode(RGB)
• Thumbnailgeneration
• Checkimageswidth/heighttomakesuretheymeetaminimumconstraint
ThepipelinesalsokeepaninternalqueueofthosemediaURLswhicharecurrentlybeingscheduledfordownload,and
connectthoseresponsesthatarrivecontainingthesamemediatothatqueue. Thisavoidsdownloadingthesamemedia
morethanoncewhenit’ssharedbyseveralitems.
5.9.1 Using the Files Pipeline
Thetypicalworkflow,whenusingtheFilesPipelinegoeslikethis:
1. InaSpider,youscrapeanitemandputtheURLsofthedesiredintoafile_urlsfield.
2. Theitemisreturnedfromthespiderandgoestotheitempipeline.
3. WhentheitemreachestheFilesPipeline,theURLsinthefile_urlsfieldarescheduledfordownloadusing
the standard Scrapy scheduler and downloader (which means the scheduler and downloader middlewares are
reused),butwithahigherpriority,processingthembeforeotherpagesarescraped. Theitemremains“locked”
atthatparticularpipelinestageuntilthefileshavefinishdownloading(orfailforsomereason).
206 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
4. Whenthefilesaredownloaded,anotherfield(files)willbepopulatedwiththeresults. Thisfieldwillcontain
alistofdictswithinformationaboutthedownloadedfiles,suchasthedownloadedpath,theoriginalscrapedurl
(takenfromthefile_urlsfield),thefilechecksumandthefilestatus. Thefilesinthelistofthefilesfieldwill
retainthesameorderoftheoriginalfile_urlsfield. Ifsomefilefaileddownloading,anerrorwillbelogged
andthefilewon’tbepresentinthefilesfield.
5.9.2 Using the Images Pipeline
UsingtheImagesPipelineisalotlikeusingtheFilesPipeline,exceptthedefaultfieldnamesusedaredifferent:
youuseimage_urlsfortheimageURLsofanitemanditwillpopulateanimagesfieldfortheinformationaboutthe
downloadedimages.
TheadvantageofusingtheImagesPipelineforimagefilesisthatyoucanconfiguresomeextrafunctionslikegen-
eratingthumbnailsandfilteringtheimagesbasedontheirsize.
TheImagesPipelinerequiresPillow8.0.0orgreater. ItisusedforthumbnailingandnormalizingimagestoJPEG/RGB
format.
5.9.3 Enabling your Media Pipeline
ToenableyourmediapipelineyoumustfirstaddittoyourprojectITEM_PIPELINES setting.
ForImagesPipeline,use:
ITEM_PIPELINES = {"scrapy.pipelines.images.ImagesPipeline": 1}
ForFilesPipeline,use:
ITEM_PIPELINES = {"scrapy.pipelines.files.FilesPipeline": 1}
(cid:242) Note
YoucanalsouseboththeFilesandImagesPipelineatthesametime.
Then,configurethetargetstoragesettingtoavalidvaluethatwillbeusedforstoringthedownloadedimages. Otherwise
thepipelinewillremaindisabled,evenifyouincludeitintheITEM_PIPELINES setting.
FortheFilesPipeline,settheFILES_STORE setting:
FILES_STORE = "/path/to/valid/dir"
FortheImagesPipeline,settheIMAGES_STORE setting:
IMAGES_STORE = "/path/to/valid/dir"
5.9.4 File Naming
DefaultFileNaming
Bydefault,filesarestoredusinganSHA-1hashoftheirURLsforthefilenames.
Forexample,thefollowingimageURL:
http://www.example.com/image.jpg
WhoseSHA-1 hashis:
5.9. Downloadingandprocessingfilesandimages 207

ScrapyDocumentation,Release2.13.3
3afec3b4765f8f0a07b78f98c07b83f013567a0a
Willbedownloadedandstoredusingyourchosenstoragemethod andthefollowingfilename:
3afec3b4765f8f0a07b78f98c07b83f013567a0a.jpg
CustomFileNaming
Youmaywishtouseadifferentcalculatedfilenameforsavedfiles. Forexample,classifyinganimagebyincluding
metainthefilename.
Customizefilenamesbyoverridingthefile_pathmethodofyourmediapipeline.
Forexample,animagepipelinewithimageURL:
http://www.example.com/product/images/large/front/0000000004166
Canbeprocessedintoafilenamewithacondensedhashandtheperspectivefront:
00b08510e4_front.jpg
Byoverridingfile_pathlikethis:
import hashlib
def file_path(self, request, response=None, info=None, *, item=None):
image_url_hash = hashlib.shake_256(request.url.encode()).hexdigest(5)
image_perspective = request.url.split("/")[-2]
image_filename = f"{image_url_hash}_{image_perspective}.jpg"
return image_filename
. Warning
If your custom file name scheme relies on meta data that can vary between scrapes it may lead to unexpected
re-downloadingofexistingmediausingnewfilenames.
For example, if your custom file name scheme uses a product title and the site changes an item’s product title
betweenscrapes,Scrapywillre-downloadthesamemediausingupdatedfilenames.
Formoreinformationaboutthefile_pathmethod,seeExtendingtheMediaPipelines.
5.9.5 Supported Storage
Filesystemstorage
Filesystemstoragewillsavefilestothefollowingpath:
<IMAGES_STORE>/full/<FILE_NAME>
Where:
• <IMAGES_STORE>isthedirectorydefinedinIMAGES_STORE settingfortheImagesPipeline.
208 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
• fullisasub-directorytoseparatefullimagesfromthumbnails(ifused). FormoreinfoseeThumbnailgeneration
forimages.
• <FILE_NAME>isthefilenameassignedtothefile. FormoreinfoseeFileNaming.
FTPserverstorage
Addedinversion2.0.
FILES_STOREandIMAGES_STOREcanpointtoanFTPserver. Scrapywillautomaticallyuploadthefilestotheserver.
FILES_STORE andIMAGES_STORE shouldbewritteninoneofthefollowingforms:
ftp://username:password@address:port/path
ftp://address:port/path
If usernameandpasswordarenotprovided,theyaretakenfromtheFTP_USER andFTP_PASSWORD settingsrespec-
tively.
FTPsupportstwodifferentconnectionmodes: activeorpassive. Scrapyusesthepassiveconnectionmodebydefault.
Tousetheactiveconnectionmodeinstead,settheFEED_STORAGE_FTP_ACTIVE settingtoTrue.
AmazonS3storage
Ifbotocore>=1.4.87isinstalled,FILES_STOREandIMAGES_STOREcanrepresentanAmazonS3bucket. Scrapywill
automaticallyuploadthefilestothebucket.
Forexample,thisisavalidIMAGES_STORE value:
IMAGES_STORE = "s3://bucket/images"
You can modify the Access Control List (ACL) policy used for the stored files, which is defined by the
FILES_STORE_S3_ACL andIMAGES_STORE_S3_ACL settings. Bydefault, theACLissettoprivate. Tomakethe
filespubliclyavailableusethepublic-readpolicy:
IMAGES_STORE_S3_ACL = "public-read"
Formoreinformation,seecannedACLsintheAmazonS3DeveloperGuide.
YoucanalsouseotherS3-likestorages. Storageslikeself-hostedMinioorZenkoCloudServer. Allyouneedtodois
setendpointoptioninyouScrapysettings:
AWS_ENDPOINT_URL = "http://minio.example.com:9000"
Forself-hostingyoualsomightfeeltheneednottouseSSLandnottoverifySSLconnection:
AWS_USE_SSL = False # or True (None by default)
AWS_VERIFY = False # or True (None by default)
GoogleCloudStorage
FILES_STORE and IMAGES_STORE can represent a Google Cloud Storage bucket. Scrapy will automatically upload
thefilestothebucket. (requiresgoogle-cloud-storage)
Forexample,thesearevalidIMAGES_STORE andGCS_PROJECT_ID settings:
IMAGES_STORE = "gs://bucket/images/"
GCS_PROJECT_ID = "project_id"
5.9. Downloadingandprocessingfilesandimages 209

ScrapyDocumentation,Release2.13.3
Forinformationaboutauthentication,seethisdocumentation.
You can modify the Access Control List (ACL) policy used for the stored files, which is defined by the
FILES_STORE_GCS_ACLandIMAGES_STORE_GCS_ACLsettings. Bydefault,theACLissetto''(emptystring)which
meansthatCloudStorageappliesthebucket’sdefaultobjectACLtotheobject. Tomakethefilespubliclyavailable
usethepublicReadpolicy:
IMAGES_STORE_GCS_ACL = "publicRead"
Formoreinformation,seePredefinedACLsintheGoogleCloudPlatformDeveloperGuide.
5.9.6 Usage example
Inordertouseamediapipeline,firstenableit.
Then, if a spider returns an item object with the URLs field (file_urls or image_urls, for the Files or Images
Pipelinerespectively),thepipelinewillputtheresultsundertherespectivefield(filesorimages).
When using item types for which fields are defined beforehand, you must define both the URLs field and the results
field. Forexample,whenusingtheimagespipeline,itemsmustdefineboththeimage_urlsandtheimagesfield. For
instance,usingtheItem class:
import scrapy
class MyItem(scrapy.Item):
# ... other item fields ...
image_urls = scrapy.Field()
images = scrapy.Field()
IfyouwanttouseanotherfieldnamefortheURLskeyorfortheresultskey,itisalsopossibletooverrideit.
FortheFilesPipeline,setFILES_URLS_FIELD and/orFILES_RESULT_FIELD settings:
FILES_URLS_FIELD = "field_name_for_your_files_urls"
FILES_RESULT_FIELD = "field_name_for_your_processed_files"
FortheImagesPipeline,setIMAGES_URLS_FIELD and/orIMAGES_RESULT_FIELD settings:
IMAGES_URLS_FIELD = "field_name_for_your_images_urls"
IMAGES_RESULT_FIELD = "field_name_for_your_processed_images"
If you need something more complex and want to override the custom pipeline behaviour, see Extending the Media
Pipelines.
If you have multiple image pipelines inheriting from ImagePipeline and you want to have different settings in dif-
ferent pipelines you can set setting keys preceded with uppercase name of your pipeline class. E.g. if your
pipeline is called MyPipeline and you want to have custom IMAGES_URLS_FIELD you define setting MYP-
IPELINE_IMAGES_URLS_FIELDandyourcustomsettingswillbeused.
5.9.7 Additional features
Fileexpiration
The Image Pipeline avoids downloading files that were downloaded recently. To adjust this retention delay use the
FILES_EXPIRES setting (or IMAGES_EXPIRES, in case of Images Pipeline), which specifies the delay in number of
days:
210 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
# 120 days of delay for files expiration
FILES_EXPIRES = 120
# 30 days of delay for images expiration
IMAGES_EXPIRES = 30
Thedefaultvalueforbothsettingsis90days.
IfyouhavepipelinethatsubclassesFilesPipelineandyou’dliketohavedifferentsettingforityoucansetsettingkeys
precededbyuppercaseclassname. E.g. givenpipelineclasscalledMyPipelineyoucansetsettingkey:
MYPIPELINE_FILES_EXPIRES=180
andpipelineclassMyPipelinewillhaveexpirationtimesetto180.
Thelastmodifiedtimefromthefileisusedtodeterminetheageofthefileindays,whichisthencomparedtotheset
expirationtimetodetermineifthefileisexpired.
Thumbnailgenerationforimages
TheImagesPipelinecanautomaticallycreatethumbnailsofthedownloadedimages. Inordertousethisfeature,you
mustsetIMAGES_THUMBStoadictionarywherethekeysarethethumbnailnamesandthevaluesaretheirdimensions.
Forexample:
IMAGES_THUMBS = {
"small": (50, 50),
"big": (270, 270),
}
Whenyouusethisfeature,theImagesPipelinewillcreatethumbnailsoftheeachspecifiedsizewiththisformat:
<IMAGES_STORE>/thumbs/<size_name>/<image_id>.jpg
Where:
• <size_name>istheonespecifiedintheIMAGES_THUMBS dictionarykeys(small,big,etc)
• <image_id>istheSHA-1hashoftheimageurl
Exampleofimagefilesstoredusingsmallandbigthumbnailnames:
<IMAGES_STORE>/full/63bbfea82b8880ed33cdb762aa11fab722a90a24.jpg
<IMAGES_STORE>/thumbs/small/63bbfea82b8880ed33cdb762aa11fab722a90a24.jpg
<IMAGES_STORE>/thumbs/big/63bbfea82b8880ed33cdb762aa11fab722a90a24.jpg
Thefirstoneisthefullimage,asdownloadedfromthesite.
Filteringoutsmallimages
WhenusingtheImagesPipeline,youcandropimageswhicharetoosmall,byspecifyingtheminimumallowedsize
intheIMAGES_MIN_HEIGHT andIMAGES_MIN_WIDTH settings.
Forexample:
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110
5.9. Downloadingandprocessingfilesandimages 211

ScrapyDocumentation,Release2.13.3
(cid:242) Note
Thesizeconstraintsdon’taffectthumbnailgenerationatall.
Itispossibletosetjustonesizeconstraintorboth. Whensettingbothofthem,onlyimagesthatsatisfybothminimum
sizeswillbesaved. Fortheaboveexample,imagesofsizes(105x105)or(105x200)or(200x105)willallbedropped
becauseatleastonedimensionisshorterthantheconstraint.
Bydefault,therearenosizeconstraints,soallimagesareprocessed.
Allowingredirections
Bydefaultmediapipelinesignoreredirects,i.e. anHTTPredirectiontoamediafileURLrequestwillmeanthemedia
downloadisconsideredfailed.
Tohandlemediaredirections,setthissettingtoTrue:
MEDIA_ALLOW_REDIRECTS = True
5.9.8 Extending the Media Pipelines
SeeherethemethodsthatyoucanoverrideinyourcustomFilesPipeline:
class scrapy.pipelines.files.FilesPipeline
file_path(self,request,response=None,info=None,*,item=None)
Thismethodiscalledonceperdownloadeditem. Itreturnsthedownloadpathofthefileoriginatingfrom
thespecifiedresponse.
Inadditiontoresponse,thismethodreceivestheoriginalrequest,infoanditem
Youcanoverridethismethodtocustomizethedownloadpathofeachfile.
For example, if file URLs end like regular paths (e.g. https://example.com/a/b/c/foo.png), you
can use the following approach to download all files into the files folder with their original filenames
(e.g. files/foo.png):
from pathlib import PurePosixPath
from scrapy.utils.httpobj import urlparse_cached
from scrapy.pipelines.files import FilesPipeline
class MyFilesPipeline(FilesPipeline):
def file_path(self, request, response=None, info=None, *, item=None):
return "files/" + PurePosixPath(urlparse_cached(request).path).name
Similarly,youcanusetheitemtodeterminethefilepathbasedonsomeitemproperty.
Bydefaultthefile_path()methodreturnsfull/<request URL hash>.<extension>.
Addedinversion2.4: Theitemparameter.
get_media_requests(item,info)
Asseenontheworkflow,thepipelinewillgettheURLsoftheimagestodownloadfromtheitem. Inorder
todothis,youcanoverridetheget_media_requests()methodandreturnaRequestforeachfileURL:
212 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
from itemadapter import ItemAdapter
def get_media_requests(self, item, info):
adapter = ItemAdapter(item)
for file_url in adapter["file_urls"]:
yield scrapy.Request(file_url)
Those requests will be processed by the pipeline and, when they have finished downloading, the results
will be sent to the item_completed() method, as a list of 2-element tuples. Each tuple will contain
(success, file_info_or_error)where:
• successisabooleanwhichisTrueiftheimagewasdownloadedsuccessfullyorFalseifitfailed
forsomereason
• file_info_or_errorisadictcontainingthefollowingkeys(ifsuccessisTrue)oraFailureif
therewasaproblem.
– url-theurlwherethefilewasdownloadedfrom. Thisistheurloftherequestreturnedfrom
theget_media_requests()method.
– path-thepath(relativetoFILES_STORE)wherethefilewasstored
– checksum-aMD5hashoftheimagecontents
– status-thefilestatusindication.
Addedinversion2.2.
Itcanbeoneofthefollowing:
∗ downloaded-filewasdownloaded.
∗ uptodate-filewasnotdownloaded, asitwasdownloadedrecently, accordingtothefile
expirationpolicy.
∗ cached-filewasalreadyscheduledfordownload,byanotheritemsharingthesamefile.
Thelistoftuplesreceivedbyitem_completed()isguaranteedtoretainthesameorderoftherequests
returnedfromtheget_media_requests()method.
Here’satypicalvalueoftheresultsargument:
[
(
True,
{
"checksum": "2b00042f7481c7b056c4b410d28f33cf",
"path": "full/0a79c461a4062ac383dc4fade7bc09f1384a3910.jpg",
"url": "http://www.example.com/files/product1.pdf",
"status": "downloaded",
},
),
(False, Failure(...)),
]
Bydefaulttheget_media_requests()methodreturnsNonewhichmeanstherearenofilestodownload
fortheitem.
5.9. Downloadingandprocessingfilesandimages 213

ScrapyDocumentation,Release2.13.3
item_completed(results,item,info)
The FilesPipeline.item_completed() method called when all file requests for a single item have
completed(eitherfinisheddownloading,orfailedforsomereason).
The item_completed() method must return the output that will be sent to subsequent item pipeline
stages,soyoumustreturn(ordrop)theitem,asyouwouldinanypipeline.
Hereisanexampleoftheitem_completed()methodwherewestorethedownloadedfilepaths(passed
inresults)inthefile_pathsitemfield,andwedroptheitemifitdoesn’tcontainanyfiles:
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
def item_completed(self, results, item, info):
file_paths = [x["path"] for ok, x in results if ok]
if not file_paths:
raise DropItem("Item contains no files")
adapter = ItemAdapter(item)
adapter["file_paths"] = file_paths
return item
Bydefault,theitem_completed()methodreturnstheitem.
SeeherethemethodsthatyoucanoverrideinyourcustomImagesPipeline:
class scrapy.pipelines.images.ImagesPipeline
The ImagesPipeline is an extension of the FilesPipeline, customizing the field names and
addingcustombehaviorforimages.
file_path(self,request,response=None,info=None,*,item=None)
Thismethodiscalledonceperdownloadeditem. Itreturnsthedownloadpathofthefileoriginatingfrom
thespecifiedresponse.
Inadditiontoresponse,thismethodreceivestheoriginalrequest,infoanditem
Youcanoverridethismethodtocustomizethedownloadpathofeachfile.
For example, if file URLs end like regular paths (e.g. https://example.com/a/b/c/foo.png), you
can use the following approach to download all files into the files folder with their original filenames
(e.g. files/foo.png):
from pathlib import PurePosixPath
from scrapy.utils.httpobj import urlparse_cached
from scrapy.pipelines.images import ImagesPipeline
class MyImagesPipeline(ImagesPipeline):
def file_path(self, request, response=None, info=None, *, item=None):
return "files/" + PurePosixPath(urlparse_cached(request).path).name
Similarly,youcanusetheitemtodeterminethefilepathbasedonsomeitemproperty.
Bydefaultthefile_path()methodreturnsfull/<request URL hash>.<extension>.
Addedinversion2.4: Theitemparameter.
214 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
thumb_path(self,request,thumb_id,response=None,info=None,*,item=None)
ThismethodiscalledforeveryitemofIMAGES_THUMBS perdownloadeditem. Itreturnsthethumbnail
downloadpathoftheimageoriginatingfromthespecifiedresponse.
Inadditiontoresponse,thismethodreceivestheoriginalrequest,thumb_id,infoanditem.
Youcanoverridethismethodtocustomizethethumbnaildownloadpathofeachimage. Youcanusethe
itemtodeterminethefilepathbasedonsomeitemproperty.
By default the thumb_path() method returns thumbs/<size name>/<request URL hash>.
<extension>.
get_media_requests(item,info)
Works the same way as FilesPipeline.get_media_requests() method, but using a different field
nameforimageurls.
MustreturnaRequestforeachimageURL.
item_completed(results,item,info)
TheImagesPipeline.item_completed()methodiscalledwhenallimagerequestsforasingleitem
havecompleted(eitherfinisheddownloading,orfailedforsomereason).
WorksthesamewayasFilesPipeline.item_completed()method,butusingadifferentfieldnames
forstoringimagedownloadingresults.
Bydefault,theitem_completed()methodreturnstheitem.
5.9.9 Custom Images pipeline example
HereisafullexampleoftheImagesPipelinewhosemethodsareexemplifiedabove:
import scrapy
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
class MyImagesPipeline(ImagesPipeline):
def get_media_requests(self, item, info):
for image_url in item["image_urls"]:
yield scrapy.Request(image_url)
def item_completed(self, results, item, info):
image_paths = [x["path"] for ok, x in results if ok]
if not image_paths:
raise DropItem("Item contains no images")
adapter = ItemAdapter(item)
adapter["image_paths"] = image_paths
return item
ToenableyourcustommediapipelinecomponentyoumustadditsclassimportpathtotheITEM_PIPELINESsetting,
likeinthefollowingexample:
ITEM_PIPELINES = {"myproject.pipelines.MyImagesPipeline": 300}
5.9. Downloadingandprocessingfilesandimages 215

ScrapyDocumentation,Release2.13.3
5.10 Deploying Spiders
ThissectiondescribesthedifferentoptionsyouhavefordeployingyourScrapyspiderstorunthemonaregularbasis.
RunningScrapyspidersinyourlocalmachineisveryconvenientforthe(early)developmentstage, butnotsomuch
whenyouneedtoexecutelong-runningspidersormovespiderstoruninproductioncontinuously. Thisiswherethe
solutionsfordeployingScrapyspiderscomein.
PopularchoicesfordeployingScrapyspidersare:
• Scrapyd (opensource)
• ZyteScrapyCloud (cloud-based)
5.10.1 Deploying to a Scrapyd Server
ScrapydisanopensourceapplicationtorunScrapyspiders. ItprovidesaserverwithHTTPAPI,capableofrunning
andmonitoringScrapyspiders.
TodeployspiderstoScrapyd,youcanusethescrapyd-deploytoolprovidedbythescrapyd-clientpackage. Pleaserefer
tothescrapyd-deploydocumentationformoreinformation.
ScrapydismaintainedbysomeoftheScrapydevelopers.
5.10.2 Deploying to Zyte Scrapy Cloud
ZyteScrapyCloudisahosted,cloud-basedservicebyZyte,thecompanybehindScrapy.
ZyteScrapyCloudremovestheneedtosetupandmonitorserversandprovidesaniceUItomanagespidersandreview
scrapeditems,logsandstats.
TodeployspiderstoZyteScrapyCloudyoucanusetheshubcommandlinetool. PleaserefertotheZyteScrapyCloud
documentationformoreinformation.
ZyteScrapyCloudiscompatiblewithScrapydandonecanswitchbetweenthemasneeded-theconfigurationisread
fromthescrapy.cfgfilejustlikescrapyd-deploy.
5.11 AutoThrottle extension
ThisisanextensionforautomaticallythrottlingcrawlingspeedbasedonloadofboththeScrapyserverandthewebsite
youarecrawling.
5.11.1 Design goals
1. benicertositesinsteadofusingdefaultdownloaddelayofzero
2. automaticallyadjustScrapytotheoptimumcrawlingspeed,sotheuserdoesn’thavetotunethedownloaddelays
to find the optimum one. The user only needs to specify the maximum concurrent requests it allows, and the
extensiondoestherest.
5.11.2 How it works
Scrapy allows defining the concurrency and delay of different download slots, e.g. through the DOWNLOAD_SLOTS
setting. BydefaultrequestsareassignedtoslotsbasedontheirURLdomain,althoughitispossibletocustomizethe
downloadslotofanyrequest.
The AutoThrottle extension adjusts the delay of each download slot dynamically, to make your spider send
AUTOTHROTTLE_TARGET_CONCURRENCY concurrentrequestsonaveragetoeachremotewebsite.
216 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
Itusesdownloadlatencytocomputethedelays. Themainideaisthefollowing: ifaserverneedslatencysecondsto
respond,aclientshouldsendarequesteachlatency/NsecondstohaveNrequestsprocessedinparallel.
Insteadofadjustingthedelaysonecanjustsetasmallfixeddownloaddelayandimposehardlimitsonconcurrency
usingCONCURRENT_REQUESTS_PER_DOMAIN orCONCURRENT_REQUESTS_PER_IP options. Itwillprovideasimilar
effect,buttherearesomeimportantdifferences:
• becausethedownloaddelayissmalltherewillbeoccasionalburstsofrequests;
• oftennon-200(error)responsescanbereturnedfasterthanregularresponses, sowithasmalldownloaddelay
andahardconcurrencylimitcrawlerwillbesendingrequeststoserverfasterwhenserverstartstoreturnerrors.
Butthisisanoppositeofwhatcrawlershoulddo-incaseoferrorsitmakesmoresensetoslowdown: these
errorsmaybecausedbythehighrequestrate.
AutoThrottledoesn’thavetheseissues.
5.11.3 Throttling algorithm
AutoThrottlealgorithmadjustsdownloaddelaysbasedonthefollowingrules:
1. spidersalwaysstartwithadownloaddelayofAUTOTHROTTLE_START_DELAY;
2. whenaresponseisreceived,thetargetdownloaddelayiscalculatedaslatency / Nwherelatencyisalatency
oftheresponse,andNisAUTOTHROTTLE_TARGET_CONCURRENCY.
3. downloaddelayfornextrequestsissettotheaverageofpreviousdownloaddelayandthetargetdownloaddelay;
4. latenciesofnon-200responsesarenotallowedtodecreasethedelay;
5. downloaddelaycan’tbecomelessthanDOWNLOAD_DELAY orgreaterthanAUTOTHROTTLE_MAX_DELAY
(cid:242) Note
The AutoThrottle extension honours the standard Scrapy settings for concurrency and delay. This means that it
willrespectCONCURRENT_REQUESTS_PER_DOMAINandCONCURRENT_REQUESTS_PER_IPoptionsandneverseta
downloaddelaylowerthanDOWNLOAD_DELAY.
InScrapy,thedownloadlatencyismeasuredasthetimeelapsedbetweenestablishingtheTCPconnectionandreceiving
theHTTPheaders.
NotethattheselatenciesareveryhardtomeasureaccuratelyinacooperativemultitaskingenvironmentbecauseScrapy
may be busy processing a spider callback, for example, and unable to attend downloads. However, these latencies
shouldstillgiveareasonableestimateofhowbusyScrapy(andultimately,theserver)is,andthisextensionbuildson
thatpremise.
5.11.4 Prevent specific requests from triggering slot delay adjustments
AutoThrottleadjuststhedelayofdownloadslotsbasedonthelatenciesofresponsesthatbelongtothatdownloadslot.
Theonlyexceptionsarenon-200responses,whichareonlytakenintoaccounttoincreasethatdelay,butignoredifthey
woulddecreasethatdelay.
Youcanalsosettheautothrottle_dont_adjust_delayrequestmetadatakeytoTrueinanyrequesttopreventits
responselatencyfromimpactingthedelayofitsdownloadslot:
from scrapy import Request
Request("https://example.com", meta={"autothrottle_dont_adjust_delay": True})
5.11. AutoThrottleextension 217

ScrapyDocumentation,Release2.13.3
Note, however, that AutoThrottle still determines the starting delay of every download slot by setting the
download_delay attribute on the running spider. If you want AutoThrottle not to impact a download slot at all,
inadditiontosettingthismetakeyinallrequeststhatusethatdownloadslot,youmightwanttosetacustomvaluefor
thedelayattributeofthatdownloadslot,e.g. usingDOWNLOAD_SLOTS.
5.11.5 Settings
ThesettingsusedtocontroltheAutoThrottleextensionare:
• AUTOTHROTTLE_ENABLED
• AUTOTHROTTLE_START_DELAY
• AUTOTHROTTLE_MAX_DELAY
• AUTOTHROTTLE_TARGET_CONCURRENCY
• AUTOTHROTTLE_DEBUG
• CONCURRENT_REQUESTS_PER_DOMAIN
• CONCURRENT_REQUESTS_PER_IP
• DOWNLOAD_DELAY
FormoreinformationseeHowitworks.
AUTOTHROTTLE_ENABLED
Default: False
EnablestheAutoThrottleextension.
AUTOTHROTTLE_START_DELAY
Default: 5.0
Theinitialdownloaddelay(inseconds).
AUTOTHROTTLE_MAX_DELAY
Default: 60.0
Themaximumdownloaddelay(inseconds)tobesetincaseofhighlatencies.
AUTOTHROTTLE_TARGET_CONCURRENCY
Default: 1.0
AveragenumberofrequestsScrapyshouldbesendinginparalleltoremotewebsites. Itmustbehigherthan0.0.
By default, AutoThrottle adjusts the delay to send a single concurrent request to each of the remote websites. Set
this option to a higher value (e.g. 2.0) to increase the throughput and the load on remote servers. A lower
AUTOTHROTTLE_TARGET_CONCURRENCYvalue(e.g. 0.5)makesthecrawlermoreconservativeandpolite.
Note that CONCURRENT_REQUESTS_PER_DOMAIN and CONCURRENT_REQUESTS_PER_IP options are still respected
whenAutoThrottleextensionisenabled. Thismeansthatif AUTOTHROTTLE_TARGET_CONCURRENCYissettoavalue
higherthanCONCURRENT_REQUESTS_PER_DOMAIN orCONCURRENT_REQUESTS_PER_IP,thecrawlerwon’treachthis
numberofconcurrentrequests.
At every given time point Scrapy can be sending more or less concurrent requests than
AUTOTHROTTLE_TARGET_CONCURRENCY; it is a suggested value the crawler tries to approach, not a hard limit.
218 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
AUTOTHROTTLE_DEBUG
Default: False
EnableAutoThrottledebugmodewhichwilldisplaystatsoneveryresponsereceived,soyoucanseehowthethrottling
parametersarebeingadjustedinrealtime.
5.12 Benchmarking
ScrapycomeswithasimplebenchmarkingsuitethatspawnsalocalHTTPserverandcrawlsitatthemaximumpossible
speed. ThegoalofthisbenchmarkingistogetanideaofhowScrapyperformsinyourhardware, inordertohavea
commonbaselineforcomparisons. Itusesasimplespiderthatdoesnothingandjustfollowslinks.
Torunituse:
scrapy bench
Youshouldseeanoutputlikethis:
2016-12-16 21:18:48 [scrapy.utils.log] INFO: Scrapy 1.2.2 started (bot: quotesbot)
2016-12-16 21:18:48 [scrapy.utils.log] INFO: Overridden settings: {'CLOSESPIDER_TIMEOUT
': 10, 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['quotesbot.spiders'], 'LOGSTATS_
˓→
INTERVAL': 1, 'BOT_NAME': 'quotesbot', 'LOG_LEVEL': 'INFO', 'NEWSPIDER_MODULE':
˓→
'quotesbot.spiders'}
˓→
2016-12-16 21:18:49 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.closespider.CloseSpider',
'scrapy.extensions.logstats.LogStats',
'scrapy.extensions.telnet.TelnetConsole',
'scrapy.extensions.corestats.CoreStats']
2016-12-16 21:18:49 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.offsite.OffsiteMiddleware',
'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
'scrapy.downloadermiddlewares.retry.RetryMiddleware',
'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
'scrapy.downloadermiddlewares.stats.DownloaderStats']
2016-12-16 21:18:49 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
'scrapy.spidermiddlewares.referer.RefererMiddleware',
'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
'scrapy.spidermiddlewares.depth.DepthMiddleware']
2016-12-16 21:18:49 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2016-12-16 21:18:49 [scrapy.core.engine] INFO: Spider opened
2016-12-16 21:18:49 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min),␣
scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:50 [scrapy.extensions.logstats] INFO: Crawled 70 pages (at 4200 pages/
min), scraped 0 items (at 0 items/min)
˓→
(continuesonnextpage)
5.12. Benchmarking 219

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
2016-12-16 21:18:51 [scrapy.extensions.logstats] INFO: Crawled 134 pages (at 3840 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:52 [scrapy.extensions.logstats] INFO: Crawled 198 pages (at 3840 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:53 [scrapy.extensions.logstats] INFO: Crawled 254 pages (at 3360 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:54 [scrapy.extensions.logstats] INFO: Crawled 302 pages (at 2880 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:55 [scrapy.extensions.logstats] INFO: Crawled 358 pages (at 3360 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:56 [scrapy.extensions.logstats] INFO: Crawled 406 pages (at 2880 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:57 [scrapy.extensions.logstats] INFO: Crawled 438 pages (at 1920 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:58 [scrapy.extensions.logstats] INFO: Crawled 470 pages (at 1920 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:18:59 [scrapy.core.engine] INFO: Closing spider (closespider_timeout)
2016-12-16 21:18:59 [scrapy.extensions.logstats] INFO: Crawled 518 pages (at 2880 pages/
min), scraped 0 items (at 0 items/min)
˓→
2016-12-16 21:19:00 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 229995,
'downloader/request_count': 534,
'downloader/request_method_count/GET': 534,
'downloader/response_bytes': 1565504,
'downloader/response_count': 534,
'downloader/response_status_count/200': 534,
'finish_reason': 'closespider_timeout',
'finish_time': datetime.datetime(2016, 12, 16, 16, 19, 0, 647725),
'log_count/INFO': 17,
'request_depth_max': 19,
'response_received_count': 534,
'scheduler/dequeued': 533,
'scheduler/dequeued/memory': 533,
'scheduler/enqueued': 10661,
'scheduler/enqueued/memory': 10661,
'start_time': datetime.datetime(2016, 12, 16, 16, 18, 49, 799869)}
2016-12-16 21:19:00 [scrapy.core.engine] INFO: Spider closed (closespider_timeout)
ThattellsyouthatScrapyisabletocrawlabout3000pagesperminuteinthehardwarewhereyourunit. Notethatthis
isaverysimplespiderintendedtofollowlinks,anycustomspideryouwritewillprobablydomorestuffwhichresults
inslowercrawlrates. Howslowerdependsonhowmuchyourspiderdoesandhowwellit’swritten.
Usescrapy-benchformorecomplexbenchmarking.
5.13 Jobs: pausing and resuming crawls
Sometimes,forbigsites,it’sdesirabletopausecrawlsandbeabletoresumethemlater.
Scrapysupportsthisfunctionalityoutoftheboxbyprovidingthefollowingfacilities:
• aschedulerthatpersistsscheduledrequestsondisk
• aduplicatesfilterthatpersistsvisitedrequestsondisk
• anextensionthatkeepssomespiderstate(key/valuepairs)persistentbetweenbatches
220 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
5.13.1 Job directory
ToenablepersistencesupportyoujustneedtodefineajobdirectorythroughtheJOBDIRsetting. Thisdirectorywillbe
forstoringallrequireddatatokeepthestateofasinglejob(i.e. aspiderrun). It’simportanttonotethatthisdirectory
mustnotbesharedbydifferentspiders,orevendifferentjobs/runsofthesamespider,asit’smeanttobeusedforstoring
thestateofasinglejob.
5.13.2 How to use it
Tostartaspiderwithpersistencesupportenabled,runitlikethis:
scrapy crawl somespider -s JOBDIR=crawls/somespider-1
Then,youcanstopthespidersafelyatanytime(bypressingCtrl-Corsendingasignal),andresumeitlaterbyissuing
thesamecommand:
scrapy crawl somespider -s JOBDIR=crawls/somespider-1
5.13.3 Keeping persistent state between batches
Sometimesyou’llwanttokeepsomepersistentspiderstatebetweenpause/resumebatches. Youcanusethespider.
stateattributeforthat,whichshouldbeadict. There’sabuilt-inextensionthattakescareofserializing,storingand
loadingthatattributefromthejobdirectory,whenthespiderstartsandstops.
Here’sanexampleofacallbackthatusesthespiderstate(otherspidercodeisomittedforbrevity):
def parse_item(self, response):
# parse item here
self.state["items_count"] = self.state.get("items_count", 0) + 1
5.13.4 Persistence gotchas
ThereareafewthingstokeepinmindifyouwanttobeabletousetheScrapypersistencesupport:
Cookiesexpiration
Cookies may expire. So, if you don’t resume your spider quickly the requests scheduled may no longer work. This
won’tbeanissueifyourspiderdoesn’trelyoncookies.
Requestserialization
Forpersistencetowork, Request objectsmustbeserializablewithpickle, exceptforthe callbackand errback
valuespassedtotheir__init__method,whichmustbemethodsoftherunningSpiderclass.
Ifyouwishtologtherequeststhatcouldn’tbeserialized, youcansettheSCHEDULER_DEBUG settingtoTrueinthe
project’ssettingspage. ItisFalsebydefault.
5.14 Coroutines
Addedinversion2.0.
Scrapysupportsthecoroutinesyntax(i.e. async def).
5.14. Coroutines 221

ScrapyDocumentation,Release2.13.3
5.14.1 Supported callables
Thefollowingcallablesmaybedefinedascoroutinesusingasync def,andhenceusecoroutinesyntax(e.g. await,
async for,async with):
• Thestart()spidermethod,whichmustbedefinedasanasynchronousgenerator.
Addedinversion2.13.
• Requestcallbacks.
Ifyouareusinganycustomorthird-partyspidermiddleware,seeMixingsynchronousandasynchronousspider
middlewares.
Changedinversion2.7: Outputofasynccallbacksisnowprocessedasynchronouslyinsteadofcollectingallof
itfirst.
• Theprocess_item()methodofitempipelines.
• Theprocess_request(),process_response(),andprocess_exception()methodsofdownloadermid-
dlewares.
• Theprocess_spider_output()methodofspidermiddlewares.
Ifdefinedasacoroutine,itmustbeanasynchronousgenerator. Theinputresultparameterisanasynchronous
iterable.
SeealsoMixingsynchronousandasynchronousspidermiddlewaresandUniversalspidermiddlewares.
Addedinversion2.7.
• Theprocess_start()methodofspidermiddlewares,whichmustbedefinedasanasynchronousgenerator.
Addedinversion2.13.
• Signalhandlersthatsupportdeferreds.
5.14.2 Using Deferred-based APIs
In addition to native coroutine APIs Scrapy has some APIs that return a Deferred object or take a user-supplied
functionthatreturnsaDeferredobject. TheseAPIsarealsoasynchronousbutdon’tyetsupportnativeasync def
syntax. Inthefutureweplantoaddsupportfortheasync defsyntaxtotheseAPIsorreplacethemwithotherAPIs
wherechangingtheexistingonesispossible.
ThefollowingScrapymethodsreturnDeferredobjects(thislistisnotcompleteasitonlyincludesmethodsthatwe
thinkmaybeusefulforusercode):
• scrapy.crawler.Crawler:
– crawl()
– stop()
• scrapy.crawler.CrawlerRunner(alsoinheritedbyscrapy.crawler.CrawlerProcess):
– crawl()
– stop()
– join()
• scrapy.core.engine.ExecutionEngine:
– download()
• scrapy.signalmanager.SignalManager:
222 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
– send_catch_log_deferred()
• MailSender
– send()
The following user-supplied methods can return Deferred objects (the methods that can also return coroutines are
listedinSupportedcallables):
• Customdownloadhandlers(seeDOWNLOAD_HANDLERS):
– download_request()
– close()
• Customdownloaderimplementations(seeDOWNLOADER):
– fetch()
• Customschedulerimplementations(seeSCHEDULER):
– open()
– close()
• Customdupefilters(seeDUPEFILTER_CLASS):
– open()
– close()
• Customfeedstorages(seeFEED_STORAGES):
– store()
• Subclassesof scrapy.pipelines.media.MediaPipeline:
– media_to_download()
– item_completed()
• Customstoragesusedbysubclassesofscrapy.pipelines.files.FilesPipeline:
– persist_file()
– stat_file()
InmostcasesyoucanusetheseAPIsincodethatotherwiseusescoroutines,bywrappingaDeferredobjectintoa
Futureobjectorviceversa. SeeIntegratingDeferredcodeandasynciocodeformoreinformationaboutthis.
Forexample:
• The ExecutionEngine.download() method returns a Deferred object that fires with the downloaded re-
sponse. You can use this object directly in Deferred-based code or convert it into a Future object with
maybe_deferred_to_future().
• Acustomdownloadhandlerneedstodefinea download_request()methodthatreturnsaDeferredobject.
You can write a method that works with Deferreds and returns one directly, or you can write a coroutine and
convertitintoafunctionthatreturnsaDeferredwithdeferred_f_from_coro_f().
5.14.3 General usage
ThereareseveralusecasesforcoroutinesinScrapy.
Code that would return Deferreds when written for previous Scrapy versions, such as downloader middlewares and
signalhandlers,canberewrittentobeshorterandcleaner:
5.14. Coroutines 223

ScrapyDocumentation,Release2.13.3
from itemadapter import ItemAdapter
class DbPipeline:
def _update_item(self, data, item):
adapter = ItemAdapter(item)
adapter["field"] = data
return item
def process_item(self, item, spider):
adapter = ItemAdapter(item)
dfd = db.get_some_data(adapter["id"])
dfd.addCallback(self._update_item, item)
return dfd
becomes:
from itemadapter import ItemAdapter
class DbPipeline:
async def process_item(self, item, spider):
adapter = ItemAdapter(item)
adapter["field"] = await db.get_some_data(adapter["id"])
return item
Coroutinesmaybeusedtocallasynchronouscode. Thisincludesothercoroutines,functionsthatreturnDeferredsand
functionsthatreturnawaitableobjectssuchasFuture. ThismeansyoucanusemanyusefulPythonlibrariesproviding
suchcode:
class MySpiderDeferred(Spider):
# ...
async def parse(self, response):
additional_response = await treq.get("https://additional.url")
additional_data = await treq.content(additional_response)
# ... use response and additional_data to yield items and requests
class MySpiderAsyncio(Spider):
# ...
async def parse(self, response):
async with aiohttp.ClientSession() as session:
async with session.get("https://additional.url") as additional_response:
additional_data = await additional_response.text()
# ... use response and additional_data to yield items and requests
(cid:242) Note
Manylibrariesthatusecoroutines,suchasaio-libs,requiretheasyncioloopandtousethemyouneedtoenable
asynciosupportinScrapy.
224 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
(cid:242) Note
IfyouwanttoawaitonDeferredswhileusingtheasyncioreactor,youneedtowrapthem.
Commonusecasesforasynchronouscodeinclude:
• requestingdatafromwebsites,databasesandotherservices(instart(),callbacks,pipelinesandmiddlewares);
• storingdataindatabases(inpipelinesandmiddlewares);
• delayingthespiderinitializationuntilsomeexternalevent(inthespider_opened handler);
• callingasynchronousScrapymethodslikeExecutionEngine.download()(seethescreenshotpipelineexam-
ple).
5.14.4 Inline requests
Thespiderbelowshowshowtosendarequestandawaititsresponseallfromwithinaspidercallback:
from scrapy import Spider, Request
from scrapy.utils.defer import maybe_deferred_to_future
class SingleRequestSpider(Spider):
name = "single"
start_urls = ["https://example.org/product"]
async def parse(self, response, **kwargs):
additional_request = Request("https://example.org/price")
deferred = self.crawler.engine.download(additional_request)
additional_response = await maybe_deferred_to_future(deferred)
yield {
"h1": response.css("h1").get(),
"price": additional_response.css("#price").get(),
}
Youcanalsosendmultiplerequestsinparallel:
from scrapy import Spider, Request
from scrapy.utils.defer import maybe_deferred_to_future
from twisted.internet.defer import DeferredList
class MultipleRequestsSpider(Spider):
name = "multiple"
start_urls = ["https://example.com/product"]
async def parse(self, response, **kwargs):
additional_requests = [
Request("https://example.com/price"),
Request("https://example.com/color"),
]
deferreds = []
for r in additional_requests:
deferred = self.crawler.engine.download(r)
(continuesonnextpage)
5.14. Coroutines 225

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
deferreds.append(deferred)
responses = await maybe_deferred_to_future(DeferredList(deferreds))
yield {
"h1": response.css("h1::text").get(),
"price": responses[0][1].css(".price::text").get(),
"price2": responses[1][1].css(".color::text").get(),
}
5.14.5 Mixing synchronous and asynchronous spider middlewares
Addedinversion2.7.
TheoutputofaRequestcallbackispassedastheresultparametertotheprocess_spider_output()methodofthe
firstspidermiddlewarefromthelistofactivespidermiddlewares. Thentheoutputofthatprocess_spider_output
methodispassedtotheprocess_spider_outputmethodofthenextspidermiddleware,andsoonforeveryactive
spidermiddleware.
Scrapysupportsmixingcoroutinemethodsandsynchronousmethodsinthischainofcalls.
However, if any of the process_spider_output methods is defined as a synchronous method, and the previous
Requestcallbackorprocess_spider_outputmethodisacoroutine,therearesomedrawbackstotheasynchronous-
to-synchronous conversion that Scrapy does so that the synchronous process_spider_output method gets a syn-
chronousiterableasitsresultparameter:
• The whole output of the previous Request callback or process_spider_output method is awaited at this
point.
• IfanexceptionraiseswhileawaitingtheoutputofthepreviousRequestcallbackorprocess_spider_output
method,noneofthatoutputwillbeprocessed.
Thiscontrastswiththeregularbehavior,whereallitemsyieldedbeforeanexceptionraisesareprocessed.
Asynchronous-to-synchronousconversionsaresupportedforbackwardcompatibility,buttheyaredeprecatedandwill
stopworkinginafutureversionofScrapy.
Toavoidasynchronous-to-synchronousconversions,whendefiningRequestcallbacksascoroutinemethodsorwhen
using spider middlewares whose process_spider_output method is an asynchronous generator, all active spider
middlewaresmusteitherhavetheirprocess_spider_outputmethoddefinedasanasynchronousgeneratorordefine
aprocess_spider_output_asyncmethod.
Formiddlewareusers
If you have asynchronous callbacks or use asynchronous-only spider middlewares you should make sure the
asynchronous-to-synchronous conversions described above don’t happen. To do this, make sure all spider middle-
wares you use support asynchronous spider output. Even if you don’t have asynchronous callbacks and don’t use
asynchronous-onlyspidermiddlewaresinyourproject,it’sstillagoodideatomakesureallmiddlewaresyouusesup-
portasynchronousspideroutput,sothatitwillbeeasytostartusingasynchronouscallbacksinthefuture. Becauseof
this,Scrapylogsawarningwhenitdetectsasynchronous-onlyspidermiddleware.
Ifyouwanttoupdatemiddlewaresyouwrote,seethefollowingsection. Ifyouhave3rd-partymiddlewaresthataren’t
yetupdatedbytheirauthors,youcansubclassthemtomakethemuniversalandusethesubclassesinyourprojects.
226 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
Formiddlewareauthors
Ifyouhaveaspidermiddlewarethatdefinesasynchronousprocess_spider_outputmethod,youshouldupdateit
tosupportasynchronousspideroutputforbettercompatibility,evenifyoudon’tyetuseitwithasynchronouscallbacks,
especiallyifyoupublishthismiddlewareforotherpeopletouse. Youhavetwooptionsforthis:
1. Makethemiddlewareasynchronous,bymakingtheprocess_spider_outputmethodanasynchronousgener-
ator.
2. Makethemiddlewareuniversal,asdescribedinthenextsection.
Ifyourmiddlewarewon’tbeusedinprojectswithsynchronous-onlymiddlewares,e.g. becauseit’saninternalmiddle-
wareandyouknowthatallothermiddlewaresinyourprojectsarealreadyupdated,it’ssafetochoosethefirstoption.
Otherwise,it’sbettertochoosethesecondoption.
Universalspidermiddlewares
Addedinversion2.7.
Toallowwritingaspidermiddlewarethatsupportsasynchronousexecutionofitsprocess_spider_outputmethodin
Scrapy2.7andlater(avoidingasynchronous-to-synchronousconversions)whilemaintainingsupportforolderScrapy
versions,youmaydefineprocess_spider_outputasasynchronousmethodanddefineanasynchronousgenerator
versionofthatmethodwithanalternativename: process_spider_output_async.
Forexample:
class UniversalSpiderMiddleware:
def process_spider_output(self, response, result, spider):
for r in result:
# ... do something with r
yield r
async def process_spider_output_async(self, response, result, spider):
async for r in result:
# ... do something with r
yield r
(cid:242) Note
Thisisaninterimmeasuretoallow,foratime,towritecodethatworksinScrapy2.7andlaterwithoutrequiring
asynchronous-to-synchronousconversions,andworksinearlierScrapyversionsaswell.
InsomefutureversionofScrapy,however,thisfeaturewillbedeprecatedand,eventually,inalaterversionofScrapy,
thisfeaturewillberemoved,andallspidermiddlewareswillbeexpectedtodefinetheirprocess_spider_output
methodasanasynchronousgenerator.
Since 2.13.0, Scrapy provides a base class, BaseSpiderMiddleware, which implements the
process_spider_output() and process_spider_output_async() methods, so instead of duplicating the
processingcodeyoucanoverridetheget_processed_request()and/ortheget_processed_item()method.
5.15 asyncio
Addedinversion2.0.
Scrapyhaspartialsupportforasyncio. Afteryouinstalltheasyncioreactor,youmayuseasyncioandasyncio-
poweredlibrariesinanycoroutine.
5.15. asyncio 227

ScrapyDocumentation,Release2.13.3
5.15.1 Installing the asyncio reactor
To enable asyncio support, your TWISTED_REACTOR setting needs to be set to 'twisted.internet.
asyncioreactor.AsyncioSelectorReactor',whichisthedefaultvalue.
IfyouareusingCrawlerRunner,youalsoneedtoinstalltheAsyncioSelectorReactorreactormanually. Youcan
dothatusinginstall_reactor():
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
5.15.2 Handling a pre-installed reactor
twisted.internet.reactorandsomeotherTwistedimportsinstallthedefaultTwistedreactorasasideeffect. Once
aTwistedreactorisinstalled,itisnotpossibletoswitchtoadifferentreactoratruntime.
If you configure the asyncio Twisted reactor and, at run time, Scrapy complains that a different reactor is already
installed,chancesareyouhavesomesuchimportsinyourcode.
You can usually fix the issue by moving those offending module-level Twisted imports to the method or function
definitionswheretheyareused. Forexample,ifyouhavesomethinglike:
from twisted.internet import reactor
def my_function():
reactor.callLater(...)
Switchtosomethinglike:
def my_function():
from twisted.internet import reactor
reactor.callLater(...)
Alternatively, you can try to manually install the asyncio reactor, with install_reactor(), before those imports
happen.
5.15.3 Integrating Deferred code and asyncio code
Coroutine functions can await on Deferreds by wrapping them into asyncio.Future objects. Scrapy provides two
helpersforthis:
scrapy.utils.defer.deferred_to_future(d: Deferred[_T])→Future[_T]
Addedinversion2.6.0.
Returnanasyncio.Futureobjectthatwrapsd.
Whenusingtheasyncioreactor,youcannotawaitonDeferredobjectsfromScrapycallablesdefinedascorou-
tines, you can only await on Future objects. Wrapping Deferred objects into Future objects allows you to
waitonthem:
class MySpider(Spider):
...
async def parse(self, response):
additional_request = scrapy.Request('https://example.org/price')
deferred = self.crawler.engine.download(additional_request)
additional_response = await deferred_to_future(deferred)
228 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
scrapy.utils.defer.maybe_deferred_to_future(d: Deferred[_T])→Deferred[_T]|Future[_T]
Addedinversion2.6.0.
Returnd asanobjectthatcanbeawaitedfromaScrapycallabledefinedasacoroutine.
WhatyoucanawaitinScrapycallablesdefinedascoroutinesdependsonthevalueofTWISTED_REACTOR:
• Whenusingtheasyncioreactor,youcanonlyawaitonasyncio.Futureobjects.
• Whennotusingtheasyncioreactor,youcanonlyawaitonDeferredobjects.
If you want to write code that uses Deferred objects but works with any reactor, use this function on all
Deferredobjects:
class MySpider(Spider):
...
async def parse(self, response):
additional_request = scrapy.Request('https://example.org/price')
deferred = self.crawler.engine.download(additional_request)
additional_response = await maybe_deferred_to_future(deferred)
(cid:17) Tip
If you don’t need to support reactors other than the default AsyncioSelectorReactor, you can use
deferred_to_future(),otherwiseyoushouldusemaybe_deferred_to_future().
(cid:17) Tip
IfyouneedtousethesefunctionsincodethataimstobecompatiblewithlowerversionsofScrapythatdonotprovide
thesefunctions,downtoScrapy2.0(earlierversionsdonotsupportasyncio),youcancopytheimplementation
ofthesefunctionsintoyourowncode.
CoroutinesandfuturescanbewrappedintoDeferreds(forexample,whenaScrapyAPIrequirespassingaDeferredto
it)usingthefollowinghelpers:
scrapy.utils.defer.deferred_from_coro(o: _CT)→Deferred
scrapy.utils.defer.deferred_from_coro(o: _T)→_T
ConvertsacoroutineorotherawaitableobjectintoaDeferred,orreturnstheobjectasisifitisn’tacoroutine.
scrapy.utils.defer.deferred_f_from_coro_f(coro_f: Callable[_P,Coroutine[Any,Any,_T]])→
Callable[_P,Deferred[_T]]
ConvertsacoroutinefunctionintoafunctionthatreturnsaDeferred.
Thecoroutinefunctionwillbecalledatthetimewhenthewrapperiscalled. Wrapperargswillbepassedtoit.
Thisisusefulforcallbackchains,ascallbackfunctionsarecalledwiththepreviouscallbackresult.
5.15.4 Enforcing asyncio as a requirement
If you are writing a component that requires asyncio to work, use scrapy.utils.reactor.
is_asyncio_reactor_installed()toenforceitasarequirement. Forexample:
from scrapy.utils.reactor import is_asyncio_reactor_installed
(continuesonnextpage)
5.15. asyncio 229

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class MyComponent:
def __init__(self):
if not is_asyncio_reactor_installed():
raise ValueError(
f"{MyComponent.__qualname__} requires the asyncio Twisted "
f"reactor. Make sure you have it configured in the "
f"TWISTED_REACTOR setting. See the asyncio documentation "
f"of Scrapy for more information."
)
scrapy.utils.reactor.is_asyncio_reactor_installed()→bool
CheckwhethertheinstalledreactorisAsyncioSelectorReactor.
RaiseaRuntimeErrorifnoreactorisinstalled.
Changedinversion2.13: InearlierScrapyversionsthisfunctionsilentlyinstalledthedefaultreactoriftherewas
noreactorinstalled. Nowitraisesanexceptiontopreventsilentproblemsinthiscase.
5.15.5 Windows-specific notes
TheWindowsimplementationofasynciocanusetwoeventloopimplementations, ProactorEventLoop(default)
andSelectorEventLoop. However,onlySelectorEventLoopworkswithTwisted.
ScrapychangestheeventloopclasstoSelectorEventLoopautomaticallywhenyouchangetheTWISTED_REACTOR
settingorcallinstall_reactor().
(cid:242) Note
OtherlibrariesyouusemayrequireProactorEventLoop,e.g. becauseitsupportssubprocesses(thisisthecase
withplaywright),soyoucannotusethemtogetherwithScrapyonWindows(butyoushouldbeabletousethem
onWSLornativeLinux).
5.15.6 Using custom asyncio loops
Youcanalsousecustomasyncioeventloopswiththeasyncioreactor. SettheASYNCIO_EVENT_LOOP settingtothe
importpathofthedesiredeventloopclasstouseitinsteadofthedefaultasyncioeventloop.
5.15.7 Switching to a non-asyncio reactor
If for some reason your code doesn’t work with the asyncio reactor, you can use a different reactor by setting the
TWISTED_REACTOR setting to its import path (e.g. 'twisted.internet.epollreactor.EPollReactor') or to
None,whichwillusethedefaultreactorforyourplatform.
FrequentlyAskedQuestions
Getanswerstomostfrequentlyaskedquestions.
DebuggingSpiders
LearnhowtodebugcommonproblemsofyourScrapyspider.
SpidersContracts
Learnhowtousecontractsfortestingyourspiders.
CommonPractices
GetfamiliarwithsomeScrapycommonpractices.
230 Chapter5. Solvingspecificproblems

ScrapyDocumentation,Release2.13.3
BroadCrawls
TuneScrapyforcrawlingalotdomainsinparallel.
Usingyourbrowser’sDeveloperToolsforscraping
Learnhowtoscrapewithyourbrowser’sdevelopertools.
Selectingdynamically-loadedcontent
Readwebpagedatathatisloadeddynamically.
Debuggingmemoryleaks
Learnhowtofindandgetridofmemoryleaksinyourcrawler.
Downloadingandprocessingfilesandimages
Downloadfilesand/orimagesassociatedwithyourscrapeditems.
DeployingSpiders
DeployingyourScrapyspidersandruntheminaremoteserver.
AutoThrottleextension
Adjustcrawlratedynamicallybasedonload.
Benchmarking
CheckhowScrapyperformsonyourhardware.
Jobs: pausingandresumingcrawls
Learnhowtopauseandresumecrawlsforlargespiders.
Coroutines
Usethecoroutinesyntax.
asyncio
Useasyncioandasyncio-poweredlibraries.
5.15. asyncio 231

ScrapyDocumentation,Release2.13.3
232 Chapter5. Solvingspecificproblems

CHAPTER
SIX
EXTENDING SCRAPY
6.1 Architecture overview
ThisdocumentdescribesthearchitectureofScrapyandhowitscomponentsinteract.
6.1.1 Overview
ThefollowingdiagramshowsanoverviewoftheScrapyarchitecturewithitscomponentsandanoutlineofthedata
flowthattakesplaceinsidethesystem(shownbytheredarrows). Abriefdescriptionofthecomponentsisincluded
belowwithlinksformoredetailedinformationaboutthem. Thedataflowisalsodescribedbelow.
6.1.2 Data flow
ThedataflowinScrapyiscontrolledbytheexecutionengine,andgoeslikethis:
233

ScrapyDocumentation,Release2.13.3
1. TheEnginegetstheinitialRequeststocrawlfromtheSpider.
2. TheEngineschedulestheRequestsintheSchedulerandasksforthenextRequeststocrawl.
3. TheSchedulerreturnsthenextRequeststotheEngine.
4. The Engine sends the Requests to the Downloader, passing through the Downloader Middlewares (see
process_request()).
5. OncethepagefinishesdownloadingtheDownloader generatesaResponse(withthatpage)andsendsittothe
Engine,passingthroughtheDownloaderMiddlewares(seeprocess_response()).
6. TheEnginereceivestheResponsefromtheDownloaderandsendsittotheSpiderforprocessing,passingthrough
theSpiderMiddleware(seeprocess_spider_input()).
7. TheSpiderprocessestheResponseandreturnsscrapeditemsandnewRequests(tofollow)totheEngine,passing
throughtheSpiderMiddleware(seeprocess_spider_output()).
8. TheEnginesendsprocesseditemstoItemPipelines,thensendprocessedRequeststotheSchedulerandasksfor
possiblenextRequeststocrawl.
9. Theprocessrepeats(fromstep3)untiltherearenomorerequestsfromtheScheduler.
6.1.3 Components
ScrapyEngine
The engine is responsible for controlling the data flow between all components of the system, and triggering events
whencertainactionsoccur. SeetheDataFlowsectionaboveformoredetails.
Scheduler
Thescheduler receivesrequestsfromtheengineandenqueuesthemforfeedingthemlater(alsototheengine)when
theenginerequeststhem.
Downloader
TheDownloaderisresponsibleforfetchingwebpagesandfeedingthemtotheenginewhich,inturn,feedsthemtothe
spiders.
Spiders
SpidersarecustomclasseswrittenbyScrapyuserstoparseresponsesandextractitemsfromthemoradditionalrequests
tofollow. FormoreinformationseeSpiders.
ItemPipeline
The Item Pipeline is responsible for processing the items once they have been extracted (or scraped) by the spiders.
Typicaltasksincludecleansing,validationandpersistence(likestoringtheiteminadatabase). Formoreinformation
seeItemPipeline.
Downloadermiddlewares
DownloadermiddlewaresarespecifichooksthatsitbetweentheEngineandtheDownloaderandprocessrequestswhen
theypassfromtheEnginetotheDownloader,andresponsesthatpassfromDownloadertotheEngine.
UseaDownloadermiddlewareifyouneedtodooneofthefollowing:
• processarequestjustbeforeitissenttotheDownloader(i.e. rightbeforeScrapysendstherequesttothewebsite);
• changereceivedresponsebeforepassingittoaspider;
234 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
• sendanewRequestinsteadofpassingreceivedresponsetoaspider;
• passresponsetoaspiderwithoutfetchingawebpage;
• silentlydropsomerequests.
FormoreinformationseeDownloaderMiddleware.
Spidermiddlewares
SpidermiddlewaresarespecifichooksthatsitbetweentheEngineandtheSpidersandareabletoprocessspiderinput
(responses)andoutput(itemsandrequests).
UseaSpidermiddlewareifyouneedto
• post-processoutputofspidercallbacks-change/add/removerequestsoritems;
• post-processstartrequestsoritems;
• handlespiderexceptions;
• callerrbackinsteadofcallbackforsomeoftherequestsbasedonresponsecontent.
FormoreinformationseeSpiderMiddleware.
6.1.4 Event-driven networking
ScrapyiswrittenwithTwisted,apopularevent-drivennetworkingframeworkforPython. Thus,it’simplementedusing
anon-blocking(akaasynchronous)codeforconcurrency.
FormoreinformationaboutasynchronousprogrammingandTwistedseetheselinks:
• IntroductiontoDeferreds
• TwistedIntroduction-Krondo
6.2 Add-ons
Scrapy’sadd-onsystemisaframeworkwhichunifiesmanagingandconfiguringcomponentsthatextendScrapy’score
functionality,suchasmiddlewares,extensions,orpipelines. Itprovidesuserswithaplug-and-playexperienceinScrapy
extensionmanagement,andgrantsextensiveconfigurationcontroltodevelopers.
6.2.1 Activating and configuring add-ons
DuringCrawlerinitialization,thelistofenabledadd-onsisreadfromyourADDONSsetting.
TheADDONSsettingisadictinwhicheverykeyisanadd-onclassoritsimportpathandthevalueisitspriority.
Thisisanexamplewheretwoadd-onsareenabledinaproject’ssettings.py:
ADDONS = {
'path.to.someaddon': 0,
SomeAddonClass: 1,
}
6.2.2 Writing your own add-ons
Add-onsarecomponentsthatincludeoneorbothofthefollowingmethods:
6.2. Add-ons 235

ScrapyDocumentation,Release2.13.3
update_settings(settings)
ThismethodiscalledduringtheinitializationoftheCrawler. Here, youshouldperformdependencychecks
(e.g. forexternalPythonlibraries)andupdatetheSettingsobjectaswished,e.g. enablecomponentsforthis
add-onorsetrequiredconfigurationofotherextensions.
Parameters
settings(Settings)–ThesettingsobjectstoringScrapy/componentconfiguration
classmethod update_pre_crawler_settings(cls,settings)
Usethisclassmethodinsteadoftheupdate_settings()methodtoupdatepre-crawlersettingswhosevalue
isusedbeforetheCrawlerobjectiscreated.
Parameters
settings(BaseSettings)–ThesettingsobjectstoringScrapy/componentconfiguration
The settings set by the add-on should use the addon priority (see Populating the settings and scrapy.settings.
BaseSettings.set()):
class MyAddon:
def update_settings(self, settings):
settings.set("DNSCACHE_ENABLED", True, "addon")
Thisallowsuserstooverridethesesettingsintheprojectorspiderconfiguration.
Wheneditingthevalueofasettinginsteadofoverridingitentirely, itisusuallybesttoleaveitspriorityunchanged.
Forexample,wheneditingacomponentprioritydictionary.
If the update_settings method raises scrapy.exceptions.NotConfigured, the add-on will be skipped. This
makesiteasytoenableanadd-ononlywhensomeconditionsaremet.
Fallbacks
Somecomponentsprovidedbyadd-onsneedtofallbackto“default”implementations,e.g. acustomdownloadhandler
needstosendtherequestthatitdoesn’thandleviathedefaultdownloadhandler,orastatscollectorthatincludessome
additionalprocessingbutotherwiseusesthedefaultstatscollector. Andit’spossiblethataprojectneedstouseseveral
customcomponentsofthesametype,e.g. twocustomdownloadhandlersthatsupportdifferentkindsofcustomrequests
andstillneedtousethedefaultdownloadhandlerforotherrequests. Tomakesuchusecaseseasiertoconfigure,we
recommendthatsuchcustomcomponentsshouldbewritteninthefollowingway:
1. Thecustomcomponent(e.g. MyDownloadHandler)shouldn’tinheritfromthedefaultScrapyone(e.g. scrapy.
core.downloader.handlers.http.HTTPDownloadHandler), but instead be able to load the class of the
fallback component from a special setting (e.g. MY_FALLBACK_DOWNLOAD_HANDLER), create an instance of it
anduseit.
2. The add-ons that include these components should read the current value of the default setting (e.g.
DOWNLOAD_HANDLERS) in their update_settings() methods, save that value into the fallback setting
(MY_FALLBACK_DOWNLOAD_HANDLERmentionedearlier)andsetthedefaultsettingtothecomponentprovided
bytheadd-on(e.g. MyDownloadHandler). Ifthefallbacksettingisalreadysetbytheuser,theyshouldn’tchange
it.
3. This way, if there are several add-ons that want to modify the same setting, all of them will fallback to the
componentfromthepreviousoneandthentotheScrapydefault. Theorderofthatdependsonthepriorityorder
intheADDONSsetting.
236 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
6.2.3 Add-on examples
Setsomebasicconfiguration:
from myproject.pipelines import MyPipeline
class MyAddon:
def update_settings(self, settings):
settings.set("DNSCACHE_ENABLED", True, "addon")
settings.remove_from_list("METAREFRESH_IGNORE_TAGS", "noscript")
settings.setdefault_in_component_priority_dict(
"ITEM_PIPELINES", MyPipeline, 200
)
(cid:17) Tip
When editing a component priority dictionary setting, like ITEM_PIPELINES, consider using setting
methods like replace_in_component_priority_dict(), set_in_component_priority_dict() and
setdefault_in_component_priority_dict()toavoidmistakes.
Checkdependencies:
class MyAddon:
def update_settings(self, settings):
try:
import boto
except ImportError:
raise NotConfigured("MyAddon requires the boto library")
...
Accessthecrawlerinstance:
class MyAddon:
def __init__(self, crawler) -> None:
super().__init__()
self.crawler = crawler
@classmethod
def from_crawler(cls, crawler):
return cls(crawler)
def update_settings(self, settings): ...
Useafallbackcomponent:
from scrapy.core.downloader.handlers.http import HTTPDownloadHandler
from scrapy.utils.misc import build_from_crawler
FALLBACK_SETTING = "MY_FALLBACK_DOWNLOAD_HANDLER"
(continuesonnextpage)
6.2. Add-ons 237

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class MyHandler:
lazy = False
def __init__(self, settings, crawler):
dhcls = load_object(settings.get(FALLBACK_SETTING))
self._fallback_handler = build_from_crawler(dhcls, crawler)
def download_request(self, request, spider):
if request.meta.get("my_params"):
# handle the request
...
else:
return self._fallback_handler.download_request(request, spider)
class MyAddon:
def update_settings(self, settings):
if not settings.get(FALLBACK_SETTING):
settings.set(
FALLBACK_SETTING,
settings.getwithbase("DOWNLOAD_HANDLERS")["https"],
"addon",
)
settings["DOWNLOAD_HANDLERS"]["https"] = MyHandler
6.3 Downloader Middleware
ThedownloadermiddlewareisaframeworkofhooksintoScrapy’srequest/responseprocessing. It’salight,low-level
systemforgloballyalteringScrapy’srequestsandresponses.
6.3.1 Activating a downloader middleware
To activate a downloader middleware component, add it to the DOWNLOADER_MIDDLEWARES setting, which is a dict
whosekeysarethemiddlewareclasspathsandtheirvaluesarethemiddlewareorders.
Here’sanexample:
DOWNLOADER_MIDDLEWARES = {
"myproject.middlewares.CustomDownloaderMiddleware": 543,
}
The DOWNLOADER_MIDDLEWARES setting is merged with the DOWNLOADER_MIDDLEWARES_BASE setting defined in
Scrapy(andnotmeanttobeoverridden)andthensortedbyordertogetthefinalsortedlistofenabledmiddlewares:
thefirstmiddlewareistheoneclosertotheengineandthelastistheoneclosertothedownloader. Inotherwords,the
process_request()methodofeachmiddlewarewillbeinvokedinincreasingmiddlewareorder(100,200,300,...)
andtheprocess_response()methodofeachmiddlewarewillbeinvokedindecreasingorder.
TodecidewhichordertoassigntoyourmiddlewareseetheDOWNLOADER_MIDDLEWARES_BASEsettingandpickavalue
according to where you want to insert the middleware. The order does matter because each middleware performs a
differentactionandyourmiddlewarecoulddependonsomeprevious(orsubsequent)middlewarebeingapplied.
Ifyouwanttodisableabuilt-inmiddleware(theonesdefinedinDOWNLOADER_MIDDLEWARES_BASE andenabledby
default) you must define it in your project’s DOWNLOADER_MIDDLEWARES setting and assign None as its value. For
example,ifyouwanttodisabletheuser-agentmiddleware:
238 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
DOWNLOADER_MIDDLEWARES = {
"myproject.middlewares.CustomDownloaderMiddleware": 543,
"scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
}
Finally,keepinmindthatsomemiddlewaresmayneedtobeenabledthroughaparticularsetting. Seeeachmiddleware
documentationformoreinfo.
6.3.2 Writing your own downloader middleware
Eachdownloadermiddlewareisacomponentthatdefinesoneormoreofthesemethods:
class scrapy.downloadermiddlewares.DownloaderMiddleware
(cid:242) Note
Anyofthedownloadermiddlewaremethodsmayalsoreturnadeferred.
process_request(request,spider)
Thismethodiscalledforeachrequestthatgoesthroughthedownloadmiddleware.
process_request()shouldeither: returnNone,returnaResponseobject,returnaRequestobject,or
raiseIgnoreRequest.
If it returns None, Scrapy will continue processing this request, executing all other middlewares until,
finally,theappropriatedownloaderhandleriscalledtherequestperformed(anditsresponsedownloaded).
If it returns a Response object, Scrapy won’t bother calling any other process_request() or
process_exception() methods, or the appropriate download function; it’ll return that response. The
process_response()methodsofinstalledmiddlewareisalwayscalledoneveryresponse.
IfitreturnsaRequestobject,Scrapywillstopcallingprocess_request()methodsandreschedulethe
returnedrequest. Oncethenewlyreturnedrequestisperformed,theappropriatemiddlewarechainwillbe
calledonthedownloadedresponse.
IfitraisesanIgnoreRequest exception,theprocess_exception()methodsofinstalleddownloader
middleware will be called. If none of them handle the exception, the errback function of the request
(Request.errback)iscalled. Ifnocodehandlestheraisedexception,itisignoredandnotlogged(unlike
otherexceptions).
Parameters
• request(Requestobject)–therequestbeingprocessed
• spider(Spiderobject)–thespiderforwhichthisrequestisintended
process_response(request,response,spider)
process_response() should either: return a Response object, return a Request object or raise a
IgnoreRequestexception.
If it returns a Response (it could be the same given response, or a brand-new one), that response will
continuetobeprocessedwiththeprocess_response()ofthenextmiddlewareinthechain.
IfitreturnsaRequestobject,themiddlewarechainishaltedandthereturnedrequestisrescheduledtobe
downloadedinthefuture. Thisisthesamebehaviorasifarequestisreturnedfromprocess_request().
If it raises an IgnoreRequest exception, the errback function of the request (Request.errback) is
called. Ifnocodehandlestheraisedexception,itisignoredandnotlogged(unlikeotherexceptions).
6.3. DownloaderMiddleware 239

ScrapyDocumentation,Release2.13.3
Parameters
• request(isaRequestobject)–therequestthatoriginatedtheresponse
• response(Responseobject)–theresponsebeingprocessed
• spider(Spiderobject)–thespiderforwhichthisresponseisintended
process_exception(request,exception,spider)
Scrapycallsprocess_exception()whenadownloadhandleroraprocess_request()(fromadown-
loadermiddleware)raisesanexception(includinganIgnoreRequestexception)
process_exception()shouldreturn: eitherNone,aResponseobject,oraRequestobject.
If it returns None, Scrapy will continue processing this exception, executing any other
process_exception() methods of installed middleware, until no middleware is left and the de-
faultexceptionhandlingkicksin.
If it returns a Response object, the process_response() method chain of installed middleware is
started,andScrapywon’tbothercallinganyotherprocess_exception()methodsofmiddleware.
IfitreturnsaRequestobject,thereturnedrequestisrescheduledtobedownloadedinthefuture. Thisstops
the execution of process_exception() methods of the middleware the same as returning a response
would.
Parameters
• request(isaRequestobject)–therequestthatgeneratedtheexception
• exception(anExceptionobject)–theraisedexception
• spider(Spiderobject)–thespiderforwhichthisrequestisintended
6.3.3 Built-in downloader middleware reference
This page describes all downloader middleware components that come with Scrapy. For information on how to use
themandhowtowriteyourowndownloadermiddleware,seethedownloadermiddlewareusageguide.
Foralistofthecomponentsenabledbydefault(andtheirorders)seetheDOWNLOADER_MIDDLEWARES_BASE setting.
CookiesMiddleware
class scrapy.downloadermiddlewares.cookies.CookiesMiddleware
Thismiddlewareenablesworkingwithsitesthatrequirecookies,suchasthosethatusesessions. Itkeepstrack
of cookies sent by web servers, and sends them back on subsequent requests (from that spider), just like web
browsersdo.
‡ Caution
When non-UTF8 encoded byte sequences are passed to a Request, the CookiesMiddleware will log a
warning. RefertoAdvancedcustomizationtocustomizetheloggingbehaviour.
‡ Caution
CookiessetviatheCookieheaderarenotconsideredbytheCookiesMiddleware. Ifyouneedtosetcookies
forarequest,usetheRequest.cookiesparameter. Thisisaknowncurrentlimitationthatisbeingworked
on.
240 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
Thefollowingsettingscanbeusedtoconfigurethecookiemiddleware:
• COOKIES_ENABLED
• COOKIES_DEBUG
Multiplecookiesessionsperspider
ThereissupportforkeepingmultiplecookiesessionsperspiderbyusingthecookiejarRequestmetakey. Bydefault
itusesasinglecookiejar(session),butyoucanpassanidentifiertousedifferentones.
Forexample:
for i, url in enumerate(urls):
yield scrapy.Request(url, meta={"cookiejar": i}, callback=self.parse_page)
Keepinmindthatthecookiejarmetakeyisnot“sticky”. Youneedtokeeppassingitalongonsubsequentrequests.
Forexample:
def parse_page(self, response):
# do some processing
return scrapy.Request(
"http://www.example.com/otherpage",
meta={"cookiejar": response.meta["cookiejar"]},
callback=self.parse_other_page,
)
COOKIES_ENABLED
Default: True
Whethertoenablethecookiesmiddleware. Ifdisabled,nocookieswillbesenttowebservers.
NoticethatdespitethevalueofCOOKIES_ENABLED settingif Request.meta['dont_merge_cookies']evaluatesto
TruetherequestcookieswillnotbesenttothewebserverandreceivedcookiesinResponsewillnotbemergedwith
theexistingcookies.
FormoredetailedinformationseethecookiesparameterinRequest.
COOKIES_DEBUG
Default: False
Ifenabled,Scrapywilllogallcookiessentinrequests(i.e. Cookieheader)andallcookiesreceivedinresponses(i.e.
Set-Cookieheader).
Here’sanexampleofalogwithCOOKIES_DEBUG enabled:
2011-04-06 14:35:10-0300 [scrapy.core.engine] INFO: Spider opened
2011-04-06 14:35:10-0300 [scrapy.downloadermiddlewares.cookies] DEBUG: Sending cookies␣
to: <GET http://www.diningcity.com/netherlands/index.html>
˓→
Cookie: clientlanguage_nl=en_EN
2011-04-06 14:35:14-0300 [scrapy.downloadermiddlewares.cookies] DEBUG: Received cookies␣
from: <200 http://www.diningcity.com/netherlands/index.html>
˓→
Set-Cookie: JSESSIONID=B~FA4DC0C496C8762AE4F1A620EAB34F38; Path=/
Set-Cookie: ip_isocode=US
Set-Cookie: clientlanguage_nl=en_EN; Expires=Thu, 07-Apr-2011 21:21:34 GMT;␣
(continuesonnextpage)
6.3. DownloaderMiddleware 241

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
Path=/
˓→
2011-04-06 14:49:50-0300 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://www.
diningcity.com/netherlands/index.html> (referer: None)
˓→
[...]
DefaultHeadersMiddleware
class scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware
ThismiddlewaresetsalldefaultrequestsheadersspecifiedintheDEFAULT_REQUEST_HEADERS setting.
DownloadTimeoutMiddleware
class scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware
This middleware sets the download timeout for requests specified in the DOWNLOAD_TIMEOUT setting or
download_timeoutspiderattribute.
(cid:242) Note
Youcanalsosetdownloadtimeoutper-requestusingdownload_timeoutRequest.metakey;thisissupportedeven
whenDownloadTimeoutMiddlewareisdisabled.
HttpAuthMiddleware
class scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware
ThismiddlewareauthenticatesallrequestsgeneratedfromcertainspidersusingBasicaccessauthentication(aka.
HTTPauth).
ToenableHTTPauthenticationforaspider,setthehttp_userandhttp_passspiderattributestotheauthen-
ticationdataandthehttp_auth_domainspiderattributetothedomainwhichrequiresthisauthentication(its
subdomains will be also handled in the same way). You can set http_auth_domain to None to enable the
authenticationforallrequestsbutyouriskleakingyourauthenticationcredentialstounrelateddomains.
. Warning
InpreviousScrapyversionsHttpAuthMiddlewaresenttheauthenticationdatawithallrequests,whichisase-
curityproblemifthespidermakesrequeststoseveraldifferentdomains. Currentlyifthehttp_auth_domain
attributeisnotset,themiddlewarewillusethedomainofthefirstrequest,whichwillworkforsomespiders
butnotforothers. Inthefuturethemiddlewarewillproduceanerrorinstead.
Example:
from scrapy.spiders import CrawlSpider
class SomeIntranetSiteSpider(CrawlSpider):
http_user = "someuser"
http_pass = "somepass"
http_auth_domain = "intranet.example.com"
name = "intranet.example.com"
# .. rest of the spider code omitted ...
242 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
HttpCacheMiddleware
class scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware
This middleware provides low-level cache to all HTTP requests and responses. It has to be combined with a
cachestoragebackendaswellasacachepolicy.
ScrapyshipswiththefollowingHTTPcachestoragebackends:
• Filesystemstoragebackend(default)
• DBMstoragebackend
YoucanchangetheHTTPcachestoragebackendwiththeHTTPCACHE_STORAGE setting. Oryoucanalsoim-
plementyourownstoragebackend.
ScrapyshipswithtwoHTTPcachepolicies:
• RFC2616policy
• Dummypolicy(default)
YoucanchangetheHTTPcachepolicywiththeHTTPCACHE_POLICY setting. Oryoucanalsoimplementyour
ownpolicy. Youcanalsoavoidcachingaresponseoneverypolicyusingdont_cachemetakeyequalsTrue.
Dummypolicy(default)
class scrapy.extensions.httpcache.DummyPolicy
ThispolicyhasnoawarenessofanyHTTPCache-Controldirectives. Everyrequestanditscorrespondingre-
sponsearecached. Whenthesamerequestisseenagain,theresponseisreturnedwithouttransferringanything
fromtheInternet.
TheDummypolicyisusefulfortestingspidersfaster(withouthavingtowaitfordownloadseverytime)andfor
tryingyourspideroffline,whenanInternetconnectionisnotavailable. Thegoalistobeableto“replay”aspider
runexactlyasitranbefore.
RFC2616policy
class scrapy.extensions.httpcache.RFC2616Policy
This policy provides a RFC2616 compliant HTTP cache, i.e. with HTTP Cache-Control awareness, aimed at
productionandusedincontinuousrunstoavoiddownloadingunmodifieddata(tosavebandwidthandspeedup
crawls).
Whatisimplemented:
• Donotattempttostoreresponses/requestswithno-storecache-controldirectiveset
• Donotserveresponsesfromcacheif no-cachecache-controldirectiveissetevenforfreshresponses
• Computefreshnesslifetimefrommax-agecache-controldirective
• ComputefreshnesslifetimefromExpiresresponseheader
• ComputefreshnesslifetimefromLast-Modifiedresponseheader(heuristicusedbyFirefox)
• ComputecurrentagefromAgeresponseheader
• ComputecurrentagefromDateheader
• RevalidatestaleresponsesbasedonLast-Modifiedresponseheader
• RevalidatestaleresponsesbasedonETagresponseheader
• SetDateheaderforanyreceivedresponsemissingit
6.3. DownloaderMiddleware 243

ScrapyDocumentation,Release2.13.3
• Supportmax-stalecache-controldirectiveinrequests
ThisallowsspiderstobeconfiguredwiththefullRFC2616cachepolicy,butavoidrevalidationonarequest-by-
requestbasis,whileremainingconformantwiththeHTTPspec.
Example:
AddCache-Control: max-stale=600toRequestheaderstoacceptresponsesthathaveexceededtheirex-
pirationtimebynomorethan600seconds.
Seealso: RFC2616,14.9.3
Whatismissing:
• Pragma: no-cachesupporthttps://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.1
• Varyheadersupporthttps://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.6
• Invalidationafterupdatesordeleteshttps://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.10
• ... probablyothers..
Filesystemstoragebackend(default)
class scrapy.extensions.httpcache.FilesystemCacheStorage
FilesystemstoragebackendisavailablefortheHTTPcachemiddleware.
Eachrequest/responsepairisstoredinadifferentdirectorycontainingthefollowingfiles:
• request_body-theplainrequestbody
• request_headers-therequestheaders(inrawHTTPformat)
• response_body-theplainresponsebody
• response_headers-therequestheaders(inrawHTTPformat)
• meta-somemetadataofthiscacheresourceinPythonrepr()format(grep-friendlyformat)
• pickled_meta-thesamemetadatainmetabutpickledformoreefficientdeserialization
The directory name is made from the request fingerprint (see scrapy.utils.request.fingerprint), and
onelevelofsubdirectoriesisusedtoavoidcreatingtoomanyfilesintothesamedirectory(whichisinefficient
inmanyfilesystems). Anexampledirectorycouldbe:
/path/to/cache/dir/example.com/72/72811f648e718090f041317756c03adb0ada46c7
DBMstoragebackend
class scrapy.extensions.httpcache.DbmCacheStorage
ADBMstoragebackendisalsoavailablefortheHTTPcachemiddleware.
Bydefault,itusesthedbm,butyoucanchangeitwiththeHTTPCACHE_DBM_MODULE setting.
Writingyourownstoragebackend
YoucanimplementacachestoragebackendbycreatingaPythonclassthatdefinesthemethodsdescribedbelow.
class scrapy.extensions.httpcache.CacheStorage
244 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
open_spider(spider)
Thismethodgetscalledafteraspiderhasbeenopenedforcrawling. Ithandlestheopen_spidersignal.
Parameters
spider(Spiderobject)–thespiderwhichhasbeenopened
close_spider(spider)
Thismethodgetscalledafteraspiderhasbeenclosed. Ithandlestheclose_spidersignal.
Parameters
spider(Spiderobject)–thespiderwhichhasbeenclosed
retrieve_response(spider,request)
Returnresponseifpresentincache,orNoneotherwise.
Parameters
• spider(Spiderobject)–thespiderwhichgeneratedtherequest
• request(Requestobject)–therequesttofindcachedresponsefor
store_response(spider,request,response)
Storethegivenresponseinthecache.
Parameters
• spider(Spiderobject)–thespiderforwhichtheresponseisintended
• request(Requestobject)–thecorrespondingrequestthespidergenerated
• response(Responseobject)–theresponsetostoreinthecache
Inordertouseyourstoragebackend,set:
• HTTPCACHE_STORAGE tothePythonimportpathofyourcustomstorageclass.
HTTPCachemiddlewaresettings
TheHttpCacheMiddlewarecanbeconfiguredthroughthefollowingsettings:
HTTPCACHE_ENABLED
Default: False
WhethertheHTTPcachewillbeenabled.
HTTPCACHE_EXPIRATION_SECS
Default: 0
Expirationtimeforcachedrequests,inseconds.
Cachedrequestsolderthanthistimewillbere-downloaded. Ifzero,cachedrequestswillneverexpire.
HTTPCACHE_DIR
Default: 'httpcache'
Thedirectorytouseforstoringthe(low-level)HTTPcache. Ifempty,theHTTPcachewillbedisabled. Ifarelative
pathisgiven,istakenrelativetotheprojectdatadir. Formoreinfosee: DefaultstructureofScrapyprojects.
6.3. DownloaderMiddleware 245

ScrapyDocumentation,Release2.13.3
HTTPCACHE_IGNORE_HTTP_CODES
Default: []
Don’tcacheresponsewiththeseHTTPcodes.
HTTPCACHE_IGNORE_MISSING
Default: False
Ifenabled,requestsnotfoundinthecachewillbeignoredinsteadofdownloaded.
HTTPCACHE_IGNORE_SCHEMES
Default: ['file']
Don’tcacheresponseswiththeseURIschemes.
HTTPCACHE_STORAGE
Default: 'scrapy.extensions.httpcache.FilesystemCacheStorage'
Theclasswhichimplementsthecachestoragebackend.
HTTPCACHE_DBM_MODULE
Default: 'dbm'
ThedatabasemoduletouseintheDBMstoragebackend. ThissettingisspecifictotheDBMbackend.
HTTPCACHE_POLICY
Default: 'scrapy.extensions.httpcache.DummyPolicy'
Theclasswhichimplementsthecachepolicy.
HTTPCACHE_GZIP
Default: False
Ifenabled,willcompressallcacheddatawithgzip. ThissettingisspecifictotheFilesystembackend.
HTTPCACHE_ALWAYS_STORE
Default: False
Ifenabled,willcachepagesunconditionally.
Aspidermaywishtohaveallresponsesavailableinthecache,forfutureusewithCache-Control: max-stale,for
instance. TheDummyPolicycachesallresponsesbutneverrevalidatesthem,andsometimesamorenuancedpolicyis
desirable.
ThissettingstillrespectsCache-Control: no-storedirectivesinresponses. Ifyoudon’twantthat,filterno-store
outoftheCache-Controlheadersinresponsesyoufeedtothecachemiddleware.
246 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS
Default: []
ListofCache-Controldirectivesinresponsestobeignored.
Sites often set “no-store”, “no-cache”, “must-revalidate”, etc., but get upset at the traffic a spider can generate if it
actually respects those directives. This allows to selectively ignore Cache-Control directives that are known to be
unimportantforthesitesbeingcrawled.
WeassumethatthespiderwillnotissueCache-Controldirectivesinrequestsunlessitactuallyneedsthem,sodirectives
inrequestsarenotfiltered.
HttpCompressionMiddleware
class scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware
Thismiddlewareallowscompressed(gzip,deflate)traffictobesent/receivedfromwebsites.
Thismiddlewarealsosupportsdecodingbrotli-compressedaswellaszstd-compressedresponses,providedthat
brotliorzstandardisinstalled,respectively.
HttpCompressionMiddlewareSettings
COMPRESSION_ENABLED
Default: True
WhethertheCompressionmiddlewarewillbeenabled.
HttpProxyMiddleware
class scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
ThismiddlewaresetstheHTTPproxytouseforrequests,bysettingtheproxymetavalueforRequestobjects.
LikethePythonstandardlibrarymoduleurllib.request,itobeysthefollowingenvironmentvariables:
• http_proxy
• https_proxy
• no_proxy
You can also set the meta key proxy per-request, to a value like http://some_proxy_server:port or
http://username:password@some_proxy_server:port. Keep in mind this value will take precedence
over http_proxy/https_proxy environment variables, and it will also ignore no_proxy environment vari-
able.
HttpProxyMiddlewaresettings
HTTPPROXY_ENABLED
Default: True
WhetherornottoenabletheHttpProxyMiddleware.
HTTPPROXY_AUTH_ENCODING
Default: "latin-1"
ThedefaultencodingforproxyauthenticationonHttpProxyMiddleware.
6.3. DownloaderMiddleware 247

ScrapyDocumentation,Release2.13.3
OffsiteMiddleware
class scrapy.downloadermiddlewares.offsite.OffsiteMiddleware
Addedinversion2.11.2.
FiltersoutRequestsforURLsoutsidethedomainscoveredbythespider.
Thismiddlewarefiltersouteveryrequestwhosehostnamesaren’tinthespider’sallowed_domainsattribute.
All subdomains of any domain in the list are also allowed. E.g. the rule www.example.org will also allow
bob.www.example.orgbutnotwww2.example.comnorexample.com.
Whenyourspiderreturnsarequestforadomainnotbelongingtothosecoveredbythespider,thismiddleware
willlogadebugmessagesimilartothisone:
DEBUG: Filtered offsite request to 'offsite.example': <GET http://offsite.example/
some/page.html>
˓→
Toavoidfillingthelogwithtoomuchnoise,itwillonlyprintoneofthesemessagesforeachnewdomainfiltered.
So, forexample, ifanotherrequestfor offsite.exampleisfiltered, nologmessagewillbeprinted. Butifa
requestforother.exampleisfiltered,amessagewillbeprinted(butonlyforthefirstrequestfiltered).
If the spider doesn’t define an allowed_domains attribute, or the attribute is empty, the offsite middleware
will allow all requests. If the request has the dont_filter attribute set to True or Request.meta has
allow_offsitesettoTrue,thentheOffsiteMiddlewarewillallowtherequestevenifitsdomainisnotlisted
inalloweddomains.
RedirectMiddleware
class scrapy.downloadermiddlewares.redirect.RedirectMiddleware
Thismiddlewarehandlesredirectionofrequestsbasedonresponsestatus.
Theurlswhichtherequestgoesthrough(whilebeingredirected)canbefoundintheredirect_urlsRequest.meta
key. Thereasonbehindeachredirectinredirect_urls canbefoundintheredirect_reasonsRequest.meta
key. Forexample: [301, 302, 307, 'meta refresh'].
The format of a reason depends on the middleware that handled the corresponding redirect. For example,
RedirectMiddleware indicatesthetriggeringresponsestatuscodeasaninteger,whileMetaRefreshMiddleware
alwaysusesthe'meta refresh'stringasreason.
TheRedirectMiddlewarecanbeconfiguredthroughthefollowingsettings(seethesettingsdocumentationformore
info):
• REDIRECT_ENABLED
• REDIRECT_MAX_TIMES
IfRequest.meta hasdont_redirectkeysettoTrue,therequestwillbeignoredbythismiddleware.
Ifyouwanttohandlesomeredirectstatuscodesinyourspider,youcanspecifytheseinthehandle_httpstatus_list
spiderattribute.
For example, if you want the redirect middleware to ignore 301 and 302 responses (and pass them through to your
spider)youcandothis:
class MySpider(CrawlSpider):
handle_httpstatus_list = [301, 302]
The handle_httpstatus_list key of Request.meta can also be used to specify which response codes to allow
on a per-request basis. You can also set the meta key handle_httpstatus_all to True if you want to allow any
responsecodeforarequest.
248 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
RedirectMiddlewaresettings
REDIRECT_ENABLED
Default: True
WhethertheRedirectmiddlewarewillbeenabled.
REDIRECT_MAX_TIMES
Default: 20
Themaximumnumberofredirectionsthatwillbefollowedforasinglerequest. Ifmaximumredirectionsareexceeded,
therequestisabortedandignored.
MetaRefreshMiddleware
class scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware
Thismiddlewarehandlesredirectionofrequestsbasedonmeta-refreshhtmltag.
TheMetaRefreshMiddlewarecanbeconfiguredthroughthefollowingsettings(seethesettingsdocumentationfor
moreinfo):
• METAREFRESH_ENABLED
• METAREFRESH_IGNORE_TAGS
• METAREFRESH_MAXDELAY
ThismiddlewareobeyREDIRECT_MAX_TIMES setting, dont_redirect, redirect_urls andredirect_reasons
requestmetakeysasdescribedforRedirectMiddleware
MetaRefreshMiddlewaresettings
METAREFRESH_ENABLED
Default: True
WhethertheMetaRefreshmiddlewarewillbeenabled.
METAREFRESH_IGNORE_TAGS
Default: []
Metatagswithinthesetagsareignored.
Changedinversion2.0:ThedefaultvalueofMETAREFRESH_IGNORE_TAGSchangedfrom["script", "noscript"]
to[].
Changedinversion2.11.2: ThedefaultvalueofMETAREFRESH_IGNORE_TAGS changedfrom[]to["noscript"].
METAREFRESH_MAXDELAY
Default: 100
Themaximummeta-refreshdelay(inseconds)tofollowtheredirection. Somesitesusemeta-refreshforredirectingto
asessionexpiredpage,sowerestrictautomaticredirectiontothemaximumdelay.
6.3. DownloaderMiddleware 249

ScrapyDocumentation,Release2.13.3
RetryMiddleware
class scrapy.downloadermiddlewares.retry.RetryMiddleware
A middleware to retry failed requests that are potentially caused by temporary problems such as a connection
timeoutorHTTP500error.
Failedpagesarecollectedonthescrapingprocessandrescheduledattheend,oncethespiderhasfinishedcrawlingall
regular(nonfailed)pages.
The RetryMiddleware can be configured through the following settings (see the settings documentation for more
info):
• RETRY_ENABLED
• RETRY_TIMES
• RETRY_HTTP_CODES
• RETRY_EXCEPTIONS
IfRequest.meta hasdont_retrykeysettoTrue,therequestwillbeignoredbythismiddleware.
Toretryrequestsfromaspidercallback,youcanusetheget_retry_request()function:
scrapy.downloadermiddlewares.retry.get_retry_request(request: Request,*,spider: Spider,reason: str
|Exception|type[Exception]='unspecified',
max_retry_times: int|None=None,
priority_adjust: int|None=None,logger:
Logger=<Logger
scrapy.downloadermiddlewares.retry
(WARNING)>,stats_base_key: str='retry')
→Request|None
ReturnsanewRequestobjecttoretrythespecifiedrequest,orNoneifretriesofthespecifiedrequesthavebeen
exhausted.
Forexample,inaSpidercallback,youcoulduseitasfollows:
def parse(self, response):
if not response.text:
new_request_or_none = get_retry_request(
response.request,
spider=self,
reason='empty',
)
return new_request_or_none
spideristheSpiderinstancewhichisaskingfortheretryrequest. Itisusedtoaccessthesettingsandstats,and
toprovideextraloggingcontext(seelogging.debug()).
reasonisastringoranExceptionobjectthatindicatesthereasonwhytherequestneedstoberetried. Itisused
tonameretrystats.
max_retry_times is a number that determines the maximum number of times that request can be retried.
If not specified or None, the number is read from the max_retry_times meta key of the request. If the
max_retry_timesmetakeyisnotdefinedorNone,thenumberisreadfromtheRETRY_TIMES setting.
priority_adjustisanumberthatdetermineshowthepriorityofthenewrequestchangesinrelationtorequest. If
notspecified,thenumberisreadfromtheRETRY_PRIORITY_ADJUST setting.
loggeristhelogging.Loggerobjecttobeusedwhenloggingmessages
stats_base_keyisastringtobeusedasthebasekeyfortheretry-relatedjobstats
250 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
RetryMiddlewareSettings
RETRY_ENABLED
Default: True
WhethertheRetrymiddlewarewillbeenabled.
RETRY_TIMES
Default: 2
Maximumnumberoftimestoretry,inadditiontothefirstdownload.
Maximumnumberofretriescanalsobespecifiedper-requestusingmax_retry_times attributeofRequest.meta.
Wheninitialized,themax_retry_timesmetakeytakeshigherprecedenceovertheRETRY_TIMES setting.
RETRY_HTTP_CODES
Default: [500, 502, 503, 504, 522, 524, 408, 429]
WhichHTTPresponsecodestoretry. Othererrors(DNSlookupissues,connectionslost,etc)arealwaysretried.
Insomecasesyoumaywanttoadd400toRETRY_HTTP_CODES becauseitisacommoncodeusedtoindicateserver
overload. ItisnotincludedbydefaultbecauseHTTPspecssayso.
RETRY_EXCEPTIONS
Default:
[
'twisted.internet.defer.TimeoutError',
'twisted.internet.error.TimeoutError',
'twisted.internet.error.DNSLookupError',
'twisted.internet.error.ConnectionRefusedError',
'twisted.internet.error.ConnectionDone',
'twisted.internet.error.ConnectError',
'twisted.internet.error.ConnectionLost',
'twisted.internet.error.TCPTimedOutError',
'twisted.web.client.ResponseFailed',
IOError,
'scrapy.core.downloader.handlers.http11.TunnelError',
]
Listofexceptionstoretry.
Eachlistentrymaybeanexceptiontypeoritsimportpathasastring.
AnexceptionwillnotbecaughtwhentheexceptiontypeisnotinRETRY_EXCEPTIONSorwhenthemaximumnumber
of retries for a request has been exceeded (see RETRY_TIMES). To learn about uncaught exception propagation, see
process_exception().
RETRY_PRIORITY_ADJUST
Default: -1
Adjustretryrequestpriorityrelativetooriginalrequest:
• apositivepriorityadjustmeanshigherpriority.
6.3. DownloaderMiddleware 251

ScrapyDocumentation,Release2.13.3
• anegativepriorityadjust(default)meanslowerpriority.
RobotsTxtMiddleware
class scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware
Thismiddlewarefiltersoutrequestsforbiddenbytherobots.txtexclusionstandard.
TomakesureScrapyrespectsrobots.txtmakesurethemiddlewareisenabledandtheROBOTSTXT_OBEY setting
isenabled.
The ROBOTSTXT_USER_AGENT setting can be used to specify the user agent string to use for matching in the
robots.txtfile. IfitisNone,theUser-AgentheaderyouaresendingwiththerequestortheUSER_AGENT setting
(inthatorder)willbeusedfordeterminingtheuseragenttouseintherobots.txtfile.
Thismiddlewarehastobecombinedwitharobots.txtparser.
Scrapyshipswithsupportforthefollowingrobots.txtparsers:
• Protego(default)
• RobotFileParser
• Robotexclusionrulesparser
Youcanchangetherobots.txtparserwiththeROBOTSTXT_PARSER setting. Oryoucanalsoimplementsupport
foranewparser.
IfRequest.meta hasdont_obey_robotstxtkeysettoTruetherequestwillbeignoredbythismiddlewareevenif
ROBOTSTXT_OBEY isenabled.
Parsersvaryinseveralaspects:
• Languageofimplementation
• Supportedspecification
• Supportforwildcardmatching
• Usageoflengthbasedrule: inparticularforAllowandDisallowdirectives,wherethemostspecificrulebased
onthelengthofthepathtrumpsthelessspecific(shorter)rule
Performancecomparisonofdifferentparsersisavailableatthefollowinglink.
Protegoparser
BasedonProtego:
• implementedinPython
• iscompliantwithGoogle’sRobots.txtSpecification
• supportswildcardmatching
• usesthelengthbasedrule
Scrapyusesthisparserbydefault.
RobotFileParser
BasedonRobotFileParser:
• isPython’sbuilt-inrobots.txtparser
• iscompliantwithMartijnKoster’s1996draftspecification
• lackssupportforwildcardmatching
252 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
• doesn’tusethelengthbasedrule
ItisfasterthanProtegoandbackward-compatiblewithversionsofScrapybefore1.8.0.
Inordertousethisparser,set:
• ROBOTSTXT_PARSER toscrapy.robotstxt.PythonRobotParser
Robotexclusionrulesparser
BasedonRobotexclusionrulesparser:
• implementedinPython
• iscompliantwithMartijnKoster’s1996draftspecification
• supportswildcardmatching
• doesn’tusethelengthbasedrule
Inordertousethisparser:
• InstallRobotexclusionrulesparserbyrunningpip install robotexclusionrulesparser
• SetROBOTSTXT_PARSER settingtoscrapy.robotstxt.RerpRobotParser
Implementingsupportforanewparser
Youcanimplementsupportforanewrobots.txtparserbysubclassingtheabstractbaseclassRobotParser andim-
plementingthemethodsdescribedbelow.
class scrapy.robotstxt.RobotParser
abstract allowed(url: str|bytes,user_agent: str|bytes)→bool
ReturnTrueif user_agentisallowedtocrawlurl,otherwisereturnFalse.
Parameters
• url(str or bytes)–AbsoluteURL
• user_agent(str or bytes)–Useragent
abstract classmethod from_crawler(crawler: Crawler,robotstxt_body: bytes)→Self
Parsethecontentofarobots.txtfileasbytes. Thismustbeaclassmethod. Itmustreturnanewinstance
oftheparserbackend.
Parameters
• crawler(Crawlerinstance)–crawlerwhichmadetherequest
• robotstxt_body(bytes)–contentofarobots.txtfile.
DownloaderStats
class scrapy.downloadermiddlewares.stats.DownloaderStats
Middlewarethatstoresstatsofallrequests,responsesandexceptionsthatpassthroughit.
TousethismiddlewareyoumustenabletheDOWNLOADER_STATS setting.
6.3. DownloaderMiddleware 253

ScrapyDocumentation,Release2.13.3
UserAgentMiddleware
class scrapy.downloadermiddlewares.useragent.UserAgentMiddleware
Middlewarethatallowsspiderstooverridethedefaultuseragent.
Inorderforaspidertooverridethedefaultuseragent,itsuser_agentattributemustbeset.
6.4 Spider Middleware
ThespidermiddlewareisaframeworkofhooksintoScrapy’sspiderprocessingmechanismwhereyoucanplugcustom
functionalitytoprocesstheresponsesthataresenttoSpidersforprocessingandtoprocesstherequestsanditemsthat
aregeneratedfromspiders.
6.4.1 Activating a spider middleware
Toactivateaspidermiddlewarecomponent,addittotheSPIDER_MIDDLEWARES setting,whichisadictwhosekeys
arethemiddlewareclasspathandtheirvaluesarethemiddlewareorders.
Here’sanexample:
SPIDER_MIDDLEWARES = {
"myproject.middlewares.CustomSpiderMiddleware": 543,
}
TheSPIDER_MIDDLEWARES settingismergedwiththeSPIDER_MIDDLEWARES_BASE settingdefinedinScrapy(and
not meant to be overridden) and then sorted by order to get the final sorted list of enabled middlewares: the
first middleware is the one closer to the engine and the last is the one closer to the spider. In other words, the
process_spider_input() method of each middleware will be invoked in increasing middleware order (100, 200,
300,...),andtheprocess_spider_output()methodofeachmiddlewarewillbeinvokedindecreasingorder.
To decide which order to assign to your middleware see the SPIDER_MIDDLEWARES_BASE setting and pick a value
according to where you want to insert the middleware. The order does matter because each middleware performs a
differentactionandyourmiddlewarecoulddependonsomeprevious(orsubsequent)middlewarebeingapplied.
Ifyouwanttodisableabuiltinmiddleware(theonesdefinedinSPIDER_MIDDLEWARES_BASE,andenabledbydefault)
you must define it in your project SPIDER_MIDDLEWARES setting and assign None as its value. For example, if you
wanttodisabletheoff-sitemiddleware:
SPIDER_MIDDLEWARES = {
"scrapy.spidermiddlewares.referer.RefererMiddleware": None,
"myproject.middlewares.CustomRefererSpiderMiddleware": 700,
}
Finally,keepinmindthatsomemiddlewaresmayneedtobeenabledthroughaparticularsetting. Seeeachmiddleware
documentationformoreinfo.
6.4.2 Writing your own spider middleware
Eachspidermiddlewareisacomponentthatdefinesoneormoreofthesemethods:
class scrapy.spidermiddlewares.SpiderMiddleware
async process_start(start: AsyncIterator[Any],/)→AsyncIterator[Any]
Iterateovertheoutputofstart()orthatoftheprocess_start()methodofanearlierspidermiddle-
ware,overridingit. Forexample:
254 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
async def process_start(self, start):
async for item_or_request in start:
yield item_or_request
Youmayyieldthesametypeofobjectsasstart().
To write spider middlewares that work on Scrapy versions lower than 2.13, define also a synchronous
process_start_requests()methodthatreturnsaniterable. Forexample:
def process_start_requests(self, start, spider):
yield from start
process_spider_input(response,spider)
Thismethodiscalledforeachresponsethatgoesthroughthespidermiddlewareandintothespider,for
processing.
process_spider_input()shouldreturnNoneorraiseanexception.
If it returns None, Scrapy will continue processing this response, executing all other middlewares until,
finally,theresponseishandedtothespiderforprocessing.
If it raises an exception, Scrapy won’t bother calling any other spider middleware
process_spider_input() and will call the request errback if there is one, otherwise it will start
the process_spider_exception() chain. The output of the errback is chained back in the other
directionforprocess_spider_output()toprocessit,orprocess_spider_exception()ifitraised
anexception.
Parameters
• response(Responseobject)–theresponsebeingprocessed
• spider(Spiderobject)–thespiderforwhichthisresponseisintended
process_spider_output(response,result,spider)
ThismethodiscalledwiththeresultsreturnedfromtheSpider,afterithasprocessedtheresponse.
process_spider_output()mustreturnaniterableofRequestobjectsanditemobjects.
Changedinversion2.7: Thismethodmaybedefinedasanasynchronousgenerator,inwhichcaseresult
isanasynchronousiterable.
Consider defining this method as an asynchronous generator, which will be a requirement in a future
version of Scrapy. However, if you plan on sharing your spider middleware with other people, consider
eitherenforcingScrapy2.7 asaminimumrequirementofyourspidermiddleware,ormakingyourspider
middlewareuniversalsothatitworkswithScrapyversionsearlierthanScrapy2.7.
Parameters
• response (Response object) – the response which generated this output from the
spider
• result(aniterableofRequestobjectsanditemobjects)–theresultreturnedbythe
spider
• spider(Spiderobject)–thespiderwhoseresultisbeingprocessed
async process_spider_output_async(response,result,spider)
Addedinversion2.7.
If defined, this method must be an asynchronous generator, which will be called instead of
process_spider_output()if resultisanasynchronousiterable.
6.4. SpiderMiddleware 255

ScrapyDocumentation,Release2.13.3
process_spider_exception(response,exception,spider)
This method is called when a spider or process_spider_output() method (from a previous spider
middleware)raisesanexception.
process_spider_exception()shouldreturneitherNoneoraniterableofRequestoritemobjects.
If it returns None, Scrapy will continue processing this exception, executing any other
process_spider_exception() in the following middleware components, until no middleware
componentsareleftandtheexceptionreachestheengine(whereit’sloggedanddiscarded).
Ifitreturnsaniterabletheprocess_spider_output()pipelinekicksin,startingfromthenextspider
middleware,andnootherprocess_spider_exception()willbecalled.
Parameters
• response(Responseobject)–theresponsebeingprocessedwhentheexceptionwas
raised
• exception(Exceptionobject)–theexceptionraised
• spider(Spiderobject)–thespiderwhichraisedtheexception
Baseclassforcustomspidermiddlewares
Scrapyprovidesabaseclassforcustomspidermiddlewares. It’snotrequiredtouseitbutitcanhelpwithsimplifying
middlewareimplementationsandreducingtheamountofboilerplatecodeinuniversalmiddlewares.
class scrapy.spidermiddlewares.base.BaseSpiderMiddleware(crawler: Crawler)
Optionalbaseclassforspidermiddlewares.
Addedinversion2.13.
This class provides helper methods for asynchronous process_spider_output() and process_start()
methods. Middlewaresthatdon’thaveeitherofthesemethodsdon’tneedtousethisclass.
You can override the get_processed_request() method to add processing code for requests and the
get_processed_item() method to add processing code for items. These methods take a single request or
itemfromthespideroutputiterableandreturnarequestoritem(thesameoranewone),orNonetoremovethis
requestoritemfromtheprocessing.
get_processed_item(item: Any,response: Response|None)→Any
Returnaprocesseditemfromthespideroutput.
Thismethodiscalledwithasingleitemfromthestartseedsorthespideroutput. Itshouldreturnthesame
oradifferentitem,orNonetoignoreit.
Parameters
• item(item object)–theinputitem
• response(ResponseobjectorNoneforstartseeds)–theresponsebeingprocessed
Returns
theprocesseditemorNone
get_processed_request(request: Request,response: Response|None)→Request|None
Returnaprocessedrequestfromthespideroutput.
Thismethodiscalledwithasinglerequestfromthestartseedsorthespideroutput. Itshouldreturnthe
sameoradifferentrequest,orNonetoignoreit.
Parameters
• request(Requestobject)–theinputrequest
256 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
• response(ResponseobjectorNoneforstartseeds)–theresponsebeingprocessed
Returns
theprocessedrequestorNone
6.4.3 Built-in spider middleware reference
ThispagedescribesallspidermiddlewarecomponentsthatcomewithScrapy. Forinformationonhowtousethemand
howtowriteyourownspidermiddleware,seethespidermiddlewareusageguide.
Foralistofthecomponentsenabledbydefault(andtheirorders)seetheSPIDER_MIDDLEWARES_BASE setting.
DepthMiddleware
class scrapy.spidermiddlewares.depth.DepthMiddleware
DepthMiddlewareisusedfortrackingthedepthofeachRequestinsidethesitebeingscraped. Itworksbysetting
request.meta['depth'] = 0 whenever there is no value previously set (usually just the first Request) and
incrementingitby1otherwise.
Itcanbeusedtolimitthemaximumdepthtoscrape,controlRequestprioritybasedontheirdepth,andthings
likethat.
The DepthMiddleware can be configured through the following settings (see the settings documentation for
moreinfo):
• DEPTH_LIMIT -Themaximumdepththatwillbeallowedtocrawlforanysite. Ifzero, nolimitwillbe
imposed.
• DEPTH_STATS_VERBOSE -Whethertocollectthenumberofrequestsforeachdepth.
• DEPTH_PRIORITY -Whethertoprioritizetherequestsbasedontheirdepth.
HttpErrorMiddleware
class scrapy.spidermiddlewares.httperror.HttpErrorMiddleware
Filteroutunsuccessful(erroneous)HTTPresponsessothatspidersdon’thavetodealwiththem,which(mostof
thetime)imposesanoverhead,consumesmoreresources,andmakesthespiderlogicmorecomplex.
AccordingtotheHTTPstandard,successfulresponsesarethosewhosestatuscodesareinthe200-300range.
Ifyoustillwanttoprocessresponsecodesoutsidethatrange,youcanspecifywhichresponsecodesthespiderisable
tohandleusingthehandle_httpstatus_listspiderattributeorHTTPERROR_ALLOWED_CODES setting.
Forexample,ifyouwantyourspidertohandle404responsesyoucandothis:
from scrapy.spiders import CrawlSpider
class MySpider(CrawlSpider):
handle_httpstatus_list = [404]
The handle_httpstatus_list key of Request.meta can also be used to specify which response codes to allow
on a per-request basis. You can also set the meta key handle_httpstatus_all to True if you want to allow any
responsecodeforarequest,andFalsetodisabletheeffectsofthehandle_httpstatus_allkey.
Keepinmind,however,thatit’susuallyabadideatohandlenon-200responses,unlessyoureallyknowwhatyou’re
doing.
Formoreinformationsee: HTTPStatusCodeDefinitions.
6.4. SpiderMiddleware 257

ScrapyDocumentation,Release2.13.3
HttpErrorMiddlewaresettings
HTTPERROR_ALLOWED_CODES
Default: []
Passallresponseswithnon-200statuscodescontainedinthislist.
HTTPERROR_ALLOW_ALL
Default: False
Passallresponses,regardlessofitsstatuscode.
RefererMiddleware
class scrapy.spidermiddlewares.referer.RefererMiddleware
PopulatesRequestRefererheader,basedontheURLoftheResponsewhichgeneratedit.
RefererMiddlewaresettings
REFERER_ENABLED
Default: True
Whethertoenablereferermiddleware.
REFERRER_POLICY
Default:'scrapy.spidermiddlewares.referer.DefaultReferrerPolicy' ReferrerPolicytoapplywhenpop-
ulatingRequest“Referer”header.
(cid:242) Note
YoucanalsosettheReferrerPolicyperrequest, usingthespecial "referrer_policy"Request.meta key, with
thesameacceptablevaluesasfortheREFERRER_POLICYsetting.
AcceptablevaluesforREFERRER_POLICY
• eitherapathtoa scrapy.spidermiddlewares.referer.ReferrerPolicysubclass—acustompolicyor
oneofthebuilt-inones(seeclassesbelow),
• oroneormorecomma-separatedstandardW3C-definedstringvalues,
• orthespecial"scrapy-default".
258 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
Stringvalue Classname(asastring)
"scrapy-default"(default) scrapy.spidermiddlewares.referer.DefaultReferrerPolicy
“no-referrer” scrapy.spidermiddlewares.referer.NoReferrerPolicy
“no-referrer-when- scrapy.spidermiddlewares.referer.NoReferrerWhenDowngradePolicy
downgrade”
“same-origin” scrapy.spidermiddlewares.referer.SameOriginPolicy
“origin” scrapy.spidermiddlewares.referer.OriginPolicy
“strict-origin” scrapy.spidermiddlewares.referer.StrictOriginPolicy
“origin-when-cross-origin” scrapy.spidermiddlewares.referer.OriginWhenCrossOriginPolicy
“strict-origin-when-cross- scrapy.spidermiddlewares.referer.StrictOriginWhenCrossOriginPolicy
origin”
“unsafe-url” scrapy.spidermiddlewares.referer.UnsafeUrlPolicy
class scrapy.spidermiddlewares.referer.DefaultReferrerPolicy
Avariantof“no-referrer-when-downgrade”,withtheadditionthat“Referer”isnotsentiftheparentrequestwas
usingfile:// ors3:// scheme.
. Warning
Scrapy’s default referrer policy — just like “no-referrer-when-downgrade”, the W3C-recommended value for
browsers—willsendanon-empty“Referer”headerfromany http(s):// toany https:// URL,evenifthe
domainisdifferent.
“same-origin”maybeabetterchoiceifyouwanttoremovereferrerinformationforcross-domainrequests.
class scrapy.spidermiddlewares.referer.NoReferrerPolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-no-referrer
Thesimplestpolicyis“no-referrer”,whichspecifiesthatnoreferrerinformationistobesentalongwithrequests
madefromaparticularrequestclienttoanyorigin. Theheaderwillbeomittedentirely.
class scrapy.spidermiddlewares.referer.NoReferrerWhenDowngradePolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-no-referrer-when-downgrade
The“no-referrer-when-downgrade”policysendsafullURLalongwithrequestsfromaTLS-protectedenviron-
mentsettingsobjecttoapotentiallytrustworthyURL,andrequestsfromclientswhicharenotTLS-protectedto
anyorigin.
Requests from TLS-protected clients to non-potentially trustworthy URLs, on the other hand, will contain no
referrerinformation. ARefererHTTPheaderwillnotbesent.
Thisisauseragent’sdefaultbehavior,ifnopolicyisotherwisespecified.
(cid:242) Note
“no-referrer-when-downgrade”policyistheW3C-recommendeddefault,andisusedbymajorwebbrowsers.
However,itisNOTScrapy’sdefaultreferrerpolicy(seeDefaultReferrerPolicy).
class scrapy.spidermiddlewares.referer.SameOriginPolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-same-origin
6.4. SpiderMiddleware 259

ScrapyDocumentation,Release2.13.3
The“same-origin”policyspecifiesthatafullURL,strippedforuseasareferrer,issentasreferrerinformation
whenmakingsame-originrequestsfromaparticularrequestclient.
Cross-originrequests,ontheotherhand,willcontainnoreferrerinformation. ARefererHTTPheaderwillnot
besent.
class scrapy.spidermiddlewares.referer.OriginPolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-origin
The“origin”policyspecifiesthatonlytheASCIIserializationoftheoriginoftherequestclientissentasreferrer
informationwhenmakingbothsame-originrequestsandcross-originrequestsfromaparticularrequestclient.
class scrapy.spidermiddlewares.referer.StrictOriginPolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-strict-origin
The“strict-origin”policysendstheASCIIserializationoftheoriginoftherequestclientwhenmakingrequests:
- from a TLS-protected environment settings object to a potentially trustworthy URL, and - from non-TLS-
protectedenvironmentsettingsobjectstoanyorigin.
RequestsfromTLS-protectedrequestclientstonon-potentiallytrustworthyURLs,ontheotherhand,willcontain
noreferrerinformation. ARefererHTTPheaderwillnotbesent.
class scrapy.spidermiddlewares.referer.OriginWhenCrossOriginPolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-origin-when-cross-origin
The“origin-when-cross-origin”policyspecifiesthatafullURL,strippedforuseasareferrer,issentasreferrer
information when making same-origin requests from a particular request client, and only the ASCII serializa-
tionoftheoriginoftherequestclientissentasreferrerinformationwhenmakingcross-originrequestsfroma
particularrequestclient.
class scrapy.spidermiddlewares.referer.StrictOriginWhenCrossOriginPolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-strict-origin-when-cross-origin
The “strict-origin-when-cross-origin” policy specifies that a full URL, stripped for use as a referrer, is sent as
referrer information when making same-origin requests from a particular request client, and only the ASCII
serializationoftheoriginoftherequestclientwhenmakingcross-originrequests:
• fromaTLS-protectedenvironmentsettingsobjecttoapotentiallytrustworthyURL,and
• fromnon-TLS-protectedenvironmentsettingsobjectstoanyorigin.
RequestsfromTLS-protectedclientstonon-potentiallytrustworthyURLs, ontheotherhand, willcontainno
referrerinformation. ARefererHTTPheaderwillnotbesent.
class scrapy.spidermiddlewares.referer.UnsafeUrlPolicy
https://www.w3.org/TR/referrer-policy/#referrer-policy-unsafe-url
The“unsafe-url”policyspecifiesthatafullURL,strippedforuseasareferrer,issentalongwithbothcross-origin
requestsandsame-originrequestsmadefromaparticularrequestclient.
Note: The policy’s name doesn’t lie; it is unsafe. This policy will leak origins and paths from TLS-protected
resources to insecure origins. Carefully consider the impact of setting such a policy for potentially sensitive
documents.
. Warning
“unsafe-url”policyisNOTrecommended.
260 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
StartSpiderMiddleware
class scrapy.spidermiddlewares.start.StartSpiderMiddleware(crawler: Crawler)
Setis_start_request.
is_start_request
metakeythatissettoTrueinstartrequests,allowingyoutotellstartrequestsapartfromotherrequests,e.g. in
downloadermiddlewares.
UrlLengthMiddleware
class scrapy.spidermiddlewares.urllength.UrlLengthMiddleware
FiltersoutrequestswithURLslongerthanURLLENGTH_LIMIT
TheUrlLengthMiddlewarecanbeconfiguredthroughthefollowingsettings(seethesettingsdocumentation
formoreinfo):
• URLLENGTH_LIMIT -ThemaximumURLlengthtoallowforcrawledURLs.
6.5 Extensions
ExtensionsarecomponentsthatallowinsertingyourowncustomfunctionalityintoScrapy.
Unlikeothercomponents,extensionsdonothaveaspecificroleinScrapy. Theyare“wildcard”componentsthatcan
beusedforanythingthatdoesnotfittheroleofanyothertypeofcomponent.
6.5.1 Loading and activating extensions
Extensionsareloadedatstartupbycreatingasingleinstanceoftheextensionclassperspiderbeingrun.
Toenableanextension,addittotheEXTENSIONS setting. Forexample:
EXTENSIONS = {
"scrapy.extensions.corestats.CoreStats": 500,
"scrapy.extensions.telnet.TelnetConsole": 500,
}
EXTENSIONSismergedwithEXTENSIONS_BASE(notmeanttobeoverridden),andtheprioritiesintheresultingvalue
determinetheloadingorder.
Asextensionstypicallydonotdependoneachother, theirloadingorderisirrelevantinmostcases. Thisiswhythe
EXTENSIONS_BASE setting defines all extensions with the same order (0). However, you may need to carefully use
prioritiesifyouaddanextensionthatdependsonotherextensionsbeingalreadyloaded.
6.5.2 Writing your own extension
Eachextensionisacomponent.
Typically,extensionsconnecttosignalsandperformtaskstriggeredbythem.
Sampleextension
Herewewillimplementasimpleextensiontoillustratetheconceptsdescribedintheprevioussection. Thisextension
willlogamessageeverytime:
• aspiderisopened
6.5. Extensions 261

ScrapyDocumentation,Release2.13.3
• aspiderisclosed
• aspecificnumberofitemsarescraped
TheextensionwillbeenabledthroughtheMYEXT_ENABLEDsettingandthenumberofitemswillbespecifiedthrough
theMYEXT_ITEMCOUNTsetting.
Hereisthecodeofsuchextension:
import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured
logger = logging.getLogger(__name__)
class SpiderOpenCloseLogging:
def __init__(self, item_count):
self.item_count = item_count
self.items_scraped = 0
@classmethod
def from_crawler(cls, crawler):
# first check if the extension should be enabled and raise
# NotConfigured otherwise
if not crawler.settings.getbool("MYEXT_ENABLED"):
raise NotConfigured
# get the number of items from settings
item_count = crawler.settings.getint("MYEXT_ITEMCOUNT", 1000)
# instantiate the extension object
ext = cls(item_count)
# connect the extension object to signals
crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)
# return the extension object
return ext
def spider_opened(self, spider):
logger.info("opened spider %s", spider.name)
def spider_closed(self, spider):
logger.info("closed spider %s", spider.name)
def item_scraped(self, item, spider):
self.items_scraped += 1
if self.items_scraped % self.item_count == 0:
logger.info("scraped %d items", self.items_scraped)
262 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
6.5.3 Built-in extensions reference
Generalpurposeextensions
LogStatsextension
class scrapy.extensions.logstats.LogStats
Logbasicstatslikecrawledpagesandscrapeditems.
CoreStatsextension
class scrapy.extensions.corestats.CoreStats
Enablethecollectionofcorestatistics,providedthestatscollectionisenabled(seeStatsCollection).
Telnetconsoleextension
class scrapy.extensions.telnet.TelnetConsole
ProvidesatelnetconsoleforgettingintoaPythoninterpreterinsidethecurrentlyrunningScrapyprocess,whichcan
beveryusefulfordebugging.
The telnet console must be enabled by the TELNETCONSOLE_ENABLED setting, and the server will listen in the port
specifiedinTELNETCONSOLE_PORT.
Memoryusageextension
class scrapy.extensions.memusage.MemoryUsage
(cid:242) Note
ThisextensiondoesnotworkinWindows.
MonitorsthememoryusedbytheScrapyprocessthatrunsthespiderand:
1. sendsanotificatione-mailwhenitexceedsacertainvalue
2. closesthespiderwhenitexceedsacertainvalue
Thenotificatione-mailscanbetriggeredwhenacertainwarningvalueisreached(MEMUSAGE_WARNING_MB)andwhen
themaximumvalueisreached(MEMUSAGE_LIMIT_MB)whichwillalsocausethespidertobeclosedandtheScrapy
processtobeterminated.
ThisextensionisenabledbytheMEMUSAGE_ENABLED settingandcanbeconfiguredwiththefollowingsettings:
• MEMUSAGE_LIMIT_MB
• MEMUSAGE_WARNING_MB
• MEMUSAGE_NOTIFY_MAIL
• MEMUSAGE_CHECK_INTERVAL_SECONDS
Memorydebuggerextension
6.5. Extensions 263

ScrapyDocumentation,Release2.13.3
class scrapy.extensions.memdebug.MemoryDebugger
Anextensionfordebuggingmemoryusage. Itcollectsinformationabout:
• objectsuncollectedbythePythongarbagecollector
• objectsleftalivethatshouldn’t. Formoreinfo,seeDebuggingmemoryleakswithtrackref
Toenablethisextension,turnontheMEMDEBUG_ENABLED setting. Theinfowillbestoredinthestats.
Spiderstateextension
class scrapy.extensions.spiderstate.SpiderState
Managesspiderstatedatabyloadingitbeforeacrawlandsavingitafter.
GiveavaluetotheJOBDIR settingtoenablethisextension. Whenenabled,thisextensionmanagesthestateattribute
ofyourSpiderinstance:
• Whenyourspidercloses(spider_closed),thecontentsofitsstateattributeareserializedintoafilenamed
spider.stateintheJOBDIR folder.
• Whenyourspideropens(spider_opened),ifapreviously-generatedspider.statefileexistsintheJOBDIR
folder,itisloadedintothestateattribute.
Foranexample,seeKeepingpersistentstatebetweenbatches.
Closespiderextension
class scrapy.extensions.closespider.CloseSpider
Closesaspiderautomaticallywhensomeconditionsaremet,usingaspecificclosingreasonforeachcondition.
Theconditionsforclosingaspidercanbeconfiguredthroughthefollowingsettings:
• CLOSESPIDER_TIMEOUT
• CLOSESPIDER_TIMEOUT_NO_ITEM
• CLOSESPIDER_ITEMCOUNT
• CLOSESPIDER_PAGECOUNT
• CLOSESPIDER_ERRORCOUNT
(cid:242) Note
When a certain closing condition is met, requests which are currently in the downloader queue (up to
CONCURRENT_REQUESTS requests)arestillprocessed.
CLOSESPIDER_TIMEOUT
Default: 0
Anintegerwhichspecifiesanumberofseconds. Ifthespiderremainsopenformorethanthatnumberofsecond, it
willbeautomaticallyclosedwiththereasonclosespider_timeout. Ifzero(ornonset),spiderswon’tbeclosedby
timeout.
264 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
CLOSESPIDER_TIMEOUT_NO_ITEM
Default: 0
Anintegerwhichspecifiesanumberofseconds. Ifthespiderhasnotproducedanyitemsinthelastnumberofseconds,
it will be closed with the reason closespider_timeout_no_item. If zero (or non set), spiders won’t be closed
regardlessifithasn’tproducedanyitems.
CLOSESPIDER_ITEMCOUNT
Default: 0
Anintegerwhichspecifiesanumberofitems. Ifthespiderscrapesmorethanthatamountandthoseitemsarepassed
bytheitempipeline,thespiderwillbeclosedwiththereasonclosespider_itemcount. Ifzero(ornonset),spiders
won’tbeclosedbynumberofpasseditems.
CLOSESPIDER_PAGECOUNT
Default: 0
Anintegerwhichspecifiesthemaximumnumberofresponsestocrawl. Ifthespidercrawlsmorethanthat,thespider
willbeclosedwiththereasonclosespider_pagecount. Ifzero(ornonset),spiderswon’tbeclosedbynumberof
crawledresponses.
CLOSESPIDER_PAGECOUNT_NO_ITEM
Default: 0
Anintegerwhichspecifiesthemaximumnumberofconsecutiveresponsestocrawlwithoutitemsscraped. Ifthespider
crawlsmoreconsecutiveresponsesthanthatandnoitemsarescrapedinthemeantime,thespiderwillbeclosedwith
thereason closespider_pagecount_no_item. Ifzero(ornotset), spiderswon’tbeclosedbynumberofcrawled
responseswithnoitems.
CLOSESPIDER_ERRORCOUNT
Default: 0
Anintegerwhichspecifiesthemaximumnumberoferrorstoreceivebeforeclosingthespider. Ifthespidergenerates
morethanthatnumberoferrors, itwillbeclosedwiththereason closespider_errorcount. Ifzero(ornonset),
spiderswon’tbeclosedbynumberoferrors.
StatsMailerextension
class scrapy.extensions.statsmailer.StatsMailer
Thissimpleextensioncanbeusedtosendanotificatione-maileverytimeadomainhasfinishedscraping,including
theScrapystatscollected. TheemailwillbesenttoallrecipientsspecifiedintheSTATSMAILER_RCPTS setting.
EmailscanbesentusingtheMailSenderclass. Toseeafulllistofparameters,includingexamplesonhowtoinstantiate
MailSenderandusemailsettings,seeSendinge-mail.
Periodiclogextension
class scrapy.extensions.periodic_log.PeriodicLog
ThisextensionperiodicallylogsrichstatdataasaJSONobject:
6.5. Extensions 265

ScrapyDocumentation,Release2.13.3
2023-08-04 02:30:57 [scrapy.extensions.logstats] INFO: Crawled 976 pages (at 162 pages/
min), scraped 925 items (at 161 items/min)
˓→
2023-08-04 02:30:57 [scrapy.extensions.periodic_log] INFO: {
"delta": {
"downloader/request_bytes": 55582,
"downloader/request_count": 162,
"downloader/request_method_count/GET": 162,
"downloader/response_bytes": 618133,
"downloader/response_count": 162,
"downloader/response_status_count/200": 162,
"item_scraped_count": 161
},
"stats": {
"downloader/request_bytes": 338243,
"downloader/request_count": 992,
"downloader/request_method_count/GET": 992,
"downloader/response_bytes": 3836736,
"downloader/response_count": 976,
"downloader/response_status_count/200": 976,
"item_scraped_count": 925,
"log_count/INFO": 21,
"log_count/WARNING": 1,
"scheduler/dequeued": 992,
"scheduler/dequeued/memory": 992,
"scheduler/enqueued": 1050,
"scheduler/enqueued/memory": 1050
},
"time": {
"elapsed": 360.008903,
"log_interval": 60.0,
"log_interval_real": 60.006694,
"start_time": "2023-08-03 23:24:57",
"utcnow": "2023-08-03 23:30:57"
}
}
Thisextensionlogsthefollowingconfigurablesections:
• "delta"showshowsomenumericstatshavechangedsincethelaststatslogmessage.
ThePERIODIC_LOG_DELTA settingdeterminesthetargetstats. Theymusthaveintorfloatvalues.
• "stats"showsthecurrentvalueofsomestats.
ThePERIODIC_LOG_STATS settingdeterminesthetargetstats.
• "time"showsdetailedtimingdata.
ThePERIODIC_LOG_TIMING_ENABLED settingdetermineswhetherornottoshowthissection.
This extension logs data at the start, then on a fixed time interval configurable through the LOGSTATS_INTERVAL
setting,andfinallyrightbeforethecrawlends.
Exampleextensionconfiguration:
custom_settings = {
"LOG_LEVEL": "INFO",
(continuesonnextpage)
266 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
"PERIODIC_LOG_STATS": {
"include": ["downloader/", "scheduler/", "log_count/", "item_scraped_count/"],
},
"PERIODIC_LOG_DELTA": {"include": ["downloader/"]},
"PERIODIC_LOG_TIMING_ENABLED": True,
"EXTENSIONS": {
"scrapy.extensions.periodic_log.PeriodicLog": 0,
},
}
PERIODIC_LOG_DELTA
Default: None
• "PERIODIC_LOG_DELTA": True-showdeltasforallintandfloatstatvalues.
• "PERIODIC_LOG_DELTA": {"include": ["downloader/", "scheduler/"]} - show deltas for stats
withnamescontaininganyconfiguredsubstring.
• "PERIODIC_LOG_DELTA": {"exclude": ["downloader/"]} - show deltas for all stats with names not
containinganyconfiguredsubstring.
PERIODIC_LOG_STATS
Default: None
• "PERIODIC_LOG_STATS": True-showthecurrentvalueofallstats.
• "PERIODIC_LOG_STATS": {"include": ["downloader/", "scheduler/"]}-showcurrentvaluesfor
statswithnamescontaininganyconfiguredsubstring.
• "PERIODIC_LOG_STATS": {"exclude": ["downloader/"]} - show current values for all stats with
namesnotcontaininganyconfiguredsubstring.
PERIODIC_LOG_TIMING_ENABLED
Default: False
Trueenablesloggingoftimingdata(i.e. the"time"section).
Debuggingextensions
Stacktracedumpextension
class scrapy.extensions.periodic_log.StackTraceDump
Dumps information about the running process when a SIGQUIT or SIGUSR2 signal is received. The information
dumpedisthefollowing:
1. enginestatus(usingscrapy.utils.engine.get_engine_status())
2. livereferences(seeDebuggingmemoryleakswithtrackref)
3. stacktraceofallthreads
Afterthestacktraceandenginestatusisdumped,theScrapyprocesscontinuesrunningnormally.
ThisextensiononlyworksonPOSIX-compliantplatforms(i.e. notWindows),becausetheSIGQUITandSIGUSR2
signalsarenotavailableonWindows.
6.5. Extensions 267

ScrapyDocumentation,Release2.13.3
ThereareatleasttwowaystosendScrapytheSIGQUITsignal:
1. BypressingCtrl-whileaScrapyprocessisrunning(Linuxonly?)
2. Byrunningthiscommand(assuming<pid>istheprocessidoftheScrapyprocess):
kill -QUIT <pid>
Debuggerextension
class scrapy.extensions.periodic_log.Debugger
InvokesaPythondebuggerinsidearunningScrapyprocesswhenaSIGUSR2signalisreceived. Afterthedebugger
isexited,theScrapyprocesscontinuesrunningnormally.
ThisextensiononlyworksonPOSIX-compliantplatforms(i.e. notWindows).
6.6 Signals
Scrapyusessignalsextensivelytonotifywhencertaineventsoccur. YoucancatchsomeofthosesignalsinyourScrapy
project(usinganextension,forexample)toperformadditionaltasksorextendScrapytoaddfunctionalitynotprovided
outofthebox.
Eventhoughsignalsprovideseveralarguments,thehandlersthatcatchthemdon’tneedtoacceptallofthem-thesignal
dispatchingmechanismwillonlydelivertheargumentsthatthehandlerreceives.
Youcanconnecttosignals(orsendyourown)throughtheSignalsAPI.
Hereisasimpleexampleshowinghowyoucancatchsignalsandperformsomeaction:
from scrapy import signals
from scrapy import Spider
class DmozSpider(Spider):
name = "dmoz"
allowed_domains = ["dmoz.org"]
start_urls = [
"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
]
@classmethod
def from_crawler(cls, crawler, *args, **kwargs):
spider = super(DmozSpider, cls).from_crawler(crawler, *args, **kwargs)
crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
return spider
def spider_closed(self, spider):
spider.logger.info("Spider closed: %s", spider.name)
def parse(self, response):
pass
268 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
6.6.1 Deferred signal handlers
SomesignalssupportreturningDeferredorawaitableobjectsfromtheirhandlers,allowingyoutorunasynchronous
codethatdoesnotblockScrapy. Ifasignalhandlerreturnsoneoftheseobjects,Scrapywaitsforthatasynchronous
operationtofinish.
Let’stakeanexampleusingcoroutines:
import scrapy
class SignalSpider(scrapy.Spider):
name = "signals"
start_urls = ["https://quotes.toscrape.com/page/1/"]
@classmethod
def from_crawler(cls, crawler, *args, **kwargs):
spider = super(SignalSpider, cls).from_crawler(crawler, *args, **kwargs)
crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)
return spider
async def item_scraped(self, item):
# Send the scraped item to the server
response = await treq.post(
"http://example.com/post",
json.dumps(item).encode("ascii"),
headers={b"Content-Type": [b"application/json"]},
)
return response
def parse(self, response):
for quote in response.css("div.quote"):
yield {
"text": quote.css("span.text::text").get(),
"author": quote.css("small.author::text").get(),
"tags": quote.css("div.tags a.tag::text").getall(),
}
SeetheBuilt-insignalsreferencebelowtoknowwhichsignalssupportDeferredandawaitableobjects.
6.6.2 Built-in signals reference
Here’sthelistofScrapybuilt-insignalsandtheirmeaning.
Enginesignals
engine_started
scrapy.signals.engine_started()
SentwhentheScrapyenginehasstartedcrawling.
Thissignalsupportsreturningdeferredsfromitshandlers.
6.6. Signals 269

ScrapyDocumentation,Release2.13.3
(cid:242) Note
Thissignalmaybefiredafterthespider_opened signal,dependingonhowthespiderwasstarted. Sodon’trely
onthissignalgettingfiredbeforespider_opened.
engine_stopped
scrapy.signals.engine_stopped()
SentwhentheScrapyengineisstopped(forexample,whenacrawlingprocesshasfinished).
Thissignalsupportsreturningdeferredsfromitshandlers.
scheduler_empty
scrapy.signals.scheduler_empty()
Sentwhenevertheengineasksforapendingrequestfromthescheduler(i.e. callsitsnext_request()method)
andtheschedulerreturnsnone.
SeeDelayingstartrequestiterationforanexample.
Itemsignals
(cid:242) Note
As at max CONCURRENT_ITEMS items are processed in parallel, many deferreds are fired together using
DeferredList. HencethenextbatchwaitsfortheDeferredListtofireandthenrunstherespectiveitemsignal
handlerforthenextbatchofscrapeditems.
item_scraped
scrapy.signals.item_scraped(item,response,spider)
Sentwhenanitemhasbeenscraped,afterithaspassedalltheItemPipelinestages(withoutbeingdropped).
Thissignalsupportsreturningdeferredsfromitshandlers.
Parameters
• item(itemobject)–thescrapeditem
• spider(Spiderobject)–thespiderwhichscrapedtheitem
• response(Response|None)–theresponsefromwheretheitemwasscraped,orNone
ifitwasyieldedfromstart().
item_dropped
scrapy.signals.item_dropped(item,response,exception,spider)
SentafteranitemhasbeendroppedfromtheItemPipelinewhensomestageraisedaDropItem exception.
Thissignalsupportsreturningdeferredsfromitshandlers.
Parameters
• item(itemobject)–theitemdroppedfromtheItemPipeline
• spider(Spiderobject)–thespiderwhichscrapedtheitem
270 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
• response(Response|None)–theresponsefromwheretheitemwasdropped,orNone
ifitwasyieldedfromstart().
• exception(DropItemexception)–theexception(whichmustbeaDropItemsubclass)
whichcausedtheitemtobedropped
item_error
scrapy.signals.item_error(item,response,spider,failure)
SentwhenaItemPipelinegeneratesanerror(i.e. raisesanexception),exceptDropItem exception.
Thissignalsupportsreturningdeferredsfromitshandlers.
Parameters
• item(itemobject)–theitemthatcausedtheerrorintheItemPipeline
• response (Response | None) – the response being processed when the exception was
raised,orNoneifitwasyieldedfromstart().
• spider(Spiderobject)–thespiderwhichraisedtheexception
• failure(twisted.python.failure.Failure)–theexceptionraised
Spidersignals
spider_closed
scrapy.signals.spider_closed(spider,reason)
Sentafteraspiderhasbeenclosed. Thiscanbeusedtoreleaseper-spiderresourcesreservedonspider_opened.
Thissignalsupportsreturningdeferredsfromitshandlers.
Parameters
• spider(Spiderobject)–thespiderwhichhasbeenclosed
• reason(str)–astringwhichdescribesthereasonwhythespiderwasclosed. Ifitwas
closedbecausethespiderhascompletedscraping,thereasonis'finished'. Otherwise,
if the spider was manually closed by calling the close_spider engine method, then
the reason is the one passed in the reason argument of that method (which defaults to
'cancelled'). Iftheenginewasshutdown(forexample,byhittingCtrl-Ctostopit)the
reasonwillbe'shutdown'.
spider_opened
scrapy.signals.spider_opened(spider)
Sentafteraspiderhasbeenopenedforcrawling. Thisistypicallyusedtoreserveper-spiderresources,butcan
beusedforanytaskthatneedstobeperformedwhenaspiderisopened.
Thissignalsupportsreturningdeferredsfromitshandlers.
Parameters
spider(Spiderobject)–thespiderwhichhasbeenopened
spider_idle
scrapy.signals.spider_idle(spider)
Sentwhenaspiderhasgoneidle,whichmeansthespiderhasnofurther:
• requestswaitingtobedownloaded
6.6. Signals 271

ScrapyDocumentation,Release2.13.3
• requestsscheduled
• itemsbeingprocessedintheitempipeline
Iftheidlestatepersistsafterallhandlersofthissignalhavefinished,theenginestartsclosingthespider. After
thespiderhasfinishedclosing,thespider_closed signalissent.
YoumayraiseaDontCloseSpiderexceptiontopreventthespiderfrombeingclosed.
Alternatively, you may raise a CloseSpider exception to provide a custom spider closing reason. An idle
handler is the perfect place to put some code that assesses the final spider results and update the final closing
reasonaccordingly(e.g. settingitto‘too_few_results’insteadof‘finished’).
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
spider(Spiderobject)–thespiderwhichhasgoneidle
(cid:242) Note
Schedulingsomerequestsinyourspider_idlehandlerdoesnotguaranteethatitcanpreventthespiderfrombeing
closed,althoughitsometimescan. That’sbecausethespidermaystillremainidleifallthescheduledrequestsare
rejectedbythescheduler(e.g. filteredduetoduplication).
spider_error
scrapy.signals.spider_error(failure,response,spider)
Sentwhenaspidercallbackgeneratesanerror(i.e. raisesanexception).
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• failure(twisted.python.failure.Failure)–theexceptionraised
• response (Response object) – the response being processed when the exception was
raised
• spider(Spiderobject)–thespiderwhichraisedtheexception
feed_slot_closed
scrapy.signals.feed_slot_closed(slot)
Sentwhenafeedexportsslotisclosed.
Thissignalsupportsreturningdeferredsfromitshandlers.
Parameters
slot(scrapy.extensions.feedexport.FeedSlot)–theslotclosed
feed_exporter_closed
scrapy.signals.feed_exporter_closed()
Sentwhenthefeedexportsextensionisclosed,duringthehandlingofthespider_closed signalbytheexten-
sion,afterallfeedexportinghasbeenhandled.
Thissignalsupportsreturningdeferredsfromitshandlers.
272 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
Requestsignals
request_scheduled
scrapy.signals.request_scheduled(request,spider)
Sent when the engine is asked to schedule a Request, to be downloaded later, before the request reaches the
scheduler.
RaiseIgnoreRequesttodroparequestbeforeitreachesthescheduler.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Addedinversion2.11.2: AllowdroppingrequestswithIgnoreRequest.
Parameters
• request(Requestobject)–therequestthatreachedthescheduler
• spider(Spiderobject)–thespiderthatyieldedtherequest
request_dropped
scrapy.signals.request_dropped(request,spider)
SentwhenaRequest,scheduledbytheenginetobedownloadedlater,isrejectedbythescheduler.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• request(Requestobject)–therequestthatreachedthescheduler
• spider(Spiderobject)–thespiderthatyieldedtherequest
request_reached_downloader
scrapy.signals.request_reached_downloader(request,spider)
SentwhenaRequestreacheddownloader.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• request(Requestobject)–therequestthatreacheddownloader
• spider(Spiderobject)–thespiderthatyieldedtherequest
request_left_downloader
scrapy.signals.request_left_downloader(request,spider)
Addedinversion2.0.
SentwhenaRequestleavesthedownloader,evenincaseoffailure.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• request(Requestobject)–therequestthatreachedthedownloader
• spider(Spiderobject)–thespiderthatyieldedtherequest
6.6. Signals 273

ScrapyDocumentation,Release2.13.3
bytes_received
Addedinversion2.2.
scrapy.signals.bytes_received(data,request,spider)
SentbytheHTTP1.1andS3downloadhandlerswhenagroupofbytesisreceivedforaspecificrequest. This
signalmightbefiredmultipletimesforthesamerequest, withpartialdataeachtime. Forinstance, apossible
scenariofora25kbresponsewouldbetwosignalsfiredwith10kbofdata,andafinalonewith5kbofdata.
HandlersforthissignalcanstopthedownloadofaresponsewhileitisinprogressbyraisingtheStopDownload
exception. PleaserefertotheStoppingthedownloadofaResponsetopicforadditionalinformationandexamples.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• data(bytesobject)–thedatareceivedbythedownloadhandler
• request(Requestobject)–therequestthatgeneratedthedownload
• spider(Spiderobject)–thespiderassociatedwiththeresponse
headers_received
Addedinversion2.5.
scrapy.signals.headers_received(headers,body_length,request,spider)
SentbytheHTTP1.1andS3downloadhandlerswhentheresponseheadersareavailableforagivenrequest,
beforedownloadinganyadditionalcontent.
HandlersforthissignalcanstopthedownloadofaresponsewhileitisinprogressbyraisingtheStopDownload
exception. PleaserefertotheStoppingthedownloadofaResponsetopicforadditionalinformationandexamples.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• headers(scrapy.http.headers.Headersobject)–theheadersreceivedbythedown-
loadhandler
• body_length(int)–expectedsizeoftheresponsebody,inbytes
• request(Requestobject)–therequestthatgeneratedthedownload
• spider(Spiderobject)–thespiderassociatedwiththeresponse
Responsesignals
response_received
scrapy.signals.response_received(response,request,spider)
SentwhentheenginereceivesanewResponsefromthedownloader.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• response(Responseobject)–theresponsereceived
• request(Requestobject)–therequestthatgeneratedtheresponse
• spider(Spiderobject)–thespiderforwhichtheresponseisintended
274 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
(cid:242) Note
Therequestargumentmightnotcontaintheoriginalrequestthatreachedthedownloader,ifaDownloaderMid-
dlewaremodifiestheResponseobjectandsetsaspecificrequestattribute.
response_downloaded
scrapy.signals.response_downloaded(response,request,spider)
SentbythedownloaderrightafteraHTTPResponseisdownloaded.
Thissignaldoesnotsupportreturningdeferredsfromitshandlers.
Parameters
• response(Responseobject)–theresponsedownloaded
• request(Requestobject)–therequestthatgeneratedtheresponse
• spider(Spiderobject)–thespiderforwhichtheresponseisintended
6.7 Scheduler
Theschedulercomponentreceivesrequestsfromtheengineandstoresthemintopersistentand/ornon-persistentdata
structures. Italsogetsthoserequestsandfeedsthembacktotheenginewhenitasksforanextrequesttobedownloaded.
6.7.1 Overriding the default scheduler
YoucanuseyourowncustomschedulerclassbysupplyingitsfullPythonpathintheSCHEDULER setting.
6.7.2 Minimal scheduler interface
class scrapy.core.scheduler.BaseScheduler
The scheduler component is responsible for storing requests received from the engine, and feeding them back
uponrequest(alsototheengine).
Theoriginalsourcesofsaidrequestsare:
• Spider: startmethod,requestscreatedforURLsinthestart_urlsattribute,requestcallbacks
• Spidermiddleware: process_spider_outputandprocess_spider_exceptionmethods
• Downloadermiddleware: process_request,process_responseandprocess_exceptionmethods
Theorderinwhichtheschedulerreturnsitsstoredrequests(viathenext_requestmethod)playsagreatpart
indeterminingtheorderinwhichthoserequestsaredownloaded. SeeRequestorder.
ThemethodsdefinedinthisclassconstitutetheminimalinterfacethattheScrapyenginewillinteractwith.
close(reason: str)→Deferred[None]|None
Calledwhenthespiderisclosedbytheengine. Itreceivesthereasonwhythecrawlfinishedasargument
andit’susefultoexecutecleaningcode.
Parameters
reason(str)–astringwhichdescribesthereasonwhythespiderwasclosed
6.7. Scheduler 275

ScrapyDocumentation,Release2.13.3
abstract enqueue_request(request: Request)→bool
Processarequestreceivedbytheengine.
ReturnTrueiftherequestisstoredcorrectly,Falseotherwise.
If False,theenginewillfirearequest_droppedsignal,andwillnotmakefurtherattemptstoschedule
therequestatalatertime. Forreference,thedefaultScrapyschedulerreturnsFalsewhentherequestis
rejectedbythedupefilter.
classmethod from_crawler(crawler: Crawler)→Self
FactorymethodwhichreceivesthecurrentCrawlerobjectasargument.
abstract has_pending_requests()→bool
Trueiftheschedulerhasenqueuedrequests,Falseotherwise
abstract next_request()→Request|None
ReturnthenextRequesttobeprocessed,orNonetoindicatethattherearenorequeststobeconsidered
readyatthemoment.
ReturningNoneimpliesthatnorequestfromtheschedulerwillbesenttothedownloaderinthecurrent
reactorcycle. Theenginewillcontinuecallingnext_requestuntilhas_pending_requestsisFalse.
open(spider: Spider)→Deferred[None]|None
Calledwhenthespiderisopenedbytheengine. Itreceivesthespiderinstanceasargumentandit’suseful
toexecuteinitializationcode.
Parameters
spider(Spider)–thespiderobjectforthecurrentcrawl
6.7.3 Default scheduler
class scrapy.core.scheduler.Scheduler
Defaultscheduler.
Requestsarestoredintopriorityqueues(SCHEDULER_PRIORITY_QUEUE)thatsortrequestsbypriority.
Bydefault, asingle, memory-basedpriority queueisusedforallrequests. Whenusing JOBDIR,adisk-based
priorityqueueisalsocreated,andonlyunserializablerequestsarestoredinthememory-basedpriorityqueue.
Foragivenpriorityvalue,requestsinmemorytakeprecedenceoverrequestsindisk.
Each priority queue stores requests in separate internal queues, one per priority value. The memory priority
queueusesSCHEDULER_MEMORY_QUEUE queues, whilethediskpriorityqueueusesSCHEDULER_DISK_QUEUE
queues. Theinternalqueuesdeterminerequestorder whenrequestshavethesamepriority. Startrequestsare
storedintoseparateinternalqueuesbydefault,andordereddifferently.
DuplicaterequestsarefilteredoutwithaninstanceofDUPEFILTER_CLASS.
Requestorder
Withdefaultsettings,pendingrequestsarestoredinaLIFOqueue(exceptforstartrequests). Asaresult,crawling
happensinDFOorder,whichisusuallythemostconvenientcrawlorder. However,youcanenforceBFOora
customorder(exceptforthefirstfewrequests).
Startrequestorder
Startrequestsaresentintheordertheyareyieldedfromstart(),andgiventhesamepriority,otherrequests
takeprecedenceoverstartrequests.
YoucansetSCHEDULER_START_MEMORY_QUEUE andSCHEDULER_START_DISK_QUEUE toNonetohandlestart
requeststhesameasotherrequestswhenitcomestoorderandpriority.
276 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
CrawlinginBFOorder
IfyoudowanttocrawlinBFOorder,youcandoitbysettingthefollowingsettings:
DEPTH_PRIORITY =1
SCHEDULER_DISK_QUEUE ="scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE ="scrapy.squeues.FifoMemoryQueue"
Crawlinginacustomorder
Youcanmanuallysetpriorityonrequeststoforceaspecificrequestorder.
Concurrencyaffectsorder
While pending requests are below the configured values of CONCURRENT_REQUESTS,
CONCURRENT_REQUESTS_PER_DOMAIN or CONCURRENT_REQUESTS_PER_IP, those requests are sent con-
currently.
As a result, the first few requests of a crawl may not follow the desired order. Lowering those settings to 1
enforcesthedesiredorderexceptfortheveryfirstrequest,butitsignificantlyslowsdownthecrawlasawhole.
__init__(dupefilter: BaseDupeFilter,jobdir: str|None=None,dqclass: type[BaseQueue]|None=None,
mqclass: type[BaseQueue]|None=None,logunser: bool=False,stats: StatsCollector|None=
None,pqclass: type[ScrapyPriorityQueue]|None=None,crawler: Crawler|None=None)
Initializethescheduler.
Parameters
• dupefilter (scrapy.dupefilters.BaseDupeFilter instance or similar: any
classthatimplementstheBaseDupeFilterinterface)–Anobjectresponsibleforcheck-
ingandfilteringduplicaterequests. ThevaluefortheDUPEFILTER_CLASS settingis
usedbydefault.
• jobdir(stror None)–Thepathofadirectorytobeusedforpersistingthecrawl’s
state. The value for the JOBDIR setting is used by default. See Jobs: pausing and
resumingcrawls.
• dqclass(class)–Aclasstobeusedaspersistentrequestqueue. Thevalueforthe
SCHEDULER_DISK_QUEUE settingisusedbydefault.
• mqclass(class)–Aclasstobeusedasnon-persistentrequestqueue. Thevaluefor
theSCHEDULER_MEMORY_QUEUE settingisusedbydefault.
• logunser (bool) – A boolean that indicates whether or not unserializable requests
shouldbelogged. ThevaluefortheSCHEDULER_DEBUG settingisusedbydefault.
• stats (scrapy.statscollectors.StatsCollector instance or similar: any
classthatimplementstheStatsCollectorinterface)–Astatscollectorobjecttorecord
statsabouttherequestschedulingprocess. ThevaluefortheSTATS_CLASS settingis
usedbydefault.
• pqclass(class)–Aclasstobeusedaspriorityqueueforrequests. Thevaluefor
theSCHEDULER_PRIORITY_QUEUE settingisusedbydefault.
• crawler (scrapy.crawler.Crawler) – The crawler object corresponding to the
currentcrawl.
6.7. Scheduler 277

ScrapyDocumentation,Release2.13.3
__len__()→int
Returnthetotalamountofenqueuedrequests
close(reason: str)→Deferred[None]|None
(1) dumppendingrequeststodiskifthereisadiskqueue
(2) returntheresultofthedupefilter’sclosemethod
enqueue_request(request: Request)→bool
UnlessthereceivedrequestisfilteredoutbytheDupefilter,attempttopushitintothediskqueue,falling
backtopushingitintothememoryqueue.
Increment the appropriate stats, such as: scheduler/enqueued, scheduler/enqueued/disk,
scheduler/enqueued/memory.
ReturnTrueiftherequestwasstoredsuccessfully,Falseotherwise.
classmethod from_crawler(crawler: Crawler)→Self
FactorymethodwhichreceivesthecurrentCrawlerobjectasargument.
has_pending_requests()→bool
Trueiftheschedulerhasenqueuedrequests,Falseotherwise
next_request()→Request|None
ReturnaRequestobjectfromthememoryqueue,fallingbacktothediskqueueifthememoryqueueis
empty. ReturnNoneiftherearenomoreenqueuedrequests.
Increment the appropriate stats, such as: scheduler/dequeued, scheduler/dequeued/disk,
scheduler/dequeued/memory.
open(spider: Spider)→Deferred[None]|None
(1) initializethememoryqueue
(2) initializethediskqueueifthejobdirattributeisavaliddirectory
(3) returntheresultofthedupefilter’sopenmethod
6.8 Item Exporters
Once you have scraped your items, you often want to persist or export those items, to use the data in some other
application. Thatis,afterall,thewholepurposeofthescrapingprocess.
For this purpose Scrapy provides a collection of Item Exporters for different output formats, such as XML, CSV or
JSON.
6.8.1 Using Item Exporters
Ifyouareinahurry,andjustwanttouseanItemExportertooutputscrapeddataseetheFeedexports. Otherwise,if
youwanttoknowhowItemExportersworkorneedmorecustomfunctionality(notcoveredbythedefaultexports),
continuereadingbelow.
InordertouseanItemExporter,youmustinstantiateitwithitsrequiredargs. EachItemExporterrequiresdifferent
arguments, so check each exporter documentation to be sure, in Built-in Item Exporters reference. After you have
instantiatedyourexporter,youhaveto:
1. callthemethodstart_exporting()inordertosignalthebeginningoftheexportingprocess
2. calltheexport_item()methodforeachitemyouwanttoexport
278 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
3. andfinallycallthefinish_exporting()tosignaltheendoftheexportingprocess
HereyoucanseeanItemPipelinewhichusesmultipleItemExporterstogroupscrapeditemstodifferentfilesaccording
tothevalueofoneoftheirfields:
from itemadapter import ItemAdapter
from scrapy.exporters import XmlItemExporter
class PerYearXmlExportPipeline:
"""Distribute items across multiple XML files according to their 'year' field"""
def open_spider(self, spider):
self.year_to_exporter = {}
def close_spider(self, spider):
for exporter, xml_file in self.year_to_exporter.values():
exporter.finish_exporting()
xml_file.close()
def _exporter_for_item(self, item):
adapter = ItemAdapter(item)
year = adapter["year"]
if year not in self.year_to_exporter:
xml_file = open(f"{year}.xml", "wb")
exporter = XmlItemExporter(xml_file)
exporter.start_exporting()
self.year_to_exporter[year] = (exporter, xml_file)
return self.year_to_exporter[year][0]
def process_item(self, item, spider):
exporter = self._exporter_for_item(item)
exporter.export_item(item)
return item
6.8.2 Serialization of item fields
By default, the field values are passed unmodified to the underlying serialization library, and the decision of how to
serializethemisdelegatedtoeachparticularserializationlibrary.
However,youcancustomizehoweachfieldvalueisserializedbeforeitispassedtotheserializationlibrary.
Therearetwowaystocustomizehowafieldwillbeserialized,whicharedescribednext.
1. Declaringaserializerinthefield
IfyouuseItem youcandeclareaserializerinthefieldmetadata. Theserializermustbeacallablewhichreceivesa
valueandreturnsitsserializedform.
Example:
import scrapy
def serialize_price(value):
return f"$ {str(value)}"
(continuesonnextpage)
6.8. ItemExporters 279

ScrapyDocumentation,Release2.13.3
(continuedfrompreviouspage)
class Product(scrapy.Item):
name = scrapy.Field()
price = scrapy.Field(serializer=serialize_price)
2. Overridingtheserialize_field()method
Youcanalsooverridetheserialize_field()methodtocustomizehowyourfieldvaluewillbeexported.
Makesureyoucallthebaseclassserialize_field()methodafteryourcustomcode.
Example:
from scrapy.exporters import XmlItemExporter
class ProductXmlExporter(XmlItemExporter):
def serialize_field(self, field, name, value):
if name == "price":
return f"$ {str(value)}"
return super().serialize_field(field, name, value)
6.8.3 Built-in Item Exporters reference
HereisalistoftheItemExportersbundledwithScrapy. Someofthemcontainoutputexamples,whichassumeyou’re
exportingthesetwoitems:
Item(name="Color TV", price="1200")
Item(name="DVD player", price="200")
BaseItemExporter
class scrapy.exporters.BaseItemExporter(fields_to_export=None,export_empty_fields=False,
encoding='utf-8',indent=0,dont_fail=False)
This is the (abstract) base class for all Item Exporters. It provides support for common features used by all
(concrete) Item Exporters, such as defining what fields to export, whether to export empty fields, or which
encodingtouse.
Thesefeaturescanbeconfiguredthroughthe__init__methodargumentswhichpopulatetheirrespectivein-
stanceattributes: fields_to_export,export_empty_fields,encoding,indent.
Addedinversion2.0: Thedont_failparameter.
export_item(item)
Exportsthegivenitem. Thismethodmustbeimplementedinsubclasses.
serialize_field(field,name,value)
Return the serialized value for the given field. You can override this method (in your custom Item Ex-
porters)ifyouwanttocontrolhowaparticularfieldorvaluewillbeserialized/exported.
Bydefault,thismethodlooksforaserializerdeclaredintheitemfield andreturnstheresultofapplying
thatserializertothevalue. Ifnoserializerisfound,itreturnsthevalueunchanged.
Parameters
280 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
• field (Field object or a dict instance) – the field being serialized. If the source
itemobjectdoesnotdefinefieldmetadata,field isanemptydict.
• name(str)–thenameofthefieldbeingserialized
• value–thevaluebeingserialized
start_exporting()
Signal the beginning of the exporting process. Some exporters may use this to generate some required
header(forexample,theXmlItemExporter). Youmustcallthismethodbeforeexportinganyitems.
finish_exporting()
Signal the end of the exporting process. Some exporters may use this to generate some required footer
(forexample,theXmlItemExporter). Youmustalwayscallthismethodafteryouhavenomoreitemsto
export.
fields_to_export
Fieldstoexport,theirorder1andtheiroutputnames.
Possiblevaluesare:
• None(allfields2,default)
• Alistoffields:
['field1', 'field2']
• Adictwherekeysarefieldsandvaluesareoutputnames:
{'field1': 'Field 1', 'field2': 'Field 2'}
export_empty_fields
Whethertoincludeempty/unpopulateditemfieldsintheexporteddata. DefaultstoFalse. Someexporters
(likeCsvItemExporter)ignorethisattributeandalwaysexportallemptyfields.
Thisoptionisignoredfordictitems.
encoding
Theoutputcharacterencoding.
indent
Amountofspacesusedtoindenttheoutputoneachlevel. Defaultsto0.
• indent=Noneselectsthemostcompactrepresentation,allitemsinthesamelinewithnoindentation
• indent<=0eachitemonitsownline,noindentation
• indent>0eachitemonitsownline,indentedwiththeprovidednumericvalue
PythonItemExporter
class scrapy.exporters.PythonItemExporter(*,dont_fail: bool=False,**kwargs: Any)
ThisisabaseclassforitemexportersthatextendsBaseItemExporterwithsupportfornesteditems.
Itserializesitemstobuilt-inPythontypes,sothatanyserializationlibrary(e.g. jsonormsgpack)canbeused
ontopofit.
1Notallexportersrespectthespecifiedfieldorder.
2Whenusingitemobjectsthatdonotexposealltheirpossiblefields,exportersthatdonotsupportexportingadifferentsubsetoffieldsperitem
willonlyexportthefieldsfoundinthefirstitemexported.
6.8. ItemExporters 281

ScrapyDocumentation,Release2.13.3
XmlItemExporter
class scrapy.exporters.XmlItemExporter(file,item_element='item',root_element='items',**kwargs)
ExportsitemsinXMLformattothespecifiedfileobject.
Parameters
• file–thefile-likeobjecttouseforexportingthedata. Itswritemethodshouldaccept
bytes(adiskfileopenedinbinarymode,aio.BytesIOobject,etc)
• root_element(str)–ThenameofrootelementintheexportedXML.
• item_element(str)–ThenameofeachitemelementintheexportedXML.
Theadditionalkeywordargumentsofthis__init__methodarepassedtotheBaseItemExporter__init__
method.
Atypicaloutputofthisexporterwouldbe:
<?xml version="1.0" encoding="utf-8"?>
<items>
<item>
<name>Color TV</name>
<price>1200</price>
</item>
<item>
<name>DVD player</name>
<price>200</price>
</item>
</items>
Unless overridden in the serialize_field() method, multi-valued fields are exported by serializing each
valueinsidea<value>element. Thisisforconvenience,asmulti-valuedfieldsareverycommon.
Forexample,theitem:
Item(name=['John', 'Doe'], age='23')
Wouldbeserializedas:
<?xml version="1.0" encoding="utf-8"?>
<items>
<item>
<name>
<value>John</value>
<value>Doe</value>
</name>
<age>23</age>
</item>
</items>
CsvItemExporter
class scrapy.exporters.CsvItemExporter(file,include_headers_line=True,join_multivalued=',',
errors=None,**kwargs)
ExportsitemsinCSVformattothegivenfile-likeobject. Ifthefields_to_exportattributeisset,itwillbe
usedtodefinetheCSVcolumns,theirorderandtheircolumnnames. Theexport_empty_fieldsattributehas
noeffectonthisexporter.
282 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
Parameters
• file–thefile-likeobjecttouseforexportingthedata. Itswritemethodshouldaccept
bytes(adiskfileopenedinbinarymode,aio.BytesIOobject,etc)
• include_headers_line (str) – If enabled, makes the exporter output a header line
with the field names taken from BaseItemExporter.fields_to_export or the first
exporteditemfields.
• join_multivalued–Thechar(orchars)thatwillbeusedforjoiningmulti-valuedfields,
iffound.
• errors(str)–Theoptionalstringthatspecifieshowencodinganddecodingerrorsare
tobehandled. Formoreinformationseeio.TextIOWrapper.
Theadditionalkeywordargumentsofthis__init__methodarepassedtotheBaseItemExporter__init__
method,andtheleftoverargumentstothecsv.writer()function,soyoucanuseanycsv.writer()function
argumenttocustomizethisexporter.
Atypicaloutputofthisexporterwouldbe:
product,price
Color TV,1200
DVD player,200
PickleItemExporter
class scrapy.exporters.PickleItemExporter(file,protocol=0,**kwargs)
Exportsitemsinpickleformattothegivenfile-likeobject.
Parameters
• file–thefile-likeobjecttouseforexportingthedata. Itswritemethodshouldaccept
bytes(adiskfileopenedinbinarymode,aio.BytesIOobject,etc)
• protocol(int)–Thepickleprotocoltouse.
Formoreinformation,seepickle.
Theadditionalkeywordargumentsofthis__init__methodarepassedtotheBaseItemExporter__init__
method.
Pickleisn’tahumanreadableformat,sonooutputexamplesareprovided.
PprintItemExporter
class scrapy.exporters.PprintItemExporter(file,**kwargs)
Exportsitemsinprettyprintformattothespecifiedfileobject.
Parameters
file–thefile-likeobjecttouseforexportingthedata. Itswritemethodshouldacceptbytes
(adiskfileopenedinbinarymode,aio.BytesIOobject,etc)
Theadditionalkeywordargumentsofthis__init__methodarepassedtotheBaseItemExporter__init__
method.
Atypicaloutputofthisexporterwouldbe:
{'name': 'Color TV', 'price': '1200'}
{'name': 'DVD player', 'price': '200'}
Longerlines(whenpresent)arepretty-formatted.
6.8. ItemExporters 283

ScrapyDocumentation,Release2.13.3
JsonItemExporter
class scrapy.exporters.JsonItemExporter(file,**kwargs)
ExportsitemsinJSONformattothespecifiedfile-likeobject,writingallobjectsasalistofobjects. Theaddi-
tional__init__methodargumentsarepassedtotheBaseItemExporter__init__method,andtheleftover
argumentstotheJSONEncoder__init__method,soyoucanuseanyJSONEncoder__init__methodargu-
menttocustomizethisexporter.
Parameters
file–thefile-likeobjecttouseforexportingthedata. Itswritemethodshouldacceptbytes
(adiskfileopenedinbinarymode,aio.BytesIOobject,etc)
Atypicaloutputofthisexporterwouldbe:
[{"name": "Color TV", "price": "1200"},
{"name": "DVD player", "price": "200"}]
. Warning
JSON is very simple and flexible serialization format, but it doesn’t scale well for large amounts of data
sinceincremental(aka. stream-mode)parsingisnotwellsupported(ifatall)amongJSONparsers(onany
language), and most of them just parse the entire object in memory. If you want the power and simplicity
ofJSONwithamorestream-friendlyformat,considerusingJsonLinesItemExporterinstead,orsplitting
theoutputinmultiplechunks.
JsonLinesItemExporter
class scrapy.exporters.JsonLinesItemExporter(file,**kwargs)
Exports items in JSON format to the specified file-like object, writing one JSON-encoded item per line. The
additional__init__methodargumentsarepassedtotheBaseItemExporter__init__method,andtheleft-
overargumentstotheJSONEncoder__init__method,soyoucanuseanyJSONEncoder__init__method
argumenttocustomizethisexporter.
Parameters
file–thefile-likeobjecttouseforexportingthedata. Itswritemethodshouldacceptbytes
(adiskfileopenedinbinarymode,aio.BytesIOobject,etc)
Atypicaloutputofthisexporterwouldbe:
{"name": "Color TV", "price": "1200"}
{"name": "DVD player", "price": "200"}
UnliketheoneproducedbyJsonItemExporter,theformatproducedbythisexporteriswellsuitedforserial-
izinglargeamountsofdata.
MarshalItemExporter
class scrapy.exporters.MarshalItemExporter(file: BytesIO,**kwargs: Any)
ExportsitemsinaPython-specificbinaryformat(seemarshal).
Parameters
file – The file-like object to use for exporting the data. Its write method should accept
bytes(adiskfileopenedinbinarymode,aBytesIOobject,etc)
284 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
6.9 Components
AScrapycomponentisanyclasswhoseobjectsarebuiltusingbuild_from_crawler().
Thatincludestheclassesthatyoumayassigntothefollowingsettings:
• ADDONS
• DNS_RESOLVER
• DOWNLOAD_HANDLERS
• DOWNLOADER_CLIENTCONTEXTFACTORY
• DOWNLOADER_MIDDLEWARES
• DUPEFILTER_CLASS
• EXTENSIONS
• FEED_EXPORTERS
• FEED_STORAGES
• ITEM_PIPELINES
• SCHEDULER
• SCHEDULER_DISK_QUEUE
• SCHEDULER_MEMORY_QUEUE
• SCHEDULER_PRIORITY_QUEUE
• SCHEDULER_START_DISK_QUEUE
• SCHEDULER_START_MEMORY_QUEUE
• SPIDER_MIDDLEWARES
Third-partyScrapycomponentsmayalsoletyoudefineadditionalScrapycomponents,usuallyconfigurablethrough
settings,tomodifytheirbehavior.
6.9.1 Initializing from the crawler
AnyScrapycomponentmayoptionallydefinethefollowingclassmethod:
classmethod from_crawler(cls,crawler: scrapy.crawler.Crawler,*args,**kwargs)
Returnaninstanceofthecomponentbasedoncrawler.
argsandkwargsarecomponent-specificargumentsthatsomecomponentsreceive. However,mostcomponents
donotgetanyarguments,andinsteadusesettings.
Ifacomponentclassdefinesthismethod,thisclassmethodiscalledtocreateanyinstanceofthecomponent.
Thecrawler objectprovidesaccesstoallScrapycorecomponentslikesettingsandsignals,allowingthecom-
ponenttoaccessthemandhookitsfunctionalityintoScrapy.
6.9.2 Settings
Componentscanbeconfiguredthroughsettings.
Componentscanreadanysettingfromthesettings attributeoftheCrawler objecttheycangetforinitialization.
Thatincludesbothbuilt-inandcustomsettings.
Forexample:
6.9. Components 285

ScrapyDocumentation,Release2.13.3
class MyExtension:
@classmethod
def from_crawler(cls, crawler):
settings = crawler.settings
return cls(settings.getbool("LOG_ENABLED"))
def __init__(self, log_is_enabled=False):
if log_is_enabled:
print("log is enabled!")
Componentsdonotneedtodeclaretheircustomsettingsprogrammatically. However,theyshoulddocumentthem,so
thatusersknowtheyexistandhowtousethem.
Itisagoodpracticetoprefixcustomsettingswiththenameofthecomponent,toavoidcollisionswithcustomsettingsof
otherexisting(orfuture)components. Forexample,anextensioncalledWarcCachingcouldprefixitscustomsettings
withWARC_CACHING_.
Anothergoodpractice,mainlyforcomponentsmeantforcomponentprioritydictionaries,istoprovideabooleanset-
tingcalled<PREFIX>_ENABLED(e.g. WARC_CACHING_ENABLED)toallowtogglingthatcomponentonandoffwithout
changingthecomponentprioritydictionarysetting. Youcanusuallycheckthevalueofsuchasettingduringinitial-
ization,andif False,raiseNotConfigured.
Whenchoosinganameforacustomsetting,itisalsoagoodideatohavealookatthenamesofbuilt-insettings,totry
tomaintainconsistencywiththem.
6.9.3 Enforcing requirements
Sometimes,yourcomponentsmayonlybeintendedtoworkundercertainconditions. Forexample,theymayrequire
aminimumversionofScrapytoworkasintended,ortheymayrequirecertainsettingstohavespecificvalues.
In addition to describing those conditions in the documentation of your component, it is a good practice to raise an
exceptionfromthe__init__methodofyourcomponentifthoseconditionsarenotmetatruntime.
In the case of downloader middlewares, extensions, item pipelines, and spider middlewares, you should raise
NotConfigured, passing a description of the issue as a parameter to the exception so that it is printed in the logs,
fortheusertosee. Forothercomponents,feelfreetoraisewhateverotherexceptionfeelsrighttoyou; forexample,
RuntimeErrorwouldmakesenseforaScrapyversionmismatch,whileValueErrormaybebetteriftheissueisthe
valueofasetting.
IfyourrequirementisaminimumScrapyversion,youmayusescrapy.__version__toenforceyourrequirement.
Forexample:
from packaging.version import parse as parse_version
import scrapy
class MyComponent:
def __init__(self):
if parse_version(scrapy.__version__) < parse_version("2.7"):
raise RuntimeError(
f"{MyComponent.__qualname__} requires Scrapy 2.7 or "
f"later, which allow defining the process_spider_output "
f"method of spider middlewares as an asynchronous "
f"generator."
)
286 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
6.9.4 API reference
Thefollowingfunctioncanbeusedtocreateaninstanceofacomponentclass:
scrapy.utils.misc.build_from_crawler(objcls: type[T],crawler: Crawler,/,*args: Any,**kwargs: Any)
→T
Constructaclassinstanceusingitsfrom_crawlerorfrom_settingsconstructor.
Addedinversion2.12.
*argsand**kwargsareforwardedtotheconstructor.
RaisesTypeErroriftheresultinginstanceisNone.
Thefollowingfunctioncanalsobeusefulwhenimplementingacomponent,toreporttheimportpathofthecomponent
class,e.g. whenreportingproblems:
scrapy.utils.python.global_object_name(obj: Any)→str
Returnthefullimportpathofthegivenobject.
>>> from scrapy import Request
>>> global_object_name(Request)
'scrapy.http.request.Request'
>>> global_object_name(Request.replace)
'scrapy.http.request.Request.replace'
6.10 Core API
ThissectiondocumentstheScrapycoreAPI,andit’sintendedfordevelopersofextensionsandmiddlewares.
6.10.1 Crawler API
ThemainentrypointtotheScrapyAPIistheCrawlerobject,whichcomponentscangetforinitialization. Itprovides
accesstoallScrapycorecomponents,anditistheonlywayforcomponentstoaccessthemandhooktheirfunctionality
into Scrapy. The Extension Manager is responsible for loading and keeping track of installed extensions and it’s
configured through the EXTENSIONS setting which contains a dictionary of all available extensions and their order
similartohowyouconfigurethedownloadermiddlewares.
class scrapy.crawler.Crawler(spidercls: type[Spider],settings: dict[str,Any]|Settings|None=None,
init_reactor: bool=False)
TheCrawlerobjectmustbeinstantiatedwithascrapy.Spidersubclassandascrapy.settings.Settings
object.
request_fingerprinter
Therequestfingerprintbuilderofthiscrawler.
Thisisusedfromextensionsandmiddlewarestobuildshort,uniqueidentifiersforrequests. SeeRequest
fingerprints.
settings
Thesettingsmanagerofthiscrawler.
Thisisusedbyextensions&middlewarestoaccesstheScrapysettingsofthiscrawler.
ForanintroductiononScrapysettingsseeSettings.
FortheAPIseeSettingsclass.
6.10. CoreAPI 287

ScrapyDocumentation,Release2.13.3
signals
Thesignalsmanagerofthiscrawler.
Thisisusedbyextensions&middlewarestohookthemselvesintoScrapyfunctionality.
ForanintroductiononsignalsseeSignals.
FortheAPIseeSignalManagerclass.
stats
Thestatscollectorofthiscrawler.
Thisisusedfromextensions&middlewarestorecordstatsoftheirbehaviour,oraccessstatscollectedby
otherextensions.
ForanintroductiononstatscollectionseeStatsCollection.
FortheAPIseeStatsCollectorclass.
extensions
Theextensionmanagerthatkeepstrackofenabledextensions.
Mostextensionswon’tneedtoaccessthisattribute.
ForanintroductiononextensionsandalistofavailableextensionsonScrapyseeExtensions.
engine
Theexecutionengine,whichcoordinatesthecorecrawlinglogicbetweenthescheduler,downloaderand
spiders.
SomeextensionmaywanttoaccesstheScrapyengine,toinspectormodifythedownloaderandscheduler
behaviour,althoughthisisanadvanceduseandthisAPIisnotyetstable.
spider
Spider currently being crawled. This is an instance of the spider class provided while constructing the
crawler,anditiscreatedaftertheargumentsgiveninthecrawl()method.
crawl(*args,**kwargs)
Startsthecrawlerbyinstantiatingitsspiderclasswiththegivenargsandkwargsarguments,whilesetting
theexecutionengineinmotion. Shouldbecalledonlyonce.
Returnsadeferredthatisfiredwhenthecrawlisfinished.
stop()→Generator[Deferred[Any],Any,None]
Startsagracefulstopofthecrawlerandreturnsadeferredthatisfiredwhenthecrawlerisstopped.
get_addon(cls: type[_T])→_T|None
Returntherun-timeinstanceofanadd-onofthespecifiedclassorasubclass,orNoneifnoneisfound.
Addedinversion2.12.
get_downloader_middleware(cls: type[_T])→_T|None
Returntherun-timeinstanceofadownloadermiddlewareofthespecifiedclassorasubclass,orNoneif
noneisfound.
Addedinversion2.12.
Thismethodcanonlybecalledafterthecrawlenginehasbeencreated,e.g. atsignalsengine_started
orspider_opened.
288 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
get_extension(cls: type[_T])→_T|None
Returntherun-timeinstanceofanextensionofthespecifiedclassorasubclass,orNoneifnoneisfound.
Addedinversion2.12.
This method can only be called after the extension manager has been created, e.g. at signals
engine_started orspider_opened.
get_item_pipeline(cls: type[_T])→_T|None
Returntherun-timeinstanceofaitempipelineofthespecifiedclassorasubclass,orNoneifnoneisfound.
Addedinversion2.12.
Thismethodcanonlybecalledafterthecrawlenginehasbeencreated,e.g. atsignalsengine_started
orspider_opened.
get_spider_middleware(cls: type[_T])→_T|None
Returntherun-timeinstanceofaspidermiddlewareofthespecifiedclassorasubclass,or Noneifnone
isfound.
Addedinversion2.12.
Thismethodcanonlybecalledafterthecrawlenginehasbeencreated,e.g. atsignalsengine_started
orspider_opened.
class scrapy.crawler.CrawlerRunner(settings: dict[str,Any]|Settings|None=None)
Thisisaconvenienthelperclassthatkeepstrackof,managesandrunscrawlersinsideanalreadysetupreactor.
TheCrawlerRunnerobjectmustbeinstantiatedwithaSettingsobject.
Thisclassshouldn’tbeneeded(sinceScrapyisresponsibleofusingitaccordingly)unlesswritingscriptsthat
manuallyhandlethecrawlingprocess. SeeRunScrapyfromascriptforanexample.
crawl(crawler_or_spidercls: type[Spider]|str|Crawler,*args: Any,**kwargs: Any)→Deferred[None]
Runacrawlerwiththeprovidedarguments.
ItwillcallthegivenCrawler’scrawl()method,whilekeepingtrackofitsoitcanbestoppedlater.
Ifcrawler_or_spiderclsisn’taCrawlerinstance,thismethodwilltrytocreateoneusingthisparam-
eterasthespiderclassgiventoit.
Returnsadeferredthatisfiredwhenthecrawlingisfinished.
Parameters
• crawler_or_spidercls (Crawler instance, Spider subclass or string) – already
createdcrawler,oraspiderclassorspider’snameinsidetheprojecttocreateit
• args–argumentstoinitializethespider
• kwargs–keywordargumentstoinitializethespider
property crawlers
Setofcrawlersstartedbycrawl()andmanagedbythisclass.
create_crawler(crawler_or_spidercls: type[Spider]|str|Crawler)→Crawler
ReturnaCrawlerobject.
• If crawler_or_spiderclsisaCrawler,itisreturnedas-is.
• If crawler_or_spiderclsisaSpidersubclass,anewCrawlerisconstructedforit.
• Ifcrawler_or_spiderclsisastring,thisfunctionfindsaspiderwiththisnameinaScrapyproject
(usingspiderloader),thencreatesaCrawlerinstanceforit.
6.10. CoreAPI 289

ScrapyDocumentation,Release2.13.3
join()
Returnsadeferredthatisfiredwhenallmanagedcrawlershavecompletedtheirexecutions.
stop()→Deferred[Any]
Stopssimultaneouslyallthecrawlingjobstakingplace.
Returnsadeferredthatisfiredwhentheyallhaveended.
class scrapy.crawler.CrawlerProcess(settings: dict[str,Any]|Settings|None=None,
install_root_handler: bool=True)
Bases: CrawlerRunner
Aclasstorunmultiplescrapycrawlersinaprocesssimultaneously.
ThisclassextendsCrawlerRunner byaddingsupportforstartingareactorandhandlingshutdownsignals,
likethekeyboardinterruptcommandCtrl-C.Italsoconfigurestop-levellogging.
ThisutilityshouldbeabetterfitthanCrawlerRunner ifyouaren’trunninganotherreactorwithinyourap-
plication.
TheCrawlerProcessobjectmustbeinstantiatedwithaSettingsobject.
Parameters
install_root_handler–whethertoinstallrootlogginghandler(default: True)
Thisclassshouldn’tbeneeded(sinceScrapyisresponsibleofusingitaccordingly)unlesswritingscriptsthat
manuallyhandlethecrawlingprocess. SeeRunScrapyfromascriptforanexample.
crawl(crawler_or_spidercls: type[Spider]|str|Crawler,*args: Any,**kwargs: Any)→Deferred[None]
Runacrawlerwiththeprovidedarguments.
ItwillcallthegivenCrawler’scrawl()method,whilekeepingtrackofitsoitcanbestoppedlater.
Ifcrawler_or_spiderclsisn’taCrawlerinstance,thismethodwilltrytocreateoneusingthisparam-
eterasthespiderclassgiventoit.
Returnsadeferredthatisfiredwhenthecrawlingisfinished.
Parameters
• crawler_or_spidercls (Crawler instance, Spider subclass or string) – already
createdcrawler,oraspiderclassorspider’snameinsidetheprojecttocreateit
• args–argumentstoinitializethespider
• kwargs–keywordargumentstoinitializethespider
property crawlers
Setofcrawlersstartedbycrawl()andmanagedbythisclass.
create_crawler(crawler_or_spidercls: type[Spider]|str|Crawler)→Crawler
ReturnaCrawlerobject.
• If crawler_or_spiderclsisaCrawler,itisreturnedas-is.
• If crawler_or_spiderclsisaSpidersubclass,anewCrawlerisconstructedforit.
• Ifcrawler_or_spiderclsisastring,thisfunctionfindsaspiderwiththisnameinaScrapyproject
(usingspiderloader),thencreatesaCrawlerinstanceforit.
join()
Returnsadeferredthatisfiredwhenallmanagedcrawlershavecompletedtheirexecutions.
290 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
start(stop_after_crawl: bool=True,install_signal_handlers: bool=True)→None
This method starts a reactor, adjusts its pool size to REACTOR_THREADPOOL_MAXSIZE, and installs a
DNScachebasedonDNSCACHE_ENABLED andDNSCACHE_SIZE.
If stop_after_crawlisTrue,thereactorwillbestoppedafterallcrawlershavefinished,usingjoin().
Parameters
• stop_after_crawl(bool)–stopornotthereactorwhenallcrawlershavefinished
• install_signal_handlers(bool)–whethertoinstalltheOSsignalhandlersfrom
TwistedandScrapy(default: True)
stop()→Deferred[Any]
Stopssimultaneouslyallthecrawlingjobstakingplace.
Returnsadeferredthatisfiredwhentheyallhaveended.
6.10.2 Settings API
scrapy.settings.SETTINGS_PRIORITIES
DictionarythatsetsthekeynameandprioritylevelofthedefaultsettingsprioritiesusedinScrapy.
Eachitemdefinesasettingsentrypoint,givingitacodenameforidentificationandanintegerpriority. Greater
prioritiestakemoreprecedenceoverlesseroneswhensettingandretrievingvaluesintheSettingsclass.
SETTINGS_PRIORITIES = {
"default": 0,
"command": 10,
"addon": 15,
"project": 20,
"spider": 30,
"cmdline": 40,
}
Foradetailedexplanationoneachsettingssources,see: Settings.
scrapy.settings.get_settings_priority(priority: int|str)→int
SmallhelperfunctionthatlooksupagivenstringpriorityintheSETTINGS_PRIORITIESdictionaryandreturns
itsnumericalvalue,ordirectlyreturnsagivennumericalpriority.
class scrapy.settings.Settings(values: _SettingsInputT=None,priority: int|str='project')
Bases: BaseSettings
ThisobjectstoresScrapysettingsfortheconfigurationofinternalcomponents,andcanbeusedforanyfurther
customization.
ItisadirectsubclassandsupportsallmethodsofBaseSettings. Additionally,afterinstantiationofthisclass,
thenewobjectwillhavetheglobaldefaultsettingsdescribedonBuilt-insettingsreferencealreadypopulated.
class scrapy.settings.BaseSettings(values: _SettingsInputT=None,priority: int|str='project')
Instances of this class behave like dictionaries, but store priorities along with their (key, value) pairs, and
canbefrozen(i.e. markedimmutable).
Key-valueentriescanbepassedoninitializationwiththevaluesargument,andtheywouldtakethepriority
level(unlessvaluesisalreadyaninstanceofBaseSettings,inwhichcasetheexistingprioritylevelswillbe
kept). Ifthe priorityargumentisastring, theprioritynamewillbelookedupinSETTINGS_PRIORITIES.
Otherwise,aspecificintegershouldbeprovided.
6.10. CoreAPI 291

ScrapyDocumentation,Release2.13.3
Oncetheobjectiscreated,newsettingscanbeloadedorupdatedwiththeset()method,andcanbeaccessed
withthesquarebracketnotationofdictionaries,orwiththeget()methodoftheinstanceanditsvalueconversion
variants. Whenrequestingastoredkey,thevaluewiththehighestprioritywillberetrieved.
add_to_list(name: bool|float|int|str|None,item: Any)→None
Appenditemtothelistsettingwiththespecifiednameifitemisnotalreadyinthatlist.
Thischangeisappliedregardlessofthepriorityofthenamesetting. Thesettingpriorityisnotaffectedby
thischangeeither.
copy()→Self
Makeadeepcopyofcurrentsettings.
This method returns a new instance of the Settings class, populated with the same values and their
priorities.
Modificationstothenewobjectwon’tbereflectedontheoriginalsettings.
copy_to_dict()→dict[bool|float|int|str|None,Any]
Makeacopyofcurrentsettingsandconverttoadict.
Thismethodreturnsanewdictpopulatedwiththesamevaluesandtheirprioritiesasthecurrentsettings.
Modificationstothereturneddictwon’tbereflectedontheoriginalsettings.
ThismethodcanbeusefulforexampleforprintingsettingsinScrapyshell.
freeze()→None
Disablefurtherchangestothecurrentsettings.
Aftercallingthismethod,thepresentstateofthesettingswillbecomeimmutable. Tryingtochangevalues
throughtheset()methodanditsvariantswon’tbepossibleandwillbealerted.
frozencopy()→Self
Returnanimmutablecopyofthecurrentsettings.
Aliasforafreeze()callintheobjectreturnedbycopy().
get(name: bool|float|int|str|None,default: Any=None)→Any
Getasettingvaluewithoutaffectingitsoriginaltype.
Parameters
• name(str)–thesettingname
• default(object)–thevaluetoreturnifnosettingisfound
getbool(name: bool|float|int|str|None,default: bool=False)→bool
Getasettingvalueasaboolean.
1,'1',True` and'True'returnTrue,while0,'0',False,'False'andNonereturnFalse.
Forexample,settingspopulatedthroughenvironmentvariablessetto'0'willreturnFalsewhenusing
thismethod.
Parameters
• name(str)–thesettingname
• default(object)–thevaluetoreturnifnosettingisfound
292 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
getdict(name: bool|float|int|str|None,default: dict[Any,Any]|None=None)→dict[Any,Any]
Getasettingvalueasadictionary. Ifthesettingoriginaltypeisadictionary,acopyofitwillbereturned. If
itisastringitwillbeevaluatedasaJSONdictionary. InthecasethatitisaBaseSettingsinstanceitself,
itwillbeconvertedtoadictionary,containingallitscurrentsettingsvaluesastheywouldbereturnedby
get(),andlosingallinformationaboutpriorityandmutability.
Parameters
• name(str)–thesettingname
• default(object)–thevaluetoreturnifnosettingisfound
getdictorlist(name: bool|float|int|str|None,default: dict[Any,Any]|list[Any]|tuple[Any]|None=
None)→dict[Any,Any]|list[Any]
Getasettingvalueaseitheradictoralist.
Ifthesettingisalreadyadictoralist,acopyofitwillbereturned.
IfitisastringitwillbeevaluatedasJSON,orasacomma-separatedlistofstringsasafallback.
Forexample,settingspopulatedfromthecommandlinewillreturn:
• {'key1': 'value1', 'key2': 'value2'} if set to '{"key1": "value1", "key2":
"value2"}'
• ['one', 'two']ifsetto'["one", "two"]'or'one,two'
Parameters
• name(string)–thesettingname
• default(any)–thevaluetoreturnifnosettingisfound
getfloat(name: bool|float|int|str|None,default: float=0.0)→float
Getasettingvalueasafloat.
Parameters
• name(str)–thesettingname
• default(object)–thevaluetoreturnifnosettingisfound
getint(name: bool|float|int|str|None,default: int=0)→int
Getasettingvalueasanint.
Parameters
• name(str)–thesettingname
• default(object)–thevaluetoreturnifnosettingisfound
getlist(name: bool|float|int|str|None,default: list[Any]|None=None)→list[Any]
Getasettingvalueasalist. Ifthesettingoriginaltypeisalist,acopyofitwillbereturned. Ifit’sastring
itwillbesplitby“,”. Ifitisanemptystring,anemptylistwillbereturned.
Forexample,settingspopulatedthroughenvironmentvariablessetto'one,two'willreturnalist[‘one’,
‘two’]whenusingthismethod.
Parameters
• name(str)–thesettingname
• default(object)–thevaluetoreturnifnosettingisfound
6.10. CoreAPI 293

ScrapyDocumentation,Release2.13.3
getpriority(name: bool|float|int|str|None)→int|None
Returnthecurrentnumericalpriorityvalueofasetting,orNoneifthegivennamedoesnotexist.
Parameters
name(str)–thesettingname
getwithbase(name: bool|float|int|str|None)→BaseSettings
Getacompositionofadictionary-likesettingandits_BASEcounterpart.
Parameters
name(str)–nameofthedictionary-likesetting
maxpriority()→int
Returnthenumericalvalueofthehighestprioritypresentthroughoutallsettings,orthenumericalvalue
fordefaultfromSETTINGS_PRIORITIES iftherearenosettingsstored.
[ ]
pop(k ,d )→v,removespecifiedkeyandreturnthecorrespondingvalue.
Ifkeyisnotfound,disreturnedifgiven,otherwiseKeyErrorisraised.
remove_from_list(name: bool|float|int|str|None,item: Any)→None
Removeitemfromthelistsettingwiththespecifiedname.
Ifitemismissing,raiseValueError.
Thischangeisappliedregardlessofthepriorityofthenamesetting. Thesettingpriorityisnotaffectedby
thischangeeither.
replace_in_component_priority_dict(name: bool|float|int|str|None,old_cls: type,new_cls: type,
priority: int|None=None)→None
Replaceold_clswithnew_clsinthenamecomponentprioritydictionary.
Ifold_clsismissing,orhasNoneasvalue,KeyErrorisraised.
Ifold_clswaspresentasanimportstring,evenmorethanonce,thosekeysaredroppedandreplacedby
new_cls.
Ifpriorityisspecified,thatisthevalueassignedtonew_clsinthecomponentprioritydictionary. Other-
wise,thevalueofold_clsisused. Ifold_clswaspresentmultipletimes(possiblewithimportstrings)with
differentvalues,thevalueassignedtonew_clsisoneofthem,withnoguaranteeaboutwhichoneitis.
Thischangeisappliedregardlessofthepriorityofthenamesetting. Thesettingpriorityisnotaffectedby
thischangeeither.
set(name: bool|float|int|str|None,value: Any,priority: int|str='project')→None
Storeakey/valueattributewithagivenpriority.
SettingsshouldbepopulatedbeforeconfiguringtheCrawlerobject(throughtheconfigure()method),
otherwisetheywon’thaveanyeffect.
Parameters
• name(str)–thesettingname
• value(object)–thevaluetoassociatewiththesetting
• priority (str or int) – the priority of the setting. Should be a key of
SETTINGS_PRIORITIES oraninteger
set_in_component_priority_dict(name: bool|float|int|str|None,cls: type,priority: int|None)→
None
Settheclscomponentinthenamecomponentprioritydictionarysettingwithpriority.
294 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
Ifclsalreadyexists,itsvalueisupdated.
Ifclswaspresentasanimportstring,evenmorethanonce,thosekeysaredroppedandreplacedbycls.
Thischangeisappliedregardlessofthepriorityofthenamesetting. Thesettingpriorityisnotaffectedby
thischangeeither.
[ ]
setdefault(k ,d )→D.get(k,d),alsosetD[k]=difknotinD
setdefault_in_component_priority_dict(name: bool|float|int|str|None,cls: type,priority: int|
None)→None
Settheclscomponentinthenamecomponentprioritydictionarysettingwithpriorityifnotalreadydefined
(evenasanimportstring).
Ifclsisnotalreadydefined,itissetregardlessofthepriorityofthenamesetting. Thesettingpriorityis
notaffectedbythischangeeither.
setmodule(module: ModuleType|str,priority: int|str='project')→None
Storesettingsfromamodulewithagivenpriority.
Thisisahelperfunctionthatcallsset()foreverygloballydeclareduppercasevariableof modulewith
theprovidedpriority.
Parameters
• module(types.ModuleType or str)–themoduleorthepathofthemodule
• priority (str or int) – the priority of the settings. Should be a key of
SETTINGS_PRIORITIES oraninteger
update(values: _SettingsInputT,priority: int|str='project')→None
Storekey/valuepairswithagivenpriority.
Thisisahelperfunctionthatcallsset()foreveryitemof valueswiththeprovidedpriority.
If valuesisastring,itisassumedtobeJSON-encodedandparsedintoadictwithjson.loads()first.
IfitisaBaseSettingsinstance,theper-keyprioritieswillbeusedandthepriorityparameterignored.
Thisallowsinserting/updatingsettingswithdifferentprioritieswithasinglecommand.
Parameters
• values(dictorstringorBaseSettings)–thesettingsnamesandvalues
• priority (str or int) – the priority of the settings. Should be a key of
SETTINGS_PRIORITIES oraninteger
6.10.3 SpiderLoader API
class scrapy.spiderloader.SpiderLoader
Thisclassisinchargeofretrievingandhandlingthespiderclassesdefinedacrosstheproject.
Custom spider loaders can be employed by specifying their path in the SPIDER_LOADER_CLASS project set-
ting. Theymustfullyimplementthescrapy.interfaces.ISpiderLoaderinterfacetoguaranteeanerrorless
execution.
from_settings(settings)
ThisclassmethodisusedbyScrapytocreateaninstanceoftheclass. It’scalledwiththecurrentproject
settings,anditloadsthespidersfoundrecursivelyinthemodulesoftheSPIDER_MODULES setting.
Parameters
settings(Settingsinstance)–projectsettings
6.10. CoreAPI 295

ScrapyDocumentation,Release2.13.3
load(spider_name)
GettheSpiderclasswiththegivenname. It’lllookintothepreviouslyloadedspidersforaspiderclass
withnamespider_nameandwillraiseaKeyErrorifnotfound.
Parameters
spider_name(str)–spiderclassname
list()
Getthenamesoftheavailablespidersintheproject.
find_by_request(request)
Listthespiders’namesthatcanhandlethegivenrequest. Willtrytomatchtherequest’surlagainstthe
domainsofthespiders.
Parameters
request(Requestinstance)–queriedrequest
6.10.4 Signals API
class scrapy.signalmanager.SignalManager(sender: Any=_Anonymous)
connect(receiver: Any,signal: Any,**kwargs: Any)→None
Connectareceiverfunctiontoasignal.
Thesignalcanbeanyobject,althoughScrapycomeswithsomepredefinedsignalsthataredocumented
intheSignalssection.
Parameters
• receiver(collections.abc.Callable)–thefunctiontobeconnected
• signal(object)–thesignaltoconnectto
disconnect(receiver: Any,signal: Any,**kwargs: Any)→None
Disconnectareceiverfunctionfromasignal. Thishastheoppositeeffectoftheconnect()method,and
theargumentsarethesame.
disconnect_all(signal: Any,**kwargs: Any)→None
Disconnectallreceiversfromthegivensignal.
Parameters
signal(object)–thesignaltodisconnectfrom
send_catch_log(signal: Any,**kwargs: Any)→list[tuple[Any,Any]]
Sendasignal,catchexceptionsandlogthem.
Thekeywordargumentsarepassedtothesignalhandlers(connectedthroughtheconnect()method).
send_catch_log_deferred(signal: Any,**kwargs: Any)→Deferred[list[tuple[Any,Any]]]
Likesend_catch_log()butsupportsreturningDeferredobjectsfromsignalhandlers.
ReturnsaDeferredthatgetsfiredonceallsignalhandlersdeferredswerefired. Sendasignal, catchex-
ceptionsandlogthem.
Thekeywordargumentsarepassedtothesignalhandlers(connectedthroughtheconnect()method).
async wait_for(signal)
Awaitthenextsignal.
SeeDelayingstartrequestiterationforanexample.
296 Chapter6. ExtendingScrapy

ScrapyDocumentation,Release2.13.3
6.10.5 Stats Collector API
ThereareseveralStatsCollectorsavailableunderthescrapy.statscollectorsmoduleandtheyallimplementthe
StatsCollectorAPIdefinedbytheStatsCollectorclass(whichtheyallinheritfrom).
class scrapy.statscollectors.StatsCollector
get_value(key,default=None)
Returnthevalueforthegivenstatskeyordefaultifitdoesn’texist.
get_stats()
Getallstatsfromthecurrentlyrunningspiderasadict.
set_value(key,value)
Setthegivenvalueforthegivenstatskey.
set_stats(stats)
Overridethecurrentstatswiththedictpassedinstatsargument.
inc_value(key,count=1,start=0)
Incrementthevalueofthegivenstatskey, bythegivencount, assumingthestartvaluegiven(whenit’s
notset).
max_value(key,value)
Setthegivenvalueforthegivenkeyonlyifcurrentvalueforthesamekeyislowerthanvalue. Ifthereis
nocurrentvalueforthegivenkey,thevalueisalwaysset.
min_value(key,value)
Setthegivenvalueforthegivenkeyonlyifcurrentvalueforthesamekeyisgreaterthanvalue. Ifthereis
nocurrentvalueforthegivenkey,thevalueisalwaysset.
clear_stats()
Clearallstats.
Thefollowingmethodsarenotpartofthestatscollectionapibutinsteadusedwhenimplementingcustomstats
collectors:
open_spider(spider)
Openthegivenspiderforstatscollection.
close_spider(spider)
Closethegivenspider. Afterthisiscalled,nomorespecificstatscanbeaccessedorcollected.
6.10.6 Engine API
class scrapy.core.engine.ExecutionEngine
needs_backout()→bool
ReturnsTrueifnomorerequestscanbesentatthemoment,orFalseotherwise.
SeeDelayingstartrequestiterationforanexample.
Architectureoverview
UnderstandtheScrapyarchitecture.
Add-ons
Enableandconfigurethird-partyextensions.
DownloaderMiddleware
Customizehowpagesgetrequestedanddownloaded.
6.10. CoreAPI 297

ScrapyDocumentation,Release2.13.3
SpiderMiddleware
Customizetheinputandoutputofyourspiders.
Extensions
ExtendScrapywithyourcustomfunctionality
Signals
Seeallavailablesignalsandhowtoworkwiththem.
Scheduler
Understandtheschedulercomponent.
ItemExporters
Quicklyexportyourscrapeditemstoafile(XML,CSV,etc).
Components
LearnthecommonAPIandsomegoodpracticeswhenbuildingcustomScrapycomponents.
CoreAPI
UseitonextensionsandmiddlewarestoextendScrapyfunctionality.
298 Chapter6. ExtendingScrapy

CHAPTER
SEVEN
ALL THE REST
7.1 Release notes
7.1.1 Scrapy 2.13.3 (2025-07-02)
• ChangedthevaluesforDOWNLOAD_DELAY (from0to1)andCONCURRENT_REQUESTS_PER_DOMAIN (from8to
1)inthedefaultprojecttemplate. (issue6597,issue6918,issue6923)
• Improvedscrapy.core.engine.ExecutionEnginelogicrelatedtoinitializationandexceptionhandling,fix-
ingseveralcaseswherethespiderwouldcrash, hangorloganunhandledexception. (issue6783, issue6784,
issue6900,issue6908,issue6910,issue6911)
• Fixed a Windows issue with feed exports using scrapy.extensions.feedexport.FileFeedStorage that
causedthefiletobecreatedonthewrongdrive. (issue6894,issue6897)
• AllowedrunningtestswithTwisted25.5.0+again. Pytest8.4.1+isnowrequiredforrunningtestsinnon-pinned
envsassupportforthenewTwistedversionwasaddedinthatversion. (issue6893)
• Fixedrunningtestswithlxml6.0.0+. (issue6919)
• Addedadeprecationnoticeforscrapy.spidermiddlewares.offsite.OffsiteMiddlewaretotheScrapy
2.11.2releasenotes. (issue6926)
• Updatedcontributiondocstorefertoruffinsteadofblack. (issue6903)
• Added.venv/and.vscode/to.gitignore. (issue6901,issue6907)
7.1.2 Scrapy 2.13.2 (2025-06-09)
• FixedabugintroducedinScrapy2.13.0thatcausedresultsofrequesterrbackstobeignoredwhentheerrback
wascalledbecauseofadownloadererror. (issue6861,issue6863)
• Addedanoteaboutthebehaviorchangeofscrapy.utils.reactor.is_asyncio_reactor_installed()
toitsdocsandtothe“Backward-incompatiblechanges”sectionoftheScrapy2.13.0releasenotes. (issue6866)
• Improvedthemessageintheexceptionraisedbyscrapy.utils.test.get_reactor_settings()whenthere
isnoreactorinstalled. (issue6866)
• Updatedthescrapy.crawler.CrawlerRunnerexamplesinCommonPracticestoinstallthereactorexplicitly,
tofixreactor-relatederrorswithScrapy2.13.0andlater. (issue6865)
• Fixedscrapy fetchnotworkingwithscrapy-poet. (issue6872)
• Fixedanexceptionproducedbyscrapy.core.engine.ExecutionEnginewhenit’sclosedbeforebeingfully
initialized. (issue6857,issue6867)
• ImprovedtheREADME,updatedtheScrapylogoinit. (issue6831,issue6833,issue6839)
299

ScrapyDocumentation,Release2.13.3
• Restricted the Twisted version used in tests to below 25.5.0, as some tests fail with 25.5.0. (issue 6878, issue
6882)
• UpdatedtypehintsforTwisted25.5.0changes. (issue6882)
• Removedtheoldartwork. (issue6874)
7.1.3 Scrapy 2.13.1 (2025-05-28)
• Givecallbackrequestsprecedenceoverstartrequestswhenpriorityvaluesarethesame.
Thismakeschangesfrom2.13.0tostartrequesthandlingmoreintuitiveandbackwardcompatible. Forscenarios
whereallrequestshavethesamepriorities,in2.13.0allstartrequestsweresentbeforethefirstcallbackrequest.
In 2.13.1, same as in 2.12 and lower, start requests are only sent when there are not enough pending callback
requeststoreachconcurrencylimits.
(issue6828)
• AddedadeepwikibadgetotheREADME.(issue6793)
• FixedatypointhecodeexampleofDelayingstartrequestiteration. (issue6812,issue6815)
• FixedatypointheSupportedcallablessectionofthedocumentation. (issue6822)
• MadethispagemoreprominentlylistedinPyPIprojectlinks. (issue6826)
7.1.4 Scrapy 2.13.0 (2025-05-08)
Highlights:
• Theasyncioreactorisnowenabledbydefault
• Replacedstart_requests()(sync)withstart()(async)andchangedhowitisiterated.
• Addedtheallow_offsiterequestmetakey
• Spidermiddlewaresthatdon’tsupportasynchronousspideroutputaredeprecated
• Addedabaseclassforuniversalspidermiddlewares
Modifiedrequirements
• DroppedsupportforPyPy3.9. (issue6613)
• AddedsupportforPyPy3.11. (issue6697)
Backward-incompatiblechanges
• The default value of the TWISTED_REACTOR setting was changed from None to "twisted.internet.
asyncioreactor.AsyncioSelectorReactor". ThisvaluewasusedinnewlygeneratedprojectssinceScrapy
2.7.0 but now existing projects that don’t explicitly set this setting will also use the asyncio reactor. You can
changethissettinginyourprojecttouseadifferentreactor. (issue6659,issue6713)
• Theiterationofstartrequestsanditemsnolongerstopsoncetherearerequestsinthescheduler,andinsteadruns
continuouslyuntilallstartrequestshavebeenscheduled.
Toreproducethepreviousbehavior,seeDelayingstartrequestiteration. (issue6729)
• An unhandled exception from the open_spider() method of a spider middleware no longer stops the crawl.
(issue6729)
• Inscrapy.core.engine.ExecutionEngine:
300 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
– Thesecondparameterof open_spider(),start_requests,hasbeenremoved. Thestartrequestsare
determinedbythespiderparameterinstead(seestart()).
– Theslotattributehasbeenrenamedto_slotandshouldnotbeused.
(issue6729)
• Inscrapy.core.engine,theSlotclasshasbeenrenamedto_Slotandshouldnotbeused. (issue6729)
• Theslottelnetvariablehasbeenremoved. (issue6729)
• Inscrapy.core.spidermw.SpiderMiddlewareManager,process_start_requests()hasbeenreplaced
byprocess_start(). (issue6729)
• Thenow-deprecatedstart_requests()method,whenitreturnsaniterableinsteadofbeingdefinedasagen-
erator,isnowexecutedaftertheschedulerinstancehasbeencreated. (issue6729)
• When using JOBDIR, start requests are now serialized into their own, s-suffixed priority folders. You can set
SCHEDULER_START_DISK_QUEUE to None or "" to change that, but the side effects may be undesirable. See
SCHEDULER_START_DISK_QUEUE fordetails. (issue6729)
• TheURLlengthlimit,setbytheURLLENGTH_LIMITsetting,isnowalsoenforcedforstartrequests. (issue6777)
• Calling scrapy.utils.reactor.is_asyncio_reactor_installed() without an installed reactor now
raises an exception instead of installing a reactor. This shouldn’t affect normal Scrapy use cases, but it may
affect3rd-partytestsuitesthatuseScrapyinternalssuchasCrawleranddon’tinstallareactorexplicitly. Ifyou
areaffectedbythischange,youmostlikelyneedtoinstallthereactorbeforerunningScrapycodethatexpectsit
tobeinstalled. (issue6732,issue6735)
• The from_settings() method of UrlLengthMiddleware, deprecated in Scrapy 2.12.0, is removed earlier
thantheusualdeprecationperiod(thiswasneededbecauseaftertheintroductionoftheBaseSpiderMiddleware
baseclassandswitchingbuilt-inspidermiddlewarestoitthosemiddlewaresneedtheCrawler instanceatrun
time). Pleaseusefrom_crawler()instead. (issue6693)
• scrapy.utils.url.escape_ajax() is no longer called when a Request instance is created. It was only
usefulforwebsitessupportingthe_escaped_fragment_featurewhichmostmodernwebsitesdon’tsupport. If
youstillneedthisyoucanmodifytheURLsbeforepassingthemtoRequest. (issue6523,issue6651)
Deprecationremovals
• Removedolddeprecatednamealiasesforsomesignals:
– stats_spider_opened(usespider_openedinstead)
– stats_spider_closingandstats_spider_closed(usespider_closedinstead)
– item_passed(useitem_scrapedinstead)
– request_received(userequest_scheduledinstead)
(issue6654,issue6655)
Deprecations
• The start_requests() method of Spider is deprecated, use start() instead, or bothto maintain support
forlowerScrapyversions. (issue456,issue3477,issue4467,issue5627,issue6729)
• The process_start_requests() method of spider middlewares is deprecated, use process_start() in-
stead, or both to maintain support for lower Scrapy versions. (issue 456, issue 3477, issue 4467, issue 5627,
issue6729)
• The __init__ method of priority queue classes (see SCHEDULER_PRIORITY_QUEUE) should now support a
keyword-onlystart_queue_clsparameter. (issue6752)
7.1. Releasenotes 301

ScrapyDocumentation,Release2.13.3
• Spidermiddlewaresthatdon’tsupportasynchronousspideroutputaredeprecated. Theasynciterabledowngrad-
ingfeature,neededforusingsuchmiddlewareswithasynchronouscallbacksandwithotherspidermiddlewares
that produce asynchronous iterables, is also deprecated. Please update all such middlewares to support asyn-
chronousspideroutput. (issue6664)
• Functionsthatwereimportedfromw3lib.urlandre-exportedinscrapy.utils.urlarenowdeprecated,you
shouldimportthemfromw3lib.urldirectly. Theyare:
– scrapy.utils.url.add_or_replace_parameter()
– scrapy.utils.url.add_or_replace_parameters()
– scrapy.utils.url.any_to_uri()
– scrapy.utils.url.canonicalize_url()
– scrapy.utils.url.file_uri_to_path()
– scrapy.utils.url.is_url()
– scrapy.utils.url.parse_data_uri()
– scrapy.utils.url.parse_url()
– scrapy.utils.url.path_to_file_uri()
– scrapy.utils.url.safe_download_url()
– scrapy.utils.url.safe_url_string()
– scrapy.utils.url.url_query_cleaner()
– scrapy.utils.url.url_query_parameter()
(issue4577,issue6583,issue6586)
• HTTP/1.0supportcodeisdeprecated. Itwasdisabledbydefaultandcouldn’tbeusedtogetherwithHTTP/1.1.
Ifyoustillneedit,youshouldwriteyourowndownloadhandlerorcopythecodefromScrapy. Thedeprecations
include:
– scrapy.core.downloader.handlers.http10.HTTP10DownloadHandler
– scrapy.core.downloader.webclient.ScrapyHTTPClientFactory
– scrapy.core.downloader.webclient.ScrapyHTTPPageGetter
– Overriding scrapy.core.downloader.contextfactory.ScrapyClientContextFactory.
getContext()
(issue6634)
• Thefollowingmodulesandfunctionsusedonlyintestsaredeprecated:
– thescrapy/utils/testprocmodule
– thescrapy/utils/testsitemodule
– scrapy.utils.test.assert_gcs_environ()
– scrapy.utils.test.get_ftp_content_and_delete()
– scrapy.utils.test.get_gcs_content_and_delete()
– scrapy.utils.test.mock_google_cloud_storage()
– scrapy.utils.test.skip_if_no_boto()
Ifyouneedtousetheminyourtestsorcode,youcancopythecodefromScrapy. (issue6696)
302 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• scrapy.utils.test.TestSpider is deprecated. If you need an empty spider class you can use scrapy.
utils.spider.DefaultSpiderorcreateyourownsubclassofscrapy.Spider. (issue6678)
• scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware is deprecated. It was disabled by
defaultandisn’tusefulformostoftheexistingwebsites. (issue6523,issue6651,issue6656)
• scrapy.utils.url.escape_ajax()isdeprecated. (issue6523,issue6651)
• scrapy.spiders.init.InitSpiderisdeprecated. Ifyoufindituseful,youcancopyitscodefromScrapy.
(issue6708,issue6714)
• scrapy.utils.versions.scrapy_components_versions() is deprecated, use scrapy.utils.
versions.get_versions()instead. (issue6582)
• BaseDupeFilter.log()isdeprecated. Itdoesnothingandshouldn’tbecalled. (issue4151)
• Passingthespiderargumenttothefollowingmethodsof Scraperisdeprecated:
– close_spider()
– enqueue_scrape()
– handle_spider_error()
– handle_spider_output()
(issue6764)
Newfeatures
• You can now yield the start requests and items of a spider from the start() spider method and from the
process_start()spidermiddlewaremethod,bothasynchronousgenerators.
Thismakesitpossibletouseasynchronouscodetogeneratethosestartrequestsanditems, e.g. readingthem
fromaqueueserviceordatabaseusinganasynchronousclient, withoutworkarounds. (issue456, issue3477,
issue4467,issue5627,issue6729)
• Startrequestsarenowscheduled assoonaspossible.
As a result, their priority is now taken into account as soon as CONCURRENT_REQUESTS is reached. (issue
456,issue3477,issue4467,issue5627,issue6729)
• Crawler.signalshasanewwait_for()method. (issue6729)
• Addedanewscheduler_empty signal. (issue6729)
• Addednewsettings: SCHEDULER_START_DISK_QUEUE andSCHEDULER_START_MEMORY_QUEUE.(issue6729)
• AddedStartSpiderMiddleware,whichsetsis_start_requesttoTrueonstartrequests. (issue6729)
• ExposedanewmethodofCrawler.engine: needs_backout(). (issue6729)
• Added the allow_offsite request meta key that can be used instead of the more general dont_filter re-
quest attribute to skip processing of the request by OffsiteMiddleware (but not by other code that checks
dont_filter). (issue3690,issue6151,issue6366)
• Addedanoptionalbaseclassforspidermiddlewares,BaseSpiderMiddleware,whichcanbehelpfulforwriting
universal spider middlewares without boilerplate and code duplication. The built-in spider middlewares now
inheritfromthisclass. (issue6693,issue6777)
• Scrapy add-ons can now define a class method called update_pre_crawler_settings() to update pre-
crawlersettings. (issue6544,issue6568)
• Addedhelpersformodifyingcomponentprioritydictionarysettings. (issue6614)
7.1. Releasenotes 303

ScrapyDocumentation,Release2.13.3
• Responsesthatuseanunknown/unsupportedencodingnowproduceawarning. IfScrapyknowsthatinstalling
anadditionalpackage(suchasbrotli)willallowdecodingtheresponse,thatwillbementionedinthewarning.
(issue4697,issue6618)
• Addedthespider_exceptions/countstatwhichtracksthetotalcountofexceptions(trackedalsobyper-type
spider_exceptions/*stats). (issue6739,issue6740)
• AddedtheDEFAULT_DROPITEM_LOG_LEVELsettingandthescrapy.exceptions.DropItem.log_levelat-
tributethatallowcustomizingtheloglevelofthemessagethatisloggedwhenanitemisdropped. (issue6603,
issue6608)
• Addedsupportforthe-b, --cookiecurlargumenttoscrapy.Request.from_curl(). (issue6684)
• AddedtheLOG_VERSIONS settingthatallowscustomizingthelistofsoftwarewhoseversionsareloggedwhen
thespiderstarts. (issue6582)
• Added the WARN_ON_GENERATOR_RETURN_VALUE setting that allows disabling run time analysis of callback
codeusedtowarnaboutincorrectreturnstatementsingenerator-basedcallbacks. Youmayneedtodisablethis
settingifthisanalysisbreaksonyourcallbackcode. (issue6731,issue6738)
Improvements
• Removedorpostponedsomecallsof itemadapter.is_item()toincreaseperformance. (issue6719)
• Improvedtheerrormessagewhenrunningascrapycommandthatrequiresaproject(suchasscrapy crawl)
outsideofaprojectdirectory. (issue2349,issue3426)
• AddedanemptyADDONS settingtothesettings.pytemplatefornewprojects. (issue6587)
Bugfixes
• YieldinganitemfromSpider.startorfromSpiderMiddleware.process_startnolongerdelaysthenext
iterationofstartingrequestsanditemsbyupto5seconds. (issue6729)
• Fixedcalculationof items_per_minuteandresponses_per_minutestats. (issue6599)
• Fixedanerrorinitializingscrapy.extensions.feedexport.GCSFeedStorage. (issue6617,issue6628)
• Fixedanerrorrunningscrapy bench. (issue6632,issue6633)
• Fixedduplicatedlogmessagesaboutthereactorandtheeventloop. (issue6636,issue6657)
• Fixedresolvingtypeannotationsof SitemapSpider._parse_sitemap()atruntime,requiredbytoolssuch
asscrapy-poet. (issue6665,issue6671)
• Calling scrapy.utils.reactor.is_asyncio_reactor_installed() without an installed reactor now
raisesanexceptioninsteadofinstallingareactor. (issue6732,issue6735)
• Restoredsupportforthex-gzipcontentencoding. (issue6618)
Documentation
• Documentedthesettingvaluessetinthedefaultprojecttemplate. (issue6762,issue6775)
• Improvedthedocsaboutasynchronousiterablesupportinspidermiddlewares. (issue6688)
• ImprovedthedocsaboutusingDeferred-basedAPIsincoroutine-basedcodeandincludedalistofsuchAPIs.
(issue6677,issue6734,issue6776)
• Improvedthecontributiondocs. (issue6561,issue6575)
• RemovedtheSplashrecommendationfromtheheadlessbrowser suggestion. Wenolongerrecommendusing
Splashandrecommendusingotherheadlessbrowsersolutionsinstead. (issue6642,issue6701)
304 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• AddedthedarkmodetotheHTMLdocumentation. (issue6653)
• Otherdocumentationimprovementsandfixes. (issue4151,issue6526,issue6620,issue6621,issue6622,issue
6623,issue6624,issue6721,issue6723,issue6780)
Packaging
• Switchedfromsetup.pytopyproject.toml. (issue6514,issue6547)
• Switchedthebuildbackendfromsetuptoolstohatchling. (issue6771)
Qualityassurance
• Replacedmostlinterswithruff. (issue6565,issue6576,issue6577,issue6581,issue6584,issue6595,issue
6601,issue6631)
• Improvedaccuracyandperformanceofcollectingtestcoverage. (issue6255,issue6610)
• Fixedanerrorthatpreventedrunningtestsfromdirectoriesotherthanthetoplevelsourcedirectory. (issue6567)
• Reducedtheamountof mockservercallsinteststoimprovetheoveralltestruntime. (issue6637,issue6648)
• Fixedteststhatwererunningthesametestcodemorethanonce. (issue6646,issue6647,issue6650)
• Refactoredteststousemorepytestfeaturesinsteadofunittestoneswherepossible. (issue6678,issue6680,
issue6695,issue6699,issue6700,issue6702,issue6709,issue6710,issue6711,issue6712,issue6725)
• Typehintsimprovementsandfixes. (issue6578,issue6579,issue6593,issue6605,issue6694)
• CI and test improvements and fixes. (issue 5360, issue 6271, issue 6547, issue 6560, issue 6602, issue 6607,
issue6609,issue6613,issue6619,issue6626,issue6679,issue6703,issue6704,issue6716,issue6720,issue
6722,issue6724,issue6741,issue6743,issue6766,issue6770,issue6772,issue6773)
• Codecleanups. (issue6600,issue6606,issue6635,issue6764)
7.1.5 Scrapy 2.12.0 (2024-11-18)
Highlights:
• DroppedsupportforPython3.8,addedsupportforPython3.13
• scrapy.Spider.start_requests()cannowyielditems
• AddedJsonResponse
• AddedCLOSESPIDER_PAGECOUNT_NO_ITEM
Modifiedrequirements
• DroppedsupportforPython3.8. (issue6466,issue6472)
• AddedsupportforPython3.13. (issue6166)
• Minimumversionsincreasedforthesedependencies:
– Twisted: 18.9.0→21.7.0
– cryptography: 36.0.0→37.0.0
– pyOpenSSL:21.0.0→22.0.0
– lxml: 4.4.1→4.6.0
• Removedsetuptoolsfromthedependencylist. (issue6487)
7.1. Releasenotes 305

ScrapyDocumentation,Release2.13.3
Backward-incompatiblechanges
• User-definedcookiesforHTTPSrequestswillhavethesecureflagsettoTrueunlessit’ssettoFalseexplictly.
ThisisimportantwhenthesecookiesarereusedinHTTPrequests,e.g. afteraredirecttoanHTTPURL.(issue
6357)
• The Reppy-based robots.txt parser, scrapy.robotstxt.ReppyRobotParser, was removed, as it doesn’t
supportPython3.9+. (issue5230,issue6099,issue6499)
• The initialization API of scrapy.pipelines.media.MediaPipeline and its subclasses was improved and
it’s possible that some previously working usage scenarios will no longer work. It can only affect you if you
define custom subclasses of MediaPipeline or create instances of these pipelines via from_settings() or
__init__()callsinsteadof from_crawler()calls.
Previously, MediaPipeline.from_crawler() called the from_settings() method if it existed or the
__init__() method otherwise, and then did some additional initialization using the crawler instance. If
thefrom_settings()methodexisted(likeinFilesPipeline)itcalled __init__()tocreatetheinstance.
It wasn’t possible to override from_crawler() without calling MediaPipeline.from_crawler() from it
which,inturn,couldn’tbecalledinsomecases(includingsubclassesof FilesPipeline).
Now, in line with the general usage of from_crawler() and from_settings() and the deprecation of the
lattertherecommendedinitializationorderisthefollowingone:
– All__init__()methodsshouldtakeacrawlerargument. Iftheyalsotakeasettingsargumentthey
shouldignoreit,usingcrawler.settingsinstead. Whentheycall__init__()ofthebaseclassthey
shouldpassthecrawlerargumenttoittoo.
– Afrom_settings()methodshouldn’tbedefined. Class-specificinitializationcodeshouldgointoeither
anoverridenfrom_crawler()methodorinto__init__().
– It’s now possible to override from_crawler() and it’s not necessary to call MediaPipeline.
from_crawler()initifotherrecommendationswerefollowed.
– Ifpipelineinstanceswerecreatedwithfrom_settings()or__init__()calls(whichwasn’tsupported
evenbefore,asitmissedimportantinitializationcode),theyshouldnowbecreatedwithfrom_crawler()
calls.
(issue6540)
• Theresponse_bodyargumentofImagesPipeline.convert_imageisnowpositional-only,asitwaschanged
fromoptionaltorequired. (issue6500)
• The convert argument of scrapy.utils.conf.build_component_list() is now positional-only, as the
precedingargument(custom)wasremoved. (issue6500)
• The overwrite_output argument of scrapy.utils.conf.feed_process_params_from_cli() is now
positional-only,astheprecedingargument(output_format)wasremoved. (issue6500)
Deprecationremovals
• Removedthescrapy.utils.request.request_fingerprint()function,deprecatedinScrapy2.7.0. (is-
sue6212,issue6213)
• Removed support for value "2.6" of setting REQUEST_FINGERPRINTER_IMPLEMENTATION, deprecated in
Scrapy2.7.0. (issue6212,issue6213)
• RFPDupeFiltersubclassesnowrequiresupportingthefingerprinterparameterintheir__init__method,
introducedinScrapy2.7.0. (issue6102,issue6113)
• Removedthescrapy.downloadermiddlewares.decompressionmodule,deprecatedinScrapy2.7.0. (issue
6100,issue6113)
306 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Removedthescrapy.utils.response.response_httprepr()function,deprecatedinScrapy2.6.0. (issue
6111,issue6116)
• Spiders with spider-level HTTP authentication, i.e. with the http_user or http_pass attributes, must now
definehttp_auth_domainaswell,whichwasintroducedinScrapy2.5.1. (issue6103,issue6113)
• Media pipelines methods file_path(), file_downloaded(), get_images(), image_downloaded(),
media_downloaded(), media_to_download(), and thumb_path() must now support an item parameter,
addedinScrapy2.4.0. (issue6107,issue6113)
• The __init__() and from_crawler() methods of feed storage backend classes must now support the
keyword-onlyfeed_optionsparameter,introducedinScrapy2.4.0. (issue6105,issue6113)
• Removed the scrapy.loader.common and scrapy.loader.processors modules, deprecated in Scrapy
2.3.0. (issue6106,issue6113)
• Removedthescrapy.utils.misc.extract_regex()function,deprecatedinScrapy2.3.0. (issue6106,issue
6113)
• Removed the scrapy.http.JSONRequest class, replaced with JsonRequest in Scrapy 1.8.0. (issue 6110,
issue6113)
• scrapy.utils.log.logformatter_adapternolongersupportsmissingargs, level, or msgparameters,
and no longer supports a format parameter, all scenarios that were deprecated in Scrapy 1.0.0. (issue 6109,
issue6116)
• AcustomclassassignedtotheSPIDER_LOADER_CLASSsettingthatdoesnotimplementtheISpiderLoaderin-
terfacewillnowraiseazope.interface.verify.DoesNotImplementexceptionatruntime. Non-compliant
classeshavebeentriggeringadeprecationwarningsinceScrapy1.0.0. (issue6101,issue6113)
• Removedthe--output-format/-tcommandlineoption,deprecatedinScrapy2.1.0. -O <URI>:<FORMAT>
shouldbeusedinstead. (issue6500)
• Runningcrawl()morethanonceonthesameCrawler instance, deprecatedinScrapy2.11.0, nowraisesan
exception. (issue6500)
• Subclassing HttpCompressionMiddleware without support for the crawler argument in __init__() and
withoutacustomfrom_crawler()method,deprecatedinScrapy2.5.0,isnolongerallowed. (issue6500)
• Removed the EXCEPTIONS_TO_RETRY attribute of RetryMiddleware, deprecated in Scrapy 2.10.0. (issue
6500)
• RemovedsupportforS3feedexports withouttheboto3packageinstalled, deprecatedinScrapy2.10.0. (issue
6500)
• Removedthescrapy.extensions.feedexport._FeedSlotclass,deprecatedinScrapy2.10.0. (issue6500)
• Removedthescrapy.pipelines.images.NoimagesDropexception,deprecatedinScrapy2.8.0. (issue6500)
• Theresponse_bodyargumentofImagesPipeline.convert_imageisnowrequired,notpassingitwasdep-
recatedinScrapy2.8.0. (issue6500)
• Removed the custom argument of scrapy.utils.conf.build_component_list(), deprecated in Scrapy
2.10.0. (issue6500)
• Removed the scrapy.utils.reactor.get_asyncio_event_loop_policy() function, deprecated in
Scrapy2.9.0. Useasyncio.get_event_loop()andrelatedstandardlibraryfunctionsinstead. (issue6500)
7.1. Releasenotes 307

ScrapyDocumentation,Release2.13.3
Deprecations
• The from_settings() methods of the Scrapy components that have them are now deprecated.
from_crawler()shouldnowbeusedinstead. Affectedcomponents:
– scrapy.dupefilters.RFPDupeFilter
– scrapy.mail.MailSender
– scrapy.middleware.MiddlewareManager
– scrapy.core.downloader.contextfactory.ScrapyClientContextFactory
– scrapy.pipelines.files.FilesPipeline
– scrapy.pipelines.images.ImagesPipeline
– scrapy.spidermiddlewares.urllength.UrlLengthMiddleware
(issue6540)
• It’snowdeprecatedtohaveafrom_settings()methodbutnofrom_crawler()methodin3rd-partyScrapy
components. You can define a simple from_crawler() method that calls cls.from_settings(crawler.
settings)tofixthisifyoudon’twanttorefactorthecode. Notethatifyouhaveafrom_crawler()method
Scrapywillnotcallthefrom_settings()methodsothelattercanberemoved. (issue6540)
• The initialization API of scrapy.pipelines.media.MediaPipeline and its subclasses was improved and
someoldusagescenariosarenowdeprecated(seealsothe“Backward-incompatiblechanges”section). Specifi-
cally:
– It’sdeprecatedtodefinean__init__()methodthatdoesn’ttakeacrawlerargument.
– It’s deprecated to call an __init__() method without passing a crawler argument. If it’s passed, it’s
alsodeprecatedtopassasettingsargument,whichwillbeignoredanyway.
– Callingfrom_settings()isdeprecated,usefrom_crawler()instead.
– Overridingfrom_settings()isdeprecated,overridefrom_crawler()instead.
(issue6540)
• TheREQUEST_FINGERPRINTER_IMPLEMENTATIONsettingisnowdeprecated. (issue6212,issue6213)
• The scrapy.utils.misc.create_instance() function is now deprecated, use scrapy.utils.misc.
build_from_crawler()instead. (issue5523,issue5884,issue6162,issue6169,issue6540)
• scrapy.core.downloader.Downloader._get_slot_key() is deprecated, use scrapy.core.
downloader.Downloader.get_slot_key()instead. (issue6340,issue6352)
• scrapy.utils.defer.process_chain_both()isnowdeprecated. (issue6397)
• scrapy.twisted_version is now deprecated, you should instead use twisted.version directly (but note
thatit’sanincremental.Versionobject,notatuple). (issue6509,issue6512)
• scrapy.utils.python.flatten() and scrapy.utils.python.iflatten() are now deprecated. (issue
6517,issue6519)
• scrapy.utils.python.equal_attributes()isnowdeprecated. (issue6517,issue6519)
• scrapy.utils.request.request_authenticate() is now deprecated, you should instead just set the
Authorizationheaderdirectly. (issue6517,issue6519)
• scrapy.utils.serialize.ScrapyJSONDecoderisnowdeprecated,itdidn’tcontainanycodesinceScrapy
1.0.0. (issue6517,issue6519)
• scrapy.utils.test.assert_samelines()isnowdeprecated. (issue6517,issue6519)
308 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• scrapy.extensions.feedexport.build_storage() is now deprecated. You can instead call the builder
callabledirectly. (issue6540)
Newfeatures
• scrapy.Spider.start_requests()cannowyielditems. (issue5289,issue6417)
(cid:242) Note
SomespidermiddlewaresmayneedtobeupdatedforScrapy2.12supportbeforeyoucanusethemincom-
binationwiththeabilitytoyielditemsfromstart_requests().
• AddedanewResponse subclass,JsonResponse,forresponseswithaJSONMIMEtype. (issue6069,issue
6171,issue6174)
• The LogStats extension now adds items_per_minute and responses_per_minute to the stats when the
spidercloses. (issue4110,issue4111)
• AddedCLOSESPIDER_PAGECOUNT_NO_ITEM whichallowsclosingthespiderifnoitemswerescrapedinaset
amountoftime. (issue6434)
• User-definedcookiescannowincludethesecurefield. (issue6357)
• AddedcomponentgetterstoCrawler:get_addon(),get_downloader_middleware(),get_extension(),
get_item_pipeline(),get_spider_middleware(). (issue6181)
• Slot delay updates by the AutoThrottle extension based on response latencies can now be disabled for specific
requestsviatheautothrottle_dont_adjust_delay metakey. (issue6246,issue6527)
• IfSPIDER_LOADER_WARN_ONLYissettoTrue,SpiderLoaderdoesnotraiseSyntaxErrorbutemitsawarning
instead. (issue6483,issue6484)
• Added support for multiple-compressed responses (ones with several encodings in the Content-Encoding
header). (issue5143,issue5964,issue6063)
• AddedsupportformultiplestandardvaluesinREFERRER_POLICY.(issue6381)
• Addedsupportforbrotlicffi(previouslynamedbrotlipy). brotliisstillrecommendedbutonlybrotlicffiworkson
PyPy. (issue6263,issue6269)
• AddedMetadataContractthatsetstherequestmeta. (issue6468,issue6469)
Improvements
• ExtendedthelistoffileextensionsthatLinkExtractorignoresbydefault. (issue6074,issue6125)
• scrapy.utils.httpobj.urlparse_cached() is now used in more places instead of urllib.parse.
urlparse(). (issue6228,issue6229)
Bugfixes
• MediaPipelineisnowanabstractclassanditsmethodsthatwereexpectedtobeoverriddeninsubclassesare
nowabstractmethods. (issue6365,issue6368)
• Fixedhandlingofinvalid@-prefixedlinesincontractextraction. (issue6383,issue6388)
• Importingscrapy.extensions.telnetnolongerinstallsthedefaultreactor. (issue6432)
• Reducedlogverbosityfordroppedrequeststhatwasincreasedin2.11.2. (issue6433,issue6475)
7.1. Releasenotes 309

ScrapyDocumentation,Release2.13.3
Documentation
• AddedSECURITY.mdthatdocumentsthesecuritypolicy. (issue5364,issue6051)
• Example code for running Scrapy from a script no longer imports twisted.internet.reactor at the top
level,whichcausedproblemswithnon-defaultreactorswhenthiscodewasusedunmodified. (issue6361,issue
6374)
• DocumentedtheSpiderStateextension. (issue6278,issue6522)
• Otherdocumentationimprovementsandfixes. (issue5920,issue6094,issue6177,issue6200,issue6207,issue
6216,issue6223,issue6317,issue6328,issue6389,issue6394,issue6402,issue6411,issue6427,issue6429,
issue6440,issue6448,issue6449,issue6462,issue6497,issue6506,issue6507,issue6524)
Qualityassurance
• Addedpy.typed,inlinewithPEP561. (issue6058,issue6059)
• Fullycoveredthecodewithtypehints(exceptforthemostcomplicatedparts,mostlyrelatedtotwisted.web.
httpandotherTwistedpartswithouttypehints). (issue5989,issue6097,issue6127,issue6129,issue6130,
issue6133,issue6143,issue6191,issue6268,issue6274,issue6275,issue6276,issue6279,issue6325,issue
6326,issue6333,issue6335,issue6336,issue6337,issue6341,issue6353,issue6356,issue6370,issue6371,
issue6384,issue6385,issue6387,issue6391,issue6395,issue6414,issue6422,issue6460,issue6466,issue
6472,issue6494,issue6498,issue6516)
• ImprovedBanditchecks. (issue6260,issue6264,issue6265)
• Addedpyupgradetothepre-commitconfiguration. (issue6392)
• Added flake8-bugbear, flake8-comprehensions, flake8-debugger, flake8-docstrings,
flake8-string-format and flake8-type-checking to the pre-commit configuration. (issue 6406,
issue6413)
• CI and test improvements and fixes. (issue 5285, issue 5454, issue 5997, issue 6078, issue 6084, issue 6087,
issue6132,issue6153,issue6154,issue6201,issue6231,issue6232,issue6235,issue6236,issue6242,issue
6245,issue6253,issue6258,issue6259,issue6270,issue6272,issue6286,issue6290,issue6296issue6367,
issue6372,issue6403,issue6416,issue6435,issue6489,issue6501,issue6504,issue6511,issue6543,issue
6545)
• Codecleanups. (issue6196,issue6197,issue6198,issue6199,issue6254,issue6257,issue6285,issue6305,
issue6343,issue6349,issue6386,issue6415,issue6463,issue6470,issue6499,issue6505,issue6510,issue
6531,issue6542)
Other
• Issuetrackerimprovements. (issue6066)
7.1.6 Scrapy 2.11.2 (2024-05-14)
Securitybugfixes
• Redirectstonon-HTTPprotocolsarenolongerfollowed. Please,seethe23j4-mw76-5v7hsecurityadvisoryfor
moreinformation. (issue457)
• TheAuthorizationheaderisnowdroppedonredirectstoadifferentscheme(http:// orhttps://) orport,
evenifthedomainisthesame. Please,seethe4qqq-9vqf-3h3fsecurityadvisoryformoreinformation.
• Whenusingsystemproxysettingsthataredifferentfor http:// and https://, redirectstoadifferentURL
schemewillnowalsotriggerthecorrespondingchangeinproxysettingsfortheredirectedrequest. Please,see
thejm3v-qxmh-hxwvsecurityadvisoryformoreinformation. (issue767)
310 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Spider.allowed_domainsisnowenforcedforallrequests,andnotonlyrequestsfromspidercallbacks. (issue
1042,issue2241,issue6358)
• xmliter_lxml()nolongerresolvesXMLentities. (issue6265)
• defusedxml is now used to make scrapy.http.request.rpc.XmlRpcRequest more secure. (issue 6250,
issue6251)
Deprecations
• scrapy.spidermiddlewares.offsite.OffsiteMiddleware (a spider middleware) is now deprecated
and not enabled by default. The new downloader middleware with the same functionality, scrapy.
downloadermiddlewares.offsite.OffsiteMiddleware,isenabledinstead. (issue2241,issue6358)
Bugfixes
• Restoredsupportforbrotlipy,whichhadbeendroppedinScrapy2.11.1infavorofbrotli. (issue6261)
(cid:242) Note
brotlipyisdeprecated,bothinScrapyandupstream. Usebrotliinsteadifyoucan.
• MakeMETAREFRESH_IGNORE_TAGS["noscript"]bydefault. ThispreventsMetaRefreshMiddlewarefrom
followingredirectsthatwouldnotbefollowedbywebbrowserswithJavaScriptenabled. (issue6342,issue6347)
• During feed export, do not close the underlying file from built-in post-processing plugins. (issue 5932, issue
6178,issue6239)
• LinkExtractornowproperlyappliestheuniqueandcanonicalizeparameters. (issue3273,issue6221)
• DonotinitializetheschedulerdiskqueueifJOBDIR isanemptystring. (issue6121,issue6124)
• FixSpider.loggernotloggingcustomextrainformation. (issue6323,issue6324)
• robots.txt files with a non-UTF-8 encoding no longer prevent parsing the UTF-8-compatible (e.g. ASCII)
partsofthedocument. (issue6292,issue6298)
• scrapy.http.cookies.WrappedRequest.get_header()nolongerraisesanexceptionifdefaultisNone.
(issue6308,issue6310)
• Selector now uses scrapy.utils.response.get_base_url() to determine the base URL of a given
Response. (issue6265)
• Themedia_to_download()methodofmediapipelinesnowlogsexceptionsbeforestrippingthem. (issue5067,
issue5068)
• When passing a callback to the parse command, build the callback callable with the right signature. (issue
6182)
Documentation
• AddaFAQentryaboutcreatingblankrequests. (issue6203,issue6208)
• Documentthatscrapy.Selector.typecanbe"json". (issue6328,issue6334)
7.1. Releasenotes 311

ScrapyDocumentation,Release2.13.3
Qualityassurance
• Makebuildsreproducible. (issue5019,issue6322)
• Packagingandtestfixes. (issue6286,issue6290,issue6312,issue6316,issue6344)
7.1.7 Scrapy 2.11.1 (2024-02-14)
Highlights:
• Securitybugfixes.
• SupportforTwisted>=23.8.0.
• Documentationimprovements.
Securitybugfixes
• AddressedReDoSvulnerabilities:
– scrapy.utils.iterators.xmliter is now deprecated in favor of xmliter_lxml(), which
XMLFeedSpidernowuses.
To minimizethe impactof thischange onexisting code, xmliter_lxml() now supportsindicating the
nodenamespacewithaprefixinthenodename,andbigfileswithhighlynestedtreeswhenusinglibxml2
2.7+.
– Fixedregularexpressionsintheimplementationoftheopen_in_browser()function.
Please,seethecc65-xxvf-f7r9securityadvisoryformoreinformation.
• DOWNLOAD_MAXSIZEandDOWNLOAD_WARNSIZEnowalsoapplytothedecompressedresponsebody. Please,see
the7j7m-v7m3-jqm7securityadvisoryformoreinformation.
• Also in relation with the 7j7m-v7m3-jqm7 security advisory, the deprecated scrapy.
downloadermiddlewares.decompressionmodulehasbeenremoved.
• TheAuthorizationheaderisnowdroppedonredirectstoadifferentdomain. Please,seethecw9j-q3vf-hrrv
securityadvisoryformoreinformation.
Modifiedrequirements
• TheTwisteddependencyisnolongerrestrictedto<23.8.0. (issue6024,issue6064,issue6142)
Bugfixes
• TheOSsignalhandlingcodewasrefactoredtonolongeruseprivateTwistedfunctions. (issue6024,issue6064,
issue6112)
Documentation
• ImproveddocumentationforCrawlerinitializationchangesmadeinthe2.11.0release. (issue6057,issue6147)
• ExtendeddocumentationforRequest.meta. (issue5565)
• Fixedthedont_merge_cookiesdocumentation. (issue5936,issue6077)
• AddedalinktoZyte’sexportguidestothefeedexportsdocumentation. (issue6183)
• Added a missing note about backward-incompatible changes in PythonItemExporter to the 2.11.0 release
notes. (issue6060,issue6081)
• Added a missing note about removing the deprecated scrapy.utils.boto.is_botocore() function to the
2.8.0releasenotes. (issue6056,issue6061)
312 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Otherdocumentationimprovements. (issue6128,issue6144,issue6163,issue6190,issue6192)
Qualityassurance
• AddedPython3.12totheCIconfiguration,re-enabledteststhatweredisabledwhenthepre-releasesupportwas
added. (issue5985,issue6083,issue6098)
• FixedatestissueonPyPy7.3.14. (issue6204,issue6205)
7.1.8 Scrapy 2.11.0 (2023-09-18)
Highlights:
• Spiderscannowmodifysettingsintheirfrom_crawler()methods,e.g. basedonspiderarguments.
• Periodicloggingofstats.
Backward-incompatiblechanges
• Most of the initialization of scrapy.crawler.Crawler instances is now done in crawl(), so the state of
instancesbeforethatmethodiscalledisnowdifferentcomparedtoolderScrapyversions. Wedonotrecommend
usingtheCrawlerinstancesbeforecrawl()iscalled. (issue6038)
• scrapy.Spider.from_crawler() is now called before the initialization of various components previously
initializedin scrapy.crawler.Crawler.__init__()andbeforethesettingsarefinalizedandfrozen. This
changewasneededtoallowchangingthesettingsinscrapy.Spider.from_crawler(). Ifyouwanttoaccess
thefinalsettingvaluesandtheinitializedCrawler attributesinthespidercodeasearlyaspossibleyoucando
thisinscrapy.Spider.start_requests()orinahandleroftheengine_started signal. (issue6038)
• TheTextResponse.json methodnowrequirestheresponsetobeinavalidJSONencoding(UTF-8,UTF-16,
orUTF-32). IfyouneedtodealwithJSONdocumentsinaninvalidencoding, use json.loads(response.
text)instead. (issue6016)
• PythonItemExporterusedthebinaryoutputbydefaultbutitnolongerdoes. (issue6006,issue6007)
Deprecationremovals
• Removed the binary export mode of PythonItemExporter, deprecated in Scrapy 1.1.0. (issue 6006, issue
6007)
(cid:242) Note
If you are using this Scrapy version on Scrapy Cloud with a stack that includes an older
Scrapy version and get a “TypeError: Unexpected options: binary” error, you may need to add
scrapinghub-entrypoint-scrapy >= 0.14.1toyourprojectrequirementsorswitchtoastackthatin-
cludesScrapy2.11.
• Removed the CrawlerRunner.spiders attribute, deprecated in Scrapy 1.0.0, use CrawlerRunner.
spider_loaderinstead. (issue6010)
• The scrapy.utils.response.response_httprepr() function, deprecated in Scrapy 2.6.0, has now been
removed. (issue6111)
7.1. Releasenotes 313

ScrapyDocumentation,Release2.13.3
Deprecations
• Runningcrawl()morethanonceonthesamescrapy.crawler.Crawlerinstanceisnowdeprecated. (issue
1587,issue6040)
Newfeatures
• Spiders can now modify settings in their from_crawler() method, e.g. based on spider arguments. (issue
1305,issue1580,issue2392,issue3663,issue6038)
• AddedthePeriodicLogextensionwhichcanbeenabledtologstatsand/ortheirdifferencesperiodically. (issue
5926)
• OptimizedthememoryusageinTextResponse.json byremovingunnecessarybodydecoding. (issue5968,
issue6016)
• Linksto.webpfilesarenowignoredbylinkextractors. (issue6021)
Bugfixes
• Fixedloggingenabledadd-ons. (issue6036)
• FixedMailSenderproducinginvalidmessagebodieswhenthecharsetargumentispassedtosend(). (issue
5096,issue5118)
• Fixedanexceptionwhenaccessingself.EXCEPTIONS_TO_RETRYfromasubclassofRetryMiddleware. (is-
sue6049,issue6050)
• scrapy.settings.BaseSettings.getdictorlist(), used to parse FEED_EXPORT_FIELDS, now handles
tuplevalues. (issue6011,issue6013)
• Callstodatetime.utcnow(),nolongerrecommendedtobeused,havebeenreplacedwithcallstodatetime.
now()withatimezone. (issue6014)
Documentation
• Updatedadeprecatedfunctioncallinapipelineexample. (issue6008,issue6009)
Qualityassurance
• Extendedtypinghints. (issue6003,issue6005,issue6031,issue6034)
• Pinnedbrotlito1.0.9forthePyPytestsas1.1.0breaksthem. (issue6044,issue6045)
• OtherCIandpre-commitimprovements. (issue6002,issue6013,issue6046)
7.1.9 Scrapy 2.10.1 (2023-08-30)
MarkedTwisted >= 23.8.0asunsupported. (issue6024,issue6026)
7.1.10 Scrapy 2.10.0 (2023-08-04)
Highlights:
• AddedPython3.12support,droppedPython3.7support.
• Thenewadd-onsframeworksimplifiesconfiguring3rd-partycomponentsthatsupportit.
• Exceptionstoretrycannowbeconfigured.
• Manyfixesandimprovementsforfeedexports.
314 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Modifiedrequirements
• DroppedsupportforPython3.7. (issue5953)
• AddedsupportfortheupcomingPython3.12. (issue5984)
• Minimumversionsincreasedforthesedependencies:
– lxml: 4.3.0→4.4.1
– cryptography: 3.4.6→36.0.0
• pkg_resourcesisnolongerused. (issue5956,issue5958)
• boto3isnowrecommendedinsteadofbotocoreforexportingtoS3. (issue5833).
Backward-incompatiblechanges
• ThevalueoftheFEED_STORE_EMPTY settingisnowTrueinsteadof False. InearlierScrapyversionsempty
files were created even when this setting was False (which was a bug that is now fixed), so the new default
shouldkeeptheoldbehavior. (issue872,issue5847)
Deprecationremovals
• WhenafunctionisassignedtotheFEED_URI_PARAMS setting,returningNoneormodifyingtheparamsinput
parameter,deprecatedinScrapy2.6,isnolongersupported. (issue5994,issue5996)
• Thescrapy.utils.reqsermodule,deprecatedinScrapy2.6,isremoved. (issue5994,issue5996)
• The scrapy.squeues classes PickleFifoDiskQueueNonRequest, PickleLifoDiskQueueNonRequest,
MarshalFifoDiskQueueNonRequest,andMarshalLifoDiskQueueNonRequest,deprecatedinScrapy2.6,
areremoved. (issue5994,issue5996)
• The property open_spiders and the methods has_capacity and schedule of scrapy.core.engine.
ExecutionEngine,deprecatedinScrapy2.6,areremoved. (issue5994,issue5998)
• Passingaspiderargumenttothespider_is_idle(),crawl()anddownload()methodsofscrapy.core.
engine.ExecutionEngine,deprecatedinScrapy2.6,isnolongersupported. (issue5994,issue5998)
Deprecations
• scrapy.utils.datatypes.CaselessDict is deprecated, use scrapy.utils.datatypes.
CaseInsensitiveDictinstead. (issue5146)
• Passingthecustomargumenttoscrapy.utils.conf.build_component_list()isdeprecated,itwasused
inthepasttomergeFOOandFOO_BASEsettingvaluesbutnowScrapyusesscrapy.settings.BaseSettings.
getwithbase()todothesame. Codethatusesthisargumentandcannotbeswitchedtogetwithbase()can
beswitchedtomergingthevaluesexplicitly. (issue5726,issue5923)
Newfeatures
• AddedsupportforScrapyadd-ons. (issue5950)
• AddedtheRETRY_EXCEPTIONS settingthatconfigureswhichexceptionswillberetriedbyRetryMiddleware.
(issue2701,issue5929)
• Added the possiiblity to close the spider if no items were produced in the specified time, configured by
CLOSESPIDER_TIMEOUT_NO_ITEM.(issue5979)
• AddedsupportfortheAWS_REGION_NAME settingtofeedexports. (issue5980)
• Addedsupportforusingpathlib.PathobjectsthatrefertoabsoluteWindowspathsintheFEEDSsetting. (issue
5939)
7.1. Releasenotes 315

ScrapyDocumentation,Release2.13.3
Bugfixes
• FixedcreatingemptyfeedsevenwithFEED_STORE_EMPTY=False. (issue872,issue5847)
• FixedusingabsoluteWindowspathswhenspecifyingoutputfiles. (issue5969,issue5971)
• FixedproblemswithuploadinglargefilestoS3byswitchingtomultipartuploads(requiresboto3). (issue960,
issue5735,issue5833)
• FixedtheJSONexporterwritingextracommaswhensomeexceptionsoccur. (issue3090,issue5952)
• Fixedthe“readofclosedfile”errorintheCSVexporter. (issue5043,issue5705)
• Fixed an error when a component added by the class object throws NotConfigured with a message. (issue
5950,issue5992)
• Addedthemissingscrapy.settings.BaseSettings.pop()method. (issue5959,issue5960,issue5963)
• AddedCaseInsensitiveDictasareplacementforCaselessDictthatfixessomeAPIinconsistencies. (issue
5146)
Documentation
• Documentedscrapy.Spider.update_settings(). (issue5745,issue5846)
• Documented possible problems with early Twisted reactor installation and their solutions. (issue 5981, issue
6000)
• Addedexamplesofmakingadditionalrequestsincallbacks. (issue5927)
• Improvedthefeedexportdocs. (issue5579,issue5931)
• Clarifiedthedocsaboutrequestobjectsonredirection. (issue5707,issue5937)
Qualityassurance
• AddedsupportforrunningtestsagainsttheinstalledScrapyversion. (issue4914,issue5949)
• Extendedtypinghints. (issue5925,issue5977)
• Fixedthetest_utils_asyncio.AsyncioTest.test_set_asyncio_event_looptest. (issue5951)
• Fixedthetest_feedexport.BatchDeliveriesTest.test_batch_path_differtestonWindows. (issue
5847)
• EnabledCIrunsforPython3.11onWindows. (issue5999)
• Simplifiedskippingteststhatdependonuvloop. (issue5984)
• Fixedtheextra-deps-pinnedtoxenv. (issue5948)
• Implementedcleanups. (issue5965,issue5986)
7.1.11 Scrapy 2.9.0 (2023-05-08)
Highlights:
• Per-domaindownloadsettings.
• Compatibilitywithnewcryptographyandnewparsel.
• JMESPathselectorsfromthenewparsel.
• Bugfixes.
316 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Deprecations
• scrapy.extensions.feedexport._FeedSlot is renamed to scrapy.extensions.feedexport.
FeedSlotandtheoldnameisdeprecated. (issue5876)
Newfeatures
• Settings corresponding to DOWNLOAD_DELAY, CONCURRENT_REQUESTS_PER_DOMAIN and
RANDOMIZE_DOWNLOAD_DELAY can now be set on a per-domain basis via the new DOWNLOAD_SLOTS
setting. (issue5328)
• Added TextResponse.jmespath(), a shortcut for JMESPath selectors available since parsel 1.8.1. (issue
5894,issue5915)
• Addedfeed_slot_closed andfeed_exporter_closed signals. (issue5876)
• Added scrapy.utils.request.request_to_curl(), a function to produce a curl command from a
Requestobject. (issue5892)
• ValuesofFILES_STORE andIMAGES_STORE cannowbepathlib.Pathinstances. (issue5801)
Bugfixes
• FixedawarningwithParsel1.8.1+. (issue5903,issue5918)
• FixedanerrorwhenusingfeedpostprocessingwithS3storage. (issue5500,issue5581)
• Addedthemissingscrapy.settings.BaseSettings.setdefault()method. (issue5811,issue5821)
• Fixed an error when using cryptography 40.0.0+ and DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING is en-
abled. (issue5857,issue5858)
• ThechecksumsreturnedbyFilesPipelineforfilesonGoogleCloudStoragearenolongerBase64-encoded.
(issue5874,issue5891)
• scrapy.utils.request.request_from_curl() now supports $-prefixed string values for the curl
--data-raw argument, which are produced by browsers for data that includes certain symbols. (issue 5899,
issue5901)
• Theparsecommandnowalsoworkswithasyncgeneratorcallbacks. (issue5819,issue5824)
• ThegenspidercommandnowproperlyworkswithHTTPSURLs. (issue3553,issue5808)
• Improvedhandlingofasyncioloops. (issue5831,issue5832)
• LinkExtractornowskipscertainmalformedURLsinsteadofraisinganexception. (issue5881)
• scrapy.utils.python.get_func_args()nowsupportsmoretypesofcallables. (issue5872,issue5885)
• Fixedanerrorwhenprocessingnon-UTF8valuesof Content-Typeheaders. (issue5914,issue5917)
• Fixed an error breaking user handling of send failures in scrapy.mail.MailSender.send(). (issue 1611,
issue5880)
Documentation
• Expandedcontributingdocs. (issue5109,issue5851)
• Addedblacken-docstopre-commitandreformattedthedocswithit. (issue5813,issue5816)
• FixedaJSissue. (issue5875,issue5877)
• Fixedmake htmlview. (issue5878,issue5879)
• Fixedtyposandothersmallerrors. (issue5827,issue5839,issue5883,issue5890,issue5895,issue5904)
7.1. Releasenotes 317

ScrapyDocumentation,Release2.13.3
Qualityassurance
• Extendedtypinghints. (issue5805,issue5889,issue5896)
• TestsformostoftheexamplesinthedocsarenowrunasapartofCI,foundproblemswerefixed. (issue5816,
issue5826,issue5919)
• RemovedusageofdeprecatedPythonclasses. (issue5849)
• Silencedinclude-ignoredwarningsfromcoverage. (issue5820)
• Fixedarandomfailureofthetest_feedexport.test_batch_path_differtest. (issue5855,issue5898)
• Updateddocstringstomatchoutputproducedbyparsel1.8.1sothattheydon’tcausetestfailures. (issue5902,
issue5919)
• OtherCIandpre-commitimprovements. (issue5802,issue5823,issue5908)
7.1.12 Scrapy 2.8.0 (2023-02-02)
Thisisamaintenancerelease,withminorfeatures,bugfixes,andcleanups.
Deprecationremovals
• Thescrapy.utils.gz.read1function,deprecatedinScrapy2.0,hasnowbeenremoved. Usetheread1()
methodofGzipFileinstead. (issue5719)
• Thescrapy.utils.python.to_native_strfunction,deprecatedinScrapy2.0,hasnowbeenremoved. Use
scrapy.utils.python.to_unicode()instead. (issue5719)
• Thescrapy.utils.python.MutableChain.nextmethod,deprecatedinScrapy2.0,hasnowbeenremoved.
Use__next__()instead. (issue5719)
• The scrapy.linkextractors.FilteringLinkExtractor class, deprecated in Scrapy 2.0, has now been
removed. UseLinkExtractorinstead. (issue5720)
• SupportforusingenvironmentvariablesprefixedwithSCRAPY_tooverridesettings,deprecatedinScrapy2.0,
hasnowbeenremoved. (issue5724)
• Support for the noconnect query string argument in proxy URLs, deprecated in Scrapy 2.0, has now been
removed. Weexpectproxiesthatusedtoneedittoworkfinewithoutit. (issue5731)
• The scrapy.utils.python.retry_on_eintr function, deprecated in Scrapy 2.3, has now been removed.
(issue5719)
• The scrapy.utils.python.WeakKeyCache class, deprecated in Scrapy 2.4, has now been removed. (issue
5719)
• Thescrapy.utils.boto.is_botocore()function,deprecatedinScrapy2.4,hasnowbeenremoved. (issue
5719)
Deprecations
• scrapy.pipelines.images.NoimagesDropisnowdeprecated. (issue5368,issue5489)
• ImagesPipeline.convert_image must now accept a response_body parameter. (issue 3055, issue 3689,
issue4753)
318 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Newfeatures
• Appliedblackcodingstyletofilesgeneratedwiththegenspiderandstartprojectcommands. (issue5809,
issue5814)
• FEED_EXPORT_ENCODING isnowsetto"utf-8"inthe settings.pyfilethatthestartproject command
generates. With this value, JSON exports won’t force the use of escape sequences for non-ASCII characters.
(issue5797,issue5800)
• TheMemoryUsageextensionnowlogsthepeakmemoryusageduringchecks,andthebinaryunitMiBisnow
usedtoavoidconfusion. (issue5717,issue5722,issue5727)
• ThecallbackparameterofRequest cannowbesettoscrapy.http.request.NO_CALLBACK(),todistin-
guishitfromNone,asthelatterindicatesthatthedefaultspidercallback(parse())istobeused. (issue5798)
Bugfixes
• EnabledunsafelegacySSLrenegotiationtofixaccesstosomeoutdatedwebsites. (issue5491,issue5790)
• FixedSTARTTLS-basedemaildeliverynotworkingwithTwisted21.2.0andbetter. (issue5386,issue5406)
• Fixedthefinish_exporting()methodofitemexportersnotbeingcalledforemptyfiles. (issue5537,issue
5758)
• FixedHTTP/2responsesgettingonlythelastvalueforaheaderwhenmultipleheaderswiththesamenameare
received. (issue5777)
• Fixedanexceptionraisedbytheshell commandonsomecaseswhenusingasyncio. (issue5740,issue5742,
issue5748,issue5759,issue5760,issue5771)
• When using CrawlSpider, callback keyword arguments (cb_kwargs) added to a request in the
process_requestcallbackofaRulewillnolongerbeignored. (issue5699)
• Theimagespipelinenolongerre-encodesJPEGfiles. (issue3055,issue3689,issue4753)
• FixedthehandlingoftransparentWebPimagesbytheimagespipeline. (issue3072,issue5766,issue5767)
• scrapy.shell.inspect_response()nolongerinhibitsSIGINT(Ctrl+C).(issue2918)
• LinkExtractorwithunique=FalsenolongerfiltersoutlinksthathaveidenticalURLand text. (issue3798,
issue3799,issue4695,issue5458)
• RobotsTxtMiddleware now ignores URL protocols that do not support robots.txt (data://, file://).
(issue5807)
• SilencedthefilelockdebuglogmessagesintroducedinScrapy2.6. (issue5753,issue5754)
• Fixed the output of scrapy -h showing an unintended **commands** line. (issue 5709, issue 5711, issue
5712)
• Madetheactiveprojectindicationintheoutputofcommandsmoreclear. (issue5715)
Documentation
• DocumentedhowtodebugspidersfromVisualStudioCode. (issue5721)
• DocumentedhowDOWNLOAD_DELAY affectsper-domainconcurrency. (issue5083,issue5540)
• Improvedconsistency. (issue5761)
• Fixedtypos. (issue5714,issue5744,issue5764)
7.1. Releasenotes 319

ScrapyDocumentation,Release2.13.3
Qualityassurance
• Appliedblackcodingstyle,sortedimportstatements,andintroducedpre-commit. (issue4654,issue4658,issue
5734,issue5737,issue5806,issue5810)
• Switchedfromos.pathtopathlib. (issue4916,issue4497,issue5682)
• AddressedmanyissuesreportedbyPylint. (issue5677)
• Improvedcodereadability. (issue5736)
• Improvedpackagemetadata. (issue5768)
• Removeddirectinvocationsof setup.py. (issue5774,issue5776)
• RemovedunnecessaryOrderedDictusages. (issue5795)
• Removedunnecessary__str__definitions. (issue5150)
• Removedobsoletecodeandcomments. (issue5725,issue5729,issue5730,issue5732)
• Fixed test and CI issues. (issue 5749, issue 5750, issue 5756, issue 5762, issue 5765, issue 5780, issue 5781,
issue5782,issue5783,issue5785,issue5786)
7.1.13 Scrapy 2.7.1 (2022-11-02)
Newfeatures
• Relaxedtherestrictionintroducedin2.6.2sothattheProxy-Authorizationheadercanagainbesetexplicitly,
as long as the proxy URL in the proxy metadata has no other credentials, and for as long as that proxy URL
remainsthesame;thisrestorescompatibilitywithscrapy-zyte-smartproxy2.1.0andolder(issue5626).
Bugfixes
• Using-O/--overwrite-outputand-t/--output-formatoptionstogethernowproducesanerrorinsteadof
ignoringtheformeroption(issue5516,issue5605).
• ReplaceddeprecatedasyncioAPIsthatimplicitlyusethecurrenteventloopwithcodethatexplicitlyrequests
aloopfromtheeventlooppolicy(issue5685,issue5689).
• FixedusesofdeprecatedScrapyAPIsinScrapyitself(issue5588,issue5589).
• FixedusesofadeprecatedPillowAPI(issue5684,issue5692).
• Improvedcodethatchecksifgeneratorsreturnvalues,sothatitnolongerfailsondecoratedmethodsandpartial
methods(issue5323,issue5592,issue5599,issue5691).
Documentation
• UpgradedtheCodeofConducttoContributorCovenantv2.1(issue5698).
• Fixedtypos(issue5681,issue5694).
Qualityassurance
• Re-enabledsomeerroneouslydisabledflake8checks(issue5688).
• Ignoredharmlessdeprecationwarningsfromtypingintests(issue5686,issue5697).
• ModernizedourCIconfiguration(issue5695,issue5696).
320 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.14 Scrapy 2.7.0 (2022-10-17)
Highlights:
• AddedPython3.11support,droppedPython3.6support
• Improvedsupportforasynchronouscallbacks
• Asynciosupportisenabledbydefaultonnewprojects
• Outputnamesofitemfieldscannowbearbitrarystrings
• Centralizedrequestfingerprintingconfigurationisnowpossible
Modifiedrequirements
Python3.7orgreaterisnowrequired;supportforPython3.6hasbeendropped. SupportfortheupcomingPython3.11
hasbeenadded.
Theminimumrequiredversionofsomedependencieshaschangedaswell:
• lxml: 3.5.0→4.3.0
• Pillow(imagespipeline): 4.0.0→7.1.0
• zope.interface: 5.0.0→5.1.0
(issue5512,issue5514,issue5524,issue5563,issue5664,issue5670,issue5678)
Deprecations
• ImagesPipeline.thumb_path mustnowacceptanitemparameter(issue5504,issue5508).
• Thescrapy.downloadermiddlewares.decompressionmoduleisnowdeprecated(issue5546,issue5547).
Newfeatures
• Theprocess_spider_output()methodofspidermiddlewarescannowbedefinedasanasynchronousgen-
erator(issue4978).
• TheoutputofRequestcallbacksdefinedascoroutinesisnowprocessedasynchronously(issue4978).
• CrawlSpidernowsupportsasynchronouscallbacks(issue5657).
• Newprojectscreatedwiththestartproject commandhaveasynciosupport enabledbydefault(issue5590,
issue5679).
• The FEED_EXPORT_FIELDS setting can now be defined as a dictionary to customize the output name of item
fields, lifting the restriction that required output names to be valid Python identifiers, e.g. preventing them to
havewhitespace(issue1008,issue3266,issue3696).
• YoucannowcustomizerequestfingerprintingthroughthenewREQUEST_FINGERPRINTER_CLASS setting,in-
stead of having to change it on every Scrapy component that relies on request fingerprinting (issue 900, issue
3420,issue4113,issue4762,issue4524).
• jsonlisnowsupportedandencouragedasafileextensionforJSONLinesfiles(issue4848).
• ImagesPipeline.thumb_path nowreceivesthesourceitem(issue5504,issue5508).
Bugfixes
• WhenusingGoogleCloudStoragewithamediapipeline,FILES_EXPIRESnowalsoworkswhenFILES_STORE
doesnotpointattherootofyourGoogleCloudStoragebucket(issue5317,issue5318).
• Theparsecommandnowsupportsasynchronouscallbacks(issue5424,issue5577).
7.1. Releasenotes 321

ScrapyDocumentation,Release2.13.3
• Whenusingtheparse commandwithaURLforwhichthereisnoavailablespider,anexceptionisnolonger
raised(issue3264,issue3265,issue5375,issue5376,issue5497).
• TextResponse now gives higher priority to the byte order mark when determining the text encoding of the
responsebody,followingtheHTMLlivingstandard(issue5601,issue5611).
• MIMEsniffingtakestheresponsebodyintoaccountinFTPandHTTP/1.0requests,aswellasincachedrequests
(issue4873).
• MIMEsniffingnowdetectsvalidHTML5documentsevenifthehtmltagismissing(issue4873).
• An exception is now raised if ASYNCIO_EVENT_LOOP has a value that does not match the asyncio event loop
actuallyinstalled(issue5529).
• FixedHeaders.getlistreturningonlythelastheader(issue5515,issue5526).
• FixedLinkExtractornotignoringthetar.gzfileextensionbydefault(issue1837,issue2067,issue4066)
Documentation
• ClarifiedthereturntypeofSpider.parse(issue5602,issue5608).
• ToenableHttpCompressionMiddleware todobrotlicompression,installingbrotliisnowrecommendedin-
steadofinstallingbrotlipy,astheformerprovidesamorerecentversionofbrotli.
• Signaldocumentationnowmentionscoroutinesupportandusesitincodeexamples(issue4852,issue5358).
• Avoidinggettingbanned nowrecommendsCommonCrawlinsteadofGooglecache(issue3582,issue5432).
• ThenewComponentstopiccoversenforcingrequirementsonScrapycomponents,likedownloadermiddlewares,
extensions, item pipelines, spider middlewares, and more; Enforcing asyncio as a requirement has also been
added(issue4978).
• Settingsnowindicatesthatsettingvaluesmustbepicklable(issue5607,issue5629).
• Removedoutdateddocumentation(issue5446,issue5373,issue5369,issue5370,issue5554).
• Fixedtypos(issue5442,issue5455,issue5457,issue5461,issue5538,issue5553,issue5558,issue5624,issue
5631).
• Fixedotherissues(issue5283,issue5284,issue5559,issue5567,issue5648,issue5659,issue5665).
Qualityassurance
• Addedacontinuousintegrationjobtoruntwinecheck(issue5655,issue5656).
• Addressedtestissuesandwarnings(issue5560,issue5561,issue5612,issue5617,issue5639,issue5645,issue
5662,issue5671,issue5675).
• Cleanedupcode(issue4991,issue4995,issue5451,issue5487,issue5542,issue5667,issue5668,issue5672).
• Appliedminorcodeimprovements(issue5661).
7.1.15 Scrapy 2.6.3 (2022-09-27)
• AddedsupportforpyOpenSSL22.1.0,removingsupportforSSLv3(issue5634,issue5635,issue5636).
• Upgradedtheminimumversionsofthefollowingdependencies:
– cryptography: 2.0→3.3
– pyOpenSSL:16.2.0→21.0.0
– service_identity: 16.0.0→18.1.0
– Twisted: 17.9.0→18.9.0
322 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
– zope.interface: 4.1.3→5.0.0
(issue5621,issue5632)
• Fixestestanddocumentationissues(issue5612,issue5617,issue5631).
7.1.16 Scrapy 2.6.2 (2022-07-25)
Securitybugfix:
• When HttpProxyMiddleware processes a request with proxy metadata, and that proxy metadata includes
proxycredentials, HttpProxyMiddleware setsthe Proxy-Authorizationheader, butonlyifthatheaderis
notalreadyset.
Therearethird-partyproxy-rotationdownloadermiddlewaresthatsetdifferentproxymetadataeverytimethey
processarequest.
Because of request retries and redirects, the same request can be processed by downloader middlewares more
thanonce,includingbothHttpProxyMiddlewareandanythird-partyproxy-rotationdownloadermiddleware.
Thesethird-partyproxy-rotationdownloadermiddlewarescouldchangetheproxymetadataofarequesttoanew
value, but fail to remove the Proxy-Authorization header from the previous value of the proxy metadata,
causingthecredentialsofoneproxytobesenttoadifferentproxy.
Topreventtheunintendedleakingofproxycredentials,thebehaviorofHttpProxyMiddlewareisnowasfollows
whenprocessingarequest:
– If the request being processed defines proxy metadata that includes credentials, the
Proxy-Authorizationheaderisalwaysupdatedtofeaturethosecredentials.
– Iftherequestbeingprocesseddefinesproxy metadatawithoutcredentials,theProxy-Authorization
headerisremovedunlessitwasoriginallydefinedforthesameproxyURL.
To remove proxy credentials while keeping the same proxy URL, remove the Proxy-Authorization
header.
– If the request has no proxy metadata, or that metadata is a falsy value (e.g. None), the
Proxy-Authorizationheaderisremoved.
ItisnolongerpossibletosetaproxyURLthroughtheproxymetadatabutsetthecredentialsthroughthe
Proxy-Authorizationheader. Setproxycredentialsthroughtheproxy metadatainstead.
Alsofixesthefollowingregressionsintroducedin2.6.0:
• CrawlerProcesssupportsagaincrawlingmultiplespiders(issue5435,issue5436)
• Installing a Twisted reactor before Scrapy does (e.g. importing twisted.internet.reactor somewhere at
the module level) no longer prevents Scrapy from starting, as long as a different reactor is not specified in
TWISTED_REACTOR (issue5525,issue5528)
• Fixed an exception that was being logged after the spider finished under certain conditions (issue 5437, issue
5440)
• The --output/-o command-line parameter supports again a value starting with a hyphen (issue 5444, issue
5445)
• Thescrapy parse -hcommandnolongerthrowsanerror(issue5481,issue5482)
7.1. Releasenotes 323

ScrapyDocumentation,Release2.13.3
7.1.17 Scrapy 2.6.1 (2022-03-01)
Fixesaregressionintroducedin2.6.0thatwouldunsettherequestmethodwhenfollowingredirects.
7.1.18 Scrapy 2.6.0 (2022-03-01)
Highlights:
• Securityfixesforcookiehandling
• Python3.10support
• asynciosupportisnolongerconsideredexperimental,andworksout-of-the-boxonWindowsregardlessofyour
Pythonversion
• Feedexportsnowsupportpathlib.Pathoutputpathsandper-feeditemfilteringandpost-processing
Securitybugfixes
• When a Request object with cookies defined gets a redirect response causing a new Request object to be
scheduled,thecookiesdefinedintheoriginalRequestobjectarenolongercopiedintothenewRequestobject.
Ifyoumanuallysetthe CookieheaderonaRequest objectandthedomainnameoftheredirectURLisnot
anexactmatchforthedomainoftheURLoftheoriginalRequestobject,yourCookieheaderisnowdropped
fromthenewRequestobject.
Theoldbehaviorcouldbeexploitedbyanattackertogainaccesstoyourcookies. Please,seethecjvr-mfj7-j4j8
securityadvisoryformoreinformation.
(cid:242) Note
Itisstillpossibletoenablethesharingofcookiesbetweendifferentdomainswithashareddomainsuffix(e.g.
example.comandanysubdomain)bydefiningtheshareddomainsuffix(e.g. example.com)asthecookie
domainwhendefiningyourcookies. SeethedocumentationoftheRequestclassformoreinformation.
• Whenthedomainofacookie,eitherreceivedintheSet-CookieheaderofaresponseordefinedinaRequest
object, issettoapublicsuffix, thecookieisnowignoredunlessthecookiedomainisthesameastherequest
domain.
Theoldbehaviorcouldbeexploitedbyanattackertoinjectcookiesfromacontrolleddomainintoyourcookiejar
that could be sent to other domains not controlled by the attacker. Please, see the mfjm-vh54-3f96 security
advisoryformoreinformation.
Modifiedrequirements
• Theh2dependencyisnowoptional,onlyneededtoenableHTTP/2support. (issue5113)
Backward-incompatiblechanges
• TheformdataparameterofFormRequest,ifspecifiedforanon-POSTrequest,nowoverridestheURLquery
string,insteadofbeingappendedtoit. (issue2919,issue3579)
• WhenafunctionisassignedtotheFEED_URI_PARAMSsetting,nowthereturnvalueofthatfunction,andnotthe
paramsinputparameter,willdeterminethefeedURIparameters,unlessthatreturnvalueisNone. (issue4962,
issue4966)
• In scrapy.core.engine.ExecutionEngine, methods crawl(), download(), schedule(), and
spider_is_idle()nowraiseRuntimeErrorifcalledbeforeopen_spider(). (issue5090)
324 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
These methods used to assume that ExecutionEngine.slot had been defined by a prior call to
open_spider(),sotheywereraisingAttributeErrorinstead.
• If the API of the configured scheduler does not meet expectations, TypeError is now raised at startup time.
Before,otherexceptionswouldberaisedatruntime. (issue3559)
• The_encodingfieldofserializedRequestobjectsisnownamedencoding,inlinewithallotherfields(issue
5130)
Deprecationremovals
• scrapy.http.TextResponse.body_as_unicode, deprecated in Scrapy 2.2, has now been removed. (issue
5393)
• scrapy.item.BaseItem,deprecatedinScrapy2.2,hasnowbeenremoved. (issue5398)
• scrapy.item.DictItem,deprecatedinScrapy1.8,hasnowbeenremoved. (issue5398)
• scrapy.Spider.make_requests_from_url,deprecatedinScrapy1.4,hasnowbeenremoved. (issue4178,
issue4356)
Deprecations
• WhenafunctionisassignedtotheFEED_URI_PARAMS setting,returningNoneormodifyingtheparamsinput
parameterisnowdeprecated. Returnanewdictionaryinstead. (issue4962,issue4966)
• scrapy.utils.reqserisdeprecated. (issue5130)
– Insteadof request_to_dict(),usethenewRequest.to_dict()method.
– Instead of request_from_dict(), use the new scrapy.utils.request.request_from_dict()
function.
• In scrapy.squeues, the following queue classes are deprecated: PickleFifoDiskQueueNonRequest,
PickleLifoDiskQueueNonRequest, MarshalFifoDiskQueueNonRequest, and
MarshalLifoDiskQueueNonRequest. You should instead use: PickleFifoDiskQueue,
PickleLifoDiskQueue,MarshalFifoDiskQueue,andMarshalLifoDiskQueue. (issue5117)
• Manyaspectsofscrapy.core.engine.ExecutionEnginethatcomefromatimewhenthisclasscouldhandle
multipleSpiderobjectsatatimehavebeendeprecated. (issue5090)
– Thehas_capacity()methodisdeprecated.
– Theschedule()methodisdeprecated,usecrawl()ordownload()instead.
– Theopen_spidersattributeisdeprecated,usespiderinstead.
– Thespiderparameterisdeprecatedforthefollowingmethods:
∗ spider_is_idle()
∗ crawl()
∗ download()
Instead,callopen_spider()firsttosettheSpiderobject.
• scrapy.utils.response.response_httprepr()isnowdeprecated. (issue4972)
7.1. Releasenotes 325

ScrapyDocumentation,Release2.13.3
Newfeatures
• Youcannowuseitemfilteringtocontrolwhichitemsareexportedtoeachoutputfeed. (issue4575,issue5178,
issue5161,issue5203)
• You can now apply post-processing to feeds, and built-in post-processing plugins are provided for output file
compression. (issue2174,issue5168,issue5190)
• TheFEEDS settingnowsupportspathlib.Pathobjectsaskeys. (issue5383,issue5384)
• EnablingasynciowhileusingWindowsandPython3.8orlaterwillautomaticallyswitchtheasyncioeventloop
toonethatallowsScrapytowork. SeeWindows-specificnotes. (issue4976,issue5315)
• ThegenspidercommandnowsupportsastartURLinsteadofadomainname. (issue4439)
• scrapy.utils.defer gained 2 new functions, deferred_to_future() and
maybe_deferred_to_future(), to help await on Deferreds when using the asyncio reactor. (issue
5288)
• AmazonS3feedexportstoragegainedsupportfortemporarysecuritycredentials(AWS_SESSION_TOKEN)and
endpointcustomization(AWS_ENDPOINT_URL).(issue4998,issue5210)
• NewLOG_FILE_APPEND settingtoallowtruncatingthelogfile. (issue5279)
• Request.cookiesvaluesthatarebool,floatorintarecasttostr. (issue5252,issue5253)
• YoumaynowraiseCloseSpider fromahandlerofthespider_idlesignaltocustomizethereasonwhythe
spiderisstopping. (issue5191)
• When using HttpProxyMiddleware, the proxy URL for non-HTTPS HTTP/1.1 requests no longer needs to
includeaURLscheme. (issue4505,issue4649)
• Allbuilt-inqueuesnowexposeapeekmethodthatreturnsthenextqueueobject(likepop)butdoesnotremove
thereturnedobjectfromthequeue. (issue5112)
Iftheunderlyingqueuedoesnotsupportpeeking(e.g. becauseyouarenotusingqueuelib1.6.1orlater),the
peekmethodraisesNotImplementedError.
• RequestandResponsenowhaveanattributesattributethatmakessubclassingeasier. ForRequest,italso
allows subclasses to work with scrapy.utils.request.request_from_dict(). (issue 1877, issue 5130,
issue5218)
• Theopen()andclose()methodsoftheschedulerarenowoptional. (issue3559)
• HTTP/1.1TunnelErrorexceptionsnowonlytruncateresponsebodieslongerthan1000characters,insteadof
thoselongerthan32characters,makingiteasiertodebugsucherrors. (issue4881,issue5007)
• ItemLoadernowsupportsnon-textresponses. (issue5145,issue5269)
Bugfixes
• The TWISTED_REACTOR and ASYNCIO_EVENT_LOOP settings are no longer ignored if defined in
custom_settings. (issue4485,issue5352)
• Removedamodule-levelTwistedreactorimportthatcouldpreventusingtheasyncioreactor. (issue5357)
• Thestartprojectcommandworkswithexistingfoldersagain. (issue4665,issue4676)
• TheFEED_URI_PARAMS settingnowbehavesasdocumented. (issue4962,issue4966)
• Request.cb_kwargsonceagainallowsthecallbackkeyword. (issue5237,issue5251,issue5264)
• Made scrapy.utils.response.open_in_browser() support more complex HTML. (issue 5319, issue
5320)
• FixedCSVFeedSpider.quotecharbeinginterpretedastheCSVfileencoding. (issue5391,issue5394)
326 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Addedmissingsetuptoolstothelistofdependencies. (issue5122)
• LinkExtractornowalsoworksasexpectedwithlinksthathavecomma-separatedrelattributevaluesinclud-
ingnofollow. (issue5225)
• FixedaTypeErrorthatcouldberaisedduringfeedexportparameterparsing. (issue5359)
Documentation
• asynciosupportisnolongerconsideredexperimental. (issue5332)
• IncludedWindows-specifichelpforasynciousage. (issue4976,issue5315)
• RewroteUsingaheadlessbrowserwithup-to-datebestpractices. (issue4484,issue4613)
• Documentedlocalfilenaminginmediapipelines. (issue5069,issue5152)
• FrequentlyAskedQuestionsnowcoversspiderfilenamecollisionissues. (issue2680,issue3669)
• ProvidedbettercontextandinstructionstodisabletheURLLENGTH_LIMIT setting. (issue5135,issue5250)
• DocumentedthatReppyparserdoesnotsupportPython3.9+. (issue5226,issue5231)
• Documentedtheschedulercomponent. (issue3537,issue3559)
• Documentedthemethodusedbymediapipelinestodetermineifafilehasexpired. (issue5120,issue5254)
• Running multiple spiders in the same process now features scrapy.utils.project.
get_project_settings()usage. (issue5070)
• Running multiple spiders in the same process now covers what happens when you define different per-spider
valuesforsomesettingsthatcannotdifferatruntime. (issue4485,issue5352)
• ExtendedthedocumentationoftheStatsMailerextension. (issue5199,issue5217)
• AddedJOBDIR toSettings. (issue5173,issue5224)
• DocumentedSpider.attribute. (issue5174,issue5244)
• DocumentedTextResponse.urljoin. (issue1582)
• Addedthebody_lengthparametertothedocumentedsignatureoftheheaders_receivedsignal. (issue5270)
• ClarifiedSelectorList.getusageinthetutorial. (issue5256)
• The documentation now features the shortest import path of classes with multiple import paths. (issue 2733,
issue5099)
• quotes.toscrape.comreferencesnowuseHTTPSinsteadofHTTP.(issue5395,issue5396)
• AddedalinktoourDiscordservertoGettinghelp. (issue5421,issue5422)
• Thepronunciationoftheprojectnameisnowofficially/skrepa/. (issue5280,issue5281)
• AddedtheScrapylogototheREADME.(issue5255,issue5258)
• Fixedissuesandimplementedminorimprovements. (issue3155,issue4335,issue5074,issue5098,issue5134,
issue5180,issue5194,issue5239,issue5266,issue5271,issue5273,issue5274,issue5276,issue5347,issue
5356,issue5414,issue5415,issue5416,issue5419,issue5420)
QualityAssurance
• AddedsupportforPython3.10. (issue5212,issue5221,issue5265)
• Significantly reduced memory usage by scrapy.utils.response.response_httprepr(), used by the
DownloaderStatsdownloadermiddleware,whichisenabledbydefault. (issue4964,issue4972)
• Removedusesofthedeprecatedoptparsemodule. (issue5366,issue5374)
7.1. Releasenotes 327

ScrapyDocumentation,Release2.13.3
• Extendedtypinghints. (issue5077,issue5090,issue5100,issue5108,issue5171,issue5215,issue5334)
• Improved tests, fixed CI issues, removed unused code. (issue 5094, issue 5157, issue 5162, issue 5198, issue
5207,issue5208,issue5229,issue5298,issue5299,issue5310,issue5316,issue5333,issue5388,issue5389,
issue5400,issue5401,issue5404,issue5405,issue5407,issue5410,issue5412,issue5425,issue5427)
• Implementedimprovementsforcontributors. (issue5080,issue5082,issue5177,issue5200)
• Implementedcleanups. (issue5095,issue5106,issue5209,issue5228,issue5235,issue5245,issue5246,issue
5292,issue5314,issue5322)
7.1.19 Scrapy 2.5.1 (2021-10-05)
• Securitybugfix:
IfyouuseHttpAuthMiddleware(i.e. thehttp_userandhttp_passspiderattributes)forHTTPauthentica-
tion,anyrequestexposesyourcredentialstotherequesttarget.
Topreventunintendedexposureofauthenticationcredentialstounintendeddomains,youmustnowadditionally
set a new, additional spider attribute, http_auth_domain, and point it to the specific domain to which the
authenticationcredentialsmustbesent.
Ifthehttp_auth_domainspiderattributeisnotset,thedomainofthefirstrequestwillbeconsideredtheHTTP
authenticationtarget,andauthenticationcredentialswillonlybesentinrequeststargetingthatdomain.
IfyouneedtosendthesameHTTPauthenticationcredentialstomultipledomains,youcanusew3lib.http.
basic_auth_header()insteadtosetthevalueoftheAuthorizationheaderofyourrequests.
If you really want your spider to send the same HTTP authentication credentials to any domain, set the
http_auth_domainspiderattributetoNone.
Finally, if you are a user of scrapy-splash, know that this version of Scrapy breaks compatibility with scrapy-
splash0.7.2andearlier. Youwillneedtoupgradescrapy-splashtoagreaterversionforittocontinuetowork.
7.1.20 Scrapy 2.5.0 (2021-04-06)
Highlights:
• OfficialPython3.9support
• ExperimentalHTTP/2support
• Newget_retry_request()functiontoretryrequestsfromspidercallbacks
• Newheaders_received signalthatallowsstoppingdownloadsearly
• NewResponse.protocolattribute
Deprecationremovals
• Removedallcodethatwasdeprecatedin1.7.0andhadnotalreadybeenremovedin2.4.0. (issue4901)
• Removed support for the SCRAPY_PICKLED_SETTINGS_TO_OVERRIDE environment variable, deprecated in
1.8.0. (issue4912)
Deprecations
• Thescrapy.utils.py36moduleisnowdeprecatedinfavorof scrapy.utils.asyncgen. (issue4900)
328 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Newfeatures
• ExperimentalHTTP/2support throughanewdownloadhandlerthatcanbeassignedtothehttpsprotocolin
theDOWNLOAD_HANDLERS setting. (issue1854,issue4769,issue5058,issue5059,issue5066)
• Thenewscrapy.downloadermiddlewares.retry.get_retry_request()functionmaybeusedfromspi-
dercallbacksormiddlewarestohandletheretryingofarequestbeyondthescenariosthatRetryMiddleware
supports. (issue3590,issue3685,issue4902)
• The new headers_received signal gives early access to response headers and allows stopping downloads.
(issue1772,issue4897)
• ThenewResponse.protocolattributegivesaccesstothestringthatidentifiestheprotocolusedtodownload
aresponse. (issue4878)
• Statsnowincludethefollowingentriesthatindicatethenumberofsuccessesandfailuresinstoringfeeds:
feedexport/success_count/<storage type>
feedexport/failed_count/<storage type>
Where <storage type> is the feed storage backend class name, such as FileFeedStorage or
FTPFeedStorage.
(issue3947,issue4850)
• The UrlLengthMiddleware spider middleware now logs ignored URLs with INFO logging level instead of
DEBUG,anditnowincludesthefollowingentryintostatstokeeptrackofthenumberofignoredURLs:
urllength/request_ignored_count
(issue5036)
• TheHttpCompressionMiddlewaredownloadermiddlewarenowlogsthenumberofdecompressedresponses
andthetotalcountofresultingbytes:
httpcompression/response_bytes
httpcompression/response_count
(issue4797,issue4799)
Bugfixes
• FixedinstallationonPyPyinstallingPyDispatcherinadditiontoPyPyDispatcher, whichcouldpreventScrapy
fromworkingdependingonwhichpackagegotimported. (issue4710,issue4814)
• Wheninspectingacallbacktocheckifitisageneratorthatalsoreturnsavalue,anexceptionisnolongerraised
ifthecallbackhasadocstringwithlowerindentationthanthefollowingcode. (issue4477,issue4935)
• The Content-Length header is no longer omitted from responses when using the default, HTTP/1.1 download
handler(seeDOWNLOAD_HANDLERS).(issue5009,issue5034,issue5045,issue5057,issue5062)
• Settingthehandle_httpstatus_allrequestmetakeytoFalsenowhasthesameeffectasnotsettingitatall,
insteadofhavingthesameeffectassettingittoTrue. (issue3851,issue4694)
Documentation
• AddedinstructionstoinstallScrapyinWindowsusingpip. (issue4715,issue4736)
• Loggingdocumentationnowincludesadditionalwaystofilterlogs. (issue4216,issue4257,issue4965)
• CoveredhowtodealwithlonglistsofalloweddomainsintheFAQ.(issue2263,issue3667)
7.1. Releasenotes 329

ScrapyDocumentation,Release2.13.3
• Coveredscrapy-benchinBenchmarking. (issue4996,issue5016)
• Clarifiedthatoneextensioninstanceiscreatedpercrawler. (issue5014)
• Fixedsomeerrorsinexamples. (issue4829,issue4830,issue4907,issue4909,issue5008)
• Fixedsomeexternallinks,typos,andsoon. (issue4892,issue4899,issue4936,issue4942,issue5005,issue
5063)
• ThelistofRequest.metakeysisnowsortedalphabetically. (issue5061,issue5065)
• UpdatedreferencestoScrapinghub,whichisnowcalledZyte. (issue4973,issue5072)
• AddedamentiontocontributorsintheREADME.(issue4956)
• Reducedthetopmarginoflists. (issue4974)
QualityAssurance
• MadePython3.9supportofficial(issue4757,issue4759)
• Extendedtypinghints(issue4895)
• FixeddeprecatedusesoftheTwistedAPI.(issue4940,issue4950,issue5073)
• Madeourtestsrunwiththenewpipresolver. (issue4710,issue4814)
• Addedteststoensurethatcoroutinesupportistested. (issue4987)
• MigratedfromTravisCItoGitHubActions. (issue4924)
• FixedCIissues. (issue4986,issue5020,issue5022,issue5027,issue5052,issue5053)
• Implementedcoderefactorings,stylefixesandcleanups. (issue4911,issue4982,issue5001,issue5002,issue
5076)
7.1.21 Scrapy 2.4.1 (2020-11-17)
• Fixedfeedexportsoverwritesupport(issue4845,issue4857,issue4859)
• FixedtheAsyncIOeventloophandling,whichcouldmakecodehang(issue4855,issue4872)
• FixedtheIPv6-capableDNSresolverCachingHostnameResolverfordownloadhandlersthatcallreactor.
resolve(issue4802,issue4803)
• Fixedtheoutputofthegenspidercommandshowingplaceholdersinsteadoftheimportpathofthegenerated
spidermodule(issue4874)
• MigratedWindowsCIfromAzurePipelinestoGitHubActions(issue4869,issue4876)
7.1.22 Scrapy 2.4.0 (2020-10-11)
Highlights:
• Python3.5supporthasbeendropped.
• Thefile_pathmethodofmediapipelinescannowaccessthesourceitem.
Thisallowsyoutosetadownloadfilepathbasedonitemdata.
• Thenewitem_export_kwargskeyoftheFEEDS settingallowstodefinekeywordparameterstopasstoitem
exporterclasses
• Youcannowchoosewhetherfeedexportsoverwriteorappendtotheoutputfile.
For example, when using the crawl or runspider commands, you can use the -O option instead of -o to
overwritetheoutputfile.
330 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Zstd-compressedresponsesarenowsupportedifzstandardisinstalled.
• Insettings,wheretheimportpathofaclassisrequired,itisnowpossibletopassaclassobjectinstead.
Modifiedrequirements
• Python3.6orgreaterisnowrequired;supportforPython3.5hasbeendropped
Asaresult:
– WhenusingPyPy,PyPy7.2.0orgreaterisnowrequired
– For Amazon S3 storage support in feed exports or media pipelines, botocore 1.4.87 or greater is now
required
– Tousetheimagespipeline,Pillow4.0.0orgreaterisnowrequired
(issue4718,issue4732,issue4733,issue4742,issue4743,issue4764)
Backward-incompatiblechanges
• CookiesMiddlewareonceagaindiscardscookiesdefinedinRequest.headers.
Wedecidedtorevertthisbugfix,introducedinScrapy2.2.0,becauseitwasreportedthatthecurrentimplemen-
tationcouldbreakexistingcode.
Ifyouneedtosetcookiesforarequest,usetheRequest.cookiesparameter.
AfutureversionofScrapywillincludeanew,betterimplementationoftherevertedbugfix.
(issue4717,issue4823)
Deprecationremovals
• scrapy.extensions.feedexport.S3FeedStorage no longer reads the values of access_key and
secret_key from the running project settings when they are not passed to its __init__ method; you must
eitherpassthoseparameterstoits__init__methodoruseS3FeedStorage.from_crawler(issue4356,is-
sue4411,issue4688)
• Rule.process_requestnolongeradmitscallableswhichexpectasinglerequestparameter,ratherthanboth
requestandresponse(issue4818)
Deprecations
• Incustommediapipelines,signaturesthatdonotacceptakeyword-onlyitemparameterinanyofthemethods
thatnowsupportthisparameterarenowdeprecated(issue4628,issue4686)
• In custom feed storage backend classes, __init__ method signatures that do not accept a keyword-only
feed_optionsparameterarenowdeprecated(issue547,issue716,issue4512)
• Thescrapy.utils.python.WeakKeyCacheclassisnowdeprecated(issue4684,issue4701)
• The scrapy.utils.boto.is_botocore() function is now deprecated, use scrapy.utils.boto.
is_botocore_available()instead(issue4734,issue4776)
Newfeatures
• Thefollowingmethodsofmediapipelinesnowacceptanitemkeyword-onlyparametercontainingthesource
item:
– Inscrapy.pipelines.files.FilesPipeline:
∗ file_downloaded()
7.1. Releasenotes 331

ScrapyDocumentation,Release2.13.3
∗ file_path()
∗ media_downloaded()
∗ media_to_download()
– Inscrapy.pipelines.images.ImagesPipeline:
∗ file_downloaded()
∗ file_path()
∗ get_images()
∗ image_downloaded()
∗ media_downloaded()
∗ media_to_download()
(issue4628,issue4686)
• Thenewitem_export_kwargskeyoftheFEEDS settingallowstodefinekeywordparameterstopasstoitem
exporterclasses(issue4606,issue4768)
• Feedexportsgainedoverwritesupport:
– Whenusingthecrawl orrunspider commands, youcanusethe-Ooptioninsteadof -otooverwrite
theoutputfile
– You can use the overwrite key in the FEEDS setting to configure whether to overwrite the output file
(True)orappendtoitscontent(False)
– The__init__andfrom_crawlermethodsoffeedstoragebackendclassesnowreceiveanewkeyword-
onlyparameter,feed_options,whichisadictionaryoffeedoptions
(issue547,issue716,issue4512)
• Zstd-compressedresponsesarenowsupportedifzstandardisinstalled(issue4831)
• Insettings,wheretheimportpathofaclassisrequired,itisnowpossibletopassaclassobjectinstead(issue
3870,issue3873).
This includes also settings where only part of its value is made of an import path, such as
DOWNLOADER_MIDDLEWARES orDOWNLOAD_HANDLERS.
• Downloadermiddlewarescannowoverrideresponse.request.
If a downloader middleware returns a Response object from process_response() or
process_exception()withacustomRequestobjectassignedtoresponse.request:
– TheresponseishandledbythecallbackofthatcustomRequest object,insteadofbeinghandledbythe
callbackoftheoriginalRequestobject
– ThatcustomRequest objectisnowsentastherequestargumenttotheresponse_received signal,
insteadoftheoriginalRequestobject
(issue4529,issue4632)
• WhenusingtheFTPfeedstoragebackend:
– ItisnowpossibletosetthenewoverwritefeedoptiontoFalsetoappendtoanexistingfileinsteadof
overwritingit
– TheFTPpasswordcannowbeomittedifitisnotnecessary
(issue547,issue716,issue4512)
332 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• The __init__ method of CsvItemExporter now supports an errors parameter to indicate how to handle
encodingerrors(issue4755)
• Whenusingasyncio,itisnowpossibletosetacustomasyncioloop(issue4306,issue4414)
• Serializedrequests(seeJobs: pausingandresumingcrawls)nowsupportcallbacksthatarespidermethodsthat
delegateonothercallable(issue4756)
• WhenaresponseislargerthanDOWNLOAD_MAXSIZE,theloggedmessageisnowawarning,insteadofanerror
(issue3874,issue3886,issue4752)
Bugfixes
• The genspider command no longer overwrites existing files unless the --force option is used (issue 4561,
issue4616,issue4623)
• Cookieswithanemptyvaluearenolongerconsideredinvalidcookies(issue4772)
• Therunspidercommandnowsupportsfileswiththe.pywfileextension(issue4643,issue4646)
• TheHttpProxyMiddlewaremiddlewarenowsimplyignoresunsupportedproxyvalues(issue3331,issue4778)
• Checks for generator callbacks with a return statement no longer warn about return statements in nested
functions(issue4720,issue4721)
• Thesystemfilemodecreationmasknolongeraffectsthepermissionsoffilesgeneratedusingthestartproject
command(issue4722)
• scrapy.utils.iterators.xmliter()nowsupportsnamespacednodenames(issue861,issue4746)
• Requestobjectscannowhaveabout: URLs,whichcanworkwhenusingaheadlessbrowser(issue4835)
Documentation
• TheFEED_URI_PARAMS settingisnowdocumented(issue4671,issue4724)
• Improved the documentation of link extractors with an usage example from a spider callback and reference
documentationfortheLink class(issue4751,issue4775)
• ClarifiedtheimpactofCONCURRENT_REQUESTS whenusingtheCloseSpiderextension(issue4836)
• RemovedreferencestoPython2’sunicodetype(issue4547,issue4703)
• Wenowhaveanofficialdeprecationpolicy(issue4705)
• OurdocumentationpoliciesnowcoverusageofSphinx’sversionaddedandversionchangeddirectives,and
wehaveremovedusagesreferencingScrapy1.4.0andearlierversions(issue3971,issue4310)
• Other documentation cleanups (issue 4090, issue 4782, issue 4800, issue 4801, issue 4809, issue 4816, issue
4825)
Qualityassurance
• Extendedtypinghints(issue4243,issue4691)
• Addedtestsforthecheck command(issue4663)
• FixedtestfailuresonDebian(issue4726,issue4727,issue4735)
• ImprovedWindowstestcoverage(issue4723)
• Switchedtoformattedstringliteralswherepossible(issue4307,issue4324,issue4672)
• Modernizedsuper()usage(issue4707)
7.1. Releasenotes 333

ScrapyDocumentation,Release2.13.3
• Othercodeandtestcleanups(issue1790,issue3288,issue4165,issue4564,issue4651,issue4714,issue4738,
issue4745,issue4747,issue4761,issue4765,issue4804,issue4817,issue4820,issue4822,issue4839)
7.1.23 Scrapy 2.3.0 (2020-08-04)
Highlights:
• FeedexportsnowsupportGoogleCloudStorageasastoragebackend
• ThenewFEED_EXPORT_BATCH_ITEM_COUNTsettingallowstodeliveroutputitemsinbatchesofuptothespec-
ifiednumberofitems.
Italsoservesasaworkaroundfordelayedfiledelivery,whichcausesScrapytoonlystartitemdeliveryafterthe
crawlhasfinishedwhenusingcertainstoragebackends(S3,FTP,andnowGCS).
• The base implementation of item loaders has been moved into a separate library, itemloaders, allowing usage
fromoutsideScrapyandaseparatereleaseschedule
Deprecationremovals
• Removedthefollowingclassesandtheirparentmodulesfromscrapy.linkextractors:
– htmlparser.HtmlParserLinkExtractor
– regex.RegexLinkExtractor
– sgml.BaseSgmlLinkExtractor
– sgml.SgmlLinkExtractor
UseLinkExtractorinstead(issue4356,issue4679)
Deprecations
• Thescrapy.utils.python.retry_on_eintrfunctionisnowdeprecated(issue4683)
Newfeatures
• FeedexportssupportGoogleCloudStorage(issue685,issue3608)
• NewFEED_EXPORT_BATCH_ITEM_COUNT settingforbatchdeliveries(issue4250,issue4434)
• Theparsecommandnowallowsspecifyinganoutputfile(issue4317,issue4377)
• Request.from_curl()andcurl_to_request_kwargs()nowalsosupport--data-raw(issue4612)
• Aparsecallbackmaynowbeusedinbuilt-inspidersubclasses,suchasCrawlSpider (issue712,issue732,
issue781,issue4254)
Bugfixes
• FixedtheCSVexportingofdataclassitemsandattr.sitems(issue4667,issue4668)
• Request.from_curl()andcurl_to_request_kwargs()nowsettherequestmethodtoPOSTwhenarequest
bodyisspecifiedandnorequestmethodisspecified(issue4612)
• TheprocessingofANSIescapesequencesinenabledinWindows10.0.14393andlater,whereitisrequiredfor
coloredoutput(issue4393,issue4403)
334 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Documentation
• Updated the OpenSSL cipher list format link in the documentation about the
DOWNLOADER_CLIENT_TLS_CIPHERS setting(issue4653)
• SimplifiedthecodeexampleinWorkingwithdataclassitems(issue4652)
Qualityassurance
• Thebaseimplementationofitemloadershasbeenmovedintoitemloaders(issue4005,issue4516)
• Fixedasilencederrorinsomeschedulertests(issue4644,issue4645)
• RenewedthelocalhostcertificateusedforSSLtests(issue4650)
• Removedcookie-handlingcodespecifictoPython2(issue4682)
• StoppedusingPython2unicodeliteralsyntax(issue4704)
• Stoppedusingabacklashforlinecontinuation(issue4673)
• RemovedunneededentriesfromtheMyPyexceptionlist(issue4690)
• AutomatedtestsnowpassonWindowsaspartofourcontinuousintegrationsystem(issue4458)
• AutomatedtestsnowpassonthelatestPyPyversionforsupportedPythonversionsinourcontinuousintegration
system(issue4504)
7.1.24 Scrapy 2.2.1 (2020-07-17)
• Thestartprojectcommandnolongermakesunintendedchangestothepermissionsoffilesinthedestination
folder,suchasremovingexecutionpermissions(issue4662,issue4666)
7.1.25 Scrapy 2.2.0 (2020-06-24)
Highlights:
• Python3.5.2+isrequirednow
• dataclassobjectsandattrsobjectsarenowvaliditemtypes
• NewTextResponse.json method
• Newbytes_received signalthatallowscancelingresponsedownload
• CookiesMiddlewarefixes
Backward-incompatiblechanges
• Support for Python 3.5.0 and 3.5.1 has been dropped; Scrapy now refuses to run with a Python version lower
than3.5.2,whichintroducedtyping.Type(issue4615)
Deprecations
• TextResponse.body_as_unicode()isnowdeprecated,useTextResponse.textinstead(issue4546,issue
4555,issue4579)
• scrapy.item.BaseItemisnowdeprecated,usescrapy.item.Item instead(issue4534)
7.1. Releasenotes 335

ScrapyDocumentation,Release2.13.3
Newfeatures
• dataclassobjectsandattrsobjectsarenowvaliditemtypes,andanewitemadapterlibrarymakesiteasytowrite
codethatsupportsanyitemtype(issue2749,issue2807,issue3761,issue3881,issue4642)
• AnewTextResponse.jsonmethodallowstodeserializeJSONresponses(issue2444,issue4460,issue4574)
• Anewbytes_received signalallowsmonitoringresponsedownloadprogressandstoppingdownloads(issue
4205,issue4559)
• The dictionaries in the result list of a media pipeline now include a new key, status, which indicates if the
file was downloaded or, if the file was not downloaded, why it was not downloaded; see FilesPipeline.
get_media_requestsformoreinformation(issue2893,issue4486)
• WhenusingGoogleCloudStorageforamediapipeline,awarningisnowloggediftheconfiguredcredentials
donotgranttherequiredpermissions(issue4346,issue4508)
• Link extractors are now serializable, as long as you do not use lambdas for parameters; for example, you can
nowpasslinkextractorsinRequest.cb_kwargsorRequest.meta whenpersistingscheduledrequests(issue
4554)
• UpgradedthepickleprotocolthatScrapyusesfromprotocol2toprotocol4,improvingserializationcapabilities
andperformance(issue4135,issue4541)
• scrapy.utils.misc.create_instance() now raises a TypeError exception if the resulting instance is
None(issue4528,issue4532)
Bugfixes
• CookiesMiddlewarenolongerdiscardscookiesdefinedinRequest.headers(issue1992,issue2400)
• CookiesMiddleware no longer re-encodes cookies defined as bytes in the cookies parameter of the
__init__methodofRequest(issue2400,issue3575)
• When FEEDS defines multiple URIs, FEED_STORE_EMPTY is False and the crawl yields no items, Scrapy no
longerstopsfeedexportsafterthefirstURI(issue4621,issue4626)
• Spider callbacksdefinedusingcoroutinesyntaxnolongerneedtoreturnaniterable,andmayinsteadreturna
Requestobject,anitem,orNone(issue4609)
• Thestartprojectcommandnowensuresthatthegeneratedprojectfoldersandfileshavetherightpermissions
(issue4604)
• Fix a KeyError exception being sometimes raised from scrapy.utils.datatypes.
LocalWeakReferencedCache(issue4597,issue4599)
• WhenFEEDS definesmultipleURIs,logmessagesaboutitemsbeingstorednowcontaininformationfromthe
correspondingfeed,insteadofalwayscontaininginformationaboutonlyoneofthefeeds(issue4619,issue4629)
Documentation
• Addedanewsectionaboutaccessingcb_kwargsfromerrbacks(issue4598,issue4634)
• CoveredchompjsinParsingJavaScriptcode(issue4556,issue4562)
• RemovedfromCoroutinesthewarningabouttheAPIbeingexperimental(issue4511,issue4513)
• RemovedreferencestounsupportedversionsofTwisted(issue4533)
• Updatedthedescriptionofthescreenshotpipelineexample,whichnowusescoroutinesyntaxinsteadofreturning
aDeferred(issue4514,issue4593)
• Removedamisleadingimportlinefromthescrapy.utils.log.configure_logging()codeexample(issue
4510,issue4587)
336 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• The display-on-hover behavior of internal documentation references now also covers links to commands,
Request.meta keys,settingsandsignals(issue4495,issue4563)
• Itisagainpossibletodownloadthedocumentationforofflinereading(issue4578,issue4585)
• Removed backslashes preceding *args and **kwargs in some function and method signatures (issue 4592,
issue4596)
Qualityassurance
• Adjustedthecodebasefurthertoourstyleguidelines(issue4237,issue4525,issue4538,issue4539,issue4540,
issue4542,issue4543,issue4544,issue4545,issue4557,issue4558,issue4566,issue4568,issue4572)
• RemovedremnantsofPython2support(issue4550,issue4553,issue4568)
• Improvedcodesharingbetweenthecrawlandrunspidercommands(issue4548,issue4552)
• Replacedchain(*iterable)withchain.from_iterable(iterable)(issue4635)
• YoumaynowruntheasynciotestswithToxonanyPythonversion(issue4521)
• Updatedtestrequirementstoreflectanincompatibilitywithpytest5.4and5.4.1(issue4588)
• ImprovedSpiderLoadertestcoverageforscenariosinvolvingduplicatespidernames(issue4549,issue4560)
• ConfiguredTravisCItoalsorunthetestswithPython3.5.2(issue4518,issue4615)
• AddedaPylintjobtoTravisCI(issue3727)
• AddedaMypyjobtoTravisCI(issue4637)
• Madeuseofsetliteralsintests(issue4573)
• CleaneduptheTravisCIconfiguration(issue4517,issue4519,issue4522,issue4537)
7.1.26 Scrapy 2.1.0 (2020-04-24)
Highlights:
• NewFEEDS settingtoexporttomultiplefeeds
• NewResponse.ip_addressattribute
Backward-incompatiblechanges
• AssertionErrorexceptionstriggeredbyassertstatementshavebeenreplacedbynewexceptiontypes,tosup-
portrunningPythoninoptimizedmode(see-O)withoutchangingScrapy’sbehaviorinanyunexpectedways.
If you catch an AssertionError exception from Scrapy, update your code to catch the corresponding new
exception.
(issue4440)
Deprecationremovals
• The LOG_UNSERIALIZABLE_REQUESTS setting is no longer supported, use SCHEDULER_DEBUG instead (issue
4385)
• The REDIRECT_MAX_METAREFRESH_DELAY setting is no longer supported, use METAREFRESH_MAXDELAY in-
stead(issue4385)
• The ChunkedTransferMiddleware middleware has been removed, including the entire scrapy.
downloadermiddlewares.chunkedmodule;chunkedtransfersworkoutofthebox(issue4431)
7.1. Releasenotes 337

ScrapyDocumentation,Release2.13.3
• ThespiderspropertyhasbeenremovedfromCrawler,useCrawlerRunner.spider_loaderorinstantiate
SPIDER_LOADER_CLASS withyoursettingsinstead(issue4398)
• TheMultiValueDict,MultiValueDictKeyError,andSiteNodeclasseshavebeenremovedfromscrapy.
utils.datatypes(issue4400)
Deprecations
• TheFEED_FORMATandFEED_URIsettingshavebeendeprecatedinfavorofthenewFEEDS setting(issue1336,
issue3858,issue4507)
Newfeatures
• Anewsetting, FEEDS,allowsconfiguringmultipleoutputfeedswithdifferentsettingseach(issue1336, issue
3858,issue4507)
• Thecrawlandrunspidercommandsnowsupportmultiple-oparameters(issue1336,issue3858,issue4507)
• Thecrawl andrunspider commandsnowsupportspecifyinganoutputformatbyappending:<format>to
theoutputfile(issue1336,issue3858,issue4507)
• ThenewResponse.ip_addressattributegivesaccesstotheIPaddressthatoriginatedaresponse(issue3903,
issue3940)
• Awarningisnowissuedwhenavalueinallowed_domainsincludesaport(issue50,issue3198,issue4413)
• Zshcompletionnowexcludesusedoptionaliasesfromthecompletionlist(issue4438)
Bugfixes
• Requestserializationnolongerbreaksforcallbacksthatarespiderattributeswhichareassignedafunctionwith
adifferentname(issue4500)
• Nonevaluesinallowed_domainsnolongercauseaTypeErrorexception(issue4410)
• Zshcompletionnolongerallowsoptionsafterarguments(issue4438)
• zope.interface5.0.0andlaterversionsarenowsupported(issue4447,issue4448)
• Spider.make_requests_from_url,deprecatedinScrapy1.4.0,nowissuesawarningwhenused(issue4412)
Documentation
• Improved the documentation about signals that allow their handlers to return a Deferred (issue 4295, issue
4390)
• OurPyPIentrynowincludeslinksforourdocumentation,oursourcecoderepositoryandourissuetracker(issue
4456)
• Coveredthecurl2scrapyserviceinthedocumentation(issue4206,issue4455)
• RemovedreferencestotheGuppylibrary,whichonlyworksinPython2(issue4285,issue4343)
• ExtendeduseofInterSphinxtolinktoPython3documentation(issue4444,issue4445)
• AddedsupportforSphinx3.0andlater(issue4475,issue4480,issue4496,issue4503)
Qualityassurance
• Removedwarningsaboutusingold,removedsettings(issue4404)
• Removed a warning about importing StringTransport from twisted.test.proto_helpers in Twisted
19.7.0ornewer(issue4409)
338 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• RemovedoutdatedDebianpackagebuildfiles(issue4384)
• Removedobjectusageasabaseclass(issue4430)
• RemovedcodethataddedsupportforoldversionsofTwistedthatwenolongersupport(issue4472)
• Fixedcodestyleissues(issue4468,issue4469,issue4471,issue4481)
• Removedtwisted.internet.defer.returnValue()calls(issue4443,issue4446,issue4489)
7.1.27 Scrapy 2.0.1 (2020-03-18)
• Response.follow_allnowsupportsanemptyURLiterableasinput(issue4408,issue4420)
• Removed top-level reactor imports to prevent errors about the wrong Twisted reactor being installed when
settingadifferentTwistedreactorusingTWISTED_REACTOR (issue4401,issue4406)
• Fixedtests(issue4422)
7.1.28 Scrapy 2.0.0 (2020-03-03)
Highlights:
• Python2supporthasbeenremoved
• Partialcoroutinesyntaxsupportandexperimentalasynciosupport
• NewResponse.follow_allmethod
• FTPsupportformediapipelines
• NewResponse.certificateattribute
• IPv6supportthroughDNS_RESOLVER
Backward-incompatiblechanges
• Python2supporthasbeenremoved,followingPython2end-of-lifeonJanuary1,2020(issue4091,issue4114,
issue4115,issue4121,issue4138,issue4231,issue4242,issue4304,issue4309,issue4373)
• Retrygaveups(seeRETRY_TIMES)arenowloggedaserrorsinsteadofasdebuginformation(issue3171,issue
3566)
• FileextensionsthatLinkExtractor ignoresbydefaultnowalsoinclude7z,7zip,apk,bz2,cdr,dmg,ico,
iso,tar,tar.gz,webm,andxz(issue1837,issue2067,issue4066)
• TheMETAREFRESH_IGNORE_TAGSsettingisnowanemptylistbydefault,followingwebbrowserbehavior(issue
3844,issue4311)
• TheHttpCompressionMiddlewarenowincludesspacesaftercommasinthevalueoftheAccept-Encoding
headerthatitsets,followingwebbrowserbehavior(issue4293)
• The__init__methodofcustomdownloadhandlers(seeDOWNLOAD_HANDLERS)orsubclassesofthefollowing
downloaderhandlersnolongerreceivesasettingsparameter:
– scrapy.core.downloader.handlers.datauri.DataURIDownloadHandler
– scrapy.core.downloader.handlers.file.FileDownloadHandler
Usethefrom_settingsorfrom_crawlerclassmethodstoexposesuchaparametertoyourcustomdownload
handlers.
(issue4126)
7.1. Releasenotes 339

ScrapyDocumentation,Release2.13.3
• We have refactored the scrapy.core.scheduler.Scheduler class and related queue classes (see
SCHEDULER_PRIORITY_QUEUE,SCHEDULER_DISK_QUEUE andSCHEDULER_MEMORY_QUEUE)tomakeiteasier
toimplementcustomschedulerqueueclasses. SeeChangestoschedulerqueueclassesbelowfordetails.
• Overriddensettingsarenowloggedinadifferentformat. Thisismoreinlinewithsimilarinformationloggedat
startup(issue4199)
Deprecationremovals
• TheScrapyshellnolongerprovidesaselproxyobject,useresponse.selectorinstead(issue4347)
• LevelDBsupporthasbeenremoved(issue4112)
• The following functions have been removed from scrapy.utils.python: isbinarytext, is_writable,
setattr_default,stringify_dict(issue4362)
Deprecations
• UsingenvironmentvariablesprefixedwithSCRAPY_tooverridesettingsisdeprecated(issue4300,issue4374,
issue4375)
• scrapy.linkextractors.FilteringLinkExtractor is deprecated, use scrapy.linkextractors.
LinkExtractorinstead(issue4045)
• ThenoconnectquerystringargumentofproxyURLsisdeprecatedandshouldberemovedfromproxyURLs
(issue4198)
• The nextmethodof scrapy.utils.python.MutableChainisdeprecated, usetheglobalnext()function
orMutableChain.__next__instead(issue4153)
Newfeatures
• Added partial support for Python’s coroutine syntax and experimental support for asyncio and asyncio-
poweredlibraries(issue4010,issue4259,issue4269,issue4270,issue4271,issue4316,issue4318)
• ThenewResponse.follow_all methodoffersthesamefunctionalityasResponse.follow butsupportsan
iterableofURLsasinputandreturnsaniterableofrequests(issue2582,issue4057,issue4286)
• MediapipelinesnowsupportFTPstorage(issue3928,issue3961)
• ThenewResponse.certificateattributeexposestheSSLcertificateoftheserverasatwisted.internet.
ssl.CertificateobjectforHTTPSresponses(issue2726,issue4054)
• AnewDNS_RESOLVER settingallowsenablingIPv6support(issue1031,issue4227)
• AnewSCRAPER_SLOT_MAX_ACTIVE_SIZEsettingallowsconfiguringtheexistingsoftlimitthatpausesrequest
downloadswhenthetotalresponsedatabeingprocessedistoohigh(issue1410,issue3551)
• AnewTWISTED_REACTOR settingallowscustomizingthereactorthatScrapyuses,allowingtoenableasyncio
supportordealwithacommonmacOSissue(issue2905,issue4294)
• Schedulerdiskandmemoryqueuesmaynowusetheclassmethodsfrom_crawlerorfrom_settings(issue
3884)
• ThenewResponse.cb_kwargsattributeservesasashortcutforResponse.request.cb_kwargs(issue4331)
• Response.follow nowsupportsaflagsparameter,forconsistencywithRequest(issue4277,issue4279)
• Itemloaderprocessorscannowberegularfunctions,theynolongerneedtobemethods(issue3899)
• Rulenowacceptsanerrbackparameter(issue4000)
• Requestnolongerrequiresacallbackparameterwhenanerrbackparameterisspecified(issue3586,issue
4008)
340 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• LogFormatternowsupportssomeadditionalmethods:
– download_errorfordownloaderrors
– item_errorforexceptionsraisedduringitemprocessingbyitempipelines
– spider_errorforexceptionsraisedfromspidercallbacks
(issue374,issue3986,issue3989,issue4176,issue4188)
• TheFEED_URIsettingnowsupportspathlib.Pathvalues(issue3731,issue4074)
• Anewrequest_left_downloadersignalissentwhenarequestleavesthedownloader(issue4303)
• Scrapy logs a warning when it detects a request callback or errback that uses yield but also returns a value,
sincethereturnedvaluewouldbelost(issue3484,issue3869)
• SpiderobjectsnowraiseanAttributeErrorexceptioniftheydonothaveastart_urlsattributenorreim-
plement scrapy.spiders.Spider.start_requests(), but have a start_url attribute (issue 4133, issue
4170)
• BaseItemExporter subclasses may now use super().__init__(**kwargs) instead of self.
_configure(kwargs) in their __init__ method, passing dont_fail=True to the parent __init__
methodifneeded,andaccessingkwargsat self._kwargsaftercallingtheirparent __init__method(issue
4193,issue4370)
• Anewkeep_fragmentsparameterof scrapy.utils.request.request_fingerprintallowstogenerate
differentfingerprintsforrequestswithdifferentfragmentsintheirURL(issue4104)
• Download handlers (see DOWNLOAD_HANDLERS) may now use the from_settings and from_crawler class
methodsthatotherScrapycomponentsalreadysupported(issue4126)
• scrapy.utils.python.MutableChain.__iter__ now returns self, allowing it to be used as a sequence
(issue4153)
Bugfixes
• Thecrawlcommandnowalsoexitswithexitcode1whenanexceptionhappensbeforethecrawlingstarts(issue
4175,issue4207)
• LinkExtractor.extract_linksnolongerre-encodesthequerystringorURLsfromnon-UTF-8responses
inUTF-8(issue998,issue1403,issue1949,issue4321)
• Thefirstspidermiddleware(seeSPIDER_MIDDLEWARES)nowalsoprocessesexceptionsraisedfromcallbacks
thataregenerators(issue4260,issue4272)
• RedirectstoURLsstartingwith3slashes(///)arenowsupported(issue4032,issue4042)
• Requestnolongeracceptsstringsasurlsimplybecausetheyhaveacolon(issue2552,issue4094)
• ThecorrectencodingisnowusedforattachnamesinMailSender(issue4229,issue4239)
• RFPDupeFilter,thedefaultDUPEFILTER_CLASS,nolongerwritesanextra\rcharacteroneachlineinWin-
dows,whichmadethesizeoftherequests.seenfileunnecessarilylargeonthatplatform(issue4283)
• Z shell auto-completion now looks for .html files, not .http files, and covers the -h command-line switch
(issue4122,issue4291)
• Addingitemstoascrapy.utils.datatypes.LocalCacheobjectwithoutalimitdefinednolongerraisesa
TypeErrorexception(issue4123)
• Fixed a typo in the message of the ValueError exception raised when scrapy.utils.misc.
create_instance()getsbothsettingsandcrawlersettoNone(issue4128)
7.1. Releasenotes 341

ScrapyDocumentation,Release2.13.3
Documentation
• API documentation now links to an online, syntax-highlighted view of the corresponding source code (issue
4148)
• Linkstounexistingdocumentationpagesnowallowaccesstothesidebar(issue4152,issue4169)
• Cross-referenceswithinourdocumentationnowdisplayatooltipwhenhovered(issue4173,issue4183)
• Improved the documentation about LinkExtractor.extract_links and simplified Link Extractors (issue
4045)
• ClarifiedhowItemLoader.item works(issue3574,issue4099)
• Clarified that logging.basicConfig() should not be used when also using CrawlerProcess (issue 2149,
issue2352,issue3146,issue3960)
• ClarifiedtherequirementsforRequestobjectswhenusingpersistence(issue4124,issue4139)
• Clarifiedhowtoinstallacustomimagepipeline(issue4034,issue4252)
• Fixedthesignaturesofthefile_pathmethodinmediapipelineexamples(issue4290)
• Covered a backward-incompatible change in Scrapy 1.7.0 affecting custom scrapy.core.scheduler.
Schedulersubclasses(issue4274)
• ImprovedtheREADME.rstandCODE_OF_CONDUCT.mdfiles(issue4059)
• Documentationexamplesarenowcheckedaspartofourtestsuiteandwehavefixedsomeoftheissuesdetected
(issue4142,issue4146,issue4171,issue4184,issue4190)
• Fixed logic issues, broken links and typos (issue 4247, issue 4258, issue 4282, issue 4288, issue 4305, issue
4308,issue4323,issue4338,issue4359,issue4361)
• Improvedconsistencywhenreferringtothe__init__methodofanobject(issue4086,issue4088)
• FixedaninconsistencybetweencodeandoutputinScrapyataglance(issue4213)
• Extendedintersphinxusage(issue4147,issue4172,issue4185,issue4194,issue4197)
• WenowusearecentversionofPythontobuildthedocumentation(issue4140,issue4249)
• Cleanedupdocumentation(issue4143,issue4275)
Qualityassurance
• Re-enabledproxyCONNECTtests(issue2545,issue4114)
• AddedBanditsecuritycheckstoourtestsuite(issue4162,issue4181)
• AddedFlake8stylecheckstoourtestsuiteandappliedmanyofthecorrespondingchanges(issue3944, issue
3945,issue4137,issue4157,issue4167,issue4174,issue4186,issue4195,issue4238,issue4246,issue4355,
issue4360,issue4365)
• Improvedtestcoverage(issue4097,issue4218,issue4236)
• Startedreportingslowesttests,andimprovedtheperformanceofsomeofthem(issue4163,issue4164)
• Fixedbrokentestsandrefactoredsometests(issue4014,issue4095,issue4244,issue4268,issue4372)
• ModifiedthetoxconfigurationtoallowrunningtestswithanyPythonversion, runBanditandFlake8testsby
default,andenforceaminimumtoxversionprogrammatically(issue4179)
• Cleanedupcode(issue3937,issue4208,issue4209,issue4210,issue4212,issue4369,issue4376,issue4378)
342 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Changestoschedulerqueueclasses
Thefollowingchangesmayimpactanycustomqueueclassesofalltypes:
• The pushmethodnolongerreceivesasecondpositionalparametercontainingrequest.priority * -1. If
you need that value, get it from the first positional parameter, request, instead, or use the new priority()
methodinscrapy.core.scheduler.ScrapyPriorityQueuesubclasses.
Thefollowingchangesmayimpactcustompriorityqueueclasses:
• Inthe__init__methodorthefrom_crawlerorfrom_settingsclassmethods:
– Theparameterthatusedtocontainafactoryfunction,qfactory,isnowpassedasakeywordparameter
nameddownstream_queue_cls.
– Anewkeywordparameterhasbeenadded: key. Itisastringthatisalwaysanemptystringformemory
queuesandindicatestheJOB_DIRvaluefordiskqueues.
– The parameter for disk queues that contains data from the previous crawl, startprios or
slot_startprios,isnowpassedasakeywordparameternamedstartprios.
– Theserializeparameterisnolongerpassed. Thediskqueueclassmusttakecareofrequestserialization
onitsownbeforewritingtodisk,usingtherequest_to_dict()andrequest_from_dict()functions
fromthescrapy.utils.reqsermodule.
Thefollowingchangesmayimpactcustomdiskandmemoryqueueclasses:
• Thesignatureofthe__init__methodisnow__init__(self, crawler, key).
ThefollowingchangesaffectspecificallytheScrapyPriorityQueueandDownloaderAwarePriorityQueueclasses
fromscrapy.core.schedulerandmayaffectsubclasses:
• Inthe__init__method,mostofthechangesdescribedaboveapply.
__init__maystillreceiveallparametersaspositionalparameters,however:
– downstream_queue_cls,whichreplacedqfactory,mustbeinstantiateddifferently.
qfactorywasinstantiatedwithapriorityvalue(integer).
Instances of downstream_queue_cls should be created using the new ScrapyPriorityQueue.
qfactoryorDownloaderAwarePriorityQueue.pqfactorymethods.
– Thenewkeyparameterdisplacedthestartpriosparameter1positiontotheright.
• Thefollowingclassattributeshavebeenadded:
– crawler
– downstream_queue_cls(detailsabove)
– key(detailsabove)
• Theserializeattributehasbeenremoved(detailsabove)
ThefollowingchangesaffectspecificallytheScrapyPriorityQueueclassandmayaffectsubclasses:
• Anewpriority()methodhasbeenaddedwhich,givenarequest,returnsrequest.priority * -1.
Itisusedinpush()tomakeupfortheremovalofitspriorityparameter.
• Thespiderattributehasbeenremoved. Usecrawler.spiderinstead.
ThefollowingchangesaffectspecificallytheDownloaderAwarePriorityQueueclassandmayaffectsubclasses:
• A new pqueues attribute offers a mapping of downloader slot names to the corresponding instances of
downstream_queue_cls.
7.1. Releasenotes 343

ScrapyDocumentation,Release2.13.3
(issue3884)
7.1.29 Scrapy 1.8.4 (2024-02-14)
Securitybugfixes:
• Due to its ReDoS vulnerabilities, scrapy.utils.iterators.xmliter is now deprecated in favor of
xmliter_lxml(),whichXMLFeedSpidernowuses.
To minimize the impact of this change on existing code, xmliter_lxml() now supports indicating the node
namespaceasaprefixinthenodename,andbigfileswithhighlynestedtreeswhenusinglibxml22.7+.
Please,seethecc65-xxvf-f7r9securityadvisoryformoreinformation.
• DOWNLOAD_MAXSIZEandDOWNLOAD_WARNSIZEnowalsoapplytothedecompressedresponsebody. Please,see
the7j7m-v7m3-jqm7securityadvisoryformoreinformation.
• Alsoinrelationwiththe7j7m-v7m3-jqm7securityadvisory,useofthescrapy.downloadermiddlewares.
decompressionmoduleisdiscouragedandwilltriggerawarning.
• TheAuthorizationheaderisnowdroppedonredirectstoadifferentdomain. Please,seethecw9j-q3vf-hrrv
securityadvisoryformoreinformation.
7.1.30 Scrapy 1.8.3 (2022-07-25)
Securitybugfix:
• When HttpProxyMiddleware processes a request with proxy metadata, and that proxy metadata includes
proxycredentials, HttpProxyMiddleware setsthe Proxy-Authorizationheader, butonlyifthatheaderis
notalreadyset.
Therearethird-partyproxy-rotationdownloadermiddlewaresthatsetdifferentproxymetadataeverytimethey
processarequest.
Because of request retries and redirects, the same request can be processed by downloader middlewares more
thanonce,includingbothHttpProxyMiddlewareandanythird-partyproxy-rotationdownloadermiddleware.
Thesethird-partyproxy-rotationdownloadermiddlewarescouldchangetheproxymetadataofarequesttoanew
value, but fail to remove the Proxy-Authorization header from the previous value of the proxy metadata,
causingthecredentialsofoneproxytobesenttoadifferentproxy.
Topreventtheunintendedleakingofproxycredentials,thebehaviorofHttpProxyMiddlewareisnowasfollows
whenprocessingarequest:
– If the request being processed defines proxy metadata that includes credentials, the
Proxy-Authorizationheaderisalwaysupdatedtofeaturethosecredentials.
– Iftherequestbeingprocesseddefinesproxy metadatawithoutcredentials,theProxy-Authorization
headerisremovedunlessitwasoriginallydefinedforthesameproxyURL.
To remove proxy credentials while keeping the same proxy URL, remove the Proxy-Authorization
header.
– If the request has no proxy metadata, or that metadata is a falsy value (e.g. None), the
Proxy-Authorizationheaderisremoved.
ItisnolongerpossibletosetaproxyURLthroughtheproxymetadatabutsetthecredentialsthroughthe
Proxy-Authorizationheader. Setproxycredentialsthroughtheproxy metadatainstead.
344 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.31 Scrapy 1.8.2 (2022-03-01)
Securitybugfixes:
• When a Request object with cookies defined gets a redirect response causing a new Request object to be
scheduled,thecookiesdefinedintheoriginalRequestobjectarenolongercopiedintothenewRequestobject.
Ifyoumanuallysetthe CookieheaderonaRequest objectandthedomainnameoftheredirectURLisnot
anexactmatchforthedomainoftheURLoftheoriginalRequestobject,yourCookieheaderisnowdropped
fromthenewRequestobject.
Theoldbehaviorcouldbeexploitedbyanattackertogainaccesstoyourcookies. Please,seethecjvr-mfj7-j4j8
securityadvisoryformoreinformation.
(cid:242) Note
Itisstillpossibletoenablethesharingofcookiesbetweendifferentdomainswithashareddomainsuffix(e.g.
example.comandanysubdomain)bydefiningtheshareddomainsuffix(e.g. example.com)asthecookie
domainwhendefiningyourcookies. SeethedocumentationoftheRequestclassformoreinformation.
• Whenthedomainofacookie,eitherreceivedintheSet-CookieheaderofaresponseordefinedinaRequest
object, issettoapublicsuffix, thecookieisnowignoredunlessthecookiedomainisthesameastherequest
domain.
Theoldbehaviorcouldbeexploitedbyanattackertoinjectcookiesintoyourrequeststosomeotherdomains.
Please,seethemfjm-vh54-3f96securityadvisoryformoreinformation.
7.1.32 Scrapy 1.8.1 (2021-10-05)
• Securitybugfix:
IfyouuseHttpAuthMiddleware(i.e. thehttp_userandhttp_passspiderattributes)forHTTPauthentica-
tion,anyrequestexposesyourcredentialstotherequesttarget.
Topreventunintendedexposureofauthenticationcredentialstounintendeddomains,youmustnowadditionally
set a new, additional spider attribute, http_auth_domain, and point it to the specific domain to which the
authenticationcredentialsmustbesent.
Ifthehttp_auth_domainspiderattributeisnotset,thedomainofthefirstrequestwillbeconsideredtheHTTP
authenticationtarget,andauthenticationcredentialswillonlybesentinrequeststargetingthatdomain.
IfyouneedtosendthesameHTTPauthenticationcredentialstomultipledomains,youcanusew3lib.http.
basic_auth_header()insteadtosetthevalueoftheAuthorizationheaderofyourrequests.
If you really want your spider to send the same HTTP authentication credentials to any domain, set the
http_auth_domainspiderattributetoNone.
Finally, if you are a user of scrapy-splash, know that this version of Scrapy breaks compatibility with scrapy-
splash0.7.2andearlier. Youwillneedtoupgradescrapy-splashtoagreaterversionforittocontinuetowork.
7.1.33 Scrapy 1.8.0 (2019-10-28)
Highlights:
• DroppedPython3.4supportandupdatedminimumrequirements;madePython3.8supportofficial
• NewRequest.from_curl()classmethod
• NewROBOTSTXT_PARSER andROBOTSTXT_USER_AGENT settings
• NewDOWNLOADER_CLIENT_TLS_CIPHERS andDOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING settings
7.1. Releasenotes 345

ScrapyDocumentation,Release2.13.3
Backward-incompatiblechanges
• Python3.4isnolongersupported,andsomeoftheminimumrequirementsofScrapyhavealsochanged:
– cssselect0.9.1
– cryptography2.0
– lxml3.5.0
– pyOpenSSL16.2.0
– queuelib1.4.2
– service_identity16.0.0
– six1.10.0
– Twisted17.9.0(16.0.0withPython2)
– zope.interface4.1.3
(issue3892)
• JSONRequestisnowcalledJsonRequestforconsistencywithsimilarclasses(issue3929,issue3982)
• Ifyouareusingacustomcontextfactory(DOWNLOADER_CLIENTCONTEXTFACTORY),its__init__methodmust
accept two new parameters: tls_verbose_logging and tls_ciphers (issue 2111, issue 3392, issue 3442,
issue3450)
• ItemLoadernowturnsthevaluesofitsinputitemintolists:
>>> item = MyItem()
>>> item["field"] = "value1"
>>> loader = ItemLoader(item=item)
>>> item["field"]
['value1']
Thisisneededtoallowaddingvaluestoexistingfields(loader.add_value('field', 'value2')).
(issue3804,issue3819,issue3897,issue3976,issue3998,issue4036)
SeealsoDeprecationremovalsbelow.
Newfeatures
• AnewRequest.from_curlclassmethodallowscreatingarequestfromacURLcommand (issue2985,issue
3862)
• AnewROBOTSTXT_PARSER settingallowschoosingwhichrobots.txtparsertouse. Itincludesbuilt-insupport
for RobotFileParser, Protego (default), Reppy, and Robotexclusionrulesparser, and allows you to implement
supportforadditionalparsers(issue754,issue2669,issue3796,issue3935,issue3969,issue4006)
• AnewROBOTSTXT_USER_AGENTsettingallowsdefiningaseparateuseragentstringtouseforrobots.txtparsing
(issue3931,issue3966)
• RulenolongerrequiresaLinkExtractorparameter(issue781,issue4016)
• UsethenewDOWNLOADER_CLIENT_TLS_CIPHERSsettingtocustomizetheTLS/SSLciphersusedbythedefault
HTTP/1.1downloader(issue3392,issue3442)
• Set the new DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING setting to True to enable debug-level messages
aboutTLSconnectionparametersafterestablishingHTTPSconnections(issue2111,issue3450)
346 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Callbacks that receive keyword arguments (see Request.cb_kwargs) can now be tested using the new
@cb_kwargsspidercontract(issue3985,issue3988)
• Whena@scrapesspidercontractfails,allmissingfieldsarenowreported(issue766,issue3939)
• Custom log formats can now drop messages by having the corresponding methods of the configured
LOG_FORMATTER returnNone(issue3984,issue3987)
• AmuchimprovedcompletiondefinitionisnowavailableforZsh(issue4069)
Bugfixes
• ItemLoader.load_item() no longer makes later calls to ItemLoader.get_output_value() or
ItemLoader.load_item() return empty data (issue 3804, issue 3819, issue 3897, issue 3976, issue
3998,issue4036)
• FixedDummyStatsCollectorraisingaTypeErrorexception(issue4007,issue4052)
• FilesPipeline.file_path andImagesPipeline.file_path nolongerchoosefileextensionsthatarenot
registeredwithIANA(issue1287,issue3953,issue3954)
• WhenusingbotocoretopersistfilesinS3,allbotocore-supportedheadersareproperlymappednow(issue3904,
issue3905)
• FTPpasswordsinFEED_URIcontainingpercent-escapedcharactersarenowproperlydecoded(issue3941)
• Amemory-handlinganderror-handlingissueinscrapy.utils.ssl.get_temp_key_info()hasbeenfixed
(issue3920)
Documentation
• Thedocumentationnowcovershowtodefineandconfigureacustomlogformat(issue3616,issue3660)
• APIdocumentationaddedforMarshalItemExporterandPythonItemExporter(issue3973)
• APIdocumentationaddedforBaseItemandItemMeta (issue3999)
• Minordocumentationfixes(issue2998,issue3398,issue3597,issue3894,issue3934,issue3978,issue3993,
issue4022,issue4028,issue4033,issue4046,issue4050,issue4055,issue4056,issue4061,issue4072,issue
4071,issue4079,issue4081,issue4089,issue4093)
Deprecationremovals
• scrapy.xlibhasbeenremoved(issue4015)
Deprecations
• The LevelDB storage backend (scrapy.extensions.httpcache.LeveldbCacheStorage) of
HttpCacheMiddlewareisdeprecated(issue4085,issue4092)
• UseoftheundocumentedSCRAPY_PICKLED_SETTINGS_TO_OVERRIDEenvironmentvariableisdeprecated(is-
sue3910)
• scrapy.item.DictItemisdeprecated,useItem instead(issue3999)
Otherchanges
• MinimumversionsofoptionalScrapyrequirementsthatarecoveredbycontinuousintegrationtestshavebeen
updated:
– botocore1.3.23
– Pillow3.4.2
7.1. Releasenotes 347

ScrapyDocumentation,Release2.13.3
Lowerversionsoftheseoptionalrequirementsmaywork,butitisnotguaranteed(issue3892)
• GitHubtemplatesforbugreportsandfeaturerequests(issue3126,issue3471,issue3749,issue3754)
• Continuousintegrationfixes(issue3923)
• Codecleanup(issue3391,issue3907,issue3946,issue3950,issue4023,issue4031)
7.1.34 Scrapy 1.7.4 (2019-10-21)
Revertthefixforissue3804(issue3819),whichhasafewundesiredsideeffects(issue3897,issue3976).
Asaresult,whenanitemloaderisinitializedwithanitem,ItemLoader.load_item()onceagainmakeslatercalls
toItemLoader.get_output_value()orItemLoader.load_item()returnemptydata.
7.1.35 Scrapy 1.7.3 (2019-08-01)
Enforcelxml4.3.5orlowerforPython3.4(issue3912,issue3918).
7.1.36 Scrapy 1.7.2 (2019-07-23)
FixPython2support(issue3889,issue3893,issue3896).
7.1.37 Scrapy 1.7.1 (2019-07-18)
Re-packagingofScrapy1.7.0,whichwasmissingsomechangesinPyPI.
7.1.38 Scrapy 1.7.0 (2019-07-18)
(cid:242) Note
MakesureyouinstallScrapy1.7.1. TheScrapy1.7.0packageinPyPIistheresultofanerroneouscommittagging
anddoesnotincludeallthechangesdescribedbelow.
Highlights:
• Improvementsforcrawlstargetingmultipledomains
• Acleanerwaytopassargumentstocallbacks
• AnewclassforJSONrequests
• Improvementsforrule-basedspiders
• Newfeaturesforfeedexports
Backward-incompatiblechanges
• 429isnowpartoftheRETRY_HTTP_CODES settingbydefault
Thischangeisbackwardincompatible. Ifyoudon’twanttoretry429,youmustoverrideRETRY_HTTP_CODES
accordingly.
• Crawler, CrawlerRunner.crawl and CrawlerRunner.create_crawler no longer accept a Spider sub-
classinstance,theyonlyacceptaSpidersubclassnow.
Spidersubclassinstanceswerenevermeanttowork,andtheywerenotworkingasonewouldexpect: insteadof
usingthepassedSpidersubclassinstance,theirfrom_crawlermethodwascalledtogenerateanewinstance.
348 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Non-defaultvaluesfortheSCHEDULER_PRIORITY_QUEUE settingmaystopworking. Schedulerpriorityqueue
classesnowneedtohandleRequestobjectsinsteadofarbitraryPythondatastructures.
• Anadditional crawlerparameterhasbeenaddedtothe __init__methodoftheScheduler class. Custom
schedulersubclasseswhichdon’tacceptarbitraryparametersintheir__init__methodmightbreakbecauseof
thischange.
Formoreinformation,seeSCHEDULER.
SeealsoDeprecationremovalsbelow.
Newfeatures
• A new scheduler priority queue, scrapy.pqueues.DownloaderAwarePriorityQueue, may be enabled
for a significant scheduling improvement on crawls targeting multiple web domains, at the cost of no
CONCURRENT_REQUESTS_PER_IP support(issue3520)
• AnewRequest.cb_kwargs attributeprovidesacleanerwaytopasskeywordargumentstocallbackmethods
(issue1138,issue3563)
• AnewJSONRequestclassoffersamoreconvenientwaytobuildJSONrequests(issue3504,issue3505)
• A process_request callback passed to the Rule __init__ method now receives the Response object that
originatedtherequestasitssecondargument(issue3682)
• Anewrestrict_textparameterfortheLinkExtractor __init__methodallowsfilteringlinksbylinking
text(issue3622,issue3635)
• AnewFEED_STORAGE_S3_ACL settingallowsdefiningacustomACLforfeedsexportedtoAmazonS3(issue
3607)
• AnewFEED_STORAGE_FTP_ACTIVE settingallowsusingFTP’sactiveconnectionmodeforfeedsexportedto
FTPservers(issue3829)
• AnewMETAREFRESH_IGNORE_TAGSsettingallowsoverridingwhichHTMLtagsareignoredwhensearchinga
responseforHTMLmetatagsthattriggeraredirect(issue1422,issue3768)
• Anewredirect_reasons requestmetakeyexposesthereason(statuscode, metarefresh)behindeveryfol-
lowedredirect(issue3581,issue3687)
• The SCRAPY_CHECK variable is now set to the true string during runs of the check command, which allows
detectingcontractcheckrunsfromcode(issue3704,issue3739)
• AnewItem.deepcopy()methodmakesiteasiertodeep-copyitems(issue1493,issue3671)
• CoreStatsalsologselapsed_time_secondsnow(issue3638)
• ExceptionsfromItemLoaderinputandoutputprocessorsarenowmoreverbose(issue3836,issue3840)
• Crawler,CrawlerRunner.crawlandCrawlerRunner.create_crawlernowfailgracefullyiftheyreceive
aSpidersubclassinstanceinsteadofthesubclassitself(issue2283,issue3610,issue3872)
Bugfixes
• process_spider_exception()isnowalsoinvokedforgenerators(issue220,issue2061)
• SystemexceptionslikeKeyboardInterruptarenolongercaught(issue3726)
• ItemLoader.load_item() no longer makes later calls to ItemLoader.get_output_value() or
ItemLoader.load_item()returnemptydata(issue3804,issue3819)
• The images pipeline (ImagesPipeline) no longer ignores these Amazon S3 settings: AWS_ENDPOINT_URL,
AWS_REGION_NAME,AWS_USE_SSL,AWS_VERIFY (issue3625)
7.1. Releasenotes 349

ScrapyDocumentation,Release2.13.3
• Fixed a memory leak in scrapy.pipelines.media.MediaPipeline affecting, for example, non-200 re-
sponsesandexceptionsfromcustommiddlewares(issue3813)
• Requestswithprivatecallbacksarenowcorrectlyunserializedfromdisk(issue3790)
• FormRequest.from_response() now handles invalid methods like major web browsers (issue 3777, issue
3794)
Documentation
• Anewtopic,Selectingdynamically-loadedcontent,coversrecommendedapproachestoreaddynamically-loaded
data(issue3703)
• BroadCrawlsnowfeaturesinformationaboutmemoryusage(issue1264,issue3866)
• ThedocumentationofRulenowcovershowtoaccessthetextofalinkwhenusingCrawlSpider(issue3711,
issue3712)
• A new section, Writing your own storage backend, covers writing a custom cache storage backend for
HttpCacheMiddleware(issue3683,issue3692)
• AnewFAQentry,Howtosplitanitemintomultipleitemsinanitempipeline?,explainswhattodowhenyou
wanttosplitanitemintomultipleitemsfromanitempipeline(issue2240,issue3672)
• UpdatedtheFAQentryaboutcrawlorder toexplainwhythefirstfewrequestsrarelyfollowthedesiredorder
(issue1739,issue3621)
• The LOGSTATS_INTERVAL setting (issue 3730), the FilesPipeline.file_path and ImagesPipeline.
file_path methods (issue 2253, issue 3609) and the Crawler.stop() method (issue 3842) are now docu-
mented
• Some parts of the documentation that were confusing or misleading are now clearer (issue 1347, issue 1789,
issue2289,issue3069,issue3615,issue3626,issue3668,issue3670,issue3673,issue3728,issue3762,issue
3861,issue3882)
• Minordocumentationfixes(issue3648,issue3649,issue3662,issue3674,issue3676,issue3694,issue3724,
issue3764,issue3767,issue3791,issue3797,issue3806,issue3812)
Deprecationremovals
ThefollowingdeprecatedAPIshavebeenremoved(issue3578):
• scrapy.conf(useCrawler.settings)
• Fromscrapy.core.downloader.handlers:
– http.HttpDownloadHandler(usehttp10.HTTP10DownloadHandler)
• scrapy.loader.ItemLoader._get_values(use_get_xpathvalues)
• scrapy.loader.XPathItemLoader(useItemLoader)
• scrapy.log(seeLogging)
• Fromscrapy.pipelines:
– files.FilesPipeline.file_key(usefile_path)
– images.ImagesPipeline.file_key(usefile_path)
– images.ImagesPipeline.image_key(usefile_path)
– images.ImagesPipeline.thumb_key(usethumb_path)
• Frombothscrapy.selectorandscrapy.selector.lxmlsel:
350 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
– HtmlXPathSelector(useSelector)
– XmlXPathSelector(useSelector)
– XPathSelector(useSelector)
– XPathSelectorList(useSelector)
• Fromscrapy.selector.csstranslator:
– ScrapyGenericTranslator(useparsel.csstranslator.GenericTranslator)
– ScrapyHTMLTranslator(useparsel.csstranslator.HTMLTranslator)
– ScrapyXPathExpr(useparsel.csstranslator.XPathExpr)
• FromSelector:
– _root(boththe__init__methodargumentandtheobjectproperty,useroot)
– extract_unquoted(usegetall)
– select(usexpath)
• FromSelectorList:
– extract_unquoted(usegetall)
– select(usexpath)
– x(usexpath)
• scrapy.spiders.BaseSpider(useSpider)
• FromSpider(andsubclasses):
– DOWNLOAD_DELAY(usedownload_delay)
– set_crawler(usefrom_crawler())
• scrapy.spiders.spiders(useSpiderLoader)
• scrapy.telnet(usescrapy.extensions.telnet)
• Fromscrapy.utils.python:
– str_to_unicode(useto_unicode)
– unicode_to_str(useto_bytes)
• scrapy.utils.response.body_or_str
Thefollowingdeprecatedsettingshavealsobeenremoved(issue3578):
• SPIDER_MANAGER_CLASS(useSPIDER_LOADER_CLASS)
Deprecations
• The queuelib.PriorityQueue value for the SCHEDULER_PRIORITY_QUEUE setting is deprecated. Use
scrapy.pqueues.ScrapyPriorityQueueinstead.
• process_requestcallbackspassedtoRulethatdonotaccepttwoargumentsaredeprecated.
• Thefollowingmodulesaredeprecated:
– scrapy.utils.http(usew3lib.http)
– scrapy.utils.markup(usew3lib.html)
– scrapy.utils.multipart(useurllib3)
7.1. Releasenotes 351

ScrapyDocumentation,Release2.13.3
• Thescrapy.utils.datatypes.MergeDictclassisdeprecatedforPython3codebases. UseChainMapin-
stead. (issue3878)
• Thescrapy.utils.gz.is_gzippedfunctionisdeprecated. Usescrapy.utils.gz.gzip_magic_number
instead.
Otherchanges
• Itisnowpossibletorunalltestsfromthesametoxenvironmentinparallel;thedocumentationnowcoversthis
andotherwaystoruntests(issue3707)
• ItisnowpossibletogenerateanAPIdocumentationcoveragereport(issue3806,issue3810,issue3860)
• Thedocumentationpoliciesnowrequiredocstrings(issue3701)thatfollowPEP257(issue3748)
• Internalfixesandcleanup(issue3629,issue3643,issue3684,issue3698,issue3734,issue3735,issue3736,
issue3737,issue3809,issue3821,issue3825,issue3827,issue3833,issue3857,issue3877)
7.1.39 Scrapy 1.6.0 (2019-01-30)
Highlights:
• betterWindowssupport;
• Python3.7compatibility;
• bigdocumentationimprovements,includingaswitchfrom.extract_first()+.extract()APIto.get()
+.getall()API;
• feedexports,FilePipelineandMediaPipelineimprovements;
• better extensibility: item_error and request_reached_downloader signals; from_crawler support for
feedexporters,feedstoragesanddupefilters.
• scrapy.contractsfixesandnewfeatures;
• telnetconsolesecurityimprovements,firstreleasedasabackportinScrapy1.5.2(2019-01-22);
• clean-upofthedeprecatedcode;
• variousbugfixes,smallnewfeaturesandusabilityimprovementsacrossthecodebase.
SelectorAPIchanges
WhilethesearenotchangesinScrapyitself,butratherintheparsellibrarywhichScrapyusesforxpath/cssselectors,
thesechangesareworthmentioninghere. Scrapynowdependsonparsel>=1.5,andScrapydocumentationisupdated
tofollowrecentparselAPIconventions.
Most visible change is that .get() and .getall() selector methods are now preferred over .extract_first()
and .extract(). We feel that these new methods result in a more concise and readable code. See extract() and
extract_first()formoredetails.
(cid:242) Note
Therearecurrentlynoplanstodeprecate.extract()and.extract_first()methods.
Anotherusefulnewfeatureistheintroductionof Selector.attribandSelectorList.attribproperties,which
makeiteasiertogetattributesofHTMLelements. SeeSelectingelementattributes.
CSSselectorsarecachedinparsel>=1.5,whichmakesthemfasterwhenthesameCSSpathisusedmanytimes. This
isverycommonincaseofScrapyspiders: callbacksareusuallycalledseveraltimes,ondifferentpages.
352 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Ifyou’reusingcustomSelectororSelectorListsubclasses,abackwardincompatiblechangeinparselmayaffect
yourcode. Seeparselchangelogforadetaileddescription,aswellasforthefulllistofimprovements.
Telnetconsole
Backwardincompatible: Scrapy’stelnetconsolenowrequiresusernameandpassword. SeeTelnetConsoleformore
details. Thischangefixesasecurityissue;seeScrapy1.5.2(2019-01-22)releasenotesfordetails.
Newextensibilityfeatures
• from_crawlersupportisaddedtofeedexportersandfeedstorages. This,amongotherthings,allowstoaccess
Scrapysettingsfromcustomfeedstoragesandexporters(issue1605,issue3348).
• from_crawlersupportisaddedtodupefilters(issue2956);thisallowstoaccesse.g. settingsoraspiderfrom
adupefilter.
• item_errorisfiredwhenanerrorhappensinapipeline(issue3256);
• request_reached_downloader isfiredwhenDownloadergetsanewRequest; thissignalcanbeusefule.g.
forcustomSchedulers(issue3393).
• newSitemapSpidersitemap_filter()methodwhichallowstoselectsitemapentriesbasedontheirattributes
inSitemapSpidersubclasses(issue3512).
• LazyloadingofDownloaderHandlersisnowoptional;thisenablesbetterinitializationerrorhandlingincustom
DownloaderHandlers(issue3394).
NewFilePipelineandMediaPipelinefeatures
• ExposemoreoptionsforS3FilesStore:AWS_ENDPOINT_URL,AWS_USE_SSL,AWS_VERIFY,AWS_REGION_NAME.
Forexample,thisallowstousealternativeorself-hostedAWS-compatibleproviders(issue2609,issue3548).
• ACLsupportforGoogleCloudStorage: FILES_STORE_GCS_ACL andIMAGES_STORE_GCS_ACL (issue3199).
scrapy.contractsimprovements
• Exceptionsincontractscodearehandledbetter(issue3377);
• dont_filter=Trueisusedforcontractrequests, whichallowstotestdifferentcallbackswiththesameURL
(issue3381);
• request_clsattributeinContractsubclasses allowtousedifferentRequestclassesincontracts, forexample
FormRequest(issue3383).
• Fixederrbackhandlingincontracts,e.g. forcaseswhereacontractisexecutedforURLwhichreturnsnon-200
response(issue3371).
Usabilityimprovements
• morestatsforRobotsTxtMiddleware(issue3100)
• INFOloglevelisusedtoshowtelnethost/port(issue3115)
• amessageisaddedtoIgnoreRequestinRobotsTxtMiddleware(issue3113)
• bettervalidationof urlargumentinResponse.follow(issue3131)
• non-zeroexitcodeisreturnedfromScrapycommandswhenerrorhappensonspiderinitialization(issue3226)
• Link extraction improvements: “ftp” is added to scheme list (issue 3152); “flv” is added to common video
extensions(issue3165)
• bettererrormessagewhenanexporterisdisabled(issue3358);
7.1. Releasenotes 353

ScrapyDocumentation,Release2.13.3
• scrapy shell --helpmentionssyntaxrequiredforlocalfiles(./file.html)-issue3496.
• RefererheadervalueisaddedtoRFPDupeFilterlogmessages(issue3588)
Bugfixes
• fixedissuewithextrablanklinesin.csvexportsunderWindows(issue3039);
• properhandlingofpicklingerrorsinPython3whenserializingobjectsfordiskqueues(issue3082)
• flagsarenowpreservedwhencopyingRequests(issue3342);
• FormRequest.from_responseclickdatashouldn’tignoreelementswithinput[type=image](issue3153).
• FormRequest.from_responseshouldpreserveduplicatekeys(issue3247)
Documentationimprovements
• Docsarere-writtentosuggest.get/.getallAPIinsteadof.extract/.extract_first. Also,Selectorsdocsareupdated
andre-structuredtomatchlatestparseldocs;theynowcontainmoretopics,suchasSelectingelementattributes
orExtensionstoCSSSelectors(issue3390).
• Using your browser’s Developer Tools for scraping is a new tutorial which replaces old Firefox and Firebug
tutorials(issue3400).
• SCRAPY_PROJECTenvironmentvariableisdocumented(issue3518);
• troubleshootingsectionisaddedtoinstallinstructions(issue3517);
• improvedlinkstobeginnerresourcesinthetutorial(issue3367,issue3468);
• fixedRETRY_HTTP_CODES defaultvaluesindocs(issue3335);
• removeunusedDEPTH_STATSoptionfromdocs(issue3245);
• othercleanups(issue3347,issue3350,issue3445,issue3544,issue3605).
Deprecationremovals
Compatibilityshimsforpre-1.0Scrapymodulenamesareremoved(issue3318):
• scrapy.command
• scrapy.contrib(withallsubmodules)
• scrapy.contrib_exp(withallsubmodules)
• scrapy.dupefilter
• scrapy.linkextractor
• scrapy.project
• scrapy.spider
• scrapy.spidermanager
• scrapy.squeue
• scrapy.stats
• scrapy.statscol
• scrapy.utils.decorator
354 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
SeeModuleRelocationsformoreinformation, orusesuggestionsfromScrapy1.5.xdeprecationwarningstoupdate
yourcode.
Otherdeprecationremovals:
• Deprecatedscrapy.interfaces.ISpiderManagerisremoved;pleaseusescrapy.interfaces.ISpiderLoader.
• DeprecatedCrawlerSettingsclassisremoved(issue3327).
• DeprecatedSettings.overridesandSettings.defaultsattributesareremoved(issue3327,issue3359).
Otherimprovements,cleanups
• AllScrapytestsnowpassonWindows;ScrapytestingsuiteisexecutedinaWindowsenvironmentonCI(issue
3315).
• Python3.7support(issue3326,issue3150,issue3547).
• TestingandCIfixes(issue3526,issue3538,issue3308,issue3311,issue3309,issue3305,issue3210,issue
3299)
• scrapy.http.cookies.CookieJar.clearaccepts“domain”,“path”and“name”optionalarguments(issue
3231).
• additionalfilesareincludedtosdist(issue3495);
• codestylefixes(issue3405,issue3304);
• unneeded.strip()callisremoved(issue3519);
• collections.dequeisusedtostoreMiddlewareManagermethodsinsteadofalist(issue3476)
7.1.40 Scrapy 1.5.2 (2019-01-22)
• Security bugfix: Telnet console extension can be easily exploited by rogue websites POSTing content to http:
//localhost:6023,wehaven’tfoundawaytoexploititfromScrapy,butitisveryeasytotrickabrowsertodoso
andelevatestheriskforlocaldevelopmentenvironment.
Thefixisbackwardincompatible,itenablestelnetuser-passwordauthenticationbydefaultwitharandomgener-
atedpassword. Ifyoucan’tupgraderightaway,pleaseconsidersettingTELNETCONSOLE_PORT outofitsdefault
value.
Seetelnetconsoledocumentationformoreinfo
• BackportCIbuildfailureunderGCEenvironmentduetobotoimporterror.
7.1.41 Scrapy 1.5.1 (2018-07-12)
Thisisamaintenancereleasewithimportantbugfixes,butnonewfeatures:
• O(N^2)gzipdecompressionissuewhichaffectedPython3andPyPyisfixed(issue3281);
• skippingofTLSvalidationerrorsisimproved(issue3166);
• Ctrl-ChandlingisfixedinPython3.5+(issue3096);
• testingfixes(issue3092,issue3263);
• documentation improvements (issue 3058, issue 3059, issue 3089, issue 3123, issue 3127, issue 3189, issue
3224,issue3280,issue3279,issue3201,issue3260,issue3284,issue3298,issue3294).
7.1. Releasenotes 355

ScrapyDocumentation,Release2.13.3
7.1.42 Scrapy 1.5.0 (2017-12-29)
Thisreleasebringssmallnewfeaturesandimprovementsacrossthecodebase. Somehighlights:
• GoogleCloudStorageissupportedinFilesPipelineandImagesPipeline.
• Crawlingwithproxyserversbecomesmoreefficient,asconnectionstoproxiescanbereusednow.
• Warnings,exceptionandloggingmessagesareimprovedtomakedebuggingeasier.
• scrapy parsecommandnowallowstosetcustomrequestmetavia--metaargument.
• CompatibilitywithPython3.6,PyPyandPyPy3isimproved;PyPyandPyPy3arenowsupportedofficially,by
runningtestsonCI.
• BetterdefaulthandlingofHTTP308,522and524statuscodes.
• Documentationisimproved,asusual.
BackwardIncompatibleChanges
• Scrapy1.5dropssupportforPython3.3.
• Default Scrapy User-Agent now uses https link to scrapy.org (issue 2983). This is technically backward-
incompatible;overrideUSER_AGENT ifyoureliedonoldvalue.
• Loggingofsettingsoverriddenbycustom_settingsisfixed;thisistechnicallybackward-incompatiblebe-
causetheloggerchangesfrom [scrapy.utils.log]to[scrapy.crawler]. Ifyou’reparsingScrapylogs,
pleaseupdateyourlogparsers(issue1343).
• LinkExtractornowignoresm4vextensionbydefault,thisischangeinbehavior.
• 522and524statuscodesareaddedtoRETRY_HTTP_CODES(issue2851)
Newfeatures
• Support<link>tagsinResponse.follow(issue2785)
• SupportforptpythonREPL(issue2654)
• GoogleCloudStoragesupportforFilesPipelineandImagesPipeline(issue2923).
• New--metaoptionofthe“scrapyparse”commandallowstopassadditionalrequest.meta(issue2883)
• Populatespidervariablewhenusingshell.inspect_response(issue2812)
• HandleHTTP308PermanentRedirect(issue2844)
• Add522and524toRETRY_HTTP_CODES(issue2851)
• Logversionsinformationatstartup(issue2857)
• scrapy.mail.MailSendernowworksinPython3(itrequiresTwisted17.9.0)
• Connectionstoproxyserversarereused(issue2743)
• Addtemplateforadownloadermiddleware(issue2755)
• ExplicitmessageforNotImplementedErrorwhenparsecallbacknotdefined(issue2831)
• CrawlerProcessgotanoptiontodisableinstallationofrootloghandler(issue2921)
• LinkExtractornowignoresm4vextensionbydefault
• BetterlogmessagesforresponsesoverDOWNLOAD_WARNSIZE andDOWNLOAD_MAXSIZE limits(issue2927)
• ShowwarningwhenaURLisputtoSpider.allowed_domainsinsteadofadomain(issue2250).
356 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Bugfixes
• Fixloggingofsettingsoverriddenbycustom_settings;thisistechnicallybackward-incompatiblebecause
the logger changes from [scrapy.utils.log] to [scrapy.crawler], so please update your log parsers if
needed(issue1343)
• Default Scrapy User-Agent now uses https link to scrapy.org (issue 2983). This is technically backward-
incompatible;overrideUSER_AGENT ifyoureliedonoldvalue.
• FixPyPyandPyPy3testfailures,supportthemofficially(issue2793,issue2935,issue2990,issue3050,issue
2213,issue3048)
• FixDNSresolverwhenDNSCACHE_ENABLED=False(issue2811)
• AddcryptographyforDebianJessietoxtestenv(issue2848)
• AddverificationtocheckifRequestcallbackiscallable(issue2766)
• Portextras/qpsclient.pytoPython3(issue2849)
• UsegetfullargspecunderthescenesforPython3tostopDeprecationWarning(issue2862)
• Updatedeprecatedtestaliases(issue2876)
• FixSitemapSpidersupportforalternatelinks(issue2853)
Docs
• AddedmissingbulletpointfortheAUTOTHROTTLE_TARGET_CONCURRENCYsetting. (issue2756)
• UpdateContributingdocs,documentnewsupportchannels(issue2762,issue:3038)
• IncludereferencestoScrapysubredditinthedocs
• Fixbrokenlinks;usehttps:// forexternallinks(issue2978,issue2982,issue2958)
• DocumentCloseSpiderextensionbetter(issue2759)
• Usepymongo.collection.Collection.insert_one()inMongoDBexample(issue2781)
• Spellingmistakeandtypos(issue2828,issue2837,issue2884,issue2924)
• ClarifyCSVFeedSpider.headersdocumentation(issue2826)
• DocumentDontCloseSpiderexceptionandclarifyspider_idle(issue2791)
• Update“Releases”sectioninREADME(issue2764)
• FixrstsyntaxinDOWNLOAD_FAIL_ON_DATALOSSdocs(issue2763)
• Smallfixindescriptionofstartprojectarguments(issue2866)
• ClarifydatatypesinResponse.bodydocs(issue2922)
• Addanoteaboutrequest.meta['depth']toDepthMiddlewaredocs(issue2374)
• Addanoteaboutrequest.meta['dont_merge_cookies']toCookiesMiddlewaredocs(issue2999)
• Up-to-dateexampleofprojectstructure(issue2964,issue2976)
• AbetterexampleofItemExportersusage(issue2989)
• Documentfrom_crawlermethodsforspideranddownloadermiddlewares(issue3019)
7.1. Releasenotes 357

ScrapyDocumentation,Release2.13.3
7.1.43 Scrapy 1.4.0 (2017-05-18)
Scrapy1.4doesnotbringthatmanybreathtakingnewfeaturesbutquiteafewhandyimprovementsnonetheless.
Scrapy now supports anonymous FTP sessions with customizable user and password via the new FTP_USER and
FTP_PASSWORD settings. And if you’re using Twisted version 17.1.0 or above, FTP is now available with Python
3.
There’sanewresponse.followmethodforcreatingrequests;itisnowarecommendedwaytocreateRequestsin
Scrapyspiders. Thismethodmakesiteasiertowritecorrectspiders;response.followhasseveraladvantagesover
creatingscrapy.Requestobjectsdirectly:
• ithandlesrelativeURLs;
• itworksproperlywithnon-asciiURLsonnon-UTF8pages;
• in addition to absolute and relative URLs it supports Selectors; for <a> elements it can also extract their href
values.
Forexample,insteadofthis:
for href in response.css('li.page a::attr(href)').extract():
url = response.urljoin(href)
yield scrapy.Request(url, self.parse, encoding=response.encoding)
Onecannowwritethis:
for a in response.css('li.page a'):
yield response.follow(a, self.parse)
Linkextractorsarealsoimproved. Theyworksimilarlytowhataregularmodernbrowserwoulddo:leadingandtrailing
whitespaceareremovedfromattributes(think href=" http://example.com")whenbuildingLinkobjects. This
whitespace-strippingalsohappensforactionattributeswithFormRequest.
PleasealsonotethatlinkextractorsdonotcanonicalizeURLsbydefaultanymore. Thiswaspuzzlingusersevery
nowandthen,andit’snotwhatbrowsersdoinfact,soweremovedthatextratransformationonextractedlinks.
ForthoseofyouwantingmorecontrolontheReferer: headerthatScrapysendswhenfollowinglinks,youcanset
yourownReferrer Policy. PriortoScrapy1.4,thedefault RefererMiddlewarewouldsimplyandblindlysetit
totheURLoftheresponsethatgeneratedtheHTTPrequest(whichcouldleakinformationonyourURLseeds). By
default, Scrapy now behaves much like your regular browser does. And this policy is fully customizable with W3C
standardvalues(orwithsomethingreallycustomofyourownifyouwish). SeeREFERRER_POLICY fordetails.
TomakeScrapyspiderseasiertodebug,Scrapylogsmorestatsbydefaultin1.4: memoryusagestats,detailedretry
stats,detailedHTTPerrorcodestats. AsimilarchangeisthatHTTPcachepathisalsovisibleinlogsnow.
Last but not least, Scrapy now has the option to make JSON and XML items more human-readable, with newlines
betweenitemsandevencustomindentingoffset,usingthenewFEED_EXPORT_INDENT setting.
Enjoy! (Orreadonfortherestofchangesinthisrelease.)
DeprecationsandBackwardIncompatibleChanges
• Defaulttocanonicalize=Falseinscrapy.linkextractors.LinkExtractor(issue2537,fixesissue1941
andissue1982): warning,thisistechnicallybackward-incompatible
• Enable memusage extension by default (issue 2539, fixes issue 2187); this is technically backward-
incompatiblesopleasecheckifyouhaveanynon-defaultMEMUSAGE_***optionsset.
• EDITOR environment variable now takes precedence over EDITOR option defined in settings.py (issue 1829);
Scrapydefaultsettingsnolongerdependonenvironmentvariables. Thisistechnicallyabackwardincompat-
iblechange.
358 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Spider.make_requests_from_urlisdeprecated(issue1728,fixesissue1495).
NewFeatures
• Acceptproxycredentialsinproxy requestmetakey(issue2526)
• Supportbrotli-compressedcontent;requiresoptionalbrotlipy(issue2535)
• Newresponse.followshortcutforcreatingrequests(issue1940)
• AddedflagsargumentandattributetoRequestobjects(issue2047)
• SupportAnonymousFTP(issue2342)
• Added retry/count, retry/max_reached and retry/reason_count/<reason> stats to
RetryMiddleware(issue2543)
• Added httperror/response_ignored_count and httperror/response_ignored_status_count/
<status>statstoHttpErrorMiddleware(issue2566)
• CustomizableReferrer policy inRefererMiddleware(issue2306)
• Newdata: URIdownloadhandler(issue2334,fixesissue2156)
• LogcachedirectorywhenHTTPCacheisused(issue2611,fixesissue2604)
• Warnuserswhenprojectcontainsduplicatespidernames(fixesissue2181)
• scrapy.utils.datatypes.CaselessDictnowacceptsMappinginstancesandnotonlydicts(issue2646)
• Mediadownloads,withFilesPipelineorImagesPipeline,cannowoptionallyhandleHTTPredirectsusing
thenewMEDIA_ALLOW_REDIRECTS setting(issue2616,fixesissue2004)
• Acceptnon-completeresponsesfromwebsitesusinganewDOWNLOAD_FAIL_ON_DATALOSSsetting(issue2590,
fixesissue2586)
• Optional pretty-printing of JSON and XML items via FEED_EXPORT_INDENT setting (issue 2456, fixes issue
1327)
• AllowdroppingfieldsinFormRequest.from_responseformdatawhenNonevalueispassed(issue667)
• Per-requestretrytimeswiththenewmax_retry_timesmetakey(issue2642)
• python -m scrapyasamoreexplicitalternativetoscrapycommand(issue2740)
Bugfixes
• LinkExtractornowstripsleadingandtrailingwhitespacesfromattributes(issue2547,fixesissue1614)
• ProperlyhandlewhitespacesinactionattributeinFormRequest(issue2548)
• BufferCONNECTresponsebytesfromproxyuntilallHTTPheadersarereceived(issue2495,fixesissue2491)
• FTPdownloadernowworksonPython3,providedyouuseTwisted>=17.1(issue2599)
• Usebodytochooseresponsetypeafterdecompressingcontent(issue2393,fixesissue2145)
• AlwaysdecompressContent-Encoding: gzipatHttpCompressionMiddlewarestage(issue2391)
• RespectcustomloglevelinSpider.custom_settings(issue2581,fixesissue1612)
• ‘makehtmlview’fixformacOS(issue2661)
• Remove“commands”fromthecommandlist(issue2695)
• FixduplicateContent-LengthheaderforPOSTrequestswithemptybody(issue2677)
• Properlycancellargedownloads,i.e. aboveDOWNLOAD_MAXSIZE (issue1616)
7.1. Releasenotes 359

ScrapyDocumentation,Release2.13.3
• ImagesPipeline: fixedprocessingoftransparentPNGimageswithpalette(issue2675)
Cleanups&Refactoring
• Tests: removetempfilesandfolders(issue2570), fixedProjectUtilsTestonmacOS(issue2569), useportable
pypyforLinuxonTravisCI(issue2710)
• Separatebuildingrequestfrom_requests_to_followinCrawlSpider(issue2562)
• Remove“Python3progress”badge(issue2567)
• Addacouplemorelinesto.gitignore(issue2557)
• Removebumpversionprereleaseconfiguration(issue2159)
• Addcodecov.ymlfile(issue2750)
• SetcontextfactoryimplementationbasedonTwistedversion(issue2577,fixesissue2560)
• Addomittedselfargumentsindefaultprojectmiddlewaretemplate(issue2595)
• Removeredundantslot.add_request()callinExecutionEngine(issue2617)
• Catchmorespecificos.errorexceptioninscrapy.pipelines.files.FSFilesStore(issue2644)
• Change“localhost”testservercertificate(issue2720)
• RemoveunusedMEMUSAGE_REPORTsetting(issue2576)
Documentation
• Binarymodeisrequiredforexporters(issue2564,fixesissue2553)
• MentionissuewithFormRequest.from_response()duetobuginlxml(issue2572)
• Usesinglequotesuniformlyintemplates(issue2596)
• Documentftp_userandftp_password metakeys(issue2587)
• Removedsectionondeprecatedcontrib/(issue2636)
• RecommendAnacondawheninstallingScrapyonWindows(issue2477,fixesissue2475)
• FAQ:rewritenoteonPython3supportonWindows(issue2690)
• Rearrangeselectorsections(issue2705)
• Remove__nonzero__fromSelectorListdocs(issue2683)
• MentionhowtodisablerequestfilteringindocumentationofDUPEFILTER_CLASS setting(issue2714)
• Addsphinx_rtd_themetodocssetupreadme(issue2668)
• OpenfileintextmodeinJSONitemwriterexample(issue2729)
• Clarifyallowed_domainsexample(issue2670)
7.1.44 Scrapy 1.3.3 (2017-03-10)
Bugfixes
• Make SpiderLoader raise ImportError again by default for missing dependencies and wrong
SPIDER_MODULES. These exceptions were silenced as warnings since 1.3.0. A new setting is introduced
totogglebetweenwarningorexceptionifneeded;seeSPIDER_LOADER_WARN_ONLY fordetails.
360 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.45 Scrapy 1.3.2 (2017-02-13)
Bugfixes
• Preserverequestclasswhenconvertingto/fromdicts(utils.reqser)(issue2510).
• Useconsistentselectorsforauthorfieldintutorial(issue2551).
• FixTLScompatibilityinTwisted17+(issue2558)
7.1.46 Scrapy 1.3.1 (2017-02-08)
Newfeatures
• Support 'True'and 'False'stringvaluesforbooleansettings(issue2519); youcannowdosomethinglike
scrapy crawl myspider -s REDIRECT_ENABLED=False.
• Support kwargs with response.xpath() to use XPath variables and ad-hoc namespaces declarations ; this
requiresatleastParselv1.1(issue2457).
• AddsupportforPython3.6(issue2485).
• RuntestsonPyPy(warning: sometestsstillfail,soPyPyisnotsupportedyet).
Bugfixes
• EnforceDNS_TIMEOUTsetting(issue2496).
• Fixview command;itwasaregressioninv1.3.0(issue2503).
• Fixtestsregarding*_EXPIRES settingswithFiles/Imagespipelines(issue2460).
• Fixnameofgeneratedpipelineclasswhenusingbasicprojecttemplate(issue2466).
• FixcompatibilitywithTwisted17+(issue2496,issue2528).
• Fixscrapy.IteminheritanceonPython3.6(issue2511).
• Enforce numeric values for components order in SPIDER_MIDDLEWARES, DOWNLOADER_MIDDLEWARES,
EXTENSIONSandSPIDER_CONTRACTS(issue2420).
Documentation
• RewordCodeofConductsectionandupgradetoContributorCovenantv1.4(issue2469).
• Clarifythatpassingspiderargumentsconvertsthemtospiderattributes(issue2483).
• DocumentformidargumentonFormRequest.from_response()(issue2497).
• Add.rstextensiontoREADMEfiles(issue2507).
• MentionLevelDBcachestoragebackend(issue2525).
• Useyieldinsamplecallbackcode(issue2533).
• AddnoteaboutHTMLentitiesdecodingwith.re()/.re_first()(issue1704).
• Typos(issue2512,issue2534,issue2531).
Cleanups
• RemoveredundantcheckinMetaRefreshMiddleware(issue2542).
• FasterchecksinLinkExtractorforallow/denypatterns(issue2538).
• RemovedeadcodesupportingoldTwistedversions(issue2544).
7.1. Releasenotes 361

ScrapyDocumentation,Release2.13.3
7.1.47 Scrapy 1.3.0 (2016-12-21)
Thisreleasecomesrathersoonafter1.2.2foronemainreason: itwasfoundoutthatreleasessince0.18upto1.2.2
(included)usesomebackportedcodefromTwisted(scrapy.xlib.tx.*),evenifnewerTwistedmodulesareavailable.
Scrapynowusestwisted.web.clientandtwisted.internet.endpointsdirectly. (Seealsocleanupsbelow.)
Asitisamajorchange,wewantedtogetthebugfixoutquicklywhilenotbreakinganyprojectsusingthe1.2series.
NewFeatures
• MailSendernowacceptssinglestringsasvaluesfortoandccarguments(issue2272)
• scrapy fetch url,scrapy shell urlandfetch(url)insideScrapyshellnowfollowHTTPredirections
bydefault(issue2290);Seefetch andshellfordetails.
• HttpErrorMiddleware now logs errors with INFO level instead of DEBUG; this is technically backward in-
compatiblesopleasecheckyourlogparsers.
• By default, logger names now use a long-form path, e.g. [scrapy.extensions.logstats], instead of
the shorter “top-level” variant of prior releases (e.g. [scrapy]); this is backward incompatible if you
have log parsers expecting the short logger name part. You can switch back to short logger names using
LOG_SHORT_NAMES settoTrue.
Dependencies&Cleanups
• ScrapynowrequiresTwisted>=13.1whichisthecaseformanyLinuxdistributionsalready.
• As a consequence, we got rid of scrapy.xlib.tx.* modules, which copied some of Twisted code for users
stuckwithan“old”Twistedversion
• ChunkedTransferMiddlewareisdeprecatedandremovedfromthedefaultdownloadermiddlewares.
7.1.48 Scrapy 1.2.3 (2017-03-03)
• Packagingfix: disallowunsupportedTwistedversionsinsetup.py
7.1.49 Scrapy 1.2.2 (2016-12-06)
Bugfixes
• Fixacryptictracebackwhenapipelinefailsonopen_spider()(issue2011)
• FixembeddedIPythonshellvariables(fixingissue396thatre-appearedin1.2.0,fixedinissue2418)
• Acoupleofpatcheswhendealingwithrobots.txt:
– handle(non-standard)relativesitemapURLs(issue2390)
– handlenon-ASCIIURLsandUser-AgentsinPython2(issue2373)
Documentation
• Document"download_latency"keyinRequest’smetadict(issue2033)
• Removepageon(deprecated&unsupported)UbuntupackagesfromToC(issue2335)
• A few fixed typos (issue 2346, issue 2369, issue 2369, issue 2380) and clarifications (issue 2354, issue 2325,
issue2414)
362 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Otherchanges
• Advertizeconda-forgeasScrapy’sofficialcondachannel(issue2387)
• Morehelpfulerrormessageswhentryingtouse.css()or.xpath()onnon-TextResponses(issue2264)
• startprojectcommandnowgeneratesasamplemiddlewares.pyfile(issue2335)
• Addmoredependencies’versioninfoinscrapy versionverboseoutput(issue2404)
• Removeall*.pycfilesfromsourcedistribution(issue2386)
7.1.50 Scrapy 1.2.1 (2016-10-21)
Bugfixes
• IncludeOpenSSL’smorepermissivedefaultcipherswhenestablishingTLS/SSLconnections(issue2314).
• Fix“Location”HTTPheaderdecodingonnon-ASCIIURLredirects(issue2321).
Documentation
• FixJsonWriterPipelineexample(issue2302).
• Variousnotes: issue2330onspidernames,issue2329onmiddlewaremethodsprocessingorder,issue2327on
gettingmulti-valuedHTTPheadersaslists.
Otherchanges
• Removedwww.fromstart_urlsinbuilt-inspidertemplates(issue2299).
7.1.51 Scrapy 1.2.0 (2016-10-03)
NewFeatures
• NewFEED_EXPORT_ENCODING settingtocustomizetheencodingusedwhenwritingitemstoafile. Thiscan
beusedtoturnoff \uXXXXescapesinJSONoutput. Thisisalsousefulforthosewantingsomethingelsethan
UTF-8forXMLorCSVoutput(issue2034).
• startprojectcommandnowsupportsanoptionaldestinationdirectorytooverridethedefaultonebasedon
theprojectname(issue2005).
• NewSCHEDULER_DEBUG settingtologrequestsserializationfailures(issue1610).
• JSONencodernowsupportsserializationof setinstances(issue2058).
• Interpretapplication/json-amazonui-streamingasTextResponse(issue1503).
• scrapyisimportedbydefaultwhenusingshelltools(shell,inspect_response)(issue2248).
Bugfixes
• DefaultRequestHeaders middleware now runs before UserAgent middleware (issue 2088). Warning: this is
technicallybackwardincompatible,thoughweconsiderthisabugfix.
• HTTPcacheextensionandpluginsthatusethe.scrapydatadirectorynowworkoutsideprojects(issue1581).
Warning: thisistechnicallybackwardincompatible,thoughweconsiderthisabugfix.
• Selectordoesnotallowpassingbothresponseandtextanymore(issue2153).
• Fixedloggingofwrongcallbacknamewithscrapy parse(issue2169).
• Fixforanoddgzipdecompressionbug(issue1606).
7.1. Releasenotes 363

ScrapyDocumentation,Release2.13.3
• FixforselectedcallbackswhenusingCrawlSpiderwithscrapy parse(issue2225).
• FixforinvalidJSONandXMLfileswhenspideryieldsnoitems(issue872).
• Implementflush()forStreamLoggeravoidingawarninginlogs(issue2125).
Refactoring
• canonicalize_urlhasbeenmovedtow3lib.url(issue2168).
Tests&Requirements
Scrapy’snewrequirementsbaselineisDebian8“Jessie”. ItwaspreviouslyUbuntu12.04Precise. Whatthismeansin
practiceisthatweruncontinuousintegrationtestswiththese(main)packagesversionsataminimum: Twisted14.0,
pyOpenSSL0.14,lxml3.4.
Scrapymayverywellworkwitholderversionsofthesepackages(thecodebasestillhasswitchesforolderTwisted
versionsforexample)butitisnotguaranteed(becauseit’snottestedanymore).
Documentation
• Grammarfixes: issue2128,issue1566.
• DownloadstatsbadgeremovedfromREADME(issue2160).
• NewScrapyarchitecturediagram(issue2165).
• UpdatedResponseparametersdocumentation(issue2197).
• RewordedmisleadingRANDOMIZE_DOWNLOAD_DELAY description(issue2190).
• AddStackOverflowasasupportchannel(issue2257).
7.1.52 Scrapy 1.1.4 (2017-03-03)
• Packagingfix: disallowunsupportedTwistedversionsinsetup.py
7.1.53 Scrapy 1.1.3 (2016-09-22)
Bugfixes
• Classattributesforsubclassesof ImagesPipelineand FilesPipelineworkastheydidbefore1.1.1(issue
2243,fixesissue2198)
Documentation
• Overviewandtutorialrewrittentousehttp://toscrape.comwebsites(issue2236,issue2249,issue2252).
7.1.54 Scrapy 1.1.2 (2016-08-18)
Bugfixes
• Introduce a missing IMAGES_STORE_S3_ACL setting to override the default ACL policy in ImagesPipeline
whenuploadingimagestoS3(notethatdefaultACLpolicyis“private”–insteadof“public-read”–sinceScrapy
1.1.0)
• IMAGES_EXPIRES defaultvaluesetbackto90(theregressionwasintroducedin1.1.1)
364 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.55 Scrapy 1.1.1 (2016-07-13)
Bugfixes
• Add“Host”headerinCONNECTrequeststoHTTPSproxies(issue2069)
• Useresponsebodywhenchoosingresponseclass(issue2001,fixesissue2000)
• DonotfailoncanonicalizingURLswithwrongnetlocs(issue2038,fixesissue2010)
• afewfixesforHttpCompressionMiddleware(andSitemapSpider):
– DonotdecodeHEADresponses(issue2008,fixesissue1899)
– HandlecharsetparameteringzipContent-Typeheader(issue2050,fixesissue2049)
– Donotdecompressgzipoctet-streamresponses(issue2065,fixesissue2063)
• Catch(andignorewithawarning)exceptionwhenverifyingcertificateagainstIP-addresshosts(issue2094,fixes
issue2092)
• Make FilesPipeline and ImagesPipeline backward compatible again regarding the use of legacy class
attributesforcustomization(issue1989,fixesissue1985)
Newfeatures
• Enablegenspidercommandoutsideprojectfolder(issue2052)
• RetryHTTPSCONNECTTunnelErrorbydefault(issue1974)
Documentation
• FEED_TEMPDIRsettingatlexicographicalposition(commit9b3c72c)
• Useidiomatic.extract_first()inoverview(issue1994)
• Updateyearsincopyrightnotice(commitc2c8036)
• Addinformationandexampleonerrbacks(issue1995)
• Use“url”variableindownloadermiddlewareexample(issue2015)
• Grammarfixes(issue2054,issue2120)
• NewFAQentryonusingBeautifulSoupinspidercallbacks(issue2048)
• AddnotesaboutScrapynotworkingonWindowswithPython3(issue2060)
• Encouragecompletetitlesinpullrequests(issue2026)
Tests
• Upgradepy.testrequirementonTravisCIandPinpytest-covto2.2.1(issue2095)
7.1.56 Scrapy 1.1.0 (2016-05-11)
This1.1releasebringsalotofinterestingfeaturesandbugfixes:
• Scrapy1.1hasbetaPython3support(requiresTwisted>=15.5). SeeBetaPython3Support formoredetails
andsomelimitations.
• Hotnewfeatures:
– Itemloadersnowsupportnestedloaders(issue1467).
– FormRequest.from_responseimprovements(issue1382,issue1137).
7.1. Releasenotes 365

ScrapyDocumentation,Release2.13.3
– AddedsettingAUTOTHROTTLE_TARGET_CONCURRENCY andimprovedAutoThrottledocs(issue1324).
– Addedresponse.texttogetbodyasunicode(issue1730).
– AnonymousS3connections(issue1358).
– Deferredsindownloadermiddlewares(issue1473). Thisenablesbetterrobots.txthandling(issue1471).
– HTTP caching now follows RFC2616 more closely, added settings HTTPCACHE_ALWAYS_STORE and
HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS (issue1151).
– Selectors were extracted to the parsel library (issue 1409). This means you can use Scrapy Selectors
withoutScrapyandalsoupgradetheselectorsenginewithoutneedingtoupgradeScrapy.
– HTTPSdownloadernowdoesTLSprotocolnegotiationbydefault,insteadofforcingTLS1.0. Youcan
alsosettheSSL/TLSmethodusingthenewDOWNLOADER_CLIENT_TLS_METHOD.
• Thesebugfixesmayrequireyourattention:
– Don’t retry bad requests (HTTP 400) by default (issue 1289). If you need the old behavior, add 400 to
RETRY_HTTP_CODES.
– Fixshellfilesargumenthandling(issue1710,issue1550). Ifyoutryscrapy shell index.htmlitwill
trytoloadtheURLhttp://index.html,usescrapy shell ./index.htmltoloadalocalfile.
– Robots.txtcomplianceisnowenabledbydefaultfornewly-createdprojects(issue1724). Scrapywillalso
waitforrobots.txttobedownloadedbeforeproceedingwiththecrawl(issue1735). Ifyouwanttodisable
thisbehavior,updateROBOTSTXT_OBEY insettings.pyfileaftercreatinganewproject.
– Exporters now work on unicode, instead of bytes by default (issue 1080). If you use
PythonItemExporter, you may want to update your code to disable binary mode which is now dep-
recated.
– AcceptXMLnodenamescontainingdotsasvalid(issue1533).
– When uploading files or images to S3 (with FilesPipeline or ImagesPipeline), the default ACL
policy is now “private” instead of “public” Warning: backward incompatible!. You can use
FILES_STORE_S3_ACL tochangeit.
– We’ve reimplemented canonicalize_url() for more correct output, especially for URLs with non-
ASCII characters (issue 1947). This could change link extractors output compared to previous Scrapy
versions. Thismayalsoinvalidatesomecacheentriesyoucouldstillhavefrompre-1.1runs. Warning:
backwardincompatible!.
Keepreadingformoredetailsonotherimprovementsandbugfixes.
BetaPython3Support
WehavebeenhardatworktomakeScrapyrunonPython3. Asaresult,nowyoucanrunspidersonPython3.3,3.4
and3.5(Twisted>=15.5required). Somefeaturesarestillmissing(andsomemayneverbeported).
Almostallbuiltinextensions/middlewaresareexpectedtowork. However,weareawareofsomelimitationsinPython
3:
• ScrapydoesnotworkonWindowswithPython3
• Sendingemailsisnotsupported
• FTPdownloadhandlerisnotsupported
• Telnetconsoleisnotsupported
366 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
AdditionalNewFeaturesandEnhancements
• ScrapynowhasaCodeofConduct(issue1681).
• Commandlinetoolnowhascompletionforzsh(issue934).
• Improvementstoscrapy shell:
– SupportforbpythonandconfigurepreferredPythonshellviaSCRAPY_PYTHON_SHELL(issue1100,issue
1444).
– SupportURLswithoutscheme(issue1498)Warning: backwardincompatible!
– Bringbacksupportforrelativefilepath(issue1710,issue1550).
• AddedMEMUSAGE_CHECK_INTERVAL_SECONDS settingtochangedefaultcheckinterval(issue1282).
• Downloadhandlersarenowlazy-loadedonfirstrequestusingtheirscheme(issue1390,issue1421).
• HTTPS download handlers do not force TLS 1.0 anymore; instead, OpenSSL’s SSLv23_method()/
TLS_method() is used allowing to try negotiating with the remote hosts the highest TLS protocol version it
can(issue1794,issue1629).
• RedirectMiddlewarenowskipsthestatuscodesfrom handle_httpstatus_listonspiderattributeorin
Request’smetakey(issue1334,issue1364,issue1447).
• Formsubmission:
– nowworkswith<button>elementstoo(issue1469).
– anemptystringisnowusedforsubmitbuttonswithoutavalue(issue1472)
• Dict-likesettingsnowhaveper-keypriorities(issue1135,issue1149andissue1586).
• Sendingnon-ASCIIemails(issue1662)
• CloseSpider and SpiderState extensions now get disabled if no relevant setting is set (issue 1723, issue
1725).
• AddedmethodExecutionEngine.close(issue1423).
• AddedmethodCrawlerRunner.create_crawler(issue1528).
• SchedulerpriorityqueuecannowbecustomizedviaSCHEDULER_PRIORITY_QUEUE (issue1822).
• .ppslinksarenowignoredbydefaultinlinkextractors(issue1835).
• temporarydatafolderforFTPandS3feedstoragescanbecustomizedusinganewFEED_TEMPDIR setting(issue
1847).
• FilesPipelineandImagesPipelinesettingsarenowinstanceattributesinsteadofclassattributes,enabling
spider-specificbehaviors(issue1891).
• JsonItemExporternowformatsopeningandclosingsquarebracketsontheirownline(firstandlastlinesof
outputfile)(issue1950).
• If available, botocore is used for S3FeedStorage, S3DownloadHandler and S3FilesStore (issue 1761,
issue1883).
• Tons of documentation updates and related fixes (issue 1291, issue 1302, issue 1335, issue 1683, issue 1660,
issue1642,issue1721,issue1727,issue1879).
• Otherrefactoring,optimizationsandcleanup(issue1476,issue1481,issue1477,issue1315,issue1290,issue
1750,issue1881).
7.1. Releasenotes 367

ScrapyDocumentation,Release2.13.3
DeprecationsandRemovals
• Addedto_bytesandto_unicode,deprecatedstr_to_unicodeandunicode_to_strfunctions(issue778).
• binary_is_textisintroduced,toreplaceuseof isbinarytext(butwithinversereturnvalue)(issue1851)
• Theoptional_featuressethasbeenremoved(issue1359).
• The--lsprofcommandlineoptionhasbeenremoved(issue1689). Warning: backwardincompatible,but
doesn’tbreakusercode.
• Thefollowingdatatypesweredeprecated(issue1720):
– scrapy.utils.datatypes.MultiValueDictKeyError
– scrapy.utils.datatypes.MultiValueDict
– scrapy.utils.datatypes.SiteNode
• Thepreviouslybundledscrapy.xlib.pydispatchlibrarywasdeprecatedandreplacedbypydispatcher.
Relocations
• telnetconsolewasrelocatedtoextensions/(issue1524).
– Note: telnet is not enabled on Python 3 (https://github.com/scrapy/scrapy/pull/1524#
issuecomment-146985595)
Bugfixes
• Scrapydoesnotretryrequeststhatgota HTTP 400 Bad Requestresponseanymore(issue1289). Warning:
backwardincompatible!
• Supportemptypasswordforhttp_proxyconfig(issue1274).
• Interpretapplication/x-jsonasTextResponse(issue1333).
• Supportlinkrelattributewithmultiplevalues(issue1201).
• Fixedscrapy.FormRequest.from_responsewhenthereisa<base>tag(issue1564).
• FixedTEMPLATES_DIR handling(issue1575).
• VariousFormRequestfixes(issue1595,issue1596,issue1597).
• Makes_monkeypatchesmorerobust(issue1634).
• FixedbugonXMLItemExporterwithnon-stringfieldsinitems(issue1738).
• FixedstartprojectcommandinmacOS(issue1635).
• FixedPythonItemExporterandCSVExporterfornon-stringitemtypes(issue1737).
• Variousloggingrelatedfixes(issue1294,issue1419,issue1263,issue1624,issue1654,issue1722,issue1726
andissue1303).
• Fixedbuginutils.template.render_templatefile()(issue1212).
• sitemapsextractionfromrobots.txtisnowcase-insensitive(issue1902).
• HTTPS+CONNECTtunnelscouldgetmixedupwhenusingmultipleproxiestosameremotehost(issue1912).
368 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.57 Scrapy 1.0.7 (2017-03-03)
• Packagingfix: disallowunsupportedTwistedversionsinsetup.py
7.1.58 Scrapy 1.0.6 (2016-05-04)
• FIX:RetryMiddlewareisnowrobusttonon-standardHTTPstatuscodes(issue1857)
• FIX:FilestorageHTTPcachewascheckingwrongmodifiedtime(issue1875)
• DOC:SupportforSphinx1.4+(issue1893)
• DOC:Consistencyinselectorsexamples(issue1869)
7.1.59 Scrapy 1.0.5 (2016-02-04)
• FIX:[Backport]IgnoreboguslinksinLinkExtractors(fixesissue907,commit108195e)
• TST:Changedbuildbotmakefiletouse‘pytest’(commit1f3d90a)
• DOC:Fixedtyposintutorialandmedia-pipeline(commit808a9eaandcommit803bd87)
• DOC: Add AjaxCrawlMiddleware to DOWNLOADER_MIDDLEWARES_BASE in settings docs (commit
aa94121)
7.1.60 Scrapy 1.0.4 (2015-12-30)
• Ignoringxlib/txfolder,dependingonTwistedversion. (commit7dfa979)
• Runonnewtravis-ciinfra(commit6e42f0b)
• Spellingfixes(commit823a1cc)
• escapenodenameinxmliterregex(commitda3c155)
• testxmlnodenamewithdots(commit4418fc3)
• TSTdon’tusebrokenPillowversionintests(commita55078c)
• disablelogonversioncommand. closes#1426(commit86fc330)
• disablelogonstartprojectcommand(commitdb4c9fe)
• AddPyPIdownloadstatsbadge(commitdf2b944)
• don’trunteststwiceonTravisifaPRismadefromascrapy/scrapybranch(commita83ab41)
• AddPython3portingstatusbadgetotheREADME(commit73ac80d)
• fixedRFPDupeFilterpersistence(commit97d080e)
• TSTatesttoshowthatdupefilterpersistenceisnotworking(commit97f2fb3)
• explicitclosefileonfile://schemehandler(commitd9b4850)
• Disabledupefilterinshell(commitc0d0734)
• DOC:Addcaptionstotoctreeswhichappearinsidebar(commitaa239ad)
• DOCRemovedpywin32frominstallinstructionsasit’salreadydeclaredasdependency. (commit10eb400)
• AddedinstallationnotesaboutusingCondaforWindowsandotherOSes. (commit1c3600a)
• Fixedminorgrammarissues. (commit7f4ddd5)
• fixedatypointhedocumentation. (commitb71f677)
• Version1nowexists(commit5456c0e)
7.1. Releasenotes 369

ScrapyDocumentation,Release2.13.3
• fixanotherinvalidxpatherror(commit0a1366e)
• fixValueError: InvalidXPath: //div/[id=”not-exists”]/text()onselectors.rst(commitca8d60f)
• Typoscorrections(commit7067117)
• fixtyposindownloader-middleware.rstandexceptions.rst,middlware->middleware(commit32f115c)
• AddnotetoUbuntuinstallsectionaboutDebiancompatibility(commit23fda69)
• ReplacealternativemacOSinstallworkaroundwithvirtualenv(commit98b63ee)
• ReferenceHomebrew’shomepageforinstallationinstructions(commit1925db1)
• Addoldestsupportedtoxversiontocontributingdocs(commit5d10d6d)
• Noteininstalldocsaboutpipbeingalreadyincludedinpython>=2.7.9(commit85c980e)
• Addnon-pythondependenciestoUbuntuinstallsectioninthedocs(commitfbd010d)
• AddmacOSinstallationsectiontodocs(commitd8f4cba)
• DOC(ENH):specifypathtortdthemeexplicitly(commitde73b1a)
• minor: scrapy.Spiderdocsgrammar(commit1ddcc7b)
• Makecommonpracticessamplecodematchthecomments(commit1b85bcf)
• nextcallrepetitivecalls(heartbeats). (commit55f7104)
• BackportfixcompatibilitywithTwisted15.4.0(commitb262411)
• pinpytestto2.7.3(commita6535c2)
• Mergepullrequest#1512frommgedmin/patch-1(commit8876111)
• Mergepullrequest#1513frommgedmin/patch-2(commit5d4daf8)
• Typo(commitf8d0682)
• Fixlistformatting(commit5f83a93)
• fixScrapysqueuetestsafterrecentchangestoqueuelib(commit3365c01)
• Mergepullrequest#1475fromrweindl/patch-1(commit2d688cd)
• Updatetutorial.rst(commitfbc1f25)
• Mergepullrequest#1449fromrhoekman/patch-1(commit7d6538c)
• Smallgrammaticalchange(commit8752294)
• Addopensslversiontoversioncommand(commit13c45ac)
7.1.61 Scrapy 1.0.3 (2015-08-11)
• addservice_identitytoScrapyinstall_requires(commitcbc2501)
• Workaroundfortravis#296(commit66af9cd)
7.1.62 Scrapy 1.0.2 (2015-08-06)
• Twisted15.3.0doesnotraisesPicklingErrorserializinglambdafunctions(commitb04dd7d)
• Minormethodnamefix(commit6f85c7f)
• minor: scrapy.Spidergrammarandclarity(commit9c9d2e0)
• PutablurbaboutsupportchannelsinCONTRIBUTING(commitc63882b)
370 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Fixedtypos(commita9ae7b0)
• Fixdocreference. (commit7c8a4fe)
7.1.63 Scrapy 1.0.1 (2015-07-01)
• UnquoterequestpathbeforepassingtoFTPClient,italreadyescapepaths(commitcc00ad2)
• includetests/tosourcedistributioninMANIFEST.in(commiteca227e)
• DOCFixSelectJmesdocumentation(commitb8567bc)
• DOCBringUbuntuandArchlinuxoutsideofWindowssubsection(commit392233f)
• DOCremoveversionsuffixfromUbuntupackage(commit5303c66)
• DOCUpdatereleasedatefor1.0(commitc89fa29)
7.1.64 Scrapy 1.0.0 (2015-06-19)
Youwillfindalotofnewfeaturesandbugfixesinthismajorrelease. Makesuretocheckourupdatedoverviewtoget
aglanceofsomeofthechanges,alongwithourbrushedtutorial.
Supportforreturningdictionariesinspiders
DeclaringandreturningScrapyItemsisnolongernecessarytocollectthescrapeddatafromyourspider,youcannow
returnexplicitdictionariesinstead.
Classicversion
class MyItem(scrapy.Item):
url = scrapy.Field()
class MySpider(scrapy.Spider):
def parse(self, response):
return MyItem(url=response.url)
Newversion
class MySpider(scrapy.Spider):
def parse(self, response):
return {'url': response.url}
Per-spidersettings(GSoC2014)
LastGoogleSummerofCodeprojectaccomplishedanimportantredesignofthemechanismusedforpopulatingset-
tings,introducingexplicitprioritiestooverrideanygivensetting. Asanextensionofthatgoal,weincludedanewlevel
ofpriorityforsettingsthatactexclusivelyforasinglespider,allowingthemtoredefineprojectsettings.
Startusingitbydefiningacustom_settingsclassvariableinyourspider:
class MySpider(scrapy.Spider):
custom_settings = {
"DOWNLOAD_DELAY": 5.0,
"RETRY_ENABLED": False,
}
Readmoreaboutsettingspopulation: Settings
7.1. Releasenotes 371

ScrapyDocumentation,Release2.13.3
PythonLogging
Scrapy1.0hasmovedawayfromTwistedloggingtosupportPythonbuiltin’sasdefaultloggingsystem. We’remain-
tainingbackwardcompatibilityformostoftheoldcustominterfacetocallloggingfunctions,butyou’llgetwarnings
toswitchtothePythonloggingAPIentirely.
Oldversion
from scrapy import log
log.msg('MESSAGE', log.INFO)
Newversion
import logging
logging.info('MESSAGE')
Loggingwithspidersremainsthesame,butontopofthelog()methodyou’llhaveaccesstoacustomloggercreated
forthespidertoissuelogevents:
class MySpider(scrapy.Spider):
def parse(self, response):
self.logger.info('Response received')
Readmoreintheloggingdocumentation: Logging
CrawlerAPIrefactoring(GSoC2014)
AnothermilestoneforlastGoogleSummerofCodewasarefactoringoftheinternalAPI,seekingasimplerandeasier
usage. Checknewcoreinterfacein: CoreAPI
AcommonsituationwhereyouwillfacethesechangesiswhilerunningScrapyfromscripts. Here’saquickexample
ofhowtorunaSpidermanuallywiththenewAPI:
from scrapy.crawler import CrawlerProcess
process = CrawlerProcess({
'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(MySpider)
process.start()
BearinmindthisfeatureisstillunderdevelopmentanditsAPImaychangeuntilitreachesastablestatus.
SeemoreexamplesforscriptsrunningScrapy: CommonPractices
ModuleRelocations
There’sbeenalargerearrangementofmodulestryingtoimprovethegeneralstructureofScrapy. Mainchangeswere
separatingvarioussubpackagesintonewprojectsanddissolvingbothscrapy.contribandscrapy.contrib_exp
into top level packages. Backward compatibility was kept among internal relocations, while importing deprecated
modulesexpectwarningsindicatingtheirnewplace.
Fulllistofrelocations
Outsourcedpackages
372 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
(cid:242) Note
These extensions went through some minor changes, e.g. some setting names were changed. Please check the
documentationineachnewrepositorytogetfamiliarwiththenewusage.
Oldlocation Newlocation
scrapy.commands.deploy scrapyd-client(Seeotheralternativeshere: DeployingSpiders)
scrapy.contrib.djangoitem scrapy-djangoitem
scrapy.webservice scrapy-jsonrpc
scrapy.contrib_expandscrapy.contribdissolutions
Oldlocation Newlocation
scrapy.contrib_exp.downloadermiddleware.decompressionscrapy.downloadermiddlewares.decompression
scrapy.contrib_exp.iterators scrapy.utils.iterators
scrapy.contrib.downloadermiddleware scrapy.downloadermiddlewares
scrapy.contrib.exporter scrapy.exporters
scrapy.contrib.linkextractors scrapy.linkextractors
scrapy.contrib.loader scrapy.loader
scrapy.contrib.loader.processor scrapy.loader.processors
scrapy.contrib.pipeline scrapy.pipelines
scrapy.contrib.spidermiddleware scrapy.spidermiddlewares
scrapy.contrib.spiders scrapy.spiders
scrapy.extensions.*
• scrapy.contrib.closespider
• scrapy.contrib.corestats
• scrapy.contrib.debug
• scrapy.contrib.feedexport
• scrapy.contrib.httpcache
• scrapy.contrib.logstats
• scrapy.contrib.memdebug
• scrapy.contrib.memusage
• scrapy.contrib.spiderstate
• scrapy.contrib.statsmailer
• scrapy.contrib.throttle
PluralrenamesandModulesunification
7.1. Releasenotes 373

ScrapyDocumentation,Release2.13.3
Oldlocation Newlocation
scrapy.command scrapy.commands
scrapy.dupefilter scrapy.dupefilters
scrapy.linkextractor scrapy.linkextractors
scrapy.spider scrapy.spiders
scrapy.squeue scrapy.squeues
scrapy.statscol scrapy.statscollectors
scrapy.utils.decorator scrapy.utils.decorators
Classrenames
Oldlocation Newlocation
scrapy.spidermanager.SpiderManager scrapy.spiderloader.SpiderLoader
Settingsrenames
Oldlocation Newlocation
SPIDER_MANAGER_CLASS SPIDER_LOADER_CLASS
Changelog
NewFeaturesandEnhancements
• Pythonlogging(issue1060,issue1235,issue1236,issue1240,issue1259,issue1278,issue1286)
• FEED_EXPORT_FIELDSoption(issue1159,issue1224)
• Dnscachesizeandtimeoutoptions(issue1132)
• supportnamespaceprefixinxmliter_lxml(issue963)
• Reactorthreadpoolmaxsizesetting(issue1123)
• Allowspiderstoreturndicts. (issue1081)
• AddResponse.urljoin()helper(issue1086)
• lookin~/.config/scrapy.cfgforuserconfig(issue1098)
• handleTLSSNI(issue1101)
• Selectorlistextractfirst(issue624,issue1145)
• AddedJmesSelect(issue1016)
• addgzipcompressiontofilesystemhttpcachebackend(issue1020)
• CSSsupportinlinkextractors(issue983)
• httpcachedont_cachemeta#19#689(issue821)
• addsignaltobesentwhenrequestisdroppedbythescheduler(issue961)
• avoiddownloadlargeresponse(issue946)
• AllowtospecifythequotecharinCSVFeedSpider(issue882)
• Addrefererto“Spidererrorprocessing”logmessage(issue795)
374 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• processrobots.txtonce(issue896)
• GSoCPer-spidersettings(issue854)
• Addprojectnamevalidation(issue817)
• GSoC API cleanup (issue 816, issue 1128, issue 1147, issue 1148, issue 1156, issue 1185, issue 1187, issue
1258,issue1268,issue1276,issue1285,issue1284)
• BemoreresponsivewithIOoperations(issue1074andissue1075)
• Doleveldbcompactionforhttpcacheonclosing(issue1297)
DeprecationsandRemovals
• Deprecatehtmlparserlinkextractor(issue1205)
• removedeprecatedcodefromFeedExporter(issue1155)
• aleftoverfor.15compatibility(issue925)
• dropsupportforCONCURRENT_REQUESTS_PER_SPIDER(issue895)
• Dropoldenginecode(issue911)
• DeprecateSgmlLinkExtractor(issue777)
Relocations
• Moveexporters/__init__.pytoexporters.py(issue1242)
• Movebaseclassestotheirpackages(issue1218,issue1233)
• Modulerelocation(issue1181,issue1210)
• renameSpiderManagertoSpiderLoader(issue1166)
• Removedjangoitem(issue1177)
• removescrapydeploycommand(issue1102)
• dissolvecontrib_exp(issue1134)
• Deletedbinfolderfromroot,fixes#913(issue914)
• Removejsonrpcbasedwebservice(issue859)
• MoveTestcasesunderprojectrootdir(issue827,issue841)
• Fixbackwardincompatibilityforrelocatedpathsinsettings(issue1267)
Documentation
• CrawlerProcessdocumentation(issue1190)
• Favoringwebscrapingoverscreenscrapinginthedescriptions(issue1188)
• SomeimprovementsforScrapytutorial(issue1180)
• DocumentingFilesPipelinetogetherwithImagesPipeline(issue1150)
• deploymentdocstweaks(issue1164)
• Addeddeploymentsectioncoveringscrapyd-deployandshub(issue1124)
• Addingmoresettingstoprojecttemplate(issue1073)
• someimprovementstooverviewpage(issue1106)
• Updatedlinkindocs/topics/architecture.rst(issue647)
7.1. Releasenotes 375

ScrapyDocumentation,Release2.13.3
• DOCreordertopics(issue1022)
• updatinglistofRequest.metaspecialkeys(issue1071)
• DOCdocumentdownload_timeout(issue898)
• DOCsimplifyextensiondocs(issue893)
• Leaksdocs(issue894)
• DOCdocumentfrom_crawlermethodforitempipelines(issue904)
• Spider_errordoesn’tsupportdeferreds(issue1292)
• Corrections&Sphinxrelatedfixes(issue1220,issue1219,issue1196,issue1172,issue1171,issue1169,issue
1160,issue1154,issue1127,issue1112,issue1105,issue1041,issue1082,issue1033,issue944,issue866,
issue864,issue796,issue1260,issue1271,issue1293,issue1298)
Bugfixes
• Itemmultiinheritancefix(issue353,issue1228)
• ItemLoader.load_item: iterateovercopyoffields(issue722)
• FixUnhandlederrorinDeferred(RobotsTxtMiddleware)(issue1131,issue1197)
• ForcetoreadDOWNLOAD_TIMEOUTasint(issue954)
• scrapy.utils.misc.load_objectshouldprintfulltraceback(issue902)
• Fixbugfor“.local”hostname(issue878)
• FixforEnabledextensions,middlewares,pipelinesinfonotprintedanymore(issue879)
• fixdont_merge_cookiesbadbehaviourwhensettofalseonmeta(issue846)
Python3InProgressSupport
• disablescrapy.telnetiftwisted.conchisnotavailable(issue1161)
• fixPython3syntaxerrorsinajaxcrawl.py(issue1162)
• morepython3compatibilitychangesforurllib(issue1121)
• assertItemsEqualwasrenamedtoassertCountEqualinPython3. (issue1070)
• Importunittest.mockifavailable. (issue1066)
• updateddeprecatedcgi.parse_qsltousesix’sparse_qsl(issue909)
• PreventPython3portregressions(issue830)
• PY3: useMutableMappingforpython3(issue810)
• PY3: usesix.BytesIOandsix.moves.cStringIO(issue803)
• PY3: fixxmlrpclibandemailimports(issue801)
• PY3: usesixforrobotparserandurlparse(issue800)
• PY3: usesix.iterkeys,six.iteritems,andtempfile(issue799)
• PY3: fixhas_keyandusesix.moves.configparser(issue798)
• PY3: usesix.moves.cPickle(issue797)
• PY3makeitpossibletorunsometestsinPython3(issue776)
Tests
• removeunnecessarylinesfrompy3-ignores(issue1243)
376 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Fixremainingwarningsfrompytestwhilecollectingtests(issue1206)
• Adddocsbuildtotravis(issue1234)
• TSTdon’tcollecttestsfromdeprecatedmodules. (issue1165)
• installservice_identitypackageinteststopreventwarnings(issue1168)
• FixdeprecatedsettingsAPIintests(issue1152)
• AddtestforwebclientwithPOSTmethodandnobodygiven(issue1089)
• py3-ignores.txtsupportscomments(issue1044)
• modernizesomeoftheasserts(issue835)
• selector.__repr__test(issue779)
Coderefactoring
• CSVFeedSpidercleanup: useiterate_spider_output(issue1079)
• removeunnecessarycheckfromscrapy.utils.spider.iter_spider_output(issue1078)
• Pydispatchpep8(issue992)
• Removedunused‘load=False’parameterfromwalk_modules()(issue871)
• Forconsistency,usejob_dirhelperinSpiderStateextension. (issue805)
• rename“sflo”localvariablestolesscryptic“log_observer”(issue775)
7.1.65 Scrapy 0.24.6 (2015-04-20)
• encodeinvalidxpathwithunicode_escapeunderPY2(commit07cb3e5)
• fixIPythonshellscopeissueandloadIPythonuserconfig(commit2c8e573)
• Fixsmalltypointhedocs(commitd694019)
• Fixsmalltypo(commitf92fa83)
• Convertedsel.xpath()callstoresponse.xpath()inExtractingthedata(commitc2c6d15)
7.1.66 Scrapy 0.24.5 (2015-02-25)
• Supportnew_getEndpointAgentsignaturesonTwisted15.0.0(commit540b9bc)
• DOCacouplemorereferencesarefixed(commitb4c454b)
• DOCfixareference(commite3c1260)
• t.i.b.ThreadedResolverisnowanew-styleclass(commit9e13f42)
• S3DownloadHandler: fixauthforrequestswithquotedpaths/queryparams(commitcdb9a0b)
• fixedthevariabletypesinmailsenderdocumentation(commitbb3a848)
• Resetitems_scrapedinsteadofitem_count(commitedb07a4)
• Tentativeattentionmessageaboutwhatdocumenttoreadforcontributions(commit7ee6f7a)
• mitmproxy0.10.1needsnetlib0.10.1too(commit874fcdd)
• pinmitmproxy0.10.1as>0.11doesnotworkwithtests(commitc6b21f0)
• Testtheparsecommandlocallyinsteadofagainstanexternalurl(commitc3a6628)
• PatchesTwistedissuewhileclosingtheconnectionpoolonHTTPDownloadHandler(commitd0bf957)
7.1. Releasenotes 377

ScrapyDocumentation,Release2.13.3
• Updatesdocumentationondynamicitemclasses. (commiteeb589a)
• Mergepullrequest#943fromLazar-T/patch-3(commit5fdab02)
• typo(commitb0ae199)
• pywin32isrequiredbyTwisted. closes#937(commit5cb0cfb)
• Updateinstall.rst(commit781286b)
• Mergepullrequest#928fromLazar-T/patch-1(commitb415d04)
• commainsteadoffullstop(commit627b9ba)
• Mergepullrequest#885fromjsma/patch-1(commitde909ad)
• Updaterequest-response.rst(commit3f3263d)
• SgmlLinkExtractor-fixforparsing<area>tagwithUnicodepresent(commit49b40f0)
7.1.67 Scrapy 0.24.4 (2014-08-09)
• pemfileisusedbymockserverandrequiredbyscrapybench(commit5eddc68b63)
• scrapybenchneedsscrapy.tests*(commitd6cb999)
7.1.68 Scrapy 0.24.3 (2014-08-09)
• noneedtowastetravis-citimeonpy3for0.24(commit8e080c1)
• Updateinstallationdocs(commit1d0c096)
• ThereisatroveclassifierforScrapyframework! (commit4c701d7)
• updateotherplaceswherew3libversionismentioned(commitd109c13)
• Updatew3librequirementto1.8.0(commit39d2ce5)
• Usew3lib.html.replace_entities()(remove_entities()isdeprecated)(commit180d3ad)
• setzip_safe=False(commita51ee8b)
• donotshiptestspackage(commitee3b371)
• scrapy.batisnotneededanymore(commitc3861cf)
• Modernizesetup.py(commit362e322)
• headerscannothandlenon-stringvalues(commit94a5c65)
• fixftptestcases(commita274a7f)
• Thesumupoftravis-cibuildsaretakinglike50mintocomplete(commitae1e2cc)
• Updateshell.rsttypo(commite49c96a)
• removesweirdindentationintheshellresults(commit1ca489d)
• improvedexplanations,clarifiedblogpostassource,addedlinkforXPathstringfunctionsinthespec(commit
65c8f05)
• renamedUserTimeoutErrorandServerTimeouterror#583(commit037f6ab)
• addingsomexpathtipstoselectorsdocs(commit2d103e0)
• fixteststoaccountforhttps://github.com/scrapy/w3lib/pull/23(commitf8d366a)
• get_func_argsmaximumrecursionfix#728(commit81344ea)
378 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Updatedinput/outputprocessorexampleaccordingto#560. (commitf7c4ea8)
• FixedPythonsyntaxintutorial. (commitdb59ed9)
• Addtestcasefortunnelingproxy(commitf090260)
• BugfixforleakingProxy-Authorizationheadertoremotehostwhenusingtunneling(commitd8793af)
• ExtractlinksfromXHTMLdocumentswithMIME-Type“application/xml”(commited1f376)
• Mergepullrequest#793fromroysc/patch-1(commit91a1106)
• Fixtypoincommands.rst(commit743e1e2)
• bettertestcaseforsettings.overrides.setdefault(commite22daaf)
• UsingCRLFaslinemarkeraccordingtohttp1.1definition(commit5ec430b)
7.1.69 Scrapy 0.24.2 (2014-07-08)
• Useamutablemappingtoproxydeprecatedsettings.overridesandsettings.defaultsattribute(commite5e8133)
• thereisnotsupportforpython3yet(commit3cd6146)
• UpdatepythoncompatibleversionsettoDebianpackages(commitfa5d76b)
• DOCfixformattinginreleasenotes(commitc6a9e20)
7.1.70 Scrapy 0.24.1 (2014-06-27)
• FixdeprecatedCrawlerSettingsandincreasebackwardcompatibilitywith.defaultsattribute(commit8e3f20a)
7.1.71 Scrapy 0.24.0 (2014-06-26)
Enhancements
• ImproveScrapytop-levelnamespace(issue494,issue684)
• Addselectorshortcutstoresponses(issue554,issue690)
• AddnewlxmlbasedLinkExtractortoreplaceunmaintainedSgmlLinkExtractor(issue559,issue761,issue763)
• CleanupsettingsAPI-partofper-spidersettingsGSoCproject(issue737)
• AddUTF8encodingheadertotemplates(issue688,issue762)
• Telnetconsolenowbindsto127.0.0.1bydefault(issue699)
• UpdateDebian/Ubuntuinstallinstructions(issue509,issue549)
• DisablesmartstringsinlxmlXPathevaluations(issue535)
• Restorefilesystembasedcacheasdefaultforhttpcachemiddleware(issue541,issue500,issue571)
• ExposecurrentcrawlerinScrapyshell(issue557)
• ImprovetestsuitecomparingCSVandXMLexporters(issue570)
• Newoffsite/filteredandoffsite/domainsstats(issue566)
• Supportprocess_linksasgeneratorinCrawlSpider(issue555)
• VerboseloggingandnewstatscountersforDupeFilter(issue553)
• AddamimetypeparametertoMailSender.send()(issue602)
• Generalizefilepipelinelogmessages(issue622)
7.1. Releasenotes 379

ScrapyDocumentation,Release2.13.3
• ReplaceunencodeablecodepointswithhtmlentitiesinSGMLLinkExtractor(issue565)
• ConvertedSEPdocumentstorstformat(issue629,issue630,issue638,issue632,issue636,issue640,issue
635,issue634,issue639,issue637,issue631,issue633,issue641,issue642)
• Testsanddocsforclickdata’snrindexinFormRequest(issue646,issue645)
• Allowtodisableadownloaderhandlerjustlikeanyothercomponent(issue650)
• Logwhenarequestisdiscardedaftertoomanyredirections(issue654)
• Logerrorresponsesiftheyarenothandledbyspidercallbacks(issue612,issue656)
• Addcontent-typechecktohttpcompressionmw(issue193,issue660)
• Runpypytestsusinglatestpypifromppa(issue674)
• Runtestsuiteusingpytestinsteadoftrial(issue679)
• Builddocsandcheckfordeadlinksintoxenvironment(issue687)
• Makescrapy.version_infoatupleofintegers(issue681,issue692)
• Inferexporter’soutputformatfromfilenameextensions(issue546,issue659,issue760)
• Supportcase-insensitivedomainsinurl_is_from_any_domain()(issue693)
• Removepep8warningsinprojectandspidertemplates(issue698)
• Testsanddocsforrequest_fingerprintfunction(issue597)
• UpdateSEP-19forGSoCprojectper-spider settings(issue705)
• Setexitcodetonon-zerowhencontractsfails(issue727)
• AddasettingtocontrolwhatclassisinstantiatedasDownloadercomponent(issue738)
• Passresponseinitem_droppedsignal(issue724)
• Improvescrapy checkcontractscommand(issue733,issue752)
• Documentspider.closed()shortcut(issue719)
• Documentrequest_scheduledsignal(issue746)
• Addanoteaboutreportingsecurityissues(issue697)
• AddLevelDBhttpcachestoragebackend(issue626,issue500)
• Sortspiderlistoutputof scrapy listcommand(issue742)
• Multipledocumentationenhancementsandfixes(issue575,issue587,issue590,issue596,issue610,issue617,
issue618,issue627,issue613,issue643,issue654,issue675,issue663,issue711,issue714)
Bugfixes
• EncodeunicodeURLvaluewhencreatingLinksinRegexLinkExtractor(issue561)
• IgnoreNonevaluesinItemLoaderprocessors(issue556)
• FixlinktextwhenthereisaninnertaginSGMLLinkExtractorandHtmlParserLinkExtractor(issue485,issue
574)
• Fixwrongchecksonsubclassingofdeprecatedclasses(issue581,issue584)
• Handleerrorscausedbyinspect.stack()failures(issue582)
• Fixareferencetounexistentengineattribute(issue593,issue594)
• Fixdynamicitemclassexampleusageoftype()(issue603)
380 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Uselucasdemarchi/codespelltofixtypos(issue628)
• FixdefaultvalueofattrsargumentinSgmlLinkExtractortobetuple(issue661)
• FixXXEflawinsitemapreader(issue676)
• Fixenginetosupportfilteredstartrequests(issue707)
• Fixoffsitemiddlewarecaseonurlswithnohostnames(issue745)
• Testsuitedoesn’trequirePILanymore(issue585)
7.1.72 Scrapy 0.22.2 (released 2014-02-14)
• fixareferencetounexistentengine.slots. closes#593(commit13c099a)
• downloaderMWdoctypo(spiderMWdoccopyremnant)(commit8ae11bf)
• Correcttypos(commit1346037)
7.1.73 Scrapy 0.22.1 (released 2014-02-08)
• localhost666canresolveundercertaincircumstances(commit2ec2279)
• testinspect.stackfailure(commitcc3eda3)
• Handlecaseswheninspect.stack()fails(commit8cb44f9)
• Fixwrongchecksonsubclassingofdeprecatedclasses. closes#581(commit46d98d6)
• Docs: 4-spaceindentforfinalspiderexample(commit13846de)
• FixHtmlParserLinkExtractorandtestsafter#485merge(commit368a946)
• BaseSgmlLinkExtractor: Fixedthemissingspacewhenthelinkhasaninnertag(commitb566388)
• BaseSgmlLinkExtractor: Addedunittestofalinkwithaninnertag(commitc1cb418)
• BaseSgmlLinkExtractor: Fixedunknown_endtag()sothatitonlysetcurrent_link=Nonewhentheendtagmatch
theopeningtag(commit7e4d627)
• FixtestsforTravis-CIbuild(commit76c7e20)
• replaceunencodeablecodepointswithhtmlentities. fixes#562and#285(commit5f87b17)
• RegexLinkExtractor: encodeURLunicodevaluewhencreatingLinks(commitd0ee545)
• Updatedthetutorialcrawloutputwithlatestoutput. (commit8da65de)
• Updatedshelldocswiththecrawlerreferenceandfixedtheactualshelloutput. (commit875b9ab)
• PEP8minoredits. (commitf89efaf)
• ExposecurrentcrawlerintheScrapyshell. (commit5349cec)
• UnusedreimportandPEP8minoredits. (commit387f414)
• IgnoreNone’svalueswhenusingtheItemLoader. (commit0632546)
• DOCFixedHTTPCACHE_STORAGEtypointhedefaultvaluewhichisnowFilesysteminsteadDbm. (commit
cde9a8c)
• showUbuntusetupinstructionsasliteralcode(commitfb5c9c5)
• UpdateUbuntuinstallationinstructions(commit70fb105)
• Mergepullrequest#550fromstray-leone/patch-1(commit6f70b6a)
• modifytheversionofScrapyUbuntupackage(commit725900d)
7.1. Releasenotes 381

ScrapyDocumentation,Release2.13.3
• fix0.22.0releasedate(commitaf0219a)
• fixtyposinnews.rstandremove(notreleasedyet)header(commitb7f58f4)
7.1.74 Scrapy 0.22.0 (released 2014-01-17)
Enhancements
• [Backwardincompatible]SwitchedHTTPCacheMiddlewarebackendtofilesystem(issue541)Torestoreold
backendsetHTTPCACHE_STORAGEtoscrapy.contrib.httpcache.DbmCacheStorage
• Proxyhttps://urlsusingCONNECTmethod(issue392,issue397)
• Addamiddlewaretocrawlajaxcrawlablepagesasdefinedbygoogle(issue343)
• Renamescrapy.spider.BaseSpidertoscrapy.spider.Spider(issue510,issue519)
• SelectorsregisterEXSLTnamespacesbydefault(issue472)
• Unifyitemloaderssimilartoselectorsrenaming(issue461)
• MakeRFPDupeFilterclasseasilysubclassable(issue533)
• ImprovetestcoverageandforthcomingPython3support(issue525)
• PromotestartupinfoonsettingsandmiddlewaretoINFOlevel(issue520)
• Supportpartialsinget_func_argsutil(issue506,issue:504)
• Allowrunningindividualtestsviatox(issue503)
• Updateextensionsignoredbylinkextractors(issue498)
• Addmiddlewaremethodstogetfiles/images/thumbspaths(issue490)
• Improveoffsitemiddlewaretests(issue478)
• AddawaytoskipdefaultRefererheadersetbyRefererMiddleware(issue475)
• Donotsendx-gzipindefaultAccept-Encodingheader(issue469)
• Supportdefininghttperrorhandlingusingsettings(issue466)
• Usemodernpythonidiomswhereveryoufindlegacies(issue497)
• Improveandcorrectdocumentation(issue527,issue524,issue521,issue517,issue512,issue505,issue502,
issue489,issue465,issue460,issue425,issue536)
Fixes
• UpdateSelectorclassimportsinCrawlSpidertemplate(issue484)
• Fixunexistentreferencetoengine.slots(issue464)
• Donottrytocallbody_as_unicode()onanon-TextResponseinstance(issue462)
• WarnwhensubclassingXPathItemLoader,previouslyitonlywarnedoninstantiation. (issue523)
• WarnwhensubclassingXPathSelector,previouslyitonlywarnedoninstantiation. (issue537)
• Multiplefixestomemorystats(issue531,issue530,issue529)
• FixoverridingurlinFormRequest.from_response()(issue507)
• Fixtestsrunnerunderpip1.5(issue513)
• Fixloggingerrorwhenspidernameisunicode(issue479)
382 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.75 Scrapy 0.20.2 (released 2013-12-09)
• UpdateCrawlSpiderTemplatewithSelectorchanges(commit6d1457d)
• fixmethodnameintutorial. closesGH-480(commitb4fc359
7.1.76 Scrapy 0.20.1 (released 2013-11-28)
• include_package_dataisrequiredtobuildwheelsfrompublishedsources(commit5ba1ad5)
• process_parallelwasleakingthefailuresonitsinternaldeferreds. closes#458(commit419a780)
7.1.77 Scrapy 0.20.0 (released 2013-11-08)
Enhancements
• NewSelector’sAPIincludingCSSselectors(issue395andissue426),
• Request/Responseurl/bodyattributesarenowimmutable(modifyingthemhadbeendeprecatedforalongtime)
• ITEM_PIPELINES isnowdefinedasadict(insteadofalist)
• SitemapspidercanfetchalternateURLs(issue360)
• Selector.remove_namespaces()nowremovenamespacesfromelement’sattributes. (issue416)
• PavedtheroadforPython3.3+(issue435,issue436,issue431,issue452)
• Newitemexporterusingnativepythontypeswithnestingsupport(issue366)
• TuneHTTP1.1poolsizesoitmatchesconcurrencydefinedbysettings(commitb43b5f575)
• scrapy.mail.MailSendernowcanconnectoverTLSorupgradeusingSTARTTLS(issue327)
• NewFilesPipelinewithfunctionalityfactoredoutfromImagesPipeline(issue370,issue409)
• RecommendPillowinsteadofPILforimagehandling(issue317)
• AddedDebianpackagesforUbuntuQuantalandRaring(commit86230c0)
• Mockserver(usedfortests)canlistenforHTTPSrequests(issue410)
• Removemultispidersupportfrommultiplecorecomponents(issue422,issue421,issue420,issue419,issue
423,issue418)
• Travis-CInowtestsScrapychangesagainstdevelopmentversionsof w3libandqueuelibpythonpackages.
• Addpypy2.1tocontinuousintegrationtests(commitecfa7431)
• Pylinted,pep8andremovedold-styleexceptionsfromsource(issue430,issue432)
• Useimportlibforparametricimports(issue445)
• HandlearegressionintroducedinPython2.7.5thataffectsXmlItemExporter(issue372)
• BugfixcrawlingshutdownonSIGINT(issue450)
• DonotsubmitresettypeinputsinFormRequest.from_response(commitb326b87)
• Donotsilencedownloaderrorswhenrequesterrbackraisesanexception(commit684cfc0)
Bugfixes
• FixtestsunderDjango1.6(commitb6bed44c)
• LotofbugfixestoretrymiddlewareunderdisconnectionsusingHTTP1.1downloadhandler
• FixinconsistenciesamongTwistedreleases(issue406)
7.1. Releasenotes 383

ScrapyDocumentation,Release2.13.3
• FixScrapyshellbugs(issue418,issue407)
• Fixinvalidvariablenameinsetup.py(issue429)
• Fixtutorialreferences(issue387)
• Improverequest-responsedocs(issue391)
• Improvebestpracticesdocs(issue399,issue400,issue401,issue402)
• Improvedjangointegrationdocs(issue404)
• Documentbindaddressrequestmeta(commit37c24e01d7)
• ImproveRequestclassdocumentation(issue226)
Other
• DroppedPython2.6support(issue448)
• Addcssselectpythonpackageasinstalldependency
• Droplibxml2andmultiselector’sbackendsupport,lxmlisrequiredfromnowon.
• MinimumTwistedversionincreasedto10.0.0,droppedTwisted8.0support.
• Runningtestsuitenowrequiresmockpythonlibrary(issue390)
Thanks
Thankstoeveryonewhocontributetothisrelease!
Listofcontributorssortedbynumberofcommits:
69 Daniel Graña <dangra@...>
37 Pablo Hoffman <pablo@...>
13 Mikhail Korobov <kmike84@...>
9 Alex Cepoi <alex.cepoi@...>
9 alexanderlukanin13 <alexander.lukanin.13@...>
8 Rolando Espinoza La fuente <darkrho@...>
8 Lukasz Biedrycki <lukasz.biedrycki@...>
6 Nicolas Ramirez <nramirez.uy@...>
3 Paul Tremberth <paul.tremberth@...>
2 Martin Olveyra <molveyra@...>
2 Stefan <misc@...>
2 Rolando Espinoza <darkrho@...>
2 Loren Davie <loren@...>
2 irgmedeiros <irgmedeiros@...>
1 Stefan Koch <taikano@...>
1 Stefan <cct@...>
1 scraperdragon <dragon@...>
1 Kumara Tharmalingam <ktharmal@...>
1 Francesco Piccinno <stack.box@...>
1 Marcos Campal <duendex@...>
1 Dragon Dave <dragon@...>
1 Capi Etheriel <barraponto@...>
1 cacovsky <amarquesferraz@...>
1 Berend Iwema <berend@...>
384 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.78 Scrapy 0.18.4 (released 2013-10-10)
• IPythonrefusestoupdatethenamespace. fix#396(commit3d32c4f)
• FixAlreadyCalledErrorreplacingarequestinshellcommand. closes#407(commitb1d8919)
• Fixstart_requests()lazinessandearlyhangs(commit89faf52)
7.1.79 Scrapy 0.18.3 (released 2013-10-03)
• fixregressiononlazyevaluationofstartrequests(commit12693a5)
• forms: donotsubmitresetinputs(commite429f63)
• increaseunittesttimeoutstodecreasetravisfalsepositivefailures(commit912202e)
• backportmasterfixestojsonexporter(commitcfc2d46)
• Fixpermissionandsetumaskbeforegeneratingsdisttarball(commit06149e0)
7.1.80 Scrapy 0.18.2 (released 2013-09-03)
• Backportscrapy checkcommandfixesandbackwardcompatiblemulticrawlerprocess(issue339)
7.1.81 Scrapy 0.18.1 (released 2013-08-27)
• removeextraimportaddedbycherrypickedchanges(commitd20304e)
• fixcrawlingtestsundertwistedpre11.0.0(commit1994f38)
• py26cannotformatzerolengthfields{}(commitabf756f)
• testPotentiaDataLosserrorsonunboundresponses(commitb15470d)
• Treatresponseswithoutcontent-lengthorTransfer-Encodingasgoodresponses(commitc4bf324)
• donoincludeResponseFailedifhttp11handlerisnotenabled(commit6cbe684)
• NewHTTPclientwrapsconnectionlostinResponseFailedexception. fix#373(commit1a20bba)
• limittravis-cibuildmatrix(commit3b01bb8)
• Mergepullrequest#375frompeterarenot/patch-1(commitfa766d7)
• Fixedsoitreferstothecorrectfolder(commit3283809)
• addedQuantal&RaringtosupportUbuntureleases(commit1411923)
• fixretrymiddlewarewhichdidn’tretrycertainconnectionerrorsaftertheupgradetohttp1client,closesGH-373
(commitbb35ed0)
• fixXmlItemExporterinPython2.7.4and2.7.5(commitde3e451)
• minorupdatesto0.18releasenotes(commitc45e5f1)
• fixcontributorslistformat(commit0b60031)
7.1.82 Scrapy 0.18.0 (released 2013-08-09)
• LotofimprovementstotestsuiterunusingTox,includingawaytotestonpypi
• HandleGETparametersforAJAXcrawlableurls(commit3fe2a32)
• Uselxmlrecoveroptiontoparsesitemaps(issue347)
• Bugfixcookiemergingbyhostnameandnotbynetloc(issue352)
7.1. Releasenotes 385

ScrapyDocumentation,Release2.13.3
• SupportdisablingHttpCompressionMiddlewareusingaflagsetting(issue359)
• SupportxmlnamespacesusingiternodesparserinXMLFeedSpider(issue12)
• Supportdont_cacherequestmetaflag(issue19)
• Bugfixscrapy.utils.gz.gunzipbrokenbychangesinpython2.7.4(commit4dc76e)
• BugfixurlencodingonSgmlLinkExtractor(issue24)
• BugfixTakeFirstprocessorshouldn’tdiscardzero(0)value(issue59)
• Supportnesteditemsinxmlexporter(issue66)
• Improvecookieshandlingperformance(issue77)
• Logdupefilteredrequestsonce(issue105)
• Splitredirectionmiddlewareintostatusandmetabasedmiddlewares(issue78)
• UseHTTP1.1asdefaultdownloaderhandler(issue109andissue318)
• SupportxpathformselectiononFormRequest.from_response(issue185)
• BugfixunicodedecodingerroronSgmlLinkExtractor(issue199)
• Bugfixsignaldispatchingonpypiinterpreter(issue205)
• Improverequestdelayandconcurrencyhandling(issue206)
• AddRFC2616cachepolicytoHttpCacheMiddleware(issue212)
• Allowcustomizationofmessagesloggedbyengine(issue214)
• MultiplesimprovementstoDjangoItem(issue217,issue218,issue221)
• ExtendScrapycommandsusingsetuptoolsentrypoints(issue260)
• Allowspiderallowed_domainsvaluetobeset/tuple(issue261)
• Supportsettings.getdict(issue269)
• Simplifyinternalscrapy.core.scraperslothandling(issue271)
• AddedItem.copy(issue290)
• Collectidledownloaderslots(issue297)
• Addftp:// schemedownloaderhandler(issue329)
• AddeddownloaderbenchmarkwebserverandspidertoolsBenchmarking
• Movedpersistent(ondisk)queuestoaseparateproject(queuelib)whichScrapynowdependson
• AddScrapycommandsusingexternallibraries(issue260)
• Added--pdboptiontoscrapycommandlinetool
• AddedXPathSelector.remove_namespaceswhichallowstoremoveallnamespacesfromXMLdocuments
forconvenience(toworkwithnamespace-lessXPaths). DocumentedinSelectors.
• Severalimprovementstospidercontracts
• NewdefaultmiddlewarenamedMetaRefreshMiddlewarethathandlesmeta-refreshhtmltagredirections,
• MetaRefreshMiddlewareandRedirectMiddlewarehavedifferentprioritiestoaddress#62
• addedfrom_crawlermethodtospiders
• addedsystemtestswithmockserver
386 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• moreimprovementstomacOScompatibility(thanksAlexCepoi)
• severalmorecleanupstosingletonsandmulti-spidersupport(thanksNicolasRamirez)
• supportcustomdownloadslots
• added–spideroptionto“shell”command.
• logoverriddensettingswhenScrapystarts
Thankstoeveryonewhocontributetothisrelease. Hereisalistofcontributorssortedbynumberofcommits:
130 Pablo Hoffman <pablo@...>
97 Daniel Graña <dangra@...>
20 Nicolás Ramírez <nramirez.uy@...>
13 Mikhail Korobov <kmike84@...>
12 Pedro Faustino <pedrobandim@...>
11 Steven Almeroth <sroth77@...>
5 Rolando Espinoza La fuente <darkrho@...>
4 Michal Danilak <mimino.coder@...>
4 Alex Cepoi <alex.cepoi@...>
4 Alexandr N Zamaraev (aka tonal) <tonal@...>
3 paul <paul.tremberth@...>
3 Martin Olveyra <molveyra@...>
3 Jordi Llonch <llonchj@...>
3 arijitchakraborty <myself.arijit@...>
2 Shane Evans <shane.evans@...>
2 joehillen <joehillen@...>
2 Hart <HartSimha@...>
2 Dan <ellisd23@...>
1 Zuhao Wan <wanzuhao@...>
1 whodatninja <blake@...>
1 vkrest <v.krestiannykov@...>
1 tpeng <pengtaoo@...>
1 Tom Mortimer-Jones <tom@...>
1 Rocio Aramberri <roschegel@...>
1 Pedro <pedro@...>
1 notsobad <wangxiaohugg@...>
1 Natan L <kuyanatan.nlao@...>
1 Mark Grey <mark.grey@...>
1 Luan <luanpab@...>
1 Libor Nenadál <libor.nenadal@...>
1 Juan M Uys <opyate@...>
1 Jonas Brunsgaard <jonas.brunsgaard@...>
1 Ilya Baryshev <baryshev@...>
1 Hasnain Lakhani <m.hasnain.lakhani@...>
1 Emanuel Schorsch <emschorsch@...>
1 Chris Tilden <chris.tilden@...>
1 Capi Etheriel <barraponto@...>
1 cacovsky <amarquesferraz@...>
1 Berend Iwema <berend@...>
7.1. Releasenotes 387

ScrapyDocumentation,Release2.13.3
7.1.83 Scrapy 0.16.5 (released 2013-05-30)
• obeyrequestmethodwhenScrapydeployisredirectedtoanewendpoint(commit8c4fcee)
• fixinaccuratedownloadermiddlewaredocumentation. refs#280(commit40667cb)
• doc: removelinkstodiveintopython.org,whichisnolongeravailable. closes#246(commitbd58bfa)
• Findformnodesininvalidhtml5documents(commite3d6945)
• Fixtypolabelingattrstypeboolinsteadoflist(commita274276)
7.1.84 Scrapy 0.16.4 (released 2013-01-23)
• fixesspellingerrorsindocumentation(commit6d2b3aa)
• adddocaboutdisablinganextension. refs#132(commitc90de33)
• Fixederrormessageformatting. log.err()doesn’tsupportcoolformattingandwhenerroroccurred,themessage
was: “ERROR:Errorprocessing%(item)s”(commitc16150c)
• lintandimproveimagespipelineerrorlogging(commit56b45fc)
• fixeddoctypos(commit243be84)
• adddocumentationtopics: BroadCrawls&CommonPractices(commit1fbb715)
• fixbuginScrapyparsecommandwhenspiderisnotspecifiedexplicitly. closes#209(commitc72e682)
• Updatedocs/topics/commands.rst(commit28eac7a)
7.1.85 Scrapy 0.16.3 (released 2012-12-07)
• Remove concurrency limitation when using download delays and still ensure inter-request delays are enforced
(commit487b9b5)
• adderrordetailswhenimagepipelinefails(commit8232569)
• improvemacOScompatibility(commit8dcf8aa)
• setup.py: useREADME.rsttopopulatelong_description(commit7b5310d)
• doc: removedobsoletereferencestoClientForm(commit80f9bb6)
• correctdocsfordefaultstoragebackend(commit2aa491b)
• doc: removedbrokenproxyhublinkfromFAQ(commitbdf61c4)
• FixeddocstypoinSpiderOpenCloseLoggingexample(commit7184094)
7.1.86 Scrapy 0.16.2 (released 2012-11-09)
• Scrapycontracts: python2.6compat(commita4a9199)
• Scrapycontractsverboseoption(commitec41673)
• properunittest-likeoutputforScrapycontracts(commit86635e4)
• addedopen_in_browsertodebuggingdoc(commitc9b690d)
• removedreferencetoglobalScrapystatsfromsettingsdoc(commitdd55067)
• FixSpiderStatebuginWindowsplatforms(commit58998f4)
388 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.87 Scrapy 0.16.1 (released 2012-10-26)
• fixedLogStatsextension,whichgotbrokenafterawrongmergebeforethe0.16release(commit8c780fd)
• betterbackwardcompatibilityforscrapy.conf.settings(commit3403089)
• extendeddocumentationonhowtoaccesscrawlerstatsfromextensions(commitc4da0b5)
• removed.hgtags(nolongerneedednowthatScrapyusesgit)(commitd52c188)
• fixdashesunderrstheaders(commitfa4f7f9)
• setreleasedatefor0.16.0innews(commite292246)
7.1.88 Scrapy 0.16.0 (released 2012-10-18)
Scrapychanges:
• addedSpidersContracts,amechanismfortestingspidersinaformal/reproducibleway
• addedoptions-oand-ttotherunspidercommand
• documentedAutoThrottleextensionandaddedtoextensionsinstalledbydefault. Youstillneedtoenableitwith
AUTOTHROTTLE_ENABLED
• majorStatsCollectionrefactoring: removedseparationofglobal/per-spiderstats,removedstats-relatedsignals
(stats_spider_opened,etc). Statsaremuchsimplernow,backwardcompatibilityiskeptontheStatsCollector
APIandsignals.
• addedaprocess_start_requests()methodtospidermiddlewares
• droppedSignalssingleton. SignalsshouldnowbeaccessedthroughtheCrawler.signalsattribute. Seethesignals
documentationformoreinfo.
• droppedStatsCollectorsingleton. StatscannowbeaccessedthroughtheCrawler.statsattribute. Seethestats
collectiondocumentationformoreinfo.
• documentedCoreAPI
• lxmlisnowthedefaultselectorsbackendinsteadof libxml2
• portedFormRequest.from_response()touselxmlinsteadofClientForm
• removedmodules: scrapy.xlib.BeautifulSoupandscrapy.xlib.ClientForm
• SitemapSpider: addedsupportforsitemapurlsendingin.xmland.xml.gz,eveniftheyadvertiseawrongcontent
type(commit10ed28b)
• StackTraceDumpextension: alsodumptrackreflivereferences(commitfe2ce93)
• nesteditemsnowfullysupportedinJSONandJSONLinesexporters
• addedcookiejarRequestmetakeytosupportmultiplecookiesessionsperspider
• decoupledencodingdetectioncodetow3lib.encoding,andportedScrapycodetousethatmodule
• droppedsupportforPython2.5. Seehttps://www.zyte.com/blog/scrapy-0-15-dropping-support-for-python-2-5/
• droppedsupportforTwisted2.5
• addedREFERER_ENABLED setting,tocontrolreferermiddleware
• changeddefaultuseragentto: Scrapy/VERSION (+http://scrapy.org)
• removed (undocumented) HTMLImageLinkExtractor class from scrapy.contrib.linkextractors.
image
• removedper-spidersettings(tobereplacedbyinstantiatingmultiplecrawlerobjects)
7.1. Releasenotes 389

ScrapyDocumentation,Release2.13.3
• USER_AGENTspiderattributewillnolongerwork,useuser_agentattributeinstead
• DOWNLOAD_TIMEOUTspiderattributewillnolongerwork,usedownload_timeoutattributeinstead
• removedENCODING_ALIASESsetting,asencodingauto-detectionhasbeenmovedtothew3liblibrary
• promotedtopics-djangoitemtomaincontrib
• LogFormattermethodnowreturndicts(insteadofstrings)tosupportlazyformatting(issue164,commitdcef7b0)
• downloaderhandlers(DOWNLOAD_HANDLERSsetting)nowreceivesettingsasthefirstargumentofthe__init__
method
• replaced memory usage accounting with (more portable) resource module, removed scrapy.utils.memory
module
• removedsignal: scrapy.mail.mail_sent
• removedTRACK_REFSsetting,nowtrackrefsisalwaysenabled
• DBMisnowthedefaultstoragebackendforHTTPcachemiddleware
• numberoflogmessages(perlevel)arenowtrackedthroughScrapystats(statname: log_count/LEVEL)
• numberreceivedresponsesarenowtrackedthroughScrapystats(statname: response_received_count)
• removedscrapy.log.startedattribute
7.1.89 Scrapy 0.14.4
• addedprecisetosupportedUbuntudistros(commitb7e46df)
• fixed bug in json-rpc webservice reported in https://groups.google.com/forum/#!topic/scrapy-users/
qgVBmFybNAQ/discussion. also removed no longer supported ‘run’ command from extras/scrapy-ws.py
(commit340fbdb)
• metatagattributesforcontent-typehttpequivcanbeinanyorder. #123(commit0cb68af)
• replace“importImage”bymorestandard“fromPILimportImage”. closes#88(commit4d17048)
• returntrialstatusasbin/runtests.shexitvalue. #118(commitb7b2e7f)
7.1.90 Scrapy 0.14.3
• forgottoincludepydispatchlicense. #118(commitfd85f9c)
• includeeggfilesusedbytestsuiteinsourcedistribution. #118(commitc897793)
• updatedocstringinprojecttemplatetoavoidconfusionwithgenspidercommand,whichmaybeconsideredas
anadvancedfeature. refs#107(commit2548dcc)
• addednotetodocs/topics/firebug.rstaboutgoogledirectorybeingshutdown(commit668e352)
• don’tdiscardslotwhenempty,justsaveinanotherdictinordertorecycleifneededagain. (commit8e9f607)
• donotfailhandlingunicodexpathsinlibxml2backedselectors(commitb830e95)
• fixedminormistakeinRequestobjectsdocumentation(commitbf3c9ee)
• fixedminordefectinlinkextractorsdocumentation(commitba14f38)
• removedsomeobsoleteremainingcoderelatedtosqlitesupportinScrapy(commit0665175)
390 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
7.1.91 Scrapy 0.14.2
• movebufferpointingtostartoffilebeforecomputingchecksum. refs#92(commit6a5bef2)
• Computeimagechecksumbeforepersistingimages. closes#92(commit9817df1)
• removeleakingreferencesincachedfailures(commit673a120)
• fixedbuginMemoryUsageextension: get_engine_status()takesexactly1argument(0given)(commit11133e9)
• fixedstruct.erroronhttpcompressionmiddleware. closes#87(commit1423140)
• ajaxcrawlingwasn’texpandingforunicodeurls(commit0de3fb4)
• Catchstart_requests()iteratorerrors. refs#83(commit454a21d)
• Speed-uplibxml2XPathSelector(commit2fbd662)
• updatedversioningdocaccordingtorecentchanges(commit0a070f5)
• scrapyd: fixeddocumentationlink(commit2b4e4c3)
• extras/makedeb.py: nolongerobtainingversionfromgit(commitcaffe0e)
7.1.92 Scrapy 0.14.1
• extras/makedeb.py: nolongerobtainingversionfromgit(commitcaffe0e)
• bumpedversionto0.14.1(commit6cb9e1c)
• fixedreferencetotutorialdirectory(commit4b86bd6)
• doc: removedduplicatedcallbackargumentfromRequest.replace()(commit1aeccdd)
• fixedformattingofscrapyddoc(commit8bf19e6)
• Dump stacks for all running threads and fix engine status dumped by StackTraceDump extension (commit
14a8e6e)
• addedcommentaboutwhywedisablesslonbotoimagesupload(commit5223575)
• SSLhandshakinghangswhendoingtoomanyparallelconnectionstoS3(commit63d583d)
• changetutorialtofollowchangesondmozsite(commitbcb3198)
• Avoid_disconnectedDeferredAttributeErrorexceptioninTwisted>=11.1.0(commit98f3f87)
• allowspidertosetautothrottlemaxconcurrency(commit175a4b5)
7.1.93 Scrapy 0.14
Newfeaturesandsettings
• SupportforAJAXcrawlableurls
• Newpersistentschedulerthatstoresrequestsondisk,allowingtosuspendandresumecrawls(r2737)
• added-ooptiontoscrapy crawl,ashortcutfordumpingscrapeditemsintoafile(orstandardoutputusing-)
• AddedsupportforpassingcustomsettingstoScrapydschedule.jsonapi(r2779,r2783)
• NewChunkedTransferMiddleware(enabledbydefault)tosupportchunkedtransferencoding(r2769)
• Addboto2.0supportforS3downloaderhandler(r2763)
• Addedmarshaltoformatssupportedbyfeedexports(r2744)
• Inrequesterrbacks,offendingrequestsarenowreceivedinfailure.requestattribute(r2738)
7.1. Releasenotes 391

ScrapyDocumentation,Release2.13.3
• Bigdownloaderrefactoringtosupportperdomain/ipconcurrencylimits(r2732)
– CONCURRENT_REQUESTS_PER_SPIDERsettinghasbeendeprecatedandreplacedby:
∗ CONCURRENT_REQUESTS, CONCURRENT_REQUESTS_PER_DOMAIN,
CONCURRENT_REQUESTS_PER_IP
– checkthedocumentationformoredetails
• AddedbuiltincachingDNSresolver(r2728)
• MovedAmazonAWS-relatedcomponents/extensions(SQSspiderqueue,SimpleDBstatscollector)toaseparate
project: [scaws](https://github.com/scrapinghub/scaws)(r2706,r2714)
• Movedspiderqueuestoscrapyd: scrapy.spiderqueue->scrapyd.spiderqueue(r2708)
• Movedsqliteutilstoscrapyd: scrapy.utils.sqlite->scrapyd.sqlite(r2781)
• Realsupportforreturningiteratorsonstart_requests()method. Theiteratorisnowconsumedduringthe
crawlwhenthespiderisgettingidle(r2704)
• AddedREDIRECT_ENABLED settingtoquicklyenable/disabletheredirectmiddleware(r2697)
• AddedRETRY_ENABLED settingtoquicklyenable/disabletheretrymiddleware(r2694)
• AddedCloseSpiderexceptiontomanuallyclosespiders(r2691)
• ImprovedencodingdetectionbyaddingsupportforHTML5metacharsetdeclaration(r2690)
• Refactoredclosespiderbehaviortowaitforalldownloadstofinishandbeprocessedbyspiders,beforeclosing
thespider(r2688)
• AddedSitemapSpider(seedocumentationinSpiderspage)(r2658)
• AddedLogStatsextensionforperiodicallyloggingbasicstats(likecrawledpagesandscrapeditems)(r2657)
• Makehandlingofgzippedresponsesmorerobust(#319,r2643). NowScrapywilltryanddecompressasmuch
aspossiblefromagzippedresponse,insteadoffailingwithanIOError.
• Simplified!MemoryDebuggerextensiontousestatsfordumpingmemorydebugginginfo(r2639)
• Addednewcommandtoeditspiders: scrapy edit(r2636)and -eflagtogenspidercommandthatusesit
(r2653)
• Changeddefaultrepresentationofitemstopretty-printeddicts. (r2631). Thisimprovesdefaultloggingbymaking
logmorereadableinthedefaultcase,forbothScrapedandDroppedlines.
• Addedspider_errorsignal(r2628)
• AddedCOOKIES_ENABLED setting(r2625)
• StatsarenowdumpedtoScrapylog(defaultvalueofSTATS_DUMP settinghasbeenchangedtoTrue). Thisis
tomakeScrapyusersmoreawareofScrapystatsandthedatathatiscollectedthere.
• Addedsupportfordynamicallyadjustingdownloaddelayandmaximumconcurrentrequests(r2599)
• AddednewDBMHTTPcachestoragebackend(r2576)
• Addedlistjobs.jsonAPItoScrapyd(r2571)
• CsvItemExporter: addedjoin_multivaluedparameter(r2578)
• Addednamespacesupporttoxmliter_lxml(r2552)
• ImprovedcookiesmiddlewarebymakingCOOKIES_DEBUGniceranddocumentingit(r2579)
• SeveralimprovementstoScrapydandLinkextractors
392 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Coderearrangedandremoved
• Mergeditempassedanditemscrapedconcepts,astheyhaveoftenprovedconfusinginthepast. This
means: (r2630)
– originalitem_scrapedsignalwasremoved
– originalitem_passedsignalwasrenamedtoitem_scraped
– oldloglinesScraped Item...wereremoved
– oldloglinesPassed Item...wererenamedtoScraped Item...linesanddowngradedtoDEBUG
level
• ReducedScrapycodebasebystripingpartofScrapycodeintotwonewlibraries:
– w3lib (several functions from scrapy.utils.{http,markup,multipart,response,url},
doneinr2584)
– scrapely(wasscrapy.contrib.ibl,doneinr2586)
• Removedunusedfunction: scrapy.utils.request.request_info()(r2577)
• Removed googledir project from examples/googledir. There’s now a new example project called dirbot
availableonGitHub: https://github.com/scrapy/dirbot
• RemovedsupportfordefaultfieldvaluesinScrapyitems(r2616)
• Removedexperimentalcrawlspiderv2(r2632)
• Removed scheduler middleware to simplify architecture. Duplicates filter is now done in the scheduler itself,
usingthesamedupefilteringclassasbefore(DUPEFILTER_CLASSsetting)(r2640)
• Removedsupportforpassingurlstoscrapy crawlcommand(usescrapy parseinstead)(r2704)
• RemoveddeprecatedExecutionQueue(r2704)
• Removed(undocumented)spidercontextextension(fromscrapy.contrib.spidercontext)(r2780)
• removedCONCURRENT_SPIDERSsetting(usescrapydmaxprocinstead)(r2789)
• Renamed attributes of core components: downloader.sites -> downloader.slots, scraper.sites -> scraper.slots
(r2717,r2718)
• RenamedsettingCLOSESPIDER_ITEMPASSEDtoCLOSESPIDER_ITEMCOUNT (r2655). Backwardcompatibility
kept.
7.1.94 Scrapy 0.12
Thenumberslike#NNNreferenceticketsintheoldissuetracker(Trac)whichisnolongeravailable.
Newfeaturesandimprovements
• Passeditemisnowsentintheitemargumentoftheitem_passed (#273)
• Addedverboseoptiontoscrapy versioncommand,usefulforbugreports(#298)
• HTTPcachenowstoredbydefaultintheprojectdatadir(#279)
• Addedprojectdatastoragedirectory(#276,#277)
• DocumentedfilestructureofScrapyprojects(seecommand-linetooldoc)
• NewlxmlbackendforXPathselectors(#147)
• Per-spidersettings(#245)
• SupportexitcodestosignalerrorsinScrapycommands(#248)
7.1. Releasenotes 393

ScrapyDocumentation,Release2.13.3
• Added-cargumenttoscrapy shellcommand
• Madelibxml2optional(#260)
• Newdeploycommand(#261)
• AddedCLOSESPIDER_PAGECOUNT setting(#253)
• AddedCLOSESPIDER_ERRORCOUNT setting(#254)
Scrapydchanges
• Scrapydnowusesoneprocessperspider
• Itstoresonelogfileperspiderrun,androtatethemkeepingthelatest5logsperspider(bydefault)
• Aminimalwebuiwasadded,availableathttp://localhost:6800bydefault
• Thereisnowascrapy servercommandtostartaScrapydserverofthecurrentproject
Changestosettings
• addedHTTPCACHE_ENABLEDsetting(Falsebydefault)toenableHTTPcachemiddleware
• changedHTTPCACHE_EXPIRATION_SECSsemantics: nowzeromeans“neverexpire”.
Deprecated/obsoletedfunctionality
• DeprecatedrunservercommandinfavorofservercommandwhichstartsaScrapydserver. Seealso:Scrapyd
changes
• DeprecatedqueuecommandinfavorofusingScrapydschedule.jsonAPI.Seealso: Scrapydchanges
• Removedthe!LxmlItemLoader(experimentalcontribwhichnevergraduatedtomaincontrib)
7.1.95 Scrapy 0.10
Thenumberslike#NNNreferenceticketsintheoldissuetracker(Trac)whichisnolongeravailable.
Newfeaturesandimprovements
• NewScrapyservicecalledscrapydfordeployingScrapycrawlersinproduction(#218)(documentationavail-
able)
• SimplifiedImagespipelineusagewhichdoesn’trequiresubclassingyourownimagespipelinenow(#217)
• ScrapyshellnowshowstheScrapylogbydefault(#206)
• Refactoredexecutionqueueinacommonbasecodeandpluggablebackendscalled“spiderqueues”(#220)
• Newpersistentspiderqueue(basedonSQLite)(#198),availablebydefault,whichallowstostartScrapyinserver
modeandthenschedulespiderstorun.
• AddeddocumentationforScrapycommand-linetoolandallitsavailablesub-commands. (documentationavail-
able)
• Feedexporterswithpluggablebackends(#197)(documentationavailable)
• Deferredsignals(#193)
• Addedtwonewmethodstoitempipelineopen_spider(),close_spider()withdeferredsupport(#195)
• Supportforoverridingdefaultrequestheadersperspider(#181)
394 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• Replaced default Spider Manager with one with similar functionality but not depending on Twisted Plugins
(#186)
• SplitDebianpackageintotwopackages-thelibraryandtheservice(#187)
• Scrapylogrefactoring(#188)
• Newextensionforkeepingpersistentspidercontextsamongdifferentruns(#203)
• Addeddont_redirectrequest.metakeyforavoidingredirects(#233)
• Addeddont_retryrequest.metakeyforavoidingretries(#234)
Command-linetoolchanges
• Newscrapycommandwhichreplacestheoldscrapy-ctl.py(#199)-thereisonlyoneglobalscrapycom-
mandnow,insteadofonescrapy-ctl.pyperproject-Addedscrapy.batscriptforrunningmoreconveniently
fromWindows
• Addedbashcompletiontocommand-linetool(#210)
• Renamedcommandstarttorunserver(#209)
APIchanges
• urlandbodyattributesofRequestobjectsarenowread-only(#230)
• Request.copy()andRequest.replace()nowalsocopiestheircallbackanderrbackattributes(#231)
• RemovedUrlFilterMiddlewarefromscrapy.contrib(alreadydisabledbydefault)
• Offsite middleware doesn’t filter out any request coming from a spider that doesn’t have a allowed_domains
attribute(#225)
• RemovedSpiderManagerload()method. Nowspidersareloadedinthe__init__methoditself.
• ChangestoScrapyManager(nowcalled“Crawler”):
– scrapy.core.manager.ScrapyManagerclassrenamedtoscrapy.crawler.Crawler
– scrapy.core.manager.scrapymanagersingletonmovedtoscrapy.project.crawler
• Movedmodule: scrapy.contrib.spidermanagertoscrapy.spidermanager
• Spider Manager singleton moved from scrapy.spider.spiders to the spiders(cid:96) attribute of
(cid:96)(cid:96)scrapy.project.crawlersingleton.
• movedStatsCollectorclasses: (#204)
– scrapy.stats.collector.StatsCollectortoscrapy.statscol.StatsCollector
– scrapy.stats.collector.SimpledbStatsCollector to scrapy.contrib.statscol.
SimpledbStatsCollector
• defaultper-commandsettingsarenowspecifiedinthedefault_settingsattributeofcommandobjectclass
(#201)
• changedargumentsofItempipelineprocess_item()methodfrom(spider, item)to(item,
spider)
– backwardcompatibilitykept(withdeprecationwarning)
• movedscrapy.core.signalsmoduletoscrapy.signals
– backwardcompatibilitykept(withdeprecationwarning)
• movedscrapy.core.exceptionsmoduletoscrapy.exceptions
7.1. Releasenotes 395

ScrapyDocumentation,Release2.13.3
– backwardcompatibilitykept(withdeprecationwarning)
• addedhandles_request()classmethodtoBaseSpider
• droppedscrapy.log.exc()function(usescrapy.log.err()instead)
• droppedcomponentargumentof scrapy.log.msg()function
• droppedscrapy.log.log_levelattribute
• Addedfrom_settings()classmethodstoSpiderManager,andItemPipelineManager
Changestosettings
• AddedHTTPCACHE_IGNORE_SCHEMESsettingtoignorecertainschemeson!HttpCacheMiddleware(#225)
• AddedSPIDER_QUEUE_CLASSsettingwhichdefinesthespiderqueuetouse(#220)
• AddedKEEP_ALIVEsetting(#220)
• RemovedSERVICE_QUEUEsetting(#220)
• RemovedCOMMANDS_SETTINGS_MODULEsetting(#201)
• RenamedREQUEST_HANDLERStoDOWNLOAD_HANDLERSandmakedownloadhandlersclasses(insteadoffunc-
tions)
7.1.96 Scrapy 0.9
Thenumberslike#NNNreferenceticketsintheoldissuetracker(Trac)whichisnolongeravailable.
Newfeaturesandimprovements
• AddedSMTP-AUTHsupporttoscrapy.mail
• Newsettingsadded: MAIL_USER,MAIL_PASS(r2065|#149)
• Addednewscrapy-ctlviewcommand-ToviewURLinthebrowser,asseenbyScrapy(r2039)
• AddedwebserviceforcontrollingScrapyprocess(thisalsodeprecatesthewebconsole. (r2053|#167)
• SupportforrunningScrapyasaservice,forproductionsystems(r1988,r2054,r2055,r2056,r2057|#168)
• Addedwrapperinductionlibrary(documentationonlyavailableinsourcecodefornow). (r2011)
• Simplifiedandimprovedresponseencodingsupport(r1961,r1969)
• AddedLOG_ENCODINGsetting(r1956,documentationavailable)
• AddedRANDOMIZE_DOWNLOAD_DELAYsetting(enabledbydefault)(r1923,docavailable)
• MailSenderisnolongerIO-blocking(r1955|#146)
• LinkextractorsandnewCrawlspidernowhandlerelativebasetagurls(r1960|#148)
• SeveralimprovementstoItemLoadersandprocessors(r2022,r2023,r2024,r2025,r2026,r2027,r2028,r2029,
r2030)
• Addedsupportforaddingvariablestotelnetconsole(r2047|#165)
• Supportforrequestswithoutcallbacks(r2050|#166)
396 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
APIchanges
• ChangeSpider.domain_nametoSpider.name(SEP-012,r1975)
• Response.encodingisnowthedetectedencoding(r1961)
• HttpErrorMiddlewarenowreturnsNoneorraisesanexception(r2006|#157)
• scrapy.commandmodulesrelocation(r2035,r2036,r2037)
• AddedExecutionQueueforfeedingspiderstoscrape(r2034)
• RemovedExecutionEnginesingleton(r2039)
• PortedS3ImagesStore(imagespipeline)tousebotoandthreads(r2033)
• Movedmodule: scrapy.management.telnettoscrapy.telnet(r2047)
Changestodefaultsettings
• ChangeddefaultSCHEDULER_ORDERtoDFO(r1939)
7.1.97 Scrapy 0.8
Thenumberslike#NNNreferenceticketsintheoldissuetracker(Trac)whichisnolongeravailable.
Newfeatures
• AddedDEFAULT_RESPONSE_ENCODINGsetting(r1809)
• Addeddont_clickargumenttoFormRequest.from_response()method(r1813,r1816)
• AddedclickdataargumenttoFormRequest.from_response()method(r1802,r1803)
• AddedsupportforHTTPproxies(HttpProxyMiddleware)(r1781,r1785)
• Offsitespidermiddlewarenowlogsmessageswhenfilteringoutrequests(r1841)
Backward-incompatiblechanges
• Changedscrapy.utils.response.get_meta_refresh()signature(r1804)
• Removeddeprecatedscrapy.item.ScrapedItemclass-usescrapy.item.Item instead(r1838)
• Removeddeprecatedscrapy.xpathmodule-usescrapy.selectorinstead. (r1836)
• Removed deprecated core.signals.domain_open signal - use core.signals.domain_opened instead
(r1822)
• log.msg()nowreceivesaspiderargument(r1822)
– Old domain argument has been deprecated and will be removed in 0.9. For spiders, you should
alwaysusethespiderargumentandpassspiderreferences. Ifyoureallywanttopassastring,use
thecomponentargumentinstead.
• Changedcoresignalsdomain_opened,domain_closed,domain_idle
• ChangedItempipelinetousespidersinsteadofdomains
– Thedomainargumentof process_item()itempipelinemethodwaschangedtospider,thenew
signatureis: process_item(spider, item)(r1827|#105)
– To quickly port your code (to work with Scrapy 0.8) just use spider.domain_name where you
previouslyuseddomain.
• ChangedStatsAPItousespidersinsteadofdomains(r1849|#113)
7.1. Releasenotes 397

ScrapyDocumentation,Release2.13.3
– StatsCollector was changed to receive spider references (instead of domains) in its methods
(set_value,inc_value,etc).
– addedStatsCollector.iter_spider_stats()method
– removedStatsCollector.list_domains()method
– Also,Statssignalswererenamedandnowpassaroundspiderreferences(insteadofdomains). Here’s
asummaryofthechanges:
– To quickly port your code (to work with Scrapy 0.8) just use spider.domain_name where you
previouslyuseddomain. spider_statscontainsexactlythesamedataasdomain_stats.
• CloseDomainextensionmovedtoscrapy.contrib.closespider.CloseSpider(r1833)
– Itssettingswerealsorenamed:
∗ CLOSEDOMAIN_TIMEOUTtoCLOSESPIDER_TIMEOUT
∗ CLOSEDOMAIN_ITEMCOUNTtoCLOSESPIDER_ITEMCOUNT
• Removed deprecated SCRAPYSETTINGS_MODULE environment variable - use SCRAPY_SETTINGS_MODULE in-
stead(r1840)
• Renamedsetting: REQUESTS_PER_DOMAINtoCONCURRENT_REQUESTS_PER_SPIDER(r1830,r1844)
• Renamedsetting: CONCURRENT_DOMAINStoCONCURRENT_SPIDERS(r1830)
• RefactoredHTTPCachemiddleware
• HTTP Cache middleware has been heavily refactored, retaining the same functionality except for the domain
sectorizationwhichwasremoved. (r1843)
• Renamedexception: DontCloseDomaintoDontCloseSpider(r1859|#120)
• Renamedextension: DelayedCloseDomaintoSpiderCloseDelay(r1861|#121)
• Removedobsoletescrapy.utils.markup.remove_escape_charsfunction-usescrapy.utils.markup.
replace_escape_charsinstead(r1865)
7.1.98 Scrapy 0.7
FirstreleaseofScrapy.
7.2 Contributing to Scrapy
s Important
Doublecheckthatyouarereadingthemostrecentversionofthisdocumentathttps://docs.scrapy.org/en/master/
contributing.html
ByparticipatinginthisprojectyouagreetoabidebythetermsofourCodeofConduct. Pleasereportunacceptable
behaviortoopensource@zyte.com.
TherearemanywaystocontributetoScrapy. Herearesomeofthem:
• Reportbugsandrequestfeaturesintheissuetracker,tryingtofollowtheguidelinesdetailedinReportingbugs
below.
• Submit patches for new functionalities and/or bug fixes. Please read Writing patches and Submitting patches
belowfordetailsonhowtowriteandsubmitapatch.
398 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
• BlogaboutScrapy. Telltheworldhowyou’reusingScrapy. Thiswillhelpnewcomerswithmoreexamplesand
willhelptheScrapyprojecttoincreaseitsvisibility.
• JointheScrapysubredditandshareyourideasonhowtoimproveScrapy. We’realwaysopentosuggestions.
• AnswerScrapyquestionsatStackOverflow.
7.2.1 Reporting bugs
(cid:242) Note
Pleasereportsecurityissuesonlytoscrapy-security@googlegroups.com. Thisisaprivatelistonlyopentotrusted
Scrapydevelopers,anditsarchivesarenotpublic.
Well-writtenbugreportsareveryhelpful,sokeepinmindthefollowingguidelineswhenyou’regoingtoreportanew
bug.
• checktheFAQfirsttoseeifyourissueisaddressedinawell-knownquestion
• ifyouhaveageneralquestionaboutScrapyusage,pleaseaskitatStackOverflow(use“scrapy”tag).
• checktheopenissuestoseeiftheissuehasalreadybeenreported. Ifithas,don’tdismissthereport,butcheck
thetickethistoryandcomments. Ifyouhaveadditionalusefulinformation,pleaseleaveacomment,orconsider
sendingapullrequestwithafix.
• searchthescrapy-userslistandScrapysubreddittoseeifithasbeendiscussedthere,orifyou’renotsureifwhat
you’reseeingisabug. Youcanalsoaskinthe#scrapyIRCchannel.
• writecomplete,reproducible,specificbugreports. Thesmallerthetestcase,thebetter. Rememberthatother
developerswon’thaveyourprojecttoreproducethebug,sopleaseincludeallrelevantfilesrequiredtoreproduce
it. SeeforexampleStackOverflow’sguideoncreatingaMinimal,Complete,andVerifiableexampleexhibiting
theissue.
• themostawesomewaytoprovideacompletereproducibleexampleistosendapullrequestwhichaddsafailing
testcasetotheScrapytestingsuite(seeSubmittingpatches). Thisishelpfulevenifyoudon’thaveanintention
tofixtheissueyourselves.
• includetheoutputof scrapy version -vsodevelopersworkingonyourbugknowexactlywhichversionand
platformitoccurredon,whichisoftenveryhelpfulforreproducingit,orknowingifitwasalreadyfixed.
7.2.2 Finding work
IfyouhavedecidedtomakeacontributiontoScrapy,butyoudonotknowwhattocontribute,youhaveafewoptions
tofindpendingwork:
• CheckoutthecontributionGitHubpage,whichlistsopenissuestaggedasgoodfirstissue.
TherearealsohelpwantedissuesbutmindthatsomemayrequirefamiliaritywiththeScrapycodebase. You
canalsotargetanyotherissueprovideditisnottaggedasdiscuss.
• If you enjoy writing documentation, there are documentation issues as well, but mind that some may require
familiaritywiththeScrapycodebaseaswell.
• Ifyouenjoywritingautomatedtests,youcanworkonincreasingourtestcoverage.
• Ifyouenjoycodecleanup,wewelcomefixesforissuesdetectedbyourstaticanalysistools. Seepyproject.
tomlforsilencedissuesthatmayneedaddressing.
Mindthatsomeissueswedonotaimtoaddressatall,andusuallyincludeacommentonthemexplainingthe
reason;nottoconfusewithcommentsthatstatewhattheissueisabout,fornon-descriptiveissuecodes.
7.2. ContributingtoScrapy 399

ScrapyDocumentation,Release2.13.3
Ifyouhavefoundanissue,makesureyoureadtheentireissuethreadbeforeyouaskquestions. Thatincludesrelated
issuesandpullrequeststhatshowupintheissuethreadwhentheissueismentionedelsewhere.
Wedonotassignissues,andyoudonotneedtoannouncethatyouaregoingtostartworkingonanissueeither. Ifyou
wanttoworkonanissue,justgoaheadandwriteapatchforit.
Donotdiscardanissuesimplybecausethereisanopenpullrequestforit. Checkifopenpullrequestsareactivefirst.
Andevenifsomeareactive,ifyouthinkyoucanbuildabetterimplementation,feelfreetocreateapullrequestwith
yourapproach.
Ifyoudecidetoworkonsomethingwithoutanopenissue,please:
• Donotcreateanissuetoworkoncodecoverageorcodecleanup,createapullrequestdirectly.
• Donotcreatebothanissueandapullrequestrightaway. Eitheropenanissuefirsttogetfeedbackonwhether
ornottheissueisworthaddressing,andcreateapullrequestlateronlyifthefeedbackfromtheteamispositive,
orcreateonlyapullrequest,ifyouthinkadiscussionwillbeeasieroveryourcode.
• Do not add docstrings for the sake of adding docstrings, or only to address silenced Ruff issues. We expect
docstringstoexistonlywhentheyaddsomethingsignificanttoreaders,suchasexplainingsomethingthatisnot
easier to understand from reading the corresponding code, summarizing a long, hard-to-read implementation,
providingcontextaboutcallingcode,orindicatingpurposelyuncaughtexceptionsfromcalledcode.
• Donotaddteststhatuseasmuchmockingaspossiblejusttotouchagivenlineofcodeandhenceimproveline
coverage. Whilewedoaimtomaximizetestcoverage,testsshouldbewrittenforrealscenarios,withminimum
mocking. Weusuallypreferend-to-endtests.
7.2.3 Writing patches
Thebetterapatchiswritten,thehigherthechancesthatit’llgetacceptedandthesooneritwillbemerged.
Well-writtenpatchesshould:
• containtheminimumamountofcoderequiredforthespecificchange. Smallpatchesareeasiertoreviewand
merge. So,ifyou’redoingmorethanonechange(orbugfix),pleaseconsidersubmittingonepatchperchange.
Donotcollapsemultiplechangesintoasinglepatch. Forbigchangesconsiderusingapatchqueue.
• passallunit-tests. SeeRunningtestsbelow.
• includeone(ormore)testcasesthatcheckthebugfixedorthenewfunctionalityadded. SeeWritingtestsbelow.
• ifyou’readdingorchangingapublic(documented)API,pleaseincludethedocumentationchangesinthesame
patch. SeeDocumentationpoliciesbelow.
• ifyou’readdingaprivateAPI,pleaseaddaregularexpressiontothecoverage_ignore_pyobjectsvariable
of docs/conf.pytoexcludethenewprivateAPIfromdocumentationcoveragechecks.
ToseeifyourprivateAPIisskippedproperly,generateadocumentationcoveragereportasfollows:
tox -e docs-coverage
• ifyouareremovingdeprecatedcode,firstmakesurethatatleast1year(12months)haspassedsincetherelease
thatintroducedthedeprecation. SeeDeprecationpolicy.
7.2.4 Submitting patches
ThebestwaytosubmitapatchistoissueapullrequestonGitHub,optionallycreatinganewissuefirst.
Remember to explain what was fixed or the new functionality (what it is, why it’s needed, etc). The more info you
include,theeasierwillbeforcoredeveloperstounderstandandacceptyourpatch.
Ifyourpullrequestaimstoresolveanopenissue,linkitaccordingly,e.g.:
400 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Resolves #123
Youcanalsodiscussthenewfunctionality(orbugfix)beforecreatingthepatch,butit’salwaysgoodtohaveapatch
readytoillustrateyourargumentsandshowthatyouhaveputsomeadditionalthoughtintothesubject. Agoodstarting
pointistosendapullrequestonGitHub. Itcanbesimpleenoughtoillustrateyouridea,andleavedocumentation/tests
forlater,aftertheideahasbeenvalidatedandprovenuseful. Alternatively,youcanstartaconversationintheScrapy
subreddittodiscussyourideafirst.
Sometimesthereisanexistingpullrequestfortheproblemyou’dliketosolve,whichisstalledforsomereason. Often
thepullrequestisinarightdirection,butchangesarerequestedbyScrapymaintainers,andtheoriginalpullrequest
authorhasn’thadtimetoaddressthem. Inthiscaseconsiderpickingupthispullrequest: openanewpullrequestwith
allcommitsfromtheoriginalpullrequest,aswellasadditionalchangestoaddresstheraisedissues. Doingsohelpsa
lot;itisnotconsideredrudeaslongastheoriginalauthorisacknowledgedbykeepinghis/hercommits.
You can pull an existing pull request to a local branch by running git fetch upstream pull/$PR_NUMBER/
head:$BRANCH_NAME_TO_CREATE(replace‘upstream’witharemotenameforscrapyrepository,$PR_NUMBERwith
anIDofthepullrequest,and$BRANCH_NAME_TO_CREATEwithanameofthebranchyouwanttocreatelocally). See
also: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/
checking-out-pull-requests-locally#modifying-an-inactive-pull-request-locally.
WhenwritingGitHubpullrequests, trytokeeptitlesshortbutdescriptive. E.g. Forbug#411: “Scrapyhangsifan
exceptionraisesinstart_requests”prefer“Fixhangingwhenexceptionoccursinstart_requests(#411)”insteadof“Fix
for#411”. Completetitlesmakeiteasytoskimthroughtheissuetracker.
Finally, try to keep aesthetic changes (PEP 8 compliance, unused imports removal, etc) in separate commits from
functionalchanges. Thiswillmakepullrequestseasiertoreviewandmorelikelytogetmerged.
7.2.5 Coding style
PleasefollowthesecodingconventionswhenwritingcodeforinclusioninScrapy:
• WeuseRuffforcodeformatting. Thereisahookinthepre-commitconfigthatwillautomaticallyformatyour
codebeforeeverycommit. YoucanalsorunRuffmanuallywithtox -e pre-commit.
• Don’tputyournameinthecodeyoucontribute;gitprovidesenoughmetadatatoidentifyauthorofthecode. See
https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git for setup instruc-
tions.
7.2.6 Pre-commit
Weusepre-committoautomaticallyaddresssimplecodeissuesbeforeeverycommit.
AfteryourcreatealocalcloneofyourforkoftheScrapyrepository:
1. Installpre-commit.
2. OntherootofyourlocalcloneoftheScrapyrepository,runthefollowingcommand:
pre-commit install
Nowpre-commitwillcheckyourchangeseverytimeyoucreateaGitcommit. Uponfindingissues,pre-commitaborts
your commit, and either fixes those issues automatically, or only reports them to you. If it fixes those issues auto-
matically,creatingyourcommitagainshouldsucceed. Otherwise,youmayneedtoaddressthecorrespondingissues
manuallyfirst.
7.2. ContributingtoScrapy 401

ScrapyDocumentation,Release2.13.3
7.2.7 Documentation policies
ForreferencedocumentationofAPImembers(classes, methods, etc.) usedocstringsandmakesurethattheSphinx
documentationusestheautodocextensiontopullthedocstrings. APIreferencedocumentationshouldfollowdocstring
conventions(PEP257)andbeIDE-friendly: short,tothepoint,anditmayprovideshortexamples.
Othertypesofdocumentation,suchastutorialsortopics,shouldbecoveredinfileswithinthedocs/directory. This
includesdocumentationthatisspecifictoanAPImember,butgoesbeyondAPIreferencedocumentation.
Inanycase,ifsomethingiscoveredinadocstring,usetheautodocextensiontopullthedocstringintothedocumen-
tationinsteadofduplicatingthedocstringinfileswithinthedocs/directory.
DocumentationupdatesthatcovernewormodifiedfeaturesmustuseSphinx’sversionaddedandversionchanged
directives. UseVERSIONasversion,wewillreplaceitwiththeactualversionrightbeforethecorrespondingrelease.
WhenwereleaseanewmajororminorversionofScrapy,weremovethesedirectivesiftheyareolderthan3years.
Documentationaboutdeprecatedfeaturesmustberemovedasthosefeaturesaredeprecated,sothatnewreadersdonot
runintoit. Newdeprecationsanddeprecationremovalsaredocumentedinthereleasenotes.
7.2.8 Tests
TestsareimplementedusingtheTwistedunit-testingframework. Runningtestsrequirestox.
Runningtests
Torunalltests:
tox
Torunaspecifictest(saytests/test_loader.py)use:
tox -- tests/test_loader.py
Torunthetestsonaspecifictoxenvironment,use-e <name>withanenvironmentnamefromtox.ini. Forexample,
torunthetestswithPython3.10use:
tox -e py310
Youcanalsospecifyacomma-separatedlistofenvironments,andusetox’sparallelmodetorunthetestsonmultiple
environmentsinparallel:
tox -e py39,py310 -p auto
Topasscommand-lineoptionstopytest,addthemafter--inyourcalltotox. Using--overridesthedefaultpositional
argumentsdefinedintox.ini,soyoumustincludethosedefaultpositionalarguments(scrapy tests)after --as
well:
tox -- scrapy tests -x # stop after first failure
You can also use the pytest-xdist plugin. For example, to run all tests on the Python 3.10 tox environment using all
yourCPUcores:
tox -e py310 -- scrapy tests -n auto
Toseecoveragereportinstallcoverage(pip install coverage)andrun:
coverage report
seeoutputof coverage --helpformoreoptionslikehtmlorxmlreport.
402 Chapter7. Alltherest

ScrapyDocumentation,Release2.13.3
Writingtests
Allfunctionality(includingnewfeaturesandbugfixes)mustincludeatestcasetocheckthatitworksasexpected,so
pleaseincludetestsforyourpatchesifyouwantthemtogetacceptedsooner.
Scrapyusesunit-tests,whicharelocatedinthetests/directory. Theirmodulenametypicallyresemblesthefullpathof
themodulethey’retesting. Forexample,theitemloaderscodeisin:
scrapy.loader
Andtheirunit-testsarein:
tests/test_loader.py
7.3 Versioning and API stability
7.3.1 Versioning
Thereare3numbersinaScrapyversion: A.B.C
• Aisthemajorversion. Thiswillrarelychangeandwillsignifyverylargechanges.
• Bisthereleasenumber. Thiswillincludemanychangesincludingfeaturesandthingsthatpossiblybreakback-
wardcompatibility,althoughwestrivetokeepthesecasesataminimum.
• Cisthebugfixreleasenumber.
Backward-incompatibilities are explicitly mentioned in the release notes, and may require special attention before
upgrading.
Developmentreleasesdonotfollow3-numbersversionandaregenerallyreleasedasdevsuffixedversions,e.g. 1.3dev.
(cid:242) Note
WithScrapy0.*series,Scrapyusedodd-numberedversionsfordevelopmentreleases. Thisisnotthecaseanymore
fromScrapy1.0onwards.
StartingwithScrapy1.0,allreleasesshouldbeconsideredproduction-ready.
Forexample:
• 1.1.1isthefirstbugfixreleaseofthe1.1series(safetouseinproduction)
7.3.2 API stability
APIstabilitywasoneofthemajorgoalsforthe1.0release.
Methodsorfunctionsthatstartwithasingledash(_)areprivateandshouldneverbereliedasstable.
Also,keepinmindthatstabledoesn’tmeancomplete: stableAPIscouldgrownewmethodsorfunctionalitybutthe
existingmethodsshouldkeepworkingthesameway.
7.3.3 Deprecation policy
WeaimtomaintainsupportfordeprecatedScrapyfeaturesforatleast1year.
Forexample,ifafeatureisdeprecatedinaScrapyversionreleasedonJune15th2020,thatfeatureshouldcontinueto
workinversionsreleasedonJune14th2021orbeforethat.
7.3. VersioningandAPIstability 403

ScrapyDocumentation,Release2.13.3
AnynewScrapyreleaseafterayearmayremovesupportforthatdeprecatedfeature.
AlldeprecatedfeaturesremovedinaScrapyreleaseareexplicitlymentionedinthereleasenotes.
Releasenotes
SeewhathaschangedinrecentScrapyversions.
ContributingtoScrapy
LearnhowtocontributetotheScrapyproject.
VersioningandAPIstability
UnderstandScrapyversioningandAPIstability.
404 Chapter7. Alltherest

PYTHON MODULE INDEX
s scrapy.pipelines.files,212
scrapy.contracts,184 scrapy.pipelines.images,214
scrapy.contracts.default,184 scrapy.robotstxt,253
scrapy.core.scheduler,275 scrapy.selector,61
scrapy.crawler,287 scrapy.settings,291
scrapy.downloadermiddlewares,239 scrapy.signalmanager,296
scrapy.downloadermiddlewares.cookies,240 scrapy.signals,269
scrapy.downloadermiddlewares.defaultheaders, scrapy.spiderloader,295
242 scrapy.spidermiddlewares,254
scrapy.downloadermiddlewares.downloadtimeout, scrapy.spidermiddlewares.base,256
242 scrapy.spidermiddlewares.depth,257
scrapy.downloadermiddlewares.httpauth,242 scrapy.spidermiddlewares.httperror,257
scrapy.downloadermiddlewares.httpcache,243 scrapy.spidermiddlewares.referer,258
scrapy.downloadermiddlewares.httpcompression, scrapy.spidermiddlewares.start,261
247 scrapy.spidermiddlewares.urllength,261
scrapy.downloadermiddlewares.httpproxy,247 scrapy.statscollectors,297
scrapy.downloadermiddlewares.offsite,248 scrapy.utils.log,166
scrapy.downloadermiddlewares.redirect,248 scrapy.utils.trackref,204
scrapy.downloadermiddlewares.retry,250
scrapy.downloadermiddlewares.robotstxt,252
scrapy.downloadermiddlewares.stats,253
scrapy.downloadermiddlewares.useragent,254
scrapy.exceptions,157
scrapy.exporters,278
scrapy.extensions.closespider,264
scrapy.extensions.corestats,263
scrapy.extensions.debug,265
scrapy.extensions.httpcache,244
scrapy.extensions.logstats,263
scrapy.extensions.memdebug,263
scrapy.extensions.memusage,263
scrapy.extensions.periodic_log,265
scrapy.extensions.spiderstate,264
scrapy.extensions.statsmailer,265
scrapy.extensions.telnet,263
scrapy.http,101
scrapy.item,65
scrapy.link,124
scrapy.linkextractors,122
scrapy.linkextractors.lxmlhtml,123
scrapy.loader,70
scrapy.mail,168
405

ScrapyDocumentation,Release2.13.3
406 PythonModuleIndex

INDEX
Symbols setting,218
__bool__()(scrapy.Selectormethod),63 AUTOTHROTTLE_START_DELAY
__init__(),95
setting,218
__init__() (scrapy.core.scheduler.Scheduler method), AUTOTHROTTLE_TARGET_CONCURRENCY
277
setting,218
__len__() (scrapy.core.scheduler.Scheduler method), AWS_ACCESS_KEY_ID
277
setting,129
AWS_ENDPOINT_URL
A setting,130
accepts() (scrapy.extensions.feedexport.ItemFilter AWS_REGION_NAME
method),94
setting,130
adapt_response() (scrapy.spiders.XMLFeedSpider AWS_SECRET_ACCESS_KEY
method),41
setting,129
add_css()(scrapy.loader.ItemLoadermethod),75 AWS_SESSION_TOKEN
add_jmes()(scrapy.loader.ItemLoadermethod),76
setting,130
add_to_list() (scrapy.settings.BaseSettings method), AWS_USE_SSL
292
setting,130
add_value()(scrapy.loader.ItemLoadermethod),76 AWS_VERIFY
add_xpath()(scrapy.loader.ItemLoadermethod),77
setting,130
ADDONS
B
setting,129
adjust_request_args() (scrapy.contracts.Contract BaseDupeFilter(classinscrapy.dupefilters),139
method),185 BaseItemExporter(classinscrapy.exporters),280
allow_offsite
BaseScheduler(classinscrapy.core.scheduler),275
reqmeta,248 BaseSettings(classinscrapy.settings),291
allowed()(scrapy.robotstxt.RobotParsermethod),253 BaseSpiderMiddleware (class in
allowed_domains(scrapy.Spiderattribute),33 scrapy.spidermiddlewares.base),256
ASYNCIO_EVENT_LOOP bench
setting,130 command,31
attrib(scrapy.Selectorattribute),62 bindaddress
attrib(scrapy.selector.SelectorListattribute),64 reqmeta,112
attributes(scrapy.http.JsonRequestattribute),116 body(scrapy.http.Responseattribute),117
attributes(scrapy.http.Responseattribute),119 body(scrapy.Requestattribute),103
attributes(scrapy.http.TextResponseattribute),120 BOT_NAME
attributes(scrapy.Requestattribute),105 setting,130
AUTOTHROTTLE_DEBUG build_from_crawler() (in module scrapy.utils.misc),
setting,218 287
autothrottle_dont_adjust_delay bytes_received
reqmeta,217 signal,274
AUTOTHROTTLE_ENABLED
bytes_received()(inmodulescrapy.signals),274
setting,218 Bz2Plugin (class in scrapy.extensions.postprocessing),
95
AUTOTHROTTLE_MAX_DELAY
407

ScrapyDocumentation,Release2.13.3
C setting,32
CacheStorage (class in scrapy.extensions.httpcache), COMPRESSION_ENABLED
244
setting,247
callback(scrapy.Requestattribute),103 CONCURRENT_ITEMS
CallbackKeywordArgumentsContract (class in
setting,131
scrapy.contracts.default),184 CONCURRENT_REQUESTS
cb_kwargs(scrapy.http.Responseattribute),118
setting,131
cb_kwargs(scrapy.Requestattribute),104 CONCURRENT_REQUESTS_PER_DOMAIN
certificate(scrapy.http.Responseattribute),118
setting,131
CONCURRENT_REQUESTS_PER_IP
check
command,27
setting,131
clear_stats() (scrapy.statscollectors.StatsCollector
configure_logging()(inmodulescrapy.utils.log),166
method),297 connect() (scrapy.signalmanager.SignalManager
method),296
close(),95
close() (scrapy.core.scheduler.BaseScheduler method),
context(scrapy.loader.ItemLoaderattribute),75
275
Contract(classinscrapy.contracts),184
close()(scrapy.core.scheduler.Schedulermethod),278
ContractFail(classinscrapy.exceptions),185
close_spider(),86 cookiejar
close_spider()(scrapy.extensions.httpcache.CacheStorage
reqmeta,241
method),245 COOKIES_DEBUG
close_spider() (scrapy.statscollectors.StatsCollector
setting,241
method),297 COOKIES_ENABLED
closed()(scrapy.Spidermethod),35
setting,241
CloseSpider,157 CookiesMiddleware (class in
scrapy.downloadermiddlewares.cookies),
CloseSpider (class in scrapy.extensions.closespider),
240
264
copy()(scrapy.http.Responsemethod),119
CLOSESPIDER_ERRORCOUNT
setting,265
copy()(scrapy.Itemmethod),65
copy()(scrapy.Requestmethod),105
CLOSESPIDER_ITEMCOUNT
setting,265
copy()(scrapy.settings.BaseSettingsmethod),292
copy_to_dict()(scrapy.settings.BaseSettingsmethod),
CLOSESPIDER_PAGECOUNT
292
setting,265
CoreStats(classinscrapy.extensions.corestats),263
CLOSESPIDER_PAGECOUNT_NO_ITEM
setting,265 crawl
command,27
CLOSESPIDER_TIMEOUT
setting,264
crawl()(scrapy.crawler.Crawlermethod),288
crawl()(scrapy.crawler.CrawlerProcessmethod),290
CLOSESPIDER_TIMEOUT_NO_ITEM
setting,264
crawl()(scrapy.crawler.CrawlerRunnermethod),289
crawled() (scrapy.logformatter.LogFormatter method),
command
164
bench,31
check,27
Crawler(classinscrapy.crawler),287
crawl,27
crawler(scrapy.Spiderattribute),33
edit,28
CrawlerProcess(classinscrapy.crawler),290
fetch,28
CrawlerRunner(classinscrapy.crawler),289
genspider,26 crawlers (scrapy.crawler.CrawlerProcess property),
290
list,28
parse,30
crawlers(scrapy.crawler.CrawlerRunnerproperty),289
runspider,31
CrawlSpider(classinscrapy.spiders),38
settings,31 create_crawler() (scrapy.crawler.CrawlerProcess
method),290
shell,29
startproject,26 create_crawler() (scrapy.crawler.CrawlerRunner
method),289
version,31
view,29
css()(scrapy.http.TextResponsemethod),121
css()(scrapy.Selectormethod),61
COMMANDS_MODULE
408 Index

ScrapyDocumentation,Release2.13.3
css()(scrapy.selector.SelectorListmethod),63 setting,133
CSVFeedSpider(classinscrapy.spiders),42 DNSCACHE_ENABLED
CsvItemExporter(classinscrapy.exporters),282 setting,133
csviter()(inmodulescrapy.utils.iterators),178 DNSCACHE_SIZE
curl_to_request_kwargs() (in module setting,133
scrapy.utils.curl),199 dont_cache
custom_settings(scrapy.Spiderattribute),33 reqmeta,243
dont_filter(scrapy.Requestattribute),105
D
dont_merge_cookies
DbmCacheStorage (class in reqmeta,102
scrapy.extensions.httpcache),244 dont_obey_robotstxt
Debugger(classinscrapy.extensions.periodic_log),268 reqmeta,252
deepcopy()(scrapy.Itemmethod),65 dont_redirect
DEFAULT_DROPITEM_LOG_LEVEL
reqmeta,248
setting,131 dont_retry
default_input_processor(scrapy.loader.ItemLoader reqmeta,250
attribute),75 DontCloseSpider,157
DEFAULT_ITEM_CLASS DOWNLOAD_DELAY
setting,132 setting,135
default_item_class (scrapy.loader.ItemLoader download_error() (scrapy.logformatter.LogFormatter
attribute),75 method),165
default_output_processor DOWNLOAD_FAIL_ON_DATALOSS
(scrapy.loader.ItemLoaderattribute),75 setting,138
DEFAULT_REQUEST_HEADERS download_fail_on_dataloss
setting,132 reqmeta,113
default_selector_class (scrapy.loader.ItemLoader DOWNLOAD_HANDLERS
attribute),75 setting,136
DefaultHeadersMiddleware (class in DOWNLOAD_HANDLERS_BASE
scrapy.downloadermiddlewares.defaultheaders), setting,136
242 download_latency
DefaultReferrerPolicy (class in reqmeta,113
scrapy.spidermiddlewares.referer),259 DOWNLOAD_MAXSIZE
deferred_f_from_coro_f() (in module setting,137
scrapy.utils.defer),229 download_maxsize
deferred_from_coro() (in module scrapy.utils.defer), reqmeta,137
229 DOWNLOAD_SLOTS
deferred_to_future() (in module scrapy.utils.defer), setting,137
228 DOWNLOAD_TIMEOUT
delimiter(scrapy.spiders.CSVFeedSpiderattribute),42 setting,137
DEPTH_LIMIT download_timeout
setting,132 reqmeta,112
DEPTH_PRIORITY DOWNLOAD_WARNSIZE
setting,132 setting,138
DEPTH_STATS_VERBOSE download_warnsize
setting,132 reqmeta,138
DepthMiddleware (class in DOWNLOADER
scrapy.spidermiddlewares.depth),257 setting,133
disconnect() (scrapy.signalmanager.SignalManager DOWNLOADER_CLIENT_TLS_CIPHERS
method),296 setting,134
disconnect_all()(scrapy.signalmanager.SignalManagerDOWNLOADER_CLIENT_TLS_METHOD
method),296 setting,134
DNS_RESOLVER DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING
setting,133 setting,134
DNS_TIMEOUT DOWNLOADER_CLIENTCONTEXTFACTORY
Index 409

ScrapyDocumentation,Release2.13.3
setting,133 setting,140
DOWNLOADER_HTTPCLIENTFACTORY extensions(scrapy.crawler.Crawlerattribute),288
setting,133 EXTENSIONS_BASE
DOWNLOADER_MIDDLEWARES setting,140
setting,134 extract_links()(scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor
DOWNLOADER_MIDDLEWARES_BASE method),124
setting,135
F
DOWNLOADER_STATS
setting,135
FEED_EXPORT_BATCH_ITEM_COUNT
DownloaderMiddleware (class in setting,99
scrapy.downloadermiddlewares),239
FEED_EXPORT_ENCODING
DownloaderStats (class in setting,98
scrapy.downloadermiddlewares.stats),253
FEED_EXPORT_FIELDS
DownloadTimeoutMiddleware (class in setting,98
scrapy.downloadermiddlewares.downloadtimeout),
FEED_EXPORT_INDENT
242 setting,98
DropItem,157
feed_exporter_closed
dropped() (scrapy.logformatter.LogFormatter method), signal,272
165 feed_exporter_closed() (in module scrapy.signals),
DummyPolicy(classinscrapy.extensions.httpcache),243 272
DummyStatsCollector(classinscrapy.statscollectors),
FEED_EXPORTERS
168 setting,99
DUPEFILTER_CLASS FEED_EXPORTERS_BASE
setting,138 setting,99
DUPEFILTER_DEBUG feed_slot_closed
setting,140 signal,272
feed_slot_closed()(inmodulescrapy.signals),272
E
FEED_STORAGE_FTP_ACTIVE
edit setting,98
command,28 FEED_STORAGE_GCS_ACL
EDITOR setting,140
setting,140 FEED_STORAGE_S3_ACL
encoding (scrapy.exporters.BaseItemExporter at- setting,98
tribute),281 FEED_STORAGES
encoding(scrapy.http.TextResponseattribute),120 setting,98
engine(scrapy.crawler.Crawlerattribute),288 FEED_STORAGES_BASE
engine_started setting,99
signal,269 FEED_STORE_EMPTY
engine_started()(inmodulescrapy.signals),269 setting,98
engine_stopped FEED_TEMPDIR
signal,270 setting,140
engine_stopped()(inmodulescrapy.signals),270 FEED_URI_PARAMS
enqueue_request()(scrapy.core.scheduler.BaseScheduler setting,100
method),275 FEEDS
enqueue_request() (scrapy.core.scheduler.Scheduler setting,96
method),278 fetch
errback(scrapy.Requestattribute),104 command,28
ExecutionEngine(classinscrapy.core.engine),297 Field(classinscrapy),67
export_empty_fields fields(scrapy.Itemattribute),65
(scrapy.exporters.BaseItemExporter attribute), fields_to_export(scrapy.exporters.BaseItemExporter
281 attribute),281
export_item() (scrapy.exporters.BaseItemExporter file_path() (scrapy.pipelines.files.FilesPipeline
method),280 method),212
EXTENSIONS
410 Index

ScrapyDocumentation,Release2.13.3
file_path() (scrapy.pipelines.images.ImagesPipeline G
method),214
GCS_PROJECT_ID
FILES_EXPIRES setting,141
setting,210
genspider
FILES_RESULT_FIELD command,26
setting,210
get()(scrapy.Selectormethod),62
FILES_STORE get()(scrapy.selector.SelectorListmethod),63
setting,207
get()(scrapy.settings.BaseSettingsmethod),292
FILES_STORE_GCS_ACL get_addon()(scrapy.crawler.Crawlermethod),288
setting,209
get_collected_values() (scrapy.loader.ItemLoader
FILES_STORE_S3_ACL method),77
setting,209
get_css()(scrapy.loader.ItemLoadermethod),77
FILES_URLS_FIELD
get_downloader_middleware()
setting,210
(scrapy.crawler.Crawlermethod),288
FilesPipeline(classinscrapy.pipelines.files),212
get_extension() (scrapy.crawler.Crawler method),
FilesystemCacheStorage (class in 288
scrapy.extensions.httpcache),244
get_item_pipeline() (scrapy.crawler.Crawler
find_by_request()(scrapy.spiderloader.SpiderLoader
method),289
method),296
get_jmes()(scrapy.loader.ItemLoadermethod),77
fingerprint(),109
get_media_requests()
fingerprint()(inmodulescrapy.utils.request),109
(scrapy.pipelines.files.FilesPipeline method),
finish_exporting()(scrapy.exporters.BaseItemExporter
212
method),281
get_media_requests()
flags(scrapy.http.Responseattribute),118
(scrapy.pipelines.images.ImagesPipeline
follow()(scrapy.http.Responsemethod),119
method),215
follow()(scrapy.http.TextResponsemethod),121
get_oldest()(inmodulescrapy.utils.trackref),205
follow_all()(scrapy.http.Responsemethod),119
get_output_value() (scrapy.loader.ItemLoader
follow_all()(scrapy.http.TextResponsemethod),121
method),78
freeze()(scrapy.settings.BaseSettingsmethod),292
get_processed_item()
from_crawler(),285
(scrapy.spidermiddlewares.base.BaseSpiderMiddleware
from_crawler() (scrapy.core.scheduler.BaseScheduler method),256
classmethod),276
get_processed_request()
from_crawler()(scrapy.core.scheduler.Schedulerclass
(scrapy.spidermiddlewares.base.BaseSpiderMiddleware
method),278
method),256
from_crawler() (scrapy.robotstxt.RobotParser class get_retry_request() (in module
method),253
scrapy.downloadermiddlewares.retry),250
from_crawler()(scrapy.Spidermethod),33
get_settings_priority() (in module
from_curl()(scrapy.Requestclassmethod),105
scrapy.settings),291
from_response() (scrapy.FormRequest class method), get_spider_middleware() (scrapy.crawler.Crawler
114
method),289
from_settings() (scrapy.spiderloader.SpiderLoader get_stats() (scrapy.statscollectors.StatsCollector
method),295
method),297
frozencopy() (scrapy.settings.BaseSettings method), get_value()(scrapy.loader.ItemLoadermethod),78
292
get_value() (scrapy.statscollectors.StatsCollector
FTP_PASSIVE_MODE method),297
setting,141
get_xpath()(scrapy.loader.ItemLoadermethod),78
FTP_PASSWORD getall()(scrapy.Selectormethod),63
setting,141
getall()(scrapy.selector.SelectorListmethod),63
ftp_password getbool()(scrapy.settings.BaseSettingsmethod),292
reqmeta,141
getdict()(scrapy.settings.BaseSettingsmethod),292
FTP_USER getdictorlist() (scrapy.settings.BaseSettings
setting,141
method),293
ftp_user getfloat()(scrapy.settings.BaseSettingsmethod),293
reqmeta,141
getint()(scrapy.settings.BaseSettingsmethod),293
Index 411

ScrapyDocumentation,Release2.13.3
getlist()(scrapy.settings.BaseSettingsmethod),293 setting,246
getpriority() (scrapy.settings.BaseSettings method), HttpCacheMiddleware (class in
293 scrapy.downloadermiddlewares.httpcache),
getwithbase() (scrapy.settings.BaseSettings method), 243
294 HttpCompressionMiddleware (class in
global_object_name() (in module scrapy.downloadermiddlewares.httpcompression),
scrapy.utils.python),287 247
GzipPlugin(classinscrapy.extensions.postprocessing), HTTPERROR_ALLOW_ALL
94 setting,258
HTTPERROR_ALLOWED_CODES
H
setting,258
handle_httpstatus_all HttpErrorMiddleware (class in
reqmeta,257 scrapy.spidermiddlewares.httperror),257
handle_httpstatus_list HTTPPROXY_AUTH_ENCODING
reqmeta,257 setting,247
has_pending_requests() HTTPPROXY_ENABLED
(scrapy.core.scheduler.BaseSchedulermethod), setting,247
276 HttpProxyMiddleware (class in
has_pending_requests() scrapy.downloadermiddlewares.httpproxy),
(scrapy.core.scheduler.Scheduler method), 247
278
I
headers(scrapy.http.Responseattribute),117
headers(scrapy.Requestattribute),103 IgnoreRequest,157
headers(scrapy.spiders.CSVFeedSpiderattribute),42 IMAGES_EXPIRES
headers_received setting,210
signal,274 IMAGES_MIN_HEIGHT
headers_received()(inmodulescrapy.signals),274 setting,211
HtmlResponse(classinscrapy.http),122 IMAGES_MIN_WIDTH
HttpAuthMiddleware (class in setting,211
scrapy.downloadermiddlewares.httpauth), IMAGES_RESULT_FIELD
242 setting,210
HTTPCACHE_ALWAYS_STORE IMAGES_STORE
setting,246 setting,207
HTTPCACHE_DBM_MODULE IMAGES_STORE_GCS_ACL
setting,246 setting,209
HTTPCACHE_DIR IMAGES_STORE_S3_ACL
setting,245 setting,209
HTTPCACHE_ENABLED IMAGES_THUMBS
setting,245 setting,211
HTTPCACHE_EXPIRATION_SECS IMAGES_URLS_FIELD
setting,245 setting,210
HTTPCACHE_GZIP ImagesPipeline(classinscrapy.pipelines.images),214
setting,246 inc_value() (scrapy.statscollectors.StatsCollector
HTTPCACHE_IGNORE_HTTP_CODES method),297
setting,245 indent (scrapy.exporters.BaseItemExporter attribute),
HTTPCACHE_IGNORE_MISSING 281
setting,246 install_reactor() (in module scrapy.utils.reactor),
HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS 149
setting,246 ip_address(scrapy.http.Responseattribute),118
HTTPCACHE_IGNORE_SCHEMES is_asyncio_reactor_installed() (in module
setting,246 scrapy.utils.reactor),230
HTTPCACHE_POLICY is_start_request
setting,246 reqmeta,261
HTTPCACHE_STORAGE Item(classinscrapy),65
412 Index

ScrapyDocumentation,Release2.13.3
item(scrapy.loader.ItemLoaderattribute),75 LOG_ENCODING
item_completed() (scrapy.pipelines.files.FilesPipeline setting,142
method),213 LOG_FILE
item_completed()(scrapy.pipelines.images.ImagesPipeline setting,142
method),215 LOG_FILE_APPEND
item_dropped setting,142
signal,270 LOG_FORMAT
item_dropped()(inmodulescrapy.signals),270 setting,142
item_error LOG_FORMATTER
signal,271 setting,142
item_error()(inmodulescrapy.signals),271 LOG_LEVEL
item_error() (scrapy.logformatter.LogFormatter setting,142
method),165 LOG_SHORT_NAMES
ITEM_PIPELINES setting,143
setting,141 LOG_STDOUT
ITEM_PIPELINES_BASE setting,142
setting,141 LOG_VERSIONS
item_scraped setting,143
signal,270 LogFormatter(classinscrapy.logformatter),164
item_scraped()(inmodulescrapy.signals),270 logger(scrapy.Spiderattribute),33
ItemFilter(classinscrapy.extensions.feedexport),94 LogStats(classinscrapy.extensions.logstats),263
ItemLoader(classinscrapy.loader),75 LOGSTATS_INTERVAL
ItemMeta(classinscrapy.item),70 setting,143
iter_all()(inmodulescrapy.utils.trackref),205 LxmlLinkExtractor (class in
iterator(scrapy.spiders.XMLFeedSpiderattribute),41 scrapy.linkextractors.lxmlhtml),123
itertag(scrapy.spiders.XMLFeedSpiderattribute),41 LZMAPlugin(classinscrapy.extensions.postprocessing),
95
J
M
jmespath()(scrapy.http.TextResponsemethod),121
jmespath()(scrapy.Selectormethod),62 MAIL_FROM
jmespath()(scrapy.selector.SelectorListmethod),63 setting,170
JOBDIR MAIL_HOST
setting,141 setting,170
join()(scrapy.crawler.CrawlerProcessmethod),290 MAIL_PASS
join()(scrapy.crawler.CrawlerRunnermethod),289 setting,170
json()(scrapy.http.TextResponsemethod),122 MAIL_PORT
JsonItemExporter(classinscrapy.exporters),284 setting,170
JsonLinesItemExporter (class in scrapy.exporters), MAIL_SSL
284 setting,170
JsonRequest(classinscrapy.http),116 MAIL_TLS
JsonResponse(classinscrapy.http),122 setting,170
MAIL_USER
L setting,170
Link(classinscrapy.link),124
MailSender(classinscrapy.mail),169
MarshalItemExporter(classinscrapy.exporters),284
list
command,28 max_retry_times
list()(scrapy.spiderloader.SpiderLoadermethod),296
reqmeta,113
load()(scrapy.spiderloader.SpiderLoadermethod),295 max_value() (scrapy.statscollectors.StatsCollector
method),297
load_item()(scrapy.loader.ItemLoadermethod),78
log()(scrapy.Spidermethod),35 maxpriority() (scrapy.settings.BaseSettings method),
294
LOG_DATEFORMAT
setting,142 maybe_deferred_to_future() (in module
scrapy.utils.defer),228
LOG_ENABLED
setting,142 MEDIA_ALLOW_REDIRECTS
Index 413

ScrapyDocumentation,Release2.13.3
setting,212 scrapy.downloadermiddlewares.httpproxy,
MEMDEBUG_ENABLED 247
setting,143 scrapy.downloadermiddlewares.offsite,248
MEMDEBUG_NOTIFY scrapy.downloadermiddlewares.redirect,
setting,143 248
MemoryDebugger (class in scrapy.downloadermiddlewares.retry,250
scrapy.extensions.memdebug),263 scrapy.downloadermiddlewares.robotstxt,
MemoryStatsCollector (class in 252
scrapy.statscollectors),168 scrapy.downloadermiddlewares.stats,253
MemoryUsage (class in scrapy.extensions.memusage), scrapy.downloadermiddlewares.useragent,
263 254
MEMUSAGE_CHECK_INTERVAL_SECONDS scrapy.exceptions,157
setting,144 scrapy.exporters,278
MEMUSAGE_ENABLED scrapy.extensions.closespider,264
setting,143 scrapy.extensions.corestats,263
MEMUSAGE_LIMIT_MB scrapy.extensions.debug,265
setting,144 scrapy.extensions.httpcache,244
MEMUSAGE_NOTIFY_MAIL scrapy.extensions.logstats,263
setting,144 scrapy.extensions.memdebug,263
MEMUSAGE_WARNING_MB scrapy.extensions.memusage,263
setting,144 scrapy.extensions.periodic_log,265
meta(scrapy.http.Responseattribute),118 scrapy.extensions.spiderstate,264
meta(scrapy.Requestattribute),104 scrapy.extensions.statsmailer,265
MetadataContract (class in scrapy.contracts.default), scrapy.extensions.telnet,263
184 scrapy.http,101
METAREFRESH_ENABLED scrapy.item,65
setting,249 scrapy.link,124
METAREFRESH_IGNORE_TAGS scrapy.linkextractors,122
setting,249 scrapy.linkextractors.lxmlhtml,123
METAREFRESH_MAXDELAY scrapy.loader,70
setting,249 scrapy.mail,168
MetaRefreshMiddleware (class in scrapy.pipelines.files,212
scrapy.downloadermiddlewares.redirect), scrapy.pipelines.images,214
249 scrapy.robotstxt,253
method(scrapy.Requestattribute),103 scrapy.selector,61
min_value() (scrapy.statscollectors.StatsCollector scrapy.settings,291
method),297 scrapy.signalmanager,296
module scrapy.signals,269
scrapy.contracts,184 scrapy.spiderloader,295
scrapy.contracts.default,184 scrapy.spidermiddlewares,254
scrapy.core.scheduler,275 scrapy.spidermiddlewares.base,256
scrapy.crawler,287 scrapy.spidermiddlewares.depth,257
scrapy.downloadermiddlewares,239 scrapy.spidermiddlewares.httperror,257
scrapy.downloadermiddlewares.cookies,240 scrapy.spidermiddlewares.referer,258
scrapy.downloadermiddlewares.defaultheaders, scrapy.spidermiddlewares.start,261
242 scrapy.spidermiddlewares.urllength,261
scrapy.downloadermiddlewares.downloadtimeout, scrapy.statscollectors,297
242 scrapy.utils.log,166
scrapy.downloadermiddlewares.httpauth, scrapy.utils.trackref,204
242
scrapy.downloadermiddlewares.httpcache, N
243 name(scrapy.Spiderattribute),33
scrapy.downloadermiddlewares.httpcompressinoanm , espaces (scrapy.spiders.XMLFeedSpider attribute),
247 41
414 Index

ScrapyDocumentation,Release2.13.3
needs_backout()(scrapy.core.engine.ExecutionEngine PeriodicLog (class in scrapy.extensions.periodic_log),
method),297 265
nested_css()(scrapy.loader.ItemLoadermethod),78 PickleItemExporter(classinscrapy.exporters),283
nested_xpath() (scrapy.loader.ItemLoader method), pop()(scrapy.settings.BaseSettingsmethod),294
79 post_process() (scrapy.contracts.Contract method),
NEWSPIDER_MODULE 185
setting,144 PprintItemExporter(classinscrapy.exporters),283
next_request() (scrapy.core.scheduler.BaseScheduler pre_process() (scrapy.contracts.Contract method),
method),276 185
next_request() (scrapy.core.scheduler.Scheduler print_live_refs() (in module scrapy.utils.trackref),
method),278 204
NO_CALLBACK()(inmodulescrapy.http.request),106 priority(scrapy.Requestattribute),104
NoReferrerPolicy (class in process_exception()
scrapy.spidermiddlewares.referer),259 (scrapy.downloadermiddlewares.DownloaderMiddleware
NoReferrerWhenDowngradePolicy (class in method),240
scrapy.spidermiddlewares.referer),259 process_item(),86
NotConfigured,157 process_request()(scrapy.downloadermiddlewares.DownloaderMiddleware
NotSupported,158 method),239
process_response()(scrapy.downloadermiddlewares.DownloaderMiddleware
O method),239
object_ref(classinscrapy.utils.trackref),204 process_results() (scrapy.spiders.XMLFeedSpider
OffsiteMiddleware (class in method),41
scrapy.downloadermiddlewares.offsite),248 process_spider_exception()
open() (scrapy.core.scheduler.BaseScheduler method), (scrapy.spidermiddlewares.SpiderMiddleware
276 method),255
open()(scrapy.core.scheduler.Schedulermethod),278 process_spider_input()
open_in_browser() (in module scrapy.utils.response), (scrapy.spidermiddlewares.SpiderMiddleware
182 method),255
open_spider(),86 process_spider_output()
open_spider()(scrapy.extensions.httpcache.CacheStorage (scrapy.spidermiddlewares.SpiderMiddleware
method),244 method),255
open_spider() (scrapy.statscollectors.StatsCollector process_spider_output_async()
method),297 (scrapy.spidermiddlewares.SpiderMiddleware
OriginPolicy (class in method),255
scrapy.spidermiddlewares.referer),260 process_start()(scrapy.spidermiddlewares.SpiderMiddleware
OriginWhenCrossOriginPolicy (class in method),254
scrapy.spidermiddlewares.referer),260 protocol(scrapy.http.Responseattribute),118
proxy
P reqmeta,247
Python Enhancement Proposals
parse
command,30 PEP 8,401
parse()(scrapy.Spidermethod),35
PythonItemExporter(classinscrapy.exporters),281
parse_node() (scrapy.spiders.XMLFeedSpider
Q
method),41
parse_row() (scrapy.spiders.CSVFeedSpider method), quotechar(scrapy.spiders.CSVFeedSpiderattribute),42
42
R
parse_start_url() (scrapy.spiders.CrawlSpider
method),39 RANDOMIZE_DOWNLOAD_DELAY
PERIODIC_LOG_DELTA setting,144
setting,267 re()(scrapy.Selectormethod),62
PERIODIC_LOG_STATS re()(scrapy.selector.SelectorListmethod),64
setting,267 re_first()(scrapy.Selectormethod),62
PERIODIC_LOG_TIMING_ENABLED re_first()(scrapy.selector.SelectorListmethod),64
setting,267 REACTOR_THREADPOOL_MAXSIZE
Index 415

ScrapyDocumentation,Release2.13.3
setting,145 handle_httpstatus_all,257
REDIRECT_ENABLED handle_httpstatus_list,257
setting,249 is_start_request,261
REDIRECT_MAX_TIMES max_retry_times,113
setting,249 proxy,247
REDIRECT_PRIORITY_ADJUST redirect_reasons,248
setting,145 redirect_urls,248
redirect_reasons referrer_policy,258
reqmeta,248 Request(classinscrapy),101
redirect_urls request(scrapy.http.Responseattribute),117
reqmeta,248 request_dropped
RedirectMiddleware (class in signal,273
scrapy.downloadermiddlewares.redirect), request_dropped()(inmodulescrapy.signals),273
248 request_fingerprinter (scrapy.crawler.Crawler at-
REFERER_ENABLED tribute),287
setting,258 REQUEST_FINGERPRINTER_CLASS
RefererMiddleware (class in setting,109
scrapy.spidermiddlewares.referer),258 request_from_dict()(inmodulescrapy.utils.request),
REFERRER_POLICY 106
setting,258 request_left_downloader
referrer_policy signal,273
reqmeta,258 request_left_downloader() (in module
register_namespace()(scrapy.Selectormethod),62 scrapy.signals),273
remove_from_list() (scrapy.settings.BaseSettings request_reached_downloader
method),294 signal,273
remove_namespaces()(scrapy.Selectormethod),62 request_reached_downloader() (in module
replace()(scrapy.http.Responsemethod),119 scrapy.signals),273
replace()(scrapy.Requestmethod),105 request_scheduled
replace_css()(scrapy.loader.ItemLoadermethod),79 signal,273
replace_in_component_priority_dict() request_scheduled()(inmodulescrapy.signals),273
(scrapy.settings.BaseSettingsmethod),294 RequestFingerprinter (class in scrapy.utils.request),
replace_jmes() (scrapy.loader.ItemLoader method), 109
79 Response(classinscrapy.http),117
replace_value() (scrapy.loader.ItemLoader method), response_downloaded
79 signal,275
replace_xpath() (scrapy.loader.ItemLoader method), response_downloaded() (in module scrapy.signals),
79 275
reqmeta response_received
allow_offsite,248 signal,274
autothrottle_dont_adjust_delay,217 response_received()(inmodulescrapy.signals),274
bindaddress,112 retrieve_response()
cookiejar,241 (scrapy.extensions.httpcache.CacheStorage
dont_cache,243 method),245
dont_merge_cookies,102 RETRY_ENABLED
dont_obey_robotstxt,252 setting,251
dont_redirect,248 RETRY_EXCEPTIONS
dont_retry,250 setting,251
download_fail_on_dataloss,113 RETRY_HTTP_CODES
download_latency,113 setting,251
download_maxsize,137 RETRY_PRIORITY_ADJUST
download_timeout,112 setting,251
download_warnsize,138 RETRY_TIMES
ftp_password,141 setting,251
ftp_user,141
416 Index

ScrapyDocumentation,Release2.13.3
RetryMiddleware (class in module,275
scrapy.downloadermiddlewares.retry),250 scrapy.crawler
ReturnsContract (class in scrapy.contracts.default), module,287
184 scrapy.downloadermiddlewares
RFC2616Policy (class in scrapy.extensions.httpcache), module,239
243 scrapy.downloadermiddlewares.cookies
RFPDupeFilter(classinscrapy.dupefilters),140 module,240
RobotParser(classinscrapy.robotstxt),253 scrapy.downloadermiddlewares.defaultheaders
ROBOTSTXT_OBEY module,242
setting,145 scrapy.downloadermiddlewares.downloadtimeout
ROBOTSTXT_PARSER module,242
setting,145 scrapy.downloadermiddlewares.httpauth
ROBOTSTXT_USER_AGENT module,242
setting,145 scrapy.downloadermiddlewares.httpcache
RobotsTxtMiddleware (class in module,243
scrapy.downloadermiddlewares.robotstxt), scrapy.downloadermiddlewares.httpcompression
252 module,247
Rule(classinscrapy.spiders),39 scrapy.downloadermiddlewares.httpproxy
rules(scrapy.spiders.CrawlSpiderattribute),38 module,247
runspider scrapy.downloadermiddlewares.offsite
command,31 module,248
scrapy.downloadermiddlewares.redirect
S module,248
SameOriginPolicy (class in scrapy.downloadermiddlewares.retry
scrapy.spidermiddlewares.referer),259 module,250
SCHEDULER scrapy.downloadermiddlewares.robotstxt
setting,145 module,252
Scheduler(classinscrapy.core.scheduler),276 scrapy.downloadermiddlewares.stats
SCHEDULER_DEBUG
module,253
setting,146 scrapy.downloadermiddlewares.useragent
SCHEDULER_DISK_QUEUE
module,254
setting,146 scrapy.exceptions
scheduler_empty
module,157
signal,270 scrapy.exporters
scheduler_empty()(inmodulescrapy.signals),270 module,278
SCHEDULER_MEMORY_QUEUE scrapy.extensions.closespider
setting,146 module,264
SCHEDULER_PRIORITY_QUEUE scrapy.extensions.corestats
setting,146 module,263
SCHEDULER_START_DISK_QUEUE scrapy.extensions.debug
setting,146 module,265
SCHEDULER_START_MEMORY_QUEUE scrapy.extensions.httpcache
setting,146 module,244
scraped() (scrapy.logformatter.LogFormatter method), scrapy.extensions.logstats
165 module,263
SCRAPER_SLOT_MAX_ACTIVE_SIZE scrapy.extensions.memdebug
setting,147 module,263
ScrapesContract (class in scrapy.contracts.default), scrapy.extensions.memusage
184 module,263
scrapy.contracts scrapy.extensions.periodic_log
module,184 module,265
scrapy.contracts.default scrapy.extensions.spiderstate
module,184 module,264
scrapy.core.scheduler scrapy.extensions.statsmailer
Index 417

ScrapyDocumentation,Release2.13.3
module,265 module,204
scrapy.extensions.telnet Selector(classinscrapy),61
module,263 selector(scrapy.http.TextResponseattribute),120
scrapy.FormRequest(built-inclass),114 selector(scrapy.loader.ItemLoaderattribute),75
scrapy.http SelectorList(classinscrapy.selector),63
module,101 send()(scrapy.mail.MailSendermethod),169
scrapy.item send_catch_log()(scrapy.signalmanager.SignalManager
module,65 method),296
scrapy.link send_catch_log_deferred()
module,124 (scrapy.signalmanager.SignalManager
scrapy.linkextractors method),296
module,122 serialize_field()(scrapy.exporters.BaseItemExporter
scrapy.linkextractors.lxmlhtml method),280
module,123 set()(scrapy.settings.BaseSettingsmethod),294
scrapy.loader set_in_component_priority_dict()
module,70 (scrapy.settings.BaseSettingsmethod),294
scrapy.mail set_stats() (scrapy.statscollectors.StatsCollector
module,168 method),297
scrapy.pipelines.files set_value() (scrapy.statscollectors.StatsCollector
module,212 method),297
scrapy.pipelines.images setdefault() (scrapy.settings.BaseSettings method),
module,214 295
scrapy.robotstxt setdefault_in_component_priority_dict()
module,253 (scrapy.settings.BaseSettingsmethod),295
scrapy.selector setmodule()(scrapy.settings.BaseSettingsmethod),295
module,61 setting
scrapy.settings ADDONS,129
module,291 ASYNCIO_EVENT_LOOP,130
scrapy.signalmanager AUTOTHROTTLE_DEBUG,218
module,296 AUTOTHROTTLE_ENABLED,218
scrapy.signals AUTOTHROTTLE_MAX_DELAY,218
module,269 AUTOTHROTTLE_START_DELAY,218
scrapy.spiderloader AUTOTHROTTLE_TARGET_CONCURRENCY,218
module,295 AWS_ACCESS_KEY_ID,129
scrapy.spidermiddlewares AWS_ENDPOINT_URL,130
module,254 AWS_REGION_NAME,130
scrapy.spidermiddlewares.base AWS_SECRET_ACCESS_KEY,129
module,256 AWS_SESSION_TOKEN,130
scrapy.spidermiddlewares.depth AWS_USE_SSL,130
module,257 AWS_VERIFY,130
scrapy.spidermiddlewares.httperror BOT_NAME,130
module,257 CLOSESPIDER_ERRORCOUNT,265
scrapy.spidermiddlewares.referer CLOSESPIDER_ITEMCOUNT,265
module,258 CLOSESPIDER_PAGECOUNT,265
scrapy.spidermiddlewares.start CLOSESPIDER_PAGECOUNT_NO_ITEM,265
module,261 CLOSESPIDER_TIMEOUT,264
scrapy.spidermiddlewares.urllength CLOSESPIDER_TIMEOUT_NO_ITEM,264
module,261 COMMANDS_MODULE,32
scrapy.spiders.Spider(built-inclass),33 COMPRESSION_ENABLED,247
scrapy.statscollectors CONCURRENT_ITEMS,131
module,297 CONCURRENT_REQUESTS,131
scrapy.utils.log CONCURRENT_REQUESTS_PER_DOMAIN,131
module,166 CONCURRENT_REQUESTS_PER_IP,131
scrapy.utils.trackref COOKIES_DEBUG,241
418 Index

ScrapyDocumentation,Release2.13.3
COOKIES_ENABLED,241 FILES_URLS_FIELD,210
DEFAULT_DROPITEM_LOG_LEVEL,131 FTP_PASSIVE_MODE,141
DEFAULT_ITEM_CLASS,132 FTP_PASSWORD,141
DEFAULT_REQUEST_HEADERS,132 FTP_USER,141
DEPTH_LIMIT,132 GCS_PROJECT_ID,141
DEPTH_PRIORITY,132 HTTPCACHE_ALWAYS_STORE,246
DEPTH_STATS_VERBOSE,132 HTTPCACHE_DBM_MODULE,246
DNS_RESOLVER,133 HTTPCACHE_DIR,245
DNS_TIMEOUT,133 HTTPCACHE_ENABLED,245
DNSCACHE_ENABLED,133 HTTPCACHE_EXPIRATION_SECS,245
DNSCACHE_SIZE,133 HTTPCACHE_GZIP,246
DOWNLOAD_DELAY,135 HTTPCACHE_IGNORE_HTTP_CODES,245
DOWNLOAD_FAIL_ON_DATALOSS,138 HTTPCACHE_IGNORE_MISSING,246
DOWNLOAD_HANDLERS,136 HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS,
DOWNLOAD_HANDLERS_BASE,136 246
DOWNLOAD_MAXSIZE,137 HTTPCACHE_IGNORE_SCHEMES,246
DOWNLOAD_SLOTS,137 HTTPCACHE_POLICY,246
DOWNLOAD_TIMEOUT,137 HTTPCACHE_STORAGE,246
DOWNLOAD_WARNSIZE,138 HTTPERROR_ALLOW_ALL,258
DOWNLOADER,133 HTTPERROR_ALLOWED_CODES,258
DOWNLOADER_CLIENT_TLS_CIPHERS,134 HTTPPROXY_AUTH_ENCODING,247
DOWNLOADER_CLIENT_TLS_METHOD,134 HTTPPROXY_ENABLED,247
DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING, IMAGES_EXPIRES,210
134 IMAGES_MIN_HEIGHT,211
DOWNLOADER_CLIENTCONTEXTFACTORY,133 IMAGES_MIN_WIDTH,211
DOWNLOADER_HTTPCLIENTFACTORY,133 IMAGES_RESULT_FIELD,210
DOWNLOADER_MIDDLEWARES,134 IMAGES_STORE,207
DOWNLOADER_MIDDLEWARES_BASE,135 IMAGES_STORE_GCS_ACL,209
DOWNLOADER_STATS,135 IMAGES_STORE_S3_ACL,209
DUPEFILTER_CLASS,138 IMAGES_THUMBS,211
DUPEFILTER_DEBUG,140 IMAGES_URLS_FIELD,210
EDITOR,140 ITEM_PIPELINES,141
EXTENSIONS,140 ITEM_PIPELINES_BASE,141
EXTENSIONS_BASE,140 JOBDIR,141
FEED_EXPORT_BATCH_ITEM_COUNT,99 LOG_DATEFORMAT,142
FEED_EXPORT_ENCODING,98 LOG_ENABLED,142
FEED_EXPORT_FIELDS,98 LOG_ENCODING,142
FEED_EXPORT_INDENT,98 LOG_FILE,142
FEED_EXPORTERS,99 LOG_FILE_APPEND,142
FEED_EXPORTERS_BASE,99 LOG_FORMAT,142
FEED_STORAGE_FTP_ACTIVE,98 LOG_FORMATTER,142
FEED_STORAGE_GCS_ACL,140 LOG_LEVEL,142
FEED_STORAGE_S3_ACL,98 LOG_SHORT_NAMES,143
FEED_STORAGES,98 LOG_STDOUT,142
FEED_STORAGES_BASE,99 LOG_VERSIONS,143
FEED_STORE_EMPTY,98 LOGSTATS_INTERVAL,143
FEED_TEMPDIR,140 MAIL_FROM,170
FEED_URI_PARAMS,100 MAIL_HOST,170
FEEDS,96 MAIL_PASS,170
FILES_EXPIRES,210 MAIL_PORT,170
FILES_RESULT_FIELD,210 MAIL_SSL,170
FILES_STORE,207 MAIL_TLS,170
FILES_STORE_GCS_ACL,209 MAIL_USER,170
FILES_STORE_S3_ACL,209 MEDIA_ALLOW_REDIRECTS,212
Index 419

ScrapyDocumentation,Release2.13.3
MEMDEBUG_ENABLED,143 TWISTED_REACTOR,149
MEMDEBUG_NOTIFY,143 URLLENGTH_LIMIT,151
MEMUSAGE_CHECK_INTERVAL_SECONDS,144 USER_AGENT,151
MEMUSAGE_ENABLED,143 WARN_ON_GENERATOR_RETURN_VALUE,151
MEMUSAGE_LIMIT_MB,144 settings
MEMUSAGE_NOTIFY_MAIL,144 command,31
MEMUSAGE_WARNING_MB,144 Settings(classinscrapy.settings),291
METAREFRESH_ENABLED,249 settings(scrapy.crawler.Crawlerattribute),287
METAREFRESH_IGNORE_TAGS,249 settings(scrapy.Spiderattribute),33
METAREFRESH_MAXDELAY,249 SETTINGS_PRIORITIES(inmodulescrapy.settings),291
NEWSPIDER_MODULE,144 shell
PERIODIC_LOG_DELTA,267 command,29
PERIODIC_LOG_STATS,267 signal
PERIODIC_LOG_TIMING_ENABLED,267 bytes_received,274
RANDOMIZE_DOWNLOAD_DELAY,144 engine_started,269
REACTOR_THREADPOOL_MAXSIZE,145 engine_stopped,270
REDIRECT_ENABLED,249 feed_exporter_closed,272
REDIRECT_MAX_TIMES,249 feed_slot_closed,272
REDIRECT_PRIORITY_ADJUST,145 headers_received,274
REFERER_ENABLED,258 item_dropped,270
REFERRER_POLICY,258 item_error,271
REQUEST_FINGERPRINTER_CLASS,109 item_scraped,270
RETRY_ENABLED,251 request_dropped,273
RETRY_EXCEPTIONS,251 request_left_downloader,273
RETRY_HTTP_CODES,251 request_reached_downloader,273
RETRY_PRIORITY_ADJUST,251 request_scheduled,273
RETRY_TIMES,251 response_downloaded,275
ROBOTSTXT_OBEY,145 response_received,274
ROBOTSTXT_PARSER,145 scheduler_empty,270
ROBOTSTXT_USER_AGENT,145 spider_closed,271
SCHEDULER,145 spider_error,272
SCHEDULER_DEBUG,146 spider_idle,271
SCHEDULER_DISK_QUEUE,146 spider_opened,271
SCHEDULER_MEMORY_QUEUE,146 update_telnet_vars,173
SCHEDULER_PRIORITY_QUEUE,146 SignalManager(classinscrapy.signalmanager),296
SCHEDULER_START_DISK_QUEUE,146 signals(scrapy.crawler.Crawlerattribute),287
SCHEDULER_START_MEMORY_QUEUE,146 sitemap_alternate_links
SCRAPER_SLOT_MAX_ACTIVE_SIZE,147 (scrapy.spiders.SitemapSpider attribute),
SPIDER_CONTRACTS,147 43
SPIDER_CONTRACTS_BASE,147 sitemap_filter() (scrapy.spiders.SitemapSpider
SPIDER_LOADER_CLASS,147 method),44
SPIDER_LOADER_WARN_ONLY,148 sitemap_follow (scrapy.spiders.SitemapSpider at-
SPIDER_MIDDLEWARES,148 tribute),43
SPIDER_MIDDLEWARES_BASE,148 sitemap_rules (scrapy.spiders.SitemapSpider at-
SPIDER_MODULES,148 tribute),43
STATS_CLASS,148 sitemap_urls(scrapy.spiders.SitemapSpiderattribute),
STATS_DUMP,148 43
STATSMAILER_RCPTS,149 SitemapSpider(classinscrapy.spiders),43
TELNETCONSOLE_ENABLED,149 Spider(classinscrapy),33
TELNETCONSOLE_HOST,173 spider(scrapy.crawler.Crawlerattribute),288
TELNETCONSOLE_PASSWORD,173 spider_closed
TELNETCONSOLE_PORT,173 signal,271
TELNETCONSOLE_USERNAME,173 spider_closed()(inmodulescrapy.signals),271
TEMPLATES_DIR,149 SPIDER_CONTRACTS
420 Index

ScrapyDocumentation,Release2.13.3
setting,147 stop()(scrapy.crawler.Crawlermethod),288
SPIDER_CONTRACTS_BASE stop()(scrapy.crawler.CrawlerProcessmethod),291
setting,147 stop()(scrapy.crawler.CrawlerRunnermethod),290
spider_error StopDownload,158
signal,272 store_response()(scrapy.extensions.httpcache.CacheStorage
spider_error()(inmodulescrapy.signals),272 method),245
spider_error() (scrapy.logformatter.LogFormatter StrictOriginPolicy (class in
method),165 scrapy.spidermiddlewares.referer),260
spider_idle StrictOriginWhenCrossOriginPolicy (class in
signal,271 scrapy.spidermiddlewares.referer),260
spider_idle()(inmodulescrapy.signals),271
T
SPIDER_LOADER_CLASS
setting,147 TelnetConsole(classinscrapy.extensions.telnet),263
SPIDER_LOADER_WARN_ONLY TELNETCONSOLE_ENABLED
setting,148 setting,149
SPIDER_MIDDLEWARES TELNETCONSOLE_HOST
setting,148 setting,173
SPIDER_MIDDLEWARES_BASE TELNETCONSOLE_PASSWORD
setting,148 setting,173
SPIDER_MODULES TELNETCONSOLE_PORT
setting,148 setting,173
spider_opened TELNETCONSOLE_USERNAME
signal,271 setting,173
spider_opened()(inmodulescrapy.signals),271
TEMPLATES_DIR
spider_stats(scrapy.statscollectors.MemoryStatsCollector setting,149
attribute),168 text(scrapy.http.TextResponseattribute),120
SpiderLoader(classinscrapy.spiderloader),295 TextResponse(classinscrapy.http),120
SpiderMiddleware (class in thumb_path() (scrapy.pipelines.images.ImagesPipeline
scrapy.spidermiddlewares),254 method),214
SpiderState (class in scrapy.extensions.spiderstate), to_dict()(scrapy.Requestmethod),106
264
TWISTED_REACTOR
StackTraceDump (class in setting,149
scrapy.extensions.periodic_log),267
start()(scrapy.crawler.CrawlerProcessmethod),290 U
start()(scrapy.Spidermethod),34
UnsafeUrlPolicy (class in
start_exporting()(scrapy.exporters.BaseItemExporter
scrapy.spidermiddlewares.referer),260
method),281
update()(scrapy.settings.BaseSettingsmethod),295
start_urls(scrapy.Spiderattribute),33
update_pre_crawler_settings(),236
startproject
update_settings(),235
command,26
update_settings()(scrapy.Spiderclassmethod),34
StartSpiderMiddleware (class in
update_telnet_vars
scrapy.spidermiddlewares.start),261
signal,173
state(scrapy.Spiderattribute),33
update_telnet_vars() (in module
stats(scrapy.crawler.Crawlerattribute),288
scrapy.extensions.telnet),173
STATS_CLASS
uri_params()(inmodulescrapy.extensions.feedexport),
setting,148
100
STATS_DUMP
url(scrapy.http.Responseattribute),117
setting,148
url(scrapy.Requestattribute),103
StatsCollector(classinscrapy.statscollectors),297
UrlContract(classinscrapy.contracts.default),184
StatsMailer (class in scrapy.extensions.statsmailer),
urljoin()(scrapy.http.Responsemethod),119
265
urljoin()(scrapy.http.TextResponsemethod),122
STATSMAILER_RCPTS
URLLENGTH_LIMIT
setting,149
setting,151
status(scrapy.http.Responseattribute),117
Index 421

ScrapyDocumentation,Release2.13.3
UrlLengthMiddleware (class in
scrapy.spidermiddlewares.urllength),261
USER_AGENT
setting,151
UserAgentMiddleware (class in
scrapy.downloadermiddlewares.useragent),
254
V
version
command,31
view
command,29
W
wait_for() (scrapy.signalmanager.SignalManager
method),296
WARN_ON_GENERATOR_RETURN_VALUE
setting,151
write(),95
X
XMLFeedSpider(classinscrapy.spiders),40
XmlItemExporter(classinscrapy.exporters),282
xmliter_lxml()(inmodulescrapy.utils.iterators),178
XmlResponse(classinscrapy.http),122
xpath()(scrapy.http.TextResponsemethod),121
xpath()(scrapy.Selectormethod),61
xpath()(scrapy.selector.SelectorListmethod),63
422 Index

