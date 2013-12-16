from django.conf import settings

IGNORE_USER_AGENTS = getattr(
        settings,
        'IGNORE_USER_AGENTS',
        [
                "Teoma", "alexa", "froogle", "Gigabot", "inktomi", "looksmart", "URL_Spider_SQL", "Firefly",
                "NationalDirectory", "Ask Jeeves", "TECNOSEEK", "InfoSeek", "WebFindBot", "girafabot", "crawler",
                "www.galaxy.com", "Googlebot", "Googlebot/2.1", "Google", "Webmaster", "Scooter", "James Bond",
                "Slurp", "msnbot", "appie", "FAST", "WebBug", "Spade", "ZyBorg", "rabaz", "Baiduspider",
                "Feedfetcher-Google", "TechnoratiSnoop", "Rankivabot", "Mediapartners-Google", "Sogou web spider",
                "WebAlta Crawler", "MJ12bot", "Yandex/", "YaDirectBot", "StackRambler", "DotBot", "dotbot"
        ]
)
