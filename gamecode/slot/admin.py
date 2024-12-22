from django.contrib import admin
from .models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_auth_user', 'game_result')
    search_fields = ('id_auth_user__username',)
    list_filter = ('game_result',)