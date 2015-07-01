import sys

from travis_tox import generate

def main():
    generate.generate_tox_config(sys.stdout)
