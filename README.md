Introduction
============
Pageviews is a very simple middleware based page view counter. It's sole purpose is to increment page views.

PageviewsPlus adds the ability to filter out search engine bots.




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

3. Add 'pageviews.middleware.PageViewsMiddleware' to MIDDLEWARE_CLASSES.
```python
    MIDDLEWARE_CLASSES = (
        "...",
        "pageviewsplus.middleware.PageViewsMiddleware"
    )
```

4. Run 'python manage.py syncdb' or 'python manage.py migrate'.
```bash
    python manage.py migrate
```

5. Add {% load pageviewsplus_tags %} to templates.

6. Insert {% pageviewsplus %} or {% pageviewsplus_url request.path %} to templates.
