from django.conf import settings

# Attributes in this settings.py file can be edited directly or overridden by adding to main project settings.py
# To add to main project settings.py add as standard django list.
# example
## IGNORED_USER_AGENTS = ['agent1', 'agent2', 'etc']
## IGNORED_URLS = ['/url1', '/url2', '/url/etc']
#To disable either feature use:
##IGNORED_USER_AGENTS = []
##IGNORED_URLS = []
#
# User agent strings can be obtained from websites such as useragentstring.com
#
IGNORED_USER_AGENTS = getattr(
        settings,
        'IGNORED_USER_AGENTS',
        [
                'Teoma', 'alexa', 'froogle', 'Gigabot', 'inktomi', 'looksmart', 'URL_Spider_SQL', 'Firefly',
                'NationalDirectory', 'Ask Jeeves', 'TECNOSEEK', 'InfoSeek', 'WebFindBot', 'girafabot', 'crawler',
                'www.galaxy.com', 'Googlebot', 'Googlebot/2.1', 'Google', 'Webmaster', 'Scooter', 'James Bond',
                'Slurp', 'msnbot', 'appie', 'FAST', 'WebBug', 'Spade', 'ZyBorg', 'rabaz', 'Baiduspider',
                'Feedfetcher-Google', 'TechnoratiSnoop', 'Rankivabot', 'Mediapartners-Google', 'Sogou web spider',
                'WebAlta Crawler', 'MJ12bot', 'Yandex/', 'YaDirectBot', 'StackRambler', 'DotBot', 'dotbot', 'bingbot'
        ]
)

##############
# IGNORED_URLS
# Include the leading '/' and include the entire url for subdomains.
# So to ignore '/blog/subdomain/subsubdomain' use that entire string.
#
IGNORED_URLS = getattr(settings, 'IGNORED_URLS', ['/sitemap.xml', '/robots.txt', '/favicon.ico', '/static', '/admin'])
