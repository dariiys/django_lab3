from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index),                              # http://127.0.0.1:8000
    path('comedy/<int:comed_id>/', views.categories),  # http://127.0.0.1:8000/comedy/2/
    path('comedy/<slug:comed_slug>/', views.categories_by_slug),  # http://127.0.0.1:8000/comedy/gfgfdgd/
    path('about/', views.about, name ='about'),
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
]