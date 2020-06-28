import os
from setuptools import setup, find_packages

TRAVIS_BUILD_VERSION = os.environ.get('TRAVIS_BUILD_NUMBER') or "0"
VERSION = f"1.0.{TRAVIS_BUILD_VERSION}"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "PyJWT >= 1.7.1", "cryptography >= 2.9.2"]

# To install the library, run the following
#
# python setup.py install

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name = 'authress-sdk',
  version = VERSION,
  description = 'Authress SDK for authorization as a service and interact with the Authress API.',
  author = 'Rhosys Developers',
  author_email = 'developers@authress.io',
  url = 'https://github.com/Authress/authress-sdk.py.git',
  include_package_data = True,
  install_requires=REQUIRES,
  packages=find_packages(),
  keywords = ['Authentication', 'Authorization', 'Authorization as a service', 'Security', 'Authress'],
  classifiers = [],
  long_description=long_description,
  long_description_content_type='text/markdown'
)
