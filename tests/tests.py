import unittest
import os

import bandcamp_embed as bce

URL_ALBUM = 'http://topshelfrecords.bandcamp.com/album/lacuna'
BASE_URL = 'http://bandcamp.com'
ALBUM_ID = 1335340116
TITLE = 'Lacuna'
ARTIST_NAME = 'Caravels'

COLORS = {
    'red': 'f00',
    'green': '0f0',
    'blue': '00f'
}

class BandcampEmbedTestCase(unittest.TestCase):

    def test_theme(self):
        bg_color = '#fff'
        links_color = '#000'
        theme = bce.Theme(COLORS, bg_color, links_color)

        self.assertEqual(COLORS, theme.colors)
        self.assertEqual(bg_color.replace('#', ''), theme.bg_color)
        self.assertEqual(links_color.replace('#', ''), theme.links_color)

    def test_theme_links_color(self):
        links_color = 'blue'
        theme = bce.Theme(COLORS, '#fff', links_color)
        self.assertEqual(COLORS[links_color], theme.links_color)

    def test_color_incorrect(self):
        self.assertRaises(ValueError, lambda: bce.LightTheme('ggg'))

    def test_layout(self):
        size = 'large'
        width = height = '100px'

        layout = bce.Layout(size, width, height)
        self.assertEqual(size, layout.size)
        self.assertEqual(width, layout.width)
        self.assertEqual(height, layout.height)

    def test_build_album(self):
        theme = bce.LightTheme('orange')
        layout = bce.StandardLayout(tracklist=False)
        html = bce.build_player(URL_ALBUM, BASE_URL, ALBUM_ID, TITLE,
            ARTIST_NAME, layout, theme)

        with open('tests/album_standard_light_orange.html') as f:
            expected = f.read()
        expected = expected.strip()

        self.assertEqual(expected, html)

    def test_build_track(self):
        theme = bce.LightTheme('orange')
        layout = bce.StandardLayout(tracklist=False)
        html = bce.build_player(URL_ALBUM, BASE_URL, ALBUM_ID, TITLE,
            ARTIST_NAME, layout, theme, track_num=6)

        with open('tests/track_standard_light_orange.html') as f:
            expected = f.read()
        expected = expected.strip()

        self.assertEqual(expected, html)

if __name__ == '__main__':
    unittest.main()
