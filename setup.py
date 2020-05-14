import os
from setuptools import setup, find_packages

TRAVIS_BUILD_VERSION = os.environ.get('TRAVIS_BUILD_NUMBER') or "0"
VERSION = f"1.0.{TRAVIS_BUILD_VERSION}"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

# To install the library, run the following
#
# python setup.py install

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
  download_url = f"https://github.com/Authress/authress-sdk.py/tarball/{VERSION}",
  keywords = ['Authentication', 'Authorization', 'Authorization as a service', 'Security', 'Authress'],
  classifiers = [],
  long_description="""\
  This is the Authress SDK used to integrate with the authorization as a service provider Authress at https://authress.io.
"""
)
