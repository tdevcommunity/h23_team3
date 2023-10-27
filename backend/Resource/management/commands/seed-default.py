from django.db import transaction
from django.core.management.base import BaseCommand
from Account.models import Professions, Stacks, Members, UserStacks, Users, Pays
from Resource.models import Ressources, Discussions, Type
from Permission.models import Roles
from BaseApi.AppEnum import *
import random

class Seeder:
    @classmethod
    def AccountSeed(cls):
        with transaction.atomic():
            for i in range(1, 20):
                if i % 2 != 0:
                    user, created = Users.objects.get_or_create(
                        email=f'john{i}@gmail.com',
                        defaults={
                            'username':f'John {i}',
                            'password':'password',
                            'first_name':f'User{i}',
                            'last_name':f'User{i}',
                            'phone':f'6000000{i}',
                            'bio':f'Bio de John {i}',
                            'pays':random.choice(Pays.objects.all()),
                            'role':Roles.objects.filter(name=UserRoleEnum.MENTOR.value).first(), 
                            'status':True,
                            'is_superuser':False
                        }
                    )
                
                # Seed des membres
                if i % 2 == 0:
                    mentor = user
                    mentore, created = Users.objects.get_or_create(
                        email=f'mentore{i}@gmail.com',
                        defaults={
                            'username':f'Mentore {i}',
                            'password':'password',
                            'first_name':f'Mentore{i}',
                            'last_name':f'Mentore{i}',
                            'phone':f'6000000{i}',
                            'bio':f'Bio de mentore {i}',
                            'pays':random.choice(Pays.objects.all()),
                            'status':True,
                            'role':Roles.objects.filter(name=UserRoleEnum.PROTECTED.value).first(),
                            'is_superuser':False
                        }
                    )
                    member, created = Members.objects.get_or_create(
                        mentor=mentor,
                        mentore=mentore,
                        status=True
                    )
                
                # Seed des UserStacks
                for _ in range(random.randrange(1, 6)): 
                    stack, created = Stacks.objects.get_or_create(
                        name=random.choice([stack.value for stack in StacksEnum])
                    )
                    userstack, created = UserStacks.objects.get_or_create(
                        user=user,
                        stack=stack
                    )
    @classmethod
    def ResourceSeed(cls):
        with transaction.atomic():
            for i in range(1, 100):
                ressource, created = Ressources.objects.get_or_create(
                    title=f'Ressource {i}',
                    content=f'Description de la ressource {i}',
                    author=random.choice(Users.objects.all()),
                    type=random.choice(Type.objects.all()),
                    status=True
                )

                # Seed des discussions
                for _ in range(random.randrange(1, 6)):
                    discussion, created = Discussions.objects.get_or_create(
                        ressource=ressource,
                        author=random.choice(Users.objects.all()),
                        content=f'Discussion {i}'
                    )

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding default data...')
        Seeder.AccountSeed()
        Seeder.ResourceSeed()
        self.stdout.write(self.style.SUCCESS('Successfully seeded default data'))