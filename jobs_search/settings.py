BOT_NAME = "jobs_search"

SPIDER_MODULES = ["jobs_search.spiders"]
NEWSPIDER_MODULE = "jobs_search.spiders"

ADDONS = {}


USER_AGENT = "jobs_search (+https://github.com/iamkorniichuk/jobs-search)"
ROBOTSTXT_OBEY = True

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False

FEED_EXPORT_ENCODING = "utf-8"
