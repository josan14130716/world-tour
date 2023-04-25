from django.contrib import admin
from .models import Trip

admin.site.site_header = " Let's tour the world"
admin.site.site_title = " World Tour "
admin.site.index_title = " Welcome to the World "

# Register your models here.


admin.site.register(Trip)
