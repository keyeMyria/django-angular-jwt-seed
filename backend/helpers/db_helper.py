# -*- coding: utf-8 -*-
# TODO "NEED TO REBUILD CLEAN METHOD ISSUE WITH ENV, CAN DELETE DJANGO SELF MIGRATIONS"
import subprocess
import os

from .utils import UtilsMixin


class PathDoesNotExist(Exception):
    pass


class DataBaseHelper(UtilsMixin):
    DEFAULT_CONST_DB_NAME = 'djangodb'
    DEFAULT_CONST_DB_USER_NAME = 'djangouser'
    DEFAULT_CONST_DB_USER_PASSWORD = 'djangopassword'

    DB_SETTINGS_PATH = os.path.join('backend', 'core', 'settings', 'database.py')
    APPS_PATH = os.path.join('backend', 'apps')
    IGNORE = ['__pycache__']

    init = None
    clean = None
    migrate = None

    def __init__(self, **kwargs):

        for key, value in kwargs.items():
            self.__setattr__(key, value)

        self.apps_list = []

        if not os.path.exists(self.APPS_PATH):
            raise PathDoesNotExist(f'path does not exists: {self.APPS_PATH}')

        for item in os.listdir(self.APPS_PATH):

            dir_path = os.path.join(self.APPS_PATH, item)

            if dir_path not in self.IGNORE and os.path.isdir(dir_path):
                self.apps_list.append(item)

        for function in [func for func in dir(self) if callable(getattr(self, func))]:

            if function.endswith('_init'):
                self.__getattribute__(function)()

        if self.init:
            self._create_db()
            self._create_db_user()
            self._create_db_name()
            self._grant_privilages()

        if self.clean:
            self._clean()

        if self.migrate:
            self._migrations()

    def _template_database(self):
        return f"\ndb_name = '{self.DEFAULT_CONST_DB_NAME}'" \
               f"\ndb_user_name = '{self.DEFAULT_CONST_DB_USER_NAME}'" \
               f"\ndb_password = '{self.DEFAULT_CONST_DB_USER_PASSWORD}'"

    def _create_db_user(self):

        command = f'sudo -u postgres bash -c \"psql -c \\\"CREATE USER {self.DEFAULT_CONST_DB_USER_NAME} WITH PASSWORD \'{self.DEFAULT_CONST_DB_USER_PASSWORD}\';\\\"\"'
        try:

            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

        except subprocess.CalledProcessError as exc:
            output = exc.output

        print(output.decode())

    def _create_db_name(self):
        command = f'sudo -u postgres bash -c \"psql -c \\\"CREATE DATABASE {self.DEFAULT_CONST_DB_NAME} ENCODING \'UTF-8\' TEMPLATE template0;\\\"\"'
        try:

            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

        except subprocess.CalledProcessError as exc:
            output = exc.output

        print(output.decode())

    def _grant_privilages(self):
        command = f'sudo -u postgres bash -c \"psql -c \\\"GRANT ALL PRIVILEGES ON DATABASE {self.DEFAULT_CONST_DB_NAME} TO {self.DEFAULT_CONST_DB_USER_NAME};\"\\\"'
        try:

            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

        except subprocess.CalledProcessError as exc:
            output = exc.output

        print(output.decode())

    def _create_db(self):
        with open(self.DB_SETTINGS_PATH, 'w') as file:
            file.write(self._template_database())

    def _clean(self):
        command = 'find . -path \"*/migrations/*.py\" -not -name \"__init__.py\" -delete && find . -path \"*/migrations/*.pyc\"  -delete'

        try:
            print(f'COMMAND: {command}')
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

        except subprocess.CalledProcessError as exc:
            output = exc.output

        print(output.decode())

    def _migrations(self):

        for item in self.apps_list:
            command = f'python backend/manage.py makemigrations {item}'
            try:
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

            except subprocess.CalledProcessError as exc:
                output = exc.output

            print(output.decode())

        self._migrate()

    def _migrate(self):

        command = f'python backend/manage.py migrate'
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

        except subprocess.CalledProcessError as exc:
            output = exc.output

        print(output.decode())

        for item in self.apps_list:
            command = f'python backend/manage.py migrate {item}'
            try:
                output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

            except subprocess.CalledProcessError as exc:
                output = exc.output

            print(output.decode())
