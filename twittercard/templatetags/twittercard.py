from django import template
from django.conf import settings
register = template.Library()

def twittercard(context, *args, **kwargs):
    request = context['request']
    type = kwargs.get('type', 'summary')

    twittercard_site = settings.get('TWITTERCARD_SITE', None)
    site = kwargs.get('site', twittercard_site)

    twittercard_site_id = settings.get('TWITTERCARD_SITE_ID', None)
    site_id = kwargs.get('site_id', twittercard_site_id)

    twittercard_creator = settings.get('TWITTERCARD_CREATOR', None)
    creator = kwargs.get('creator', twittercard_creator)

    twittercard_creator_id = settings.get('TWITTERCARD_CREATOR_ID', None)
    creator_id = kwargs.get('creator', twittercard_creator_id)

    title = kwargs.get('title', None)
    description = kwargs.get('description', None)
    url = kwargs.get('url', request.get_full_path())
    image = kwargs.get('image', None)
    image_width = kwargs.get('image_width', None)
    image_height = kwargs.get('image_width', None)
    return {
        'type': type,
        'site': site,
        'site_id': site_id,
        'creator': creator,
        'creator_id': creator_id,
        'title': title,
        'description': description,
        'type': type,
        'url':url,
        'image': image,
        'image_width': image_width,
        'image_height': image_height
    }
register.inclusion_tag('twittercard/card.html', takes_context=True)(twittercard)
