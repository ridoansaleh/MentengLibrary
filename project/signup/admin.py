from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Visitor, Book

class VisitorInline(admin.StackedInline):
    model = Visitor
    can_delete = False
    verbose_name_plural = 'Visitor'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (VisitorInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Book)
