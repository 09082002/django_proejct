from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Persons)

admin.site.register(National)

admin.site.register(Medical)

admin.site.register(Post1)

# admin.site.register(Userinfos)
#
admin.site.register(Postusers)






