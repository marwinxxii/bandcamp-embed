__version__ = '0.1.0'

COMMON_COLORS = {
    'blue': '0687f5',
    'orange': 'e99708',
    'green': '2ebd35',
    'violet': '7137dc',
    'pink': 'f171a2',
    'greyblue': '63b2cc',
    'red': 'de270f'
}
COLOR_DARK = '333333'
COLOR_WHITE = 'ffffff'

class Theme:
    def __init__(self, colors, bg_color, links_color):
        self.colors = colors
        self.bg_color = bg_color.replace('#', '')
        if links_color in self.colors:
            self.links_color = self.colors[links_color]
        elif links_color.startswith('#'):
            self.links_color = links_color.replace('#', '')
        else:
            raise ValueError('Unknown links color: %s' % links_color)

class LightTheme(Theme):
    COLORS = dict(COMMON_COLORS, dark=COLOR_DARK)
    def __init__(self, links_color):
        Theme.__init__(self, self.COLORS, COLOR_WHITE, links_color)

class DarkTheme(Theme):
    COLORS = dict(COMMON_COLORS, white=COLOR_WHITE)
    def __init__(self, links_color):
        Theme.__init__(self, self.COLORS, COLOR_DARK, links_color)

class Layout:
    def __init__(self, size, width, height):
        self.size = size
        if isinstance(width, int):
            width = '%dpx' % width
        if isinstance(height, int):
            height = '%dpx' % height
        self.width = width
        self.height = height

    def args(self):
        return None

class StandardLayout(Layout):
    SIZE = 'large'
    def __init__(self, tracklist):
        self.tracklist = tracklist
        Layout.__init__(self, self.SIZE, width=350, height=470)

    def args(self):
        if self.tracklist:
            return Layout.args(self)
        return 'tracklist=false'

class MinimalLayout(Layout):
    SIZE = 'large'
    def __init__(self):
        Layout.__init__(self, self.SIZE, width=350, height=350)

class HorizontalLayout(Layout):
    SIZE = 'medium'
    def __init__(self, artwork):
        self.artwork = artwork
        Layout.__init__(self, self.SIZE, width='100%', height=120)

    def args(self):
        if self.artwork:
            return Layout.args(self)
        return 'artwork=false'

class SmallLayout(Layout):
    SIZE = 'small'
    def __init__(self, artwork):
        self.artwork = artwork
        Layout.__init__(self, self.SIZE, width='100%', height=42)

    def args(self):
        if self.artwork:
            return Layout.args(self)
        return 'artwork=false'

IFRAME_START = '<iframe style="{style}" src="{src}" seamless>'
STYLE = 'border: 0; width: {width}; height: {height};'
SRC = '{base_url}/EmbeddedPlayer/album={album_id}/size={size}/bgcol={bg_color}/linkcol={links_color}/{args}{track}transparent=true/'
IFRAME_END = '</iframe>'
A_ELEM = '<a href="{href}">{title} by {artist_name}</a>'

def build_player(url, base_url, album_id, title, artist_name,
    layout, theme, track_num=None):
    style = STYLE.format(width=layout.width, height=layout.height)

    track = ''
    if track_num:
        track = 't=%d/' % track_num

    args = layout.args()
    if args is None:
        args = ''
    else:
        args = '%s/' % args

    src = SRC.format(base_url=base_url,
        album_id=album_id,
        size=layout.size,
        bg_color=theme.bg_color,
        links_color=theme.links_color,
        args=args,
        track=track)

    return ''.join([IFRAME_START.format(style=style, src=src),
        A_ELEM.format(href=url, title=title, artist_name=artist_name),
        IFRAME_END])
