from django.urls import path
from pedidoCli.views import IndexTemplateView
from . import views

app_name = 'pedidoCli'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
]
