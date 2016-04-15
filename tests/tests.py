from django.test import TestCase
from django.template import Template, Context


class CustomTemplateTagTest(TestCase):
    def _try(self, template_string, expected_output):
        t = Template(template_string)
        empty = {}
        c = Context(empty)
        result = t.render(c)
        result = result.replace(' ', '').replace('\t', '').replace('\n', '')
        expected_output = expected_output.replace(' ', '').replace('\t', '').replace('\n', '')
        if result != expected_output:
            raise AssertionError("Expected:\n%s\nActual:\n%s" % (expected_output, result))

class VimeoThumbnailTest(CustomTemplateTagTest):
    def test_tag(self):
        self._try(
            "{% load vimeo_thumbnail %}{% vimeo_thumbnail \"144912687\" %}",
            "https://i.vimeocdn.com/video/542874620_1280.jpg"
        )

class VimeoEmbedResponsiveTest(CustomTemplateTagTest):
    def test_tag(self):
        self._try(
            "{% load vimeo_embed_responsive %}{% vimeo_embed_responsive \"144912687\" %}",
            "<style>\
                .embed-container {\
                    position: relative;\
                    padding-bottom: 56.25%;\
                    height: 0;\
                    overflow: hidden;\
                    max-width: 100%;\
                }\
                .embed-container iframe,\
                .embed-container object,\
                .embed-container embed {\
                    position: absolute;\
                    top: 0;\
                    left: 0;\
                    width: 100%;\
                    height: 100%;\
                }\
            </style>\
            <div class='embed-container'>\
                <iframe src='http://player.vimeo.com/video/144912687'\
                    frameborder='0'\
                    webkitAllowFullScreen\
                    mozallowfullscreen\
                    allowFullScreen>\
                </iframe>\
            </div>"
        )
