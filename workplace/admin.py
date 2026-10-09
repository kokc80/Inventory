from django.contrib import admin
from .models import Workplace


# показать все поля
@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        # берём только «реальные» поля модели, исключая обратные связи
        return [
            f.name
            for f in self.model._meta.get_fields()
            if f.concrete and not f.auto_created and not f.many_to_one and not f.one_to_many
        ]

    search_fields = ["w_worker", "w_hostname"]
