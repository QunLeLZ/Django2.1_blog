from django.contrib import admin
from blog.models import Category,Tag,Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
    summernote_fields = ('body',)

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)