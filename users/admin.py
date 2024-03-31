from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from users.models import User

#admin.site.register(User)
@admin.register(User)
class UsesrAdmin(admin.ModelAdmin):
    list_display = ["username","first_name", "last_name", "email"]
    search_fields = ["username","first_name", "last_name", "email"]

    inlines = [CartTabAdmin, OrderTabularAdmin]