import subprocess

from control_module.database import db_name, db_password, db_user_name

clean_pyc_migrations_command = 'find . -path \"*/migrations/*.py\" -not -name \"__init__.py\" -delete && find . -path \"*/migrations/*.pyc\"  -delete'
create_pg_user_command = f'sudo -u postgres bash -c \"psql -c \\\"CREATE USER {db_user_name} WITH PASSWORD \'{db_password}\';\\\"\"'
create_pg_database_command = f'sudo -u postgres bash -c \"psql -c \\\"CREATE DATABASE {db_name} ENCODING \'UTF-8\' TEMPLATE template0;\\\"\"'
grant_pg_command = f'sudo -u postgres bash -c \"psql -c \\\"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user_name};\"\\\"'
manage_makemigrations = 'python manage.py makemigrations'
manage_migrate = 'python manage.py migrate'

for command in [
    clean_pyc_migrations_command,
    create_pg_user_command,
    create_pg_database_command,
    grant_pg_command,
    manage_makemigrations,
    manage_migrate
]:
    try:
        print(f'COMMAND: {command}')
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

    except subprocess.CalledProcessError as exc:
        output = exc.output

    finally:
        print(output.decode())
