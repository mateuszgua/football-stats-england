import os


class Helpers:

    def is_file_exist(self, path) -> bool:
        file_exist = os.path.isfile(path)
        if file_exist:
            return True
        else:
            return False
