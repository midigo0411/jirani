from django.urls import path
from .import views


urlpatterns = [

    path('',views.index,name="index"),
    path('<int:jobs_id>',views.detail,name="detail"),
]