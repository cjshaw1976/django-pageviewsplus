import re
from pageviewsplus import settings

def is_ignored(request, ua_pattern=""):

    #if url:
    #    for ignored_url in settings.IGNORE_URLS:
    #        if request.META["PATH_INFO"].startswith(ignored_url):
    #            return True
    #****************************************************************
    # Although less readable the following list comprehension is probably faster than separate loop lines. 
    #
    # The equivalent loops lines should read something like:
    #
    ## for ua_pattern in settings.IGNORE_USER_AGENTS:
    ##    if re.search(ua_pattern, request.META.get("HTTP_USER_AGENT",""):
    ##        return True
    ##
    ## return False    
    #

    return any(re.search(ua_pattern, request.META.get("HTTP_USER_AGENT","")) 
        for ua_pattern in settings.IGNORE_USER_AGENTS)

