import webapp2
import logging
from webapp2_extras import jinja2
from google.appengine.api import urlfetch, memcache
import constants


class BaseHandler(webapp2.RequestHandler):
  def jinja2_factory(self, app):
    j = jinja2.Jinja2(app)
    j.environment.filters.update({})
    j.environment.globals.update({
      'uri': self.uri_for,
    })
    return j

  @webapp2.cached_property
  def jinja2(self):
    return jinja2.get_jinja2(factory=self.jinja2_factory)

  def render(self, _template, **context):
    rv = self.jinja2.render_template(_template, **context)
    self.response.write(rv)


class ProxyHandler(webapp2.RequestHandler):
  def get(self):
    url = self.request.get('url')
    key = '_proxy_%s' % url
    result = memcache.get(key)
    if result is None:
      result = urlfetch.fetch(url)
      result = {'status_code': result.status_code,
                'headers': result.headers,
                'content': result.content}
      memcache.set(key, result, time=60 * 60 * 24)
    self.response.set_status(result['status_code'])
    for header in result['headers']:
      self.response.headers[header] = result['headers'][header]
    self.response.out.write(result['content'])


class HomeHandler(BaseHandler):
  def get(self):
    return self.render('index.html', constants=constants)


logging.getLogger().setLevel(logging.DEBUG)
application = webapp2.WSGIApplication([
  webapp2.Route(r'/img', 'img.Img'),
  webapp2.Route(r'/proxy', 'main.ProxyHandler', 'proxy'),
  webapp2.Route(r'/twitter', webapp2.RedirectHandler, 'twitter', defaults={
    '_uri': 'https://twitter.com/%s' % constants.TWITTER_ID}),
  webapp2.Route(r'/ex.ua', webapp2.RedirectHandler, defaults={
    '_uri': 'http://ex.ua'}),
  webapp2.Route(r'/tumblr', webapp2.RedirectHandler, defaults={
    '_uri': 'http://tumblr.com'}),
  webapp2.Route(r'/+', webapp2.RedirectHandler, 'googleplus', defaults={
    '_uri': 'https://plus.google.com/+%s' % constants.GOOGLE_PLUS_ID}),
  webapp2.Route(r'/', 'main.HomeHandler', 'home'),
], debug=True)
