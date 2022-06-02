from django.contrib import admin

# Register your models here.

from .models import Veiculo
admin.site.register(Veiculo)

from .models import Motorista
admin.site.register(Motorista)

from .models import Controle
admin.site.register(Controle)