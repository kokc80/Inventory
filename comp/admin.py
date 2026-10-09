from django.contrib import admin
from .models import Comp


# показать явные конкретные поля
@admin.register(Comp)
class CompAdmin(admin.ModelAdmin):
    list_display = ['c_name', 'c_ddr', 'c_hdd', 'c_os', 'c_install']
    # показать все поля ???
    # list_display = [field.name for field in Comp._meta.get_fields()]
    list_filter = ("c_name", "c_os", "c_ddr",)
    search_fields = ("c_name", "c_os",)
    ordering = ("c_name", "c_install",)

# # показать все поля
# @admin.register(Comp)
# class CompAdmin(admin.ModelAdmin):
#     def get_list_display(self, request):
#         # берём только «реальные» поля модели, исключая обратные связи
#         return [
#             f.name for f in self.model._meta.get_fields()
#             if f.concrete and not f.auto_created and not f.many_to_one and not f.one_to_many
#         ]
#
#     list_filter = ("c_os", "c_ddr",)
#     search_fields = ("c_name", "c_os",)
#     ordering = ("c_name",)
