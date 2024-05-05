from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Регистрация модели позователя в Админ-панели
    """
    list_display = ('id',  'chat_id', 'first_name', 'last_name', 'email', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)
