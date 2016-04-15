# django-vimeo-utils  [![Build Status](https://travis-ci.org/life-in-messiah/django-vimeo-utils.svg?branch=master)](https://travis-ci.org/life-in-messiah/django-vimeo-utils)  
Vimeo-related shortcuts for Django

## Installation
1.  
  * `pip install --user vimeo_utils`  
  * OR you can download and unzip the .tar.gz package and then run `python setup.py install` inside the unzipped directory
2. Add "vimeo_utils" to your `INSTALLED_APPS` setting like this:
```
INSTALLED_APPS = [
      'vimeo_utils',
```

## Template tags

### `vimeo_embed_responsive`
*Generates embed code from [Embed Responsively](http://embedresponsively.com/) based on the vimeo ID*  
Usage: `{% vimeo_embed_responsive vimeo_id %}`  
Note: `vimeo_id` is a string, not an integer  
Example:
```
<div class="container">
<h1>Scott Schwartz</h1>
{% vimeo_embed_responsive "144912687" %}
</div>
```

### `vimeo_thumbnail`
*Fetches the src URI for the thumbnail based on the vimeo ID*  
Usage: `{% vimeo_thumbnail vimeo_id %}`  
Note: `vimeo_id` is a string, not an integer  
Example:
```
<div class="container">
  <h1>Scott Schwartz</h1>
  <h3>The man. The legend.</h3>
  <img alt="Scott" src="{% vimeo_thumbnail "144912687" %}" />
</div>
```
