from django.contrib import admin
from .models import Call


class PhoneNumberFilter(admin.SimpleListFilter):
    title = 'Phone Number'
    parameter_name = 'phone_number'

    def lookups(self, request, model_admin):
        phone_numbers = set([call.phone_number for call in model_admin.model.objects.all()])
        return [(phone_number, phone_number) for phone_number in phone_numbers]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(phone_number=self.value())
        return queryset


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    search_fields = ['phone_number']
    list_filter = (PhoneNumberFilter,)
