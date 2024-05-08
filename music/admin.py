from django.contrib import admin
from .models import Vinyl, Label, Genre, Artist
# Register your models here.
admin.register(Vinyl)
admin.register(Label)
admin.register(Genre)
admin.register(Artist)
