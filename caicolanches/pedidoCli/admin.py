from django.contrib import admin

from .models import Cliente
from .models import Endereco
from .models import Produto

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Produto)
