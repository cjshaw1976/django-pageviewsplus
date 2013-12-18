from .models import HitCount
from django.db.models import F
from pageviewsplus.utils import is_ignored

class PageViewsPlusMiddleware:
    def process_request(self, request, *args, **kwargs):

        if 'HTTP_USER_AGENT' in request.META and is_ignored(request):
            return None
        # To test if user agents in your ignore list are not counted try change the user agent in your browser.
        # The ability is built into Chrome in Developer tools.  Other browsers may need add ons.  

        else:
            hit, hit_created = HitCount.objects.get_or_create(url=request.path)
            hit.hits = F('hits') + 1
            hit.save()
            return None
