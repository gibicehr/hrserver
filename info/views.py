from django.http import HttpResponse

from .models import Staff


DEFAULT_STAFF_ID = '00001216'


def info(request, id_):
    try:
        staff = Staff.objects.get(pk=id_)
        response = HttpResponse(f'{staff.to_json()}')
    except Staff.DoesNotExist:
        response = HttpResponse('Invalid staff ID')
    return response