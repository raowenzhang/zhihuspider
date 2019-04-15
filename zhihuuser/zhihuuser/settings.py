# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
  # 'cookie': '_zap=2a66937d-c99d-447e-b9ea-4fe2df046f3b; d_c0="ANCiHu4Txw6PTgz3mHPnGrqPUnB5dQWnRAo=|1546658057"; ISSW=1; _xsrf=kZ4SoPZreTLKCbGf00Vkklw280dhN4HN; tst=r; __utma=155987696.1679825704.1552915678.1552915678.1552915678.1; __utmz=155987696.1552915678.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); q_c1=71511bf94d804282acb9388695daa86f|1552982088000|1546658064000; capsion_ticket="2|1:0|10:1553831420|14:capsion_ticket|44:MDAwMzQ2MWU2ZWZjNDY0MzhkYTIyZTA3YTE2ZDA0NDU=|ae9386f0a5dafea8f148fae756925942607fd5e67b3b9af433f28521d90b7dfb"; z_c0="2|1:0|10:1553831433|4:z_c0|92:Mi4xQzNLLUFnQUFBQUFBMEtJZTdoUEhEaVlBQUFCZ0FsVk5DZVNLWFFENndZNGc4TWVfWTZjQXFPQ0ctZzhPR1pkUjZ3|20a2198a6ce6f8a0efc8a48fe1bcce8207868950818ab1d7cad2ab490be68e78"; __gads=ID=bd442d6801391027:T=1555210716:S=ALNI_MYJywdEUeP2pnCFY1OggVxSTx3Ktw; tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d',
  # 'referer': 'https://www.zhihu.com/people/excited-vczh/following?page=1',
  'x-zse-83': '3_1.1',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhihuuser.middlewares.ZhihuMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhihuuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MONGO_URI = 'localhost'

MONGO_DATABASE = 'zhihu'
