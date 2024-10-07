from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "user_name", "first_name", "last_name", "email", "password", "phone_number", "date_of_birth", "gender", "status", "email_verified", "subscription_type", "country", "created_at", "updated_at"]

admin.site.register(User, UserAdmin)