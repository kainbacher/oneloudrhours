# -*- coding: utf-8 -*-

from main.models import Task, Category, Rate
from django.contrib import admin
from django.contrib.auth.models import User
from actions import export_as_csv



class TaskAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        
        try:
            formuser = obj.user
        except:
            formuser = ''
            
        aktuser = request.user
    
        print formuser
        print aktuser

        if formuser == '':
            obj.user = request.user
            obj.save()
            print "no user"
        elif formuser == aktuser:
            print "user ist akt user"
            obj.save()
        else:
            print "formuser ist anderst als akt user nicht speichern"
            return False
        

    exclude = ['user',]
    actions = [export_as_csv]
	 
#    filter_horizontal = ('title',)
    list_display = ('user', 'title', 'date', 'hours', 'rate', 'amount')
    list_filter = ('user', 'category', 'rate')
    list_display_links = ['user', 'title',]
#	ordering = ('date',)
    search_fields = ('user', 'title')
    date_hierarchy = 'date'

    def amount(self, form):
        rate = form.rate.rate
        hours = form.hours
    
        return str(rate*hours)
    amount.allow_tags = True


admin.site.register(Task, TaskAdmin)




class CategoryAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        if getattr(obj, 'added_by', None) is None:
#            obj.added_by = request.user
#        obj.last_modified_by = request.user
#        obj.save()

#    exclude = ['added_by', 'last_modified_by']
    actions = [export_as_csv]
	 
#    filter_horizontal = ('members', )
    list_display = ('title', 'max_budget',)
#	list_display_links = ['last_name', 'first_name',]
#	ordering = ('last_name', 'first_name')
#	search_fields = ('first_name', 'last_name')

admin.site.register(Category, CategoryAdmin)





class RateAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        if getattr(obj, 'added_by', None) is None:
#            obj.added_by = request.user
#        obj.last_modified_by = request.user
#        obj.save()

#    exclude = ['added_by', 'last_modified_by']
    actions = [export_as_csv]
	 
#    filter_horizontal = ('members', )
    list_display = ('title', 'rate',)
#	list_display_links = ['last_name', 'first_name',]
#	ordering = ('last_name', 'first_name')
#	search_fields = ('first_name', 'last_name')

admin.site.register(Rate, RateAdmin)

