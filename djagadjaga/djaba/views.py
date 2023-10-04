from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Djaba, Owner, Category


# Create your views here.

class DjabaView(View):
    """"Список жаб"""

    def get(self, request):
        djabas = Djaba.objects.all()
        return render(request, "djabas/djaba_list.html", {"djaba_list": djabas, "title": "привет"})


class DjabaOwner(View):
    """"Хозяин жабы"""
    def get(self, request, pk, djaba_name):
        owner = Owner.objects.get(id=pk)
        return render(request, "djabas/owners.html", {
            "djaba_name": djaba_name,
            "name": owner.name,
            "surname": owner.surname,
            "age": owner.age,
            "image": owner.image
        })

class ListCategory(ListView):
    model = Category #если хотим все объекты(?)
    #queryset = по умолчанию Category.objects.all(), можно поменять например Category.objects.filter(name=sasaddas)
    template_name = "djabas/category_list.html"

# class CategoryDetailView(DetailView):
#     model = Category
#     slug_field = "name"
#     template_name = "djabas/category.html"