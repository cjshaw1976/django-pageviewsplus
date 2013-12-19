Introduction
============
Pageviews is a very simple middleware based page view counter. It's sole purpose is to increment page views.

PageviewsPlus adds the ability to ignore a list of urls and user agents such as search engine bots.  A default list is included for both.




Quickstart
==========

1. Install from github or clone the repository:
```bash
    pip install git+git://github.com/shadowym/django-pageviewsplus.git
```

2. Add 'pageviews' to INSTALLED_APPS.
```python
    INSTALLED_APPS = (
        "...",
        "pageviewsplus",
    )
```

3. Add 'pageviewsplus.middleware.PageViewsPlusMiddleware' to MIDDLEWARE_CLASSES.
```python
    MIDDLEWARE_CLASSES = (
        "...",
        "pageviewsplus.middleware.PageViewsPlusMiddleware"
    )
```

4. Run 'python manage.py syncdb' or 'python manage.py migrate'.
```bash
    python manage.py migrate
```

5. Add {% load pageviewsplus_tags %} to templates.

6. Insert {% pageviewsplus %} or {% pageviewsplus_url request.path %} to templates.

Configuration
=============

Your ``settings.py`` file contains the folling settings.

* ``IGNORE_USER_AGENTS``: this is used to define what user agents to ignore. The list is case sensitive. 

By default, ``IGNORE_USER_AGENTS`` will have the following values.

    [
    "Teoma", "alexa", "froogle", "Gigabot", "inktomi", "looksmart", "URL_Spider_SQL", "Firefly",
    "NationalDirectory", "Ask Jeeves", "TECNOSEEK", "InfoSeek", "WebFindBot", "girafabot", "crawler",
    "www.galaxy.com", "Googlebot", "Googlebot/2.1", "Google", "Webmaster", "Scooter", "James Bond",
    "Slurp", "msnbot", "appie", "FAST", "WebBug", "Spade", "ZyBorg", "rabaz", "Baiduspider",
    "Feedfetcher-Google", "TechnoratiSnoop", "Rankivabot", "Mediapartners-Google", "Sogou web spider",
    "WebAlta Crawler", "MJ12bot", "Yandex/", "YaDirectBot", "StackRambler", "DotBot", "dotbot"
    ]