from django.http import HttpResponse

from .models import Staff


def info(request, id_):
    staff = Staff.objects.get(pk=id_)
    return HttpResponse(f'{staff.to_json()}')