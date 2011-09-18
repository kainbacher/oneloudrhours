from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

    created = models.DateTimeField('Created', auto_now_add = True)
    modified = models.DateTimeField('Modified', auto_now = True)
   
    title = models.CharField(max_length=30, blank=True, verbose_name='Title')
    description = models.TextField(blank=True, null=True)    
    max_budget = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)    
    
    def __unicode__(self):
        return u'%s' % (self.title)






class Rate(models.Model):
    class Meta:
        verbose_name = 'Rate'
        verbose_name_plural = 'Rate'
        ordering = ['title']

    created = models.DateTimeField('Created', auto_now_add = True)
    modified = models.DateTimeField('Modified', auto_now = True)
   
    title = models.CharField(max_length=30, blank=True, verbose_name='Title')
    rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)    
    
    def __unicode__(self):
        return u'%s (%s EUR)' % (self.title, self.rate)




class Task(models.Model):
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['title']

    created = models.DateTimeField('Created', auto_now_add = True)
    modified = models.DateTimeField('Modified', auto_now = True)

    title = models.CharField(max_length=30, blank=True, verbose_name='Title')
    description = models.TextField(blank=True, null=True)

    date = models.DateField() 
	    
    category = models.ForeignKey(Category)
    
    hours = models.DecimalField(max_digits=5, decimal_places=2)    
    rate = models.ForeignKey(Rate)
    
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return u'%s' % (self.title)



