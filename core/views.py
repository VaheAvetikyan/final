from django.shortcuts import render

# Translate
from django.utils.translation import gettext as _

# Create your views here.
def index(request):

    user = request.user
    context = {
        "menu": _("Menu"),
        "user": user
    }

    return render(request, "core/index.html", context)