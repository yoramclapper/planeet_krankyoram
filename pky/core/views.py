from django.shortcuts import redirect
from django.views.generic import TemplateView


def home(request):
    return redirect("index")


class IndexView(TemplateView):
    template_name = "core/index.html"
