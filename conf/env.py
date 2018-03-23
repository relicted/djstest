ENVIRONMENT = 'dev'
# ENVIRONMENT = 'prod'


if ENVIRONMENT == 'dev':
    SETTINGS_FILE = 'conf.settings.dev'
elif ENVIRONMENT == 'prod':
    SETTINGS_FILE = 'conf.settings.prod'
