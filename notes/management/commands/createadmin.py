import os
import logging
from django.core.management.base import BaseCommand, CommandError
from notes.models import GGITUser


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        if not GGITUser.objects.filter(username=os.environ.get('ADMIN_USERNAME', 'admin')).exists():
            logger.info('Admin user not found. Creating one!')
            try:
                user = GGITUser.objects.create(username='admin', is_staff=True, is_superuser=True)
                user.set_password(os.environ.get('ADMIN_PASSWORD'))
                user.save()
            except Exception as e:
                logger.warning('Something went wrong %s', e)