from django.core.management.base import BaseCommand

from authapp.models import MyUser
import json, os

JSON_PATH = 'authapp/json'


def load_from_json(name_file):
    with open(os.path.join(JSON_PATH, name_file + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Метод обновления данных в базе новыми данными """
        MyUser.objects.all().delete()
        list_users = load_from_json("users")

        batchInsert = []
        for el in list_users:
            batchInsert.append(MyUser(
                                password=el.get('password'),
                                username=el.get('username'),
                                first_name=el.get('first_name'),
                                last_name=el.get('last_name'),
                                email=el.get('email'),
                            )
            )
        MyUser.objects.bulk_create(batchInsert)  # bulk_create <= Пакетная Вставка списка в базу

        # Создаем суперпользователя при помощи менеджера модели
        super_user = MyUser.objects.create_superuser('admin', 'admin@localchost.net', '12345')

