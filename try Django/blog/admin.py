from django.contrib import admin

# Register your models here.
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
	summernote_fields = '__all__'


admin.site.register(BlogPost,PostAdmin)