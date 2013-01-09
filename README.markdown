# Twitter Cards App for Django

Adds HTML Meta tags for Twitter Card support.

* [Twitter Cards](https://dev.twitter.com/docs/cards)
* [How to Create a Twitter Card](http://davidwalsh.name/twitter-cards)
	
## Installation

	pip install -e git+ssh://git@github.com:leveille/django-twittercard.git#egg=TwitterCard

## Usage

1. Add `twittercard` to your settings.py INSTALLED_APPS list
2. Define the following settings in settings.py.  Refer to the [Twitter Card Docs](https://dev.twitter.com/docs/cards) for help regarding [card and content attribution](https://dev.twitter.com/docs/cards#content).

	TWITTERCARD_SITE = '@foo'
	TWITTERCARD_SITE_ID = 'foo'
	TWITTERCARD_CREATOR = '@bar'
	TWITTERCARD_CREATOR_ID = 'bar'

2. Load the `twittercard` custom tags
3. Call the `twittercard` tag, passing in the appropriate parameters

	{% load twittercard %}
	<!DOCTYPE html>
	<html>
	    <head>
	        <meta charset="utf-8">
	        <title>Django TwitterCard Example</title>
	        {% twittercard title="Testing" description="Foobar" %}
	    </head>
	    <body></body>
	</html>

## Available `twittercard` parameters:

type
site
site_id
creator
creator_id
title
description
type
url
image
image_width
image_height

## TODO

1. Improve docs regarding parameters
2. [Check for required fields based on card type](https://github.com/leveille/django-twittercard/issues/1)
3. [Add support for player card](https://github.com/leveille/django-twittercard/issues/2)