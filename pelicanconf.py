import os

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




################################    THEMES    ##################################

######################### theme: pelican-blue ##################################
# How to setup custom font: https://egghead.io/lessons/css-use-a-custom-font-from-google-fonts-on-a-static-html-webpage
# How to customize your font: https://scalablecss.com/setup-custom-fonts-with-font-face/
THEME = './themes/pelican-blue'
SIDEBAR_DIGEST = 'LZ的随笔'
FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
    ('HOME', "http://localhost:8000"),
)
DISPLAY_SUMMARY = False
DISPLAY_CONTENT = True

########################## theme: pelican-bootstrap3 ###########################
# Please read README.md before using this template
# Article on how to customize this them: http://habeebq.github.io/customizing-the-blog.html
# THEME = 'themes/pelican-bootstrap3'
# PLUGIN_PATHS = ['./plugins']
# PLUGINS = ['i18n_subsites', 'bootstrapify']
# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# BOOTSTRAP_THEME = 'readable'
# PYGMENTS_STYLE  = 'monokai'
# # Navbar
# DISPLAY_CATEGORIES_ON_MENU = False 
# # SIDEBAR
# HIDE_SIDEBAR = True 
# # Article Header
# SHOW_ARTICLE_AUTHOR = True
# SHOW_ARTICLE_CATEGORY = True
# SHOW_DATE_MODIFIED = True
# # Bootstrap extra css
# # CUSTOM_CSS = os.path.join(THEME, 'static/css/custom.css')
# CUSTOM_CSS = "./themes/pelican-bootstrap3/static/css/custom.css"
# GOOGLEFONT = 'https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@100;300&display=swap'