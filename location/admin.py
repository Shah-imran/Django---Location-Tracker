from django.contrib import admin
from django.forms import ModelForm, PasswordInput
from .models import *

class AccountForm(ModelForm):
    
    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
            'password': PasswordInput(),
        }

class AccountAdmin(admin.ModelAdmin):
    form =  AccountForm

admin.site.register(Location)
admin.site.register(Device)
admin.site.register(Account, AccountAdmin)