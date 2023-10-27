from django.utils import timezone
from django.contrib import admin
from django.core.mail import send_mail
from Account.models import Users, Members
from Resource.models import Type
from django.utils.translation import gettext_lazy as _

# ******************************
# class StatisticsAdmin(admin.ModelAdmin):
#     list_display = ('total_users', 'male_count', 'female_count')  # Ajoutez d'autres statistiques si nécessaire
#
#     def total_users(self, obj):
#         return Users.objects.count()
#
#     def male_count(self, obj):
#         return Users.objects.filter(sexe='Male').count()
#
#     def female_count(self, obj):
#         return Users.objects.filter(sexe='Female').count()
#
#
# admin.site.register(Users, StatisticsAdmin)
# *****************************

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


class GenderFilter(admin.SimpleListFilter):
    title = _('Gender')
    parameter_name = 'sexe'

    def lookups(self, request, model_admin):
        return (
            ('Male', _('Male')),
            ('Female', _('Female')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Male':
            return queryset.filter(sexe='Male')
        if self.value() == 'Female':
            return queryset.filter(sexe='Female')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name','duration_since_creation', 'email',)
    list_display_links = ('email',)  # Lien direct vers la page de modification
    search_fields = ("first_name", "email")
    list_filter = (GenderFilter,)
    actions = ['edit_selected', 'delete_selected', 'show_user_count']

    # Méthode pour calculer la durée depuis la création de l'utilisateur
    def duration_since_creation(self, obj):
        now = timezone.now()
        duration = now - obj.created_at
        return duration.days

    def show_user_count(self, request, queryset):
        total_users = Users.objects.count()
        self.message_user(request, f"Nombre total d'utilisateurs : {total_users}")

    show_user_count.short_description = "Afficher le nombre total d'utilisateurs"
    duration_since_creation.short_description = 'Duration Since Creation'


admin.site.register(Users, UsersAdmin)