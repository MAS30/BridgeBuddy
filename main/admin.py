from django.contrib import admin

from .models import (
    Guide,
    CommunityPost,
    Comment,
    Phrase
)


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):

    list_display = ('title', 'category')


@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):

    list_display = ('title', 'user', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('user', 'post', 'created_at')


@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):

    list_display = (
        'english_text',
        'turkish_text',
        'category'
    )