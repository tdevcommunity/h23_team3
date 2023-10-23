# admin.py

from django.contrib import admin
from django.core.mail import send_mail
from .models import Members, Users


class MembersAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentore', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    actions = ['accept_requests', 'reject_requests']

    def accept_requests(self, request, queryset):
        queryset.update(status=True)
        for membership in queryset:
            # Envoyer un e-mail à l'utilisateur mentore
            subject = "Demande de mentorat acceptée"
            message = "Votre demande de mentorat a été acceptée. Vous pouvez maintenant commencer le mentorat."
            from_email = "tdev@gmail.com"
            recipient_list = [membership.mentore.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    accept_requests.short_description = "Accepter les demandes de mentorat sélectionnées"

    def reject_requests(self, request, queryset):
        queryset.delete()

    reject_requests.short_description = "Rejeter les demandes de mentorat sélectionnées"


admin.site.register(Members, MembersAdmin)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')

    def mentors_count(self, obj):
        return Users.objects.filter(is_staff=True).count()

    mentors_count.short_description = "Nombre de Mentors"

    def mentores_count(self, obj):
        return Users.objects.filter(is_staff=False).count()

    mentores_count.short_description = "Nombre de Mentores"


admin.site.register(Users, UsersAdmin)
