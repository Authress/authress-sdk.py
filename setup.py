import os
from setuptools import setup, find_packages

REQUIRES = [
  "urllib3 >= 1.25.3, <= 2.2.2",
  "python-dateutil",
  "pydantic >= 1.10.5, < 3",
  "PyJWT >= 2.4.0",
  "cryptography >= 2.9.2",
  "aenum",
  "certifi >= 14.05.14",
  "python_dateutil >= 2.5.3"
]

# To install the library, run the following
#
# python setup.py install

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

with open(os.path.join(this_directory, 'authress', 'VERSION')) as version_file:
  VERSION = version_file.read().strip()

print("Building version", VERSION)

setup(
  name = 'authress',
  version = VERSION,
  description = 'Authress SDK for authorization as a service and interact with the Authress API.',
  author = 'Authress Developers',
  author_email = 'developers@authress.io',
  url = 'https://github.com/Authress/authress-sdk.py.git',
  include_package_data = True,
  package_data={"authress": ["py.typed"]},
  install_requires=REQUIRES,
  packages = find_packages(exclude=['test', 'tests', 'tests_integration']),
  data_files=[('', ['authress/VERSION'])],
  keywords = ['Authorization as a service', 'Security', 'authorization', 'authorization as a service', 'authentication', 'user authentication', 'Authress', 'Authress client', 'access management', 'access management as a service', 'user security', 'oso', 'polar', 'open source policy engine', 'embedded authorization', 'batteries included authorization', 'verified', 'verified access', 'verified permissions'],
  classifiers = [],
  license = 'Apache-2.0',
  long_description=long_description,
  long_description_content_type='text/markdown'
)