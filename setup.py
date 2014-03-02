from setuptools import setup

import bandcamp_embed

setup(name='bandcamp-embed',
    version=bandcamp_embed.__version__,
    description='Renders HTML for embedded Bandcamp player.',
    author='Alexey Agapitov', author_email='marwinxxii@yandex.com',
    url='https://github.com/marwinxxii/bandcamp-embed',
    py_modules=['bandcamp_embed'],
    test_suite='tests'
    )
