import os
from file_object import FileObject


class Folder(FileObject):
    """Class for folders in Smart RM"""
    def __init__(self):
        super(Folder, self).__init__()
        self.num_of_obj = 0

    def make_from_dict(self, some_dict):
        super(Folder, self).make_from_dict(some_dict)
        self.num_of_obj = some_dict['num_of_obj']
        self.size = some_dict['size']

    def make_objects(self, name):
        super(Folder, self).make_object(name)
        self.num_of_obj = self.add_number_of_objects(self.path)
        self.size = self.add_size(self.path)
        self.type = 'Directory'

    @staticmethod
    def add_size(start_path):
        """
        Calculate the size of folders
        :param start_path: path of folder
        :return: size of this folder
        """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    @staticmethod
    def add_number_of_objects(path):
        """
              Calculate the number of objects in folder
              :param path: path of folder
              :return: count of files in this folder
        """
        num = 0
        for abs_path, sub_path, files in os.walk(path):
            num += len(files)
        return num
