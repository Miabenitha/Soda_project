from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('allsoda', views.soda_list),
    path('allsoda/<int:id>', views.soda_detail)
]
urlpatterns = format_suffix_patterns(urlpatterns)