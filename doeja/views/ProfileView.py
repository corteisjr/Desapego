from django.http import HttpResponse


def list_profile_view(request):
    return HttpResponse('<h1>Perfil do usuario</h1>')