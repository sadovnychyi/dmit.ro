import collections

NAME = 'Dmytro Sadovnychyi'
GITHUB_ID = 'sadovnychyi'
TWITTER_ID = 'sadovnychyi'
GOOGLE_PLUS_ID = 'DmitrySadovnychyi'
FACEBOOK_ID = 'sadovnychyid'
IMDB_ID = 'ur22646872'
INSTAGRAM_ID = 'sadovnychyi'
LINKEDIN_ID = 'sadovnychyi'
UPWORK_ID = '01c653ce808d695a28'
STACKOVERFLOW_ID = '1279005'

GITHUB_URL = 'https://github.com/{}'.format(GITHUB_ID)
TWITTER_URL = 'https://twitter.com/{}'.format(TWITTER_ID)
GOOGLE_PLUS_URL = 'https://plus.google.com/+{}'.format(GOOGLE_PLUS_ID)
FACEBOOK_URL = 'https://facebook.com/{}'.format(FACEBOOK_ID)
IMDB_URL = 'https://www.imdb.com/user/{}'.format(IMDB_ID)
INSTAGRAM_URL = 'https://instagram.com/{}'.format(INSTAGRAM_ID)
LINKEDIN_URL = 'https://linkedin.com/in/{}'.format(LINKEDIN_ID)
UPWORK_URL = 'https://www.upwork.com/users/~{}'.format(UPWORK_ID)
STACKOVERFLOW_URL = 'http://stackoverflow.com/users/{}'.format(STACKOVERFLOW_ID)

NETWORKS = collections.OrderedDict([
  ('GitHub', GITHUB_URL),
  ('Stack Overflow', STACKOVERFLOW_URL),
  ('Twitter', TWITTER_URL),
  ('Google+', GOOGLE_PLUS_URL),
  ('Facebook', FACEBOOK_URL),
  ('IMDb', IMDB_URL),
  ('Instagram', INSTAGRAM_URL),
  ('LinkedIn', LINKEDIN_URL),
  ('Upwork', UPWORK_URL),
])
