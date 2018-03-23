# ![](https://i.imgur.com/CzNa1DQ.png)

## SETUP

Install required packages:
```
pip3 install -r requirements/dev.txt
```

Initialize database:
```
python3 manage.py migrate
```

## Fixtures

load books and accounts  data
```
sh scripts/load_data.sh
```

## Authentication

`/login`:
Admin account:
    email: admin@admin.com
    password: pass1234

Manager account:
    email: manager@manager.com
    password: pass1234
   
