# Twitter Cards App for Django

Adds HTML Meta tags for Twitter Card support.

* [Twitter Cards](https://dev.twitter.com/docs/cards)
* [How to Create a Twitter Card](http://davidwalsh.name/twitter-cards)
    
## Installation

```
pip install -e git+git@github.com:leveille/django-twittercard.git#egg=twittercard
```

## Usage

1. Add `twittercard` to your settings.py `INSTALLED_APPS` list
2. There are a few configuration options to twittercard that can be placed in a dictionary called `TWITTERCARD_CONFIG` in settings.py.  Refer to the [Twitter Card Docs](https://dev.twitter.com/docs/cards) for help regarding [card and content attribution](https://dev.twitter.com/docs/cards#content).

```python
TWITTERCARD_CONFIG = {
    'SITE': '@foo',
    'SITE_ID': 'foo',
    'CREATOR': '@bar',
    'CREATOR_ID': 'bar'
}
```

* `SITE` __Not Required__: @username for the website used in the card footer.
* `SITE_ID` __Not Required__: Same as `SITE`, but the website's Twitter user ID instead. Note that user ids never change, while @usernames can be changed by the user.
* `CREATOR` __Not Required__: @username for the content creator / author.
* `CREATOR_ID` __Not Required__: Same as twitter:creator, but the Twitter user's ID.

2. Load the `twittercard` custom tags
3. Call the `twittercard` tag, passing in the appropriate parameters

```html
{% load twittercard %}
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Django TwitterCard Example</title>
        {% twittercard title="Foo" description="Bar" %}
    </head>
    <body></body>
</html>
```

The result, including the use of the `TWITTERCARD_CONFIG` options defined above, would be:

```html
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@foo">
<meta name="twitter:site:id" content="foo">
<meta name="twitter:creator" content="@bar">
<meta name="twitter:creator:id" content="bar">
<meta name="twitter:url" content="http://localhost:8000/sub/">
<meta property="twitter:title" content="Foo"/>
<meta name="twitter:description" content="Bar">
```

## Summary TwitterCard

The summary card can be used for many kinds of web content, from blog posts and news articles, to products and restaurants.

```
{% twittercard card="summary" site="" site_id="" creator="" creator_id="" url="" title="" description="" image="" %}
```

* `card` (__optional__): Defaults to summary

* `site` (**Optional**): @username for the website used in the card footer.  Will default to `TWITTERCARD_CONFIG` if supplied.

* `site_id` (**Optional**): Same as `SITE`, but the website's Twitter user ID instead. Note that user ids never change, while @usernames can be changed by the user.  Will default to `TWITTERCARD_CONFIG` if supplied.

* `creator` (**Optional**): @username for the content creator / author.

* `creator_id` (**Optional**): Same as twitter:creator, but the Twitter user's ID.

* `url` (**Required**): Canonical URL of the card content.

* `title` (**Required**): Title should be concise and will be truncated at 70 characters.

* `description` (**Required**): A description that concisely summarizes the content of the page, as appropriate for presentation within a Tweet. Do not re-use the title text as the description, or use this field to describe the general services provided by the website. Description text will be truncated at the word to 200 characters.

* `image` (**Optional**): URL to a unique image representing the content of the page. Do not use a generic image such as your website logo, author photo, or other image that spans multiple pages. Images larger than 120x120px will be resized and cropped square based on longest dimension. Images smaller than 60x60px will not be shown.

**NOTE**: If any required fields are omitted, the card may not be shown in the Tweet.

## Photo TwitterCard

The photo card puts the image front and center in the Tweet.

```
{% twittercard card="photo" site="" site_id="" creator="" creator_id="" title="" description="" image="" image_width="" image_height="" %}
```

* `card` (**Required**): Should be "photo"

* `site` (**Optional**): @username for the website used in the card footer.  Will default to `TWITTERCARD_CONFIG` if supplied.

* `site_id` (**Optional**): Same as `SITE`, but the website's Twitter user ID instead. Note that user ids never change, while @usernames can be changed by the user.  Will default to `TWITTERCARD_CONFIG` if supplied.

* `creator` (**Optional**): @username for the content creator / author.

* `creator_id` (**Optional**): Same as twitter:creator, but the Twitter user's ID.

* `title` (**Optional**): See full explanation of `title` in the Summary Card

* `description` (**Optional**): See full explanation of `description` in the Summary Card

* `image` (**Required**): A URL to the image representing the content.

* `image_width` (**Optional**): Providing width in px helps us more accurately preserve the the aspect ratio of the image when resizing.

* `image_height` (**Optional**): Providing height in px helps us more accurately preserve the the aspect ratio of the image when resizing.

## TODO

* [Check for required fields based on card type](https://github.com/leveille/django-twittercard/issues/1)
* [Add support for player card](https://github.com/leveille/django-twittercard/issues/2)

