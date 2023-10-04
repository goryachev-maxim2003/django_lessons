from django.urls import path

from . import views

urlpatterns = [
    path("", views.DjabaView.as_view()),
    path("<str:djaba_name>/<int:pk>/", views.DjabaOwner.as_view(), name = "jaba_owner"),
    path("category_list", views.ListCategory.as_view()),
    # path("category_list/<slug:slug>", views.CategoryDetailView.as_view(), name='post-detail')
]