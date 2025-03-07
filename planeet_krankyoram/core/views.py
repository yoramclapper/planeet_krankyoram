from django.views.generic import ListView
from .models import AppsLib


class IndexView(ListView):
    context_object_name = "my_apps"
    queryset = AppsLib.objects.filter(show=True)
    template_name = "core/index.html"
