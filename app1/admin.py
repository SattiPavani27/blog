# myapp/admin.py
from django.contrib import admin
from app1.models import Contact
from app1.models import Login_details
from app1.models import Registration
from app1.models import Posts
from app1.models import TextCheck


admin.site.register(Contact)
admin.site.register(Login_details)
admin.site.register(Registration)
admin.site.register(Posts)
admin.site.register(TextCheck)




