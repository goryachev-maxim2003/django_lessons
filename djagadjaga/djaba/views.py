from django.shortcuts import render
from django.views.generic.base import View

from .models import Djaba
# Create your views here.

class DjabaView(View):
    """"Список жаб"""
    def get(self, request):
        djabas = Djaba.objects.all()
        return render(request, "djabas/djaba_list.html", {"djaba_list": djabas, "title": "привет"})
