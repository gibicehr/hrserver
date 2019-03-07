from django.http import HttpResponse


def index(request):
    url = request.build_absolute_uri()
    base_url = '/'.join(url.split('/')[:3] + [''])
    response = HttpResponse(
        f'Please make an HTTP GET request to {base_url}info/&ltstaff_id&gt'
    )
    return response
