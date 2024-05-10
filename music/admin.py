from django.contrib import admin
from .models import Vinyl, Label, Genre, Artist, Track
# Register your models here.
admin.site.register(Vinyl)
admin.site.register(Label)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Track)
