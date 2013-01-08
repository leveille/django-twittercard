from django import template
from django.conf import settings
register = template.Library()

def twittercard(context, *args, **kwargs):
    request = context['request']
    type = kwargs.get('type', 'summary')
    site = kwargs.get('site', settings.TWITTERCARD_SITE)
    site_id = kwargs.get('site_id', settings.TWITTERCARD_SITE_ID)
    creator = kwargs.get('creator', settings.TWITTERCARD_CREATOR)
    creator_id = kwargs.get('creator', None)
    title = kwargs.get('title', None)
    description = kwargs.get('description', None)
    url = kwargs.get('url', request.get_full_path())
    image = kwargs.get('image', None)
    return {
        'type': type,
        'site': site,
        'site_id': site_id,
        'creator': creator,
        'title': title,
        'description': description,
        'type': type,
        'url':url,
        'image': image
    }
register.inclusion_tag('twittercard/card.html', takes_context=True)(twittercard)
