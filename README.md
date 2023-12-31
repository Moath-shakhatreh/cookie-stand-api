```
LAB - Class 34
Project: Putting it All Together
Author: Mo'ath shakhatreh

Links and Resources
back-end server url (when applicable)
http://127.0.0.1:8000/api/v1/CookieStands/

front-end application (when applicable)
Setup
.env requirements (where applicable)
[s](./requirements.txt)

PORT - 8000
DATABASE_URL - URL to the running Postgres instance/db
postgres://geetqygj:b6xxmWw99yI38kWfOhzMqNeZ0GcKzBMH@drona.db.elephantsql.com/geetqygj

```









# api-quick-start

Template Project for starting up CRUD API with Django Rest Framework

## Customization Steps

- DO NOT migrate yet
- add additional dependencies as needed
  - Re-export requirements.txt as needed
- change `CookieStands` folder to the app name of your choice
- Search through entire code base for `CookieStand`,`CookieStands` and `CookieStands` to modify code to use your resource
  - `project/settings.py`
  - `project/urls.py`
  - App's files
    - `views.py`
    - `urls.py`
    - `admin.py`
    - `serializers.py`
    - `permissions.py`
  - "Front" files
    - if including a customer facing portion of the site then update/recreate:
      - `urls_front.py`
      - `views_front.py`
      - template files
      - Make sure to update project `urls.py` to add routes to the "front".
- Update CookieStandModel with fields you need
  - Make sure to update other modules that would be affected by Model customizations. E.g. serializers, tests, etc.
- Rename `project/.env.sample` to `.env` and update as needed
  - To generate secret key use `python3 -c "import secrets; print(secrets.token_urlsafe())"`
- Run makemigrations and migrate commands when ready.
- Run `python manage.py collectstatic`
  - This repository includes static assets in repository. If you are using a Content Delivery Network then remove `staticfiles` from repository.
- Optional: Update `api_tester.py`

## Database

**NOTE:** If you are using Postgres instead of SQLite then make sure to install `psycopg2-binary` and include in `requirements.txt`
