from django.contrib import admin
from .models import loginpage
from .forms import SignUpForm
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(loginpage)

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    add_fieldsets = ((None, {'classes': ('wide',), 'fields':('username', 'first_name', 'last_name', 'email', 'password1', 'password2')}),)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(form.cleaned_data["password1"])
        return super().save_model(request, obj, form, change)
    
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)