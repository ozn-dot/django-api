from django.contrib import admin
from .models import Note, User

# Registramos nuestros modelos aquí para poder administrarlos desde el panel admin de django

admin.site.register([Note, User])
