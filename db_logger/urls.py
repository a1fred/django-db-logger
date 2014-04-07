# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns

urlpatterns = patterns(
    'db_logger.views',
    url('^admin/db_logger/generallog/$',
        'show_last_log',
        name='show_last_log'),
    url('^admin/db_logger/generallog/(\d+)$', 'show_log', name='show_log'),
    url('^admin/db_logger/generallog/delete/(\d+)$',
        'delete_log',
        name='delete_log'),
)
