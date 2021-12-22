from django.contrib import admin

from .models import Status, Users, Shops, Items, Orders, OrderItems

admin.site.register(Status)
admin.site.register(Users)
admin.site.register(Shops)
admin.site.register(Items)
admin.site.register(Orders)
admin.site.register(OrderItems)
