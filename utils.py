from pageviewsplus import settings

def is_ignored(request, visit, user_agents=True):
    
    if user_agents and request.META.get("HTTP_USER_AGENT", "") in settings.IGNORE_USER_AGENTS:
        return True

    else:
        return False