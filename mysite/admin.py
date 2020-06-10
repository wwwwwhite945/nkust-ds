from django.contrib import admin
from mysite import models

class StroyAdmin(admin.ModelAdmin):
	list_display = ('sno','content')

admin.site.register(models.Story,StroyAdmin) #將資料表註冊到後台