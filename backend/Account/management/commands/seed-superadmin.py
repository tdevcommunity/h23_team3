from django.db import transaction
from django.core.management.base import BaseCommand
from BaseApi.AppEnum import UserRoleEnum
from Account.models import Users
from Permission.models import Roles
from django.contrib.auth.models import Permission

class Seeder:
    @classmethod
    def seedSuperAdmin(cls):
        superUserRole, created = Roles.objects.get_or_create(name=UserRoleEnum.SUPER_ADMIN.value, defaults={'description': 'The super user'})
        
        super_email = input("Enter super user email:")
        super_password = input("Enter super user password:")

        with transaction.atomic():
            super_user, created = Users.objects.get_or_create(
                email=super_email,
                defaults={
                    'first_name': 'Super',
                    'last_name': 'Admin',
                    'phone': '00000001',
                    'role': superUserRole
                }
            )

            if created:
                super_user.set_password(super_password)
                super_user.save()
                    
            print (f"Message: Success, [Email: {super_email}, Password: **********]");

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding Super Admin...')
        Seeder.seedSuperAdmin()
        self.stdout.write(self.style.SUCCESS('Successfully seeded the Super Admin'))
