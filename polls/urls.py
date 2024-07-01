from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
]
"""path()
Args: 
    path(route, view, kwargs=None, name=None)
      route: string, URL pattern. 
        When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.
        Patterns don’t search GET and POST parameters, or the domain name. For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/. In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.
      view: callable, view function or view class
      name: string. Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.

Returns: 
    URLPattern
"""