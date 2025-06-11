from django.urls import path
from . import views
from django.urls import path
# from .views import predict_view

urlpatterns = [
    path('', views.patients, name='patients'),
    # path('predict/', predict_view, name='predict'),
]
