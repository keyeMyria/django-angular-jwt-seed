import os
from .utils import UtilsMixin

__PROJECT_NAME__ = 'djangoSeed'
__LOGS_DIR_NAME__ = 'logs'
__LOGS_DEBUG_FILE_NAME__ = 'debug.log'
__LOGS_PRODUCTION_FILE_NAME__ = 'production.log'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROJECT_HOME_CONFIG_DIR = os.path.join(PROJECT_BASE_DIR, f'.{__PROJECT_NAME__}')
PROJECT_LOG_DIR = os.path.join(PROJECT_HOME_CONFIG_DIR, __LOGS_DIR_NAME__)
PROJECT_DEBUG_LOG_FILE = os.path.join(PROJECT_LOG_DIR, __LOGS_DEBUG_FILE_NAME__)
PROJECT_PRODUCTION_LOG_FILE = os.path.join(PROJECT_LOG_DIR, __LOGS_PRODUCTION_FILE_NAME__)

for item in [
    PROJECT_HOME_CONFIG_DIR,
    PROJECT_LOG_DIR]: UtilsMixin().check_or_create_path(item)

for item in [
    PROJECT_DEBUG_LOG_FILE,
    PROJECT_PRODUCTION_LOG_FILE]: UtilsMixin().check_or_create_file(item)

PROJECT_SERVICE_TEMPLATE= f"""
#! /bin/bash

### BEGIN INIT INFO
# Provides:          {__PROJECT_NAME__}.sh
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: {__PROJECT_NAME__} service
# Description:       Run {__PROJECT_NAME__} service
### END INIT INFO

# Carry out specific functions when asked to by the system

export PYTHONIOENCODING="utf-8"
export LANG=C.UTF-8

case "$1" in
  start)
    echo "Starting {__PROJECT_NAME__}..."
    sudo -u root bash -c ''

    ;;
  stop)
    echo "Stopping  {__PROJECT_NAME__}..."
    sudo -u root bash -c ''
    sleep 2
    ;;
  *)
    echo "Usage: /etc/init.d/ {__PROJECT_NAME__}.sh {{start|stop}}"
    exit 1
    ;;
esac

exit 0
"""

__PROJECT_NGINX_TEMPLATE__ = """


"""

__PROJECT_UWSGI_TEMPLATE__ = f"""
# uwsgi_{__PROJECT_NAME__}.ini
# uwsgi --socket :8001 --chdir backend/ --wsgi-file backend/core/wsgi.py
[uwsgi]

# Настройки, связанные с Django
# Корневая папка проекта (полный путь)
chdir = {BASE_DIR}
# Django wsgi файл
module = core.wsgi
# полный путь к виртуальному окружению
virtualenv = {PROJECT_BASE_DIR}.venv/

# общие настройки
# master
master = true
# максимальное количество процессов
processes = 4
# полный путь к файлу сокета
socket = /tmp/{__PROJECT_NAME__}.sock
# права доступа к файлу сокета
chmod-socket    = 664
# очищать окружение от служебных файлов uwsgi по завершению
vacuum = true
pidfile         = /var/run/{__PROJECT_NAME__}.pid
logto           = {PROJECT_LOG_DIR}sproot.log
# uid and gid
uid             = www-data
gid             = www-data
"""

__PROJECT_UWSGI_PARAMS__ = """
uwsgi_param  QUERY_STRING       $query_string;
uwsgi_param  REQUEST_METHOD     $request_method;
uwsgi_param  CONTENT_TYPE       $content_type;
uwsgi_param  CONTENT_LENGTH     $content_length;

uwsgi_param  REQUEST_URI        $request_uri;
uwsgi_param  PATH_INFO          $document_uri;
uwsgi_param  DOCUMENT_ROOT      $document_root;
uwsgi_param  SERVER_PROTOCOL    $server_protocol;
uwsgi_param  REQUEST_SCHEME     $scheme;
uwsgi_param  HTTPS              $https if_not_empty;

uwsgi_param  REMOTE_ADDR        $remote_addr;
uwsgi_param  REMOTE_PORT        $remote_port;
uwsgi_param  SERVER_PORT        $server_port;
uwsgi_param  SERVER_NAME        $server_name;
"""
