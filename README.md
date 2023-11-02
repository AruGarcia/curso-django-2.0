# curso-django-2.0

## DevPro Course Repository

This repository is a part of the DevPro course, and it contains a complete application built using the Django framework.

## Project Dependencies

| Package               | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| Django                | Python web framework                                          |
| Gunicorn              | Python WSGI HTTP server for Django applications               |
| python-decouple       | Python library for separating settings from code             |
| dj-database-url       | Django database connection URL                                |
| psycopg2-binary       | PostgreSQL adapter for Python                                 |
| django-s3-folder-storage | Storage backend for Django that uses Amazon S3          |
| collectfast           | Django storage backend for speeding up `collectstatic`       |
| django-debug-toolbar  | Set of panels to display debug information about requests     |
| sentry-sdk            | Real-time error tracking and monitoring                      |
| storage               | Abstract storage class for Django                             |
| django-ordered-model  | Mixin for the Django ORM                                      |
| django-extensions     | Custom extensions for the Django Framework                   |
| ipython               | Interactive command-line shell for Python                     |

## Development Dependencies

| Package       | Description                                       |
|---------------|---------------------------------------------------|
| flake8        | Tool for enforcing code style and quality       |
| pytest-django  | Django plugin for pytest                         |
| pytest-cov    | Coverage plugin for pytest                       |
| codecov       | Platform for code coverage                        |
| model-bakery  | Smart object creator for Django                   |

## Requirements

- Python version: 3.11

This project represents my first foray into web development. The entire application has been thoroughly tested using continuous integration and continuous deployment (CI/CD) through GitHub Actions. Code coverage is monitored using Codecov, and error tracking and monitoring are implemented through Sentry. The project uses a PostgreSQL database, and the site is deployed on Heroku.

Feel free to explore the code and the various components of this project. If you have any questions or feedback, please don't hesitate to reach out.

About me: https://www.linkedin.com/in/aruana-garcia/

Application available at: https://pythonpro-project-6011015b2aca.herokuapp.com/

[![codecov](https://codecov.io/gh/AruGarcia/curso-django-2.0/branch/main/graph/badge.svg?token=IO77OWW680)](https://codecov.io/gh/AruGarcia/curso-django-2.0)