AUTHOR = 'Zhu Liang'
SITENAME = "lz's jottings"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
)

# Social widget
SOCIAL = (
    ("Twitter", "https://twitter.com/zleung"),
    # ("Instagram", "https://www.instagram.com/zleung9/"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

###########################################################################
THEME = './themes/pelican-blue'
SIDEBAR_DIGEST = 'LZ的随笔'

FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True

# TWITTER_USERNAME = 'zleung'

MENUITEMS = (
    ('HOME', "http://localhost:8000"),
)
DISPLAY_SUMMARY = False
DISPLAY_CONTENT = True