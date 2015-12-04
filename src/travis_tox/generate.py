from __future__ import unicode_literals, print_function

from tox.config import parseconfig


def generate_tox_config(fileobj):

    def print_(text):
        print(text, file=fileobj)

    print_('language: python')
    print_('python: 3.5')
    print_('env:')
    for env in parseconfig().envlist:
        print_('  - TOX_ENV={env}'.format(env=env))
    print_('install:')
    print_('  - pip install tox')
    print_('script:')
    print_('  - tox -e $TOX_ENV')
