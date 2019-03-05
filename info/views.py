from django.http import HttpResponse

from .models import Staff


DEFAULT_STAFF_ID = '00001216'


def info(request, id_):
    staff = Staff.objects.get(pk=id_)
    return HttpResponse(f'{staff.to_json()}')