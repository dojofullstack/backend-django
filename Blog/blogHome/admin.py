from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ArticulosBlog)
admin.site.register(Reporter)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)

admin.site.register(Publication)
admin.site.register(Newsletter)


