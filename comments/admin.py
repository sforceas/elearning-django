from django.contrib import admin

# Register your models here.
from .models import Comment,AnswerComment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'created', 'active_flag')
    list_filter = ('active_flag', 'created', 'updated')
    search_fields = ('user', 'comment')

@admin.register(AnswerComment)
class AnswerCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created', 'active_flag')
    list_filter = ('active_flag', 'created', 'updated')
    search_fields = ('user', 'comment')