# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
import models


def show_last_log(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    try:
        lastLog = models.GeneralLog.objects.all().order_by("-time")[0]
    except IndexError:
        return HttpResponse(
            "<body style='text-align:center;'><h1><br/>Всее!</h1></body>")
    return HttpResponseRedirect(reverse("show_last_log")+str(lastLog.pk))


def show_log(request, logId):
    if not request.user.is_superuser:
        raise PermissionDenied
    log = models.GeneralLog.objects.get(pk=logId)
    c = RequestContext(request)
    return render_to_response(
        "lastlog.html", locals(), context_instance=c)


def delete_log(request, logId):
    if not request.user.is_superuser:
        raise PermissionDenied
    try:
        log = models.GeneralLog.objects.get(pk=logId)
        log.delete()
    except models.GeneralLog.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse("show_last_log"))
