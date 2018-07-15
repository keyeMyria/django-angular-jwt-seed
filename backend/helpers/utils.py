import subprocess
import os


class UtilsMixin:

    def shell_command(self, command, error=None):
        print(f'\t{" ".join(command)}')
        try:
            proc = subprocess.Popen(
                command,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            e, out = proc.communicate()
            if e:
                return e.decode('utf-8')
            else:
                return out.decode('utf-8')

        except subprocess.CalledProcessError as err:
            if error:
                raise Exception(error)
            else:
                raise err

    def check_or_create_file(self, path: str):
        if not path:
            return
        with open(path, 'w') as f:
            f.write('\n')

    def check_or_create_path(self, path):

        if not path:
            return

        if not os.path.exists(path):
            os.makedirs(path)
