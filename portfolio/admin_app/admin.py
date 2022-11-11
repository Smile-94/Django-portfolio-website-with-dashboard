from django.contrib import admin
from admin_app.models import Message
from admin_app.models import Skills
from admin_app.models import Education
from admin_app.models import Expriences


# Register your models here.
admin.site.register(Message)
admin.site.register(Expriences)
admin.site.register(Education)
admin.site.register(Skills)
