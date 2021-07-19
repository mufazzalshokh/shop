from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from posts.models import AuthorModel, PostModel, PostTagModel, CommentModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(PostTagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(TranslationAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['author', 'tags']


class Media:
    js = (
        'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        'modeltranslation/js/tabbed_translation_fields.js',
    )
    css = {
        'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    }


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
