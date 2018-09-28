from django.contrib import admin

from periject.proj.models import Choice
from periject.proj.models import ContactDetails
from periject.proj.models import Department
from periject.proj.models import Question 

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Department)
admin.site.register(ContactDetails)



# Register your models here.
