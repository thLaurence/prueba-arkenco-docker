from django.contrib import admin
from .models import Cliente, Usuario, estado, etapa
# Register your models here.

admin.site.register(Cliente);
admin.site.register(Usuario);
admin.site.register(estado);
admin.site.register(etapa);