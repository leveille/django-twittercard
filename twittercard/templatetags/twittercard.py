from django import template
from django.conf import settings
register = template.Library()

def twittercard_summary(context, *args, **kwargs):
    card = get_twittercard_attributes(kwargs)
    card['card'] = 'summary'
    request = context['request']
    card['url'] = kwargs.get('url', request.build_absolute_uri())
    return card
register.inclusion_tag('twittercard/summary.html', takes_context=True)(twittercard_summary)

def twittercard_photo(context, *args, **kwargs):
    card = get_twittercard_attributes(kwargs)
    card['card'] = 'photo'
    card['image_width'] = kwargs.get('image_width', None)
    card['image_height'] = kwargs.get('image_height', None)
    return card
register.inclusion_tag('twittercard/photo.html', takes_context=True)(twittercard_photo)

def get_twittercard_attributes(kwargs):
    card = {}
    card['title'] = kwargs.get('title', None)
    card['description'] = kwargs.get('description', None)
    card['image'] = kwargs.get('image', None)
    config = getattr(settings, 'TWITTERCARD_CONFIG', None)
    if config is not None:
        card['site'] = kwargs.get('site', config.get('SITE', None))
        card['site_id'] = kwargs.get('site_id', config.get('SITE_ID', None))
        card['creator'] = kwargs.get('creator', config.get('CREATOR', None))
        card['creator_id'] = kwargs.get('creator_id', config.get('CREATOR_ID', None))
    return card
