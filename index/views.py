from django.http import HttpResponse


def index(request):
    url = request.build_absolute_uri() 
    response = HttpResponse(
        f'Please make an HTTP GET request to {url}info/&ltstaff_id&gt'
    )
    return response
