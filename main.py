import webapp2
import logging
from webapp2_extras import jinja2


def jinja2_factory(app):
  j = jinja2.Jinja2(app)
  j.environment.filters.update({
  })
  j.environment.globals.update({
    'uri_for': webapp2.uri_for,
  })
  return j


class BaseHandler(webapp2.RequestHandler):
  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2(factory=jinja2_factory)

  def render(self, _template, **context):
    rv = self.jinja2.render_template(_template, **context)
    self.response.write(rv)


class PolymerHandler(BaseHandler):
  def get(self):
    return self.render('index.html')


logging.getLogger().setLevel(logging.DEBUG)
application = webapp2.WSGIApplication([
  webapp2.Route(r'/', 'main.PolymerHandler'),
  webapp2.Route(r'/img', 'img.Img'),
  webapp2.Route(r'/', webapp2.RedirectHandler, defaults={'_uri': 'http://plus.google.com/102253691922262022063'}),
  webapp2.Route(r'/+', webapp2.RedirectHandler, defaults={'_uri': 'http://plus.google.com/102253691922262022063'}),
  webapp2.Route(r'/twitter', webapp2.RedirectHandler, defaults={'_uri': 'http://twitter.com/sadovnychyi'}),
  webapp2.Route(r'/vk', webapp2.RedirectHandler, defaults={'_uri': 'http://vk.com/sadovnychyi'}),
  webapp2.Route(r'/ex.ua', webapp2.RedirectHandler, defaults={'_uri': 'http://ex.ua'}),
  webapp2.Route(r'/tumblr', webapp2.RedirectHandler, defaults={'_uri': 'http://tumblr.com'}),
], debug=True)
