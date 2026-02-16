from django.contrib import admin

from core.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(RecurringTransaction)
admin.site.register(Goal)
