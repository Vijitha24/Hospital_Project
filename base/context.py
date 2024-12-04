from django.db import models
from base.models import *


def default(request):
    services = Service.objects.all()

    return {
        "services": services
    }