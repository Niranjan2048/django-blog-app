from django.contrib import admin
from .models import Post , CommentModel

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'status','created_on', 'image')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('your_name','comment_text','blog')
    list_filter = (('blog',admin.RelatedOnlyFieldListFilter),)
    search_fields = ['your_name']
admin.site.register(CommentModel, CommentAdmin)




