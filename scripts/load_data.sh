#!/bin/bash


python manage.py loaddata app/accounts/fixtures/user.json



python manage.py loaddata app/store/fixtures/author.json
python manage.py loaddata app/store/fixtures/book.json
