
<p align="center">
    <img src="https://github.com/Authress/authress-local/assets/5056218/156e3881-b359-4810-bc96-7abeaf9ddbdb" height="300px" alt="Authress Media Banner">
</p>

# Authress SDK for Python

This is the Authress SDK for Python. Authress provides an authorization API for user identity, access control, and api key management as a drop in SaaS.

The Nuget package connects to the [Authress API](https://authress.io/app/#/api). You can use Authress to build authentication and authorization directly into your applications and services. Additionally, Authress can be used locally to develop faster without needing an [Authress Account](https://authress.io).

<p align="center">
    <a href="https://badge.fury.io/py/authress" alt="Authress pypi package">
        <img src="https://badge.fury.io/py/authress.svg">
    </a>
    <a href="https://github.com/Authress/authress-sdk.py/actions/workflows/build.yml" alt="Build status">
      <img src="https://github.com/Authress/authress-sdk.py/actions/workflows/build.yml/badge.svg">
    </a>
    <a href="./LICENSE" alt="Apache-2.0">
      <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg">
    </a>
    <a href="https://authress.io/community" alt="authress community">
      <img src="https://img.shields.io/badge/Community-Authress-fbaf0b.svg">
    </a>
</p>

## Usage

```sh
pip install authress
```
(you may need to run `pip` with root permission: `sudo pip install authress`)

Then import the package:
```python
import authress
```

## Getting Started


### Reference Guide

See the SDK reference guide for a examples of commonly executed blocks with descriptions.

[SDK Documentation](./docs/README.md)


## Quick Examples:

* [Authorize using a user token](./docs/EXAMPLES.md)
* [Authorize with a service client](./docs/EXAMPLES.md)
* [Using the Authress service client as an API key](./docs/EXAMPLES.md)
* [Embedding service clients into your api](./docs/EXAMPLES.md)
* [Token verification](./docs/EXAMPLES.md)

## Contribution Guide

[Developing for the Python SDK](./contributing.md)