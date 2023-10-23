from django.utils import timezone
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
    list_display = ('get_user_count', 'get_user_count_by_gender', 'display_all_users', 'duration_since_creation', 'email',)
    list_display_links = ('email',)  # Lien direct vers la page de modification
    search_fields = ("first_name", "email")

    actions = ['edit_selected', 'delete_selected']

    def get_user_count(self, obj):
        # Comptez le nombre total d'utilisateurs
        total_users = Users.objects.count()
        return f'Total Users: {total_users}'

    def get_user_count_by_gender(self, obj):
        # Comptez le nombre d'utilisateurs par sexe
        male_count = Users.objects.filter(sexe='Male').count()
        female_count = Users.objects.filter(sexe='Female').count()
        return f'Male: ({male_count})  <--->  Female: ({female_count})'

    def display_all_users(self, obj):
        # Récupérez la liste complète des utilisateurs
        all_users = Users.objects.all()
        user_list = [f"{user.email}" for user in all_users]
        return ', '.join(user_list)

    def duration_since_creation(self, obj):
        now = timezone.now()
        duration = now - obj.created_at
        return duration.days

    duration_since_creation.short_description = 'Duration Since Creation'
    display_all_users.short_description = 'All Users'
    get_user_count.short_description = 'Total Users'
    get_user_count_by_gender.short_description = 'Users by Gender'


admin.site.register(Users, UsersAdmin)
