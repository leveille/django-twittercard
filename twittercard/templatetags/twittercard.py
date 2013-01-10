from django import template
from django.conf import settings
register = template.Library()

def twittercard(context, *args, **kwargs):
    request = context['request']
    card = kwargs.get('card', 'summary')
    title = kwargs.get('title', None)
    description = kwargs.get('description', None)
    url = kwargs.get('url', request.build_absolute_uri())
    image = kwargs.get('image', None)
    image_width = kwargs.get('image_width', None)
    image_height = kwargs.get('image_width', None)

    config = getattr(settings, 'TWITTERCARD_CONFIG', None)
    (site, site_id, creator, creator_id) = (None, None, None, None)
    if config is not None:
        site = kwargs.get('site', config.get('SITE', None))
        site_id = kwargs.get('site_id', config.get('SITE_ID', None))
        creator = kwargs.get('creator', config.get('CREATOR', None))
        creator_id = kwargs.get('creator_id', config.get('CREATOR_ID', None))

    return {
        'card': card,
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
