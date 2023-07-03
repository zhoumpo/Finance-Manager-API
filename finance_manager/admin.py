from django.contrib import admin
from .models import Account, Bank, Category, Transaction


admin.site.register(Bank)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
