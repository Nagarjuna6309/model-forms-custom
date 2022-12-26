from django.contrib import admin

# Register your models here.
from app.models import *
class Topic_costumview(admin.ModelAdmin):
    list_display=('topic_name',)


class Webpages_view(admin.ModelAdmin):
    list_display=('topic_name','name','url')
    
    
class Access_view(admin.ModelAdmin):
    list_display=('topic_name','date')

admin.site.register(Topic,Topic_costumview)
admin.site.register(Webpage,Webpages_view)
admin.site.register(AccessRecord,Access_view)
