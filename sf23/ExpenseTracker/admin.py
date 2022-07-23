from django.contrib import admin


# Register your models here.
from ExpenseTracker import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','amount','date','remarks')

		#this name function is used to generate the name, as u'll see in the output later
    def name(self,obj):
        return obj
admin.site.register(models.ExpenseRecords, AuthorAdmin)