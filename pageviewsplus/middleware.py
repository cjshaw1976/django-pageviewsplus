import re
from .models import HitCount
from django.db.models import F
from pageviewsplus import settings

class PageViewsPlusMiddleware:


    def is_ignored_url(self, request, url_pattern=''):

        # Although less readable the following list comprehension is probably faster than separate loop lines.
        #
        # The equivalent loops lines should read something like:
        ##
        ## for ignored_url in settings.IGNORED_URLS:
        ##    if request.META['PATH_INFO'].startswith(ignored_url)):
        ##        return True
        ##
        ## return False

        return any(request.META['PATH_INFO'].startswith(ignored_url)
            for ignored_url in settings.IGNORED_URLS)


    def is_ignored_ua(self, request, ua_pattern=''):

        return any(re.search(ua_pattern, request.META['HTTP_USER_AGENT']) 
                for ua_pattern in settings.IGNORED_USER_AGENTS)


    def process_request(self, request, *args, **kwargs):

        if settings.IGNORED_URLS and self.is_ignored_url(request):
            return None

        # To test if user agents in your ignore list are not counted try change the user agent in your browser.
        # The ability is built into Chrome in Developer tools.  Other browsers may need add ons.
        # Search engine bot user agent strings can be obtained from websites such as useragentstring.com
        elif 'HTTP_USER_AGENT' in request.META and settings.IGNORED_USER_AGENTS and self.is_ignored_ua(request):
            return None
        else:
            hit, hit_created = HitCount.objects.get_or_create(url=request.path)
            hit.hits = F('hits') + 1
            hit.save()
            return None
