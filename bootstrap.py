# -*- coding: utf-8 -*-
import argparse
import os
import sys

## ADD DJANGO TO PATH

DJANGO_PROJECT_PATH = os.path.join(os.getcwd(), 'backend')
if not os.path.exists(DJANGO_PROJECT_PATH):
    raise Exception(f'bootstrap helper not in project root path!!')

sys.path.append(DJANGO_PROJECT_PATH)

from helpers import (
    BASE_DIR,
    PROJECT_BASE_DIR,
    PROJECT_DEBUG_LOG_FILE,
    PROJECT_PRODUCTION_LOG_FILE,
    UtilsMixin
)

print(
    f"\nPROJECT_BASE_DIR: {PROJECT_BASE_DIR},\nDJANGO_BASE_DIR: {BASE_DIR},\nPROJECT_DEBUG_LOG_FILE: {PROJECT_DEBUG_LOG_FILE},\nPROJECT_PRODUCTION_LOG_FILE: {PROJECT_PRODUCTION_LOG_FILE}")

from helpers.db_helper import DataBaseHelper


class ProjectHelper(UtilsMixin):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)

        self.db_helper = DataBaseHelper(**kwargs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Bootstrap helper script`s',
        epilog=""
    )

    # parser.add_argument('--init', action="store_true", help='')
    #
    # parser.add_argument('--clean', action="store_true", help='')
    #
    # parser.add_argument('--migrate', action="store_true", help='')

    kwargs = parser.parse_args()
