from django import template
from django.utils.safestring import mark_safe
import requests

register = template.Library()


@register.simple_tag(name='vimeo_embed_responsive')
def vimeo_embed_responsive(vimeo_id):
    return mark_safe("\
    <style>\
        .embed-container {{\
            position: relative;\
            padding-bottom: 56.25%;\
            height: 0;\
            overflow: hidden;\
            max-width: 100%;\
        }}\
        .embed-container iframe,\
        .embed-container object,\
        .embed-container embed {{\
            position: absolute;\
            top: 0;\
            left: 0;\
            width: 100%;\
            height: 100%;\
        }}\
    </style>\
    <div class='embed-container'>\
        <iframe src='http://player.vimeo.com/video/{0}'\
            frameborder='0'\
            webkitAllowFullScreen\
            mozallowfullscreen\
            allowFullScreen>\
        </iframe>\
    </div>".format(vimeo_id))
