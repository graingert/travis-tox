import io

from travis_tox import generate

example = """language: python
python: 3.5
env:
  - TOX_ENV=py26
  - TOX_ENV=py27
  - TOX_ENV=py33
  - TOX_ENV=py34
  - TOX_ENV=py35
  - TOX_ENV=lint
install:
  - pip install tox
script:
  - tox -e $TOX_ENV
"""


def test_this_package():
    fileobj = io.StringIO()
    generate.generate_tox_config(fileobj)
    assert fileobj.getvalue() == example
