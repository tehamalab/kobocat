#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 coding=utf-8
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _, ugettext_lazy

from onadata.apps.restservice.models import RestService


class Command(BaseCommand):
    """
    A faster method is available with PostgreSQL:
        UPDATE restservice_restservice
            SET service_url = REGEXP_REPLACE(
                service_url,
                '/assets/([^/]*)/submissions/',
                '/assets/\1/hook-signal/'
            )
            WHERE service_url LIKE '/assets/%';
    """

    help = ugettext_lazy("Updates KPI rest service endpoint")

    def handle(self, *args, **kwargs):

        rest_services = RestService.objects.filter(name="kpi_hook").all()
        for rest_service in rest_services:
            service_url = rest_service.service_url
            if service_url.endswith("/submissions/"):
                service_url = service_url.replace("/submissions/", "/hook-signal/")
                rest_service.service_url = service_url
                rest_service.save(update_fields=["service_url"])

        print("Done!")
