Add db_logger in INSTALLED_APPS

`
INSTALLED_APPS += (
    "db_logger",
)
`

My logging settings:
`
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
            'class': 'db_logger.dbh.DBHandler',
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
`
