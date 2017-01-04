[![PyPI version](https://badge.fury.io/py/django-indb-logger.svg)](https://badge.fury.io/py/django-indb-logger)

# INSTALLATION

* Add db_logger in **INSTALLED_APPS**

```
    INSTALLED_APPS += (
        "indb_logger",
    )
```

* Set LOGGING dict in **settings.py**,

For example, my logging settings:

```python
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'log_db': {
                'class': 'indb_logger.dbh.DBHandler',
                'expiry': 2,  # days
                'formatter': 'verbose',
                },
        },
        'loggers': {
            'django.request': {
                'handlers': ['log_db'],
                'level': 'WARNING',
                'propagate': True,
            },
        },
    }
```

# USAGE

* See how log entry adding in
    `http://yourproject.com/admin/indb_logger/generallog/`
* PROFIT
