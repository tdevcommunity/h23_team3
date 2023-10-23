from django.db import transaction
from django.core.management.base import BaseCommand
from Account.models import Pays, Professions, Stacks
from Resource.models import Type
from BaseApi.AppEnum import *
import pycountry

class Seeder:
    @classmethod
    def countrySeed(cls):
        with transaction.atomic():
            pays_data = [{'code': country.alpha_2, 'name': country.name} for country in pycountry.countries]
            for data in pays_data:
                Pays.objects.get_or_create(code=data['code'], defaults={'name': data['name']})
    
    @classmethod
    def seed_types_resources(cls):
        with transaction.atomic():
            for type in TypeResourcesEnum:
                Type.objects.get_or_create(name=type.value)
                
    @classmethod
    def seed_professions(cls):
        with transaction.atomic():
            for profession in ProfessionsEnum:
                Professions.objects.get_or_create(name=profession.value)

    @classmethod
    def seed_stacks(cls):
        with transaction.atomic():
            for stack in StacksEnum:
                Stacks.objects.get_or_create(name=stack.value)

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding de pays...')
        Seeder.countrySeed()

        self.stdout.write('Seeding de professions...')
        Seeder.seed_professions()

        self.stdout.write('Seeding types de resources...')
        Seeder.seed_types_resources()

        self.stdout.write('Seeding stacks...')
        Seeder.seed_stacks()

        self.stdout.write(self.style.SUCCESS('Successfully seeded pays, stacks, and type'))