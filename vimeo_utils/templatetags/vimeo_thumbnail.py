from django import template
import requests

register = template.Library()


@register.simple_tag(name='vimeo_thumbnail')
def vimeo_thumbnail(vimeo_id):
    prefix = "https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/"
    url = prefix + vimeo_id
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["thumbnail_url"]
    else:
        raise Exception("HTTP response for %s returned a status code %i" % (url, response.status_code))
