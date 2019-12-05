from django.contrib import admin

from .models import Estabelecimento
from .models import Endereco

admin.site.register(Estabelecimento)
admin.site.register(Endereco)