from django.contrib import admin
from .models import Members
from .models import Users
from .forms import CustomUserCreationForm


# class MembersAdmin(admin.ModelAdmin):
#     list_display = ('mentor', 'mentore', 'status', 'created_at', 'updated_at')
#     list_filter = ('mentor', 'mentore')
#     actions = ['accept_requests', 'reject_requests']
#
#     def accept_requests(self, request, queryset):
#         for member in queryset:
#             member.status = True
#             member.save()
#
#     accept_requests.short_description = "Accepter les demandes sélectionnées"
#
#     def reject_requests(self, request, queryset):
#         for member in queryset:
#             member.status = False
#             member.save()
#
#     reject_requests.short_description = "Rejeter les demandes sélectionnées"
#
#     def get_actions(self, request):
#         actions = super().get_actions(request)
#         if 'delete_selected' in actions:
#             del actions['delete_selected']
#         return actions
#
#
# admin.site.register(Members, MembersAdmin)


class UsersAdmin(admin.ModelAdmin):
    form = CustomUserCreationForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if form.cleaned_data.get('is_mentor'):
            # L'utilisateur est ajouté en tant que mentor
            obj.mentor.add(obj)
        if form.cleaned_data.get('is_mentore'):
            # L'utilisateur est ajouté en tant que mentore
            obj.mentore.add(obj)


admin.site.register(Users, UsersAdmin)