import logging
import os
import re
import shutil
import sys
import source.src.directory
import source.src.my_exceptions
import source.src.serialization
import source.src.verification
import bin_command
import source.src.file_object
from command import Command
from source.src.dry_run import dry_run


class RFCommand(Command):

    def __init__(self, my_trash):
        super(Command, self).__init__()
        self.dried = my_trash.dried
        self.trash = my_trash
        self.files_to_return = []

    def execute(self, list_of_files):
        return self.delete_files(list_of_files, self.trash)

    def cancel(self, list_of_files):
        self.trash.rootLogger.info('Cancel for rfc')
        temp_recover_command = bin_command.RecCommand(self.trash)
        temp_recover_command.execute(list_of_files)

    @dry_run
    def real_delete(self, files_to_delete, length, my_trash):
        arr_files = [source.src.file_object.FileObject() for i in xrange(0, length)]

        for index, each_file in enumerate(files_to_delete):
            if os.path.islink(each_file):
                arr_files[index].set_type('Link')
            else:
                arr_files[index].set_type('File')
            arr_files[index].make_object(each_file)
            os.rename(each_file, str(arr_files[index].hash))
            shutil.move(arr_files[index].hash, my_trash.path_of_trash)
            #my_trash.arr_json_files.append(arr_files[index].__dict__)

            # for ind in xrange(0, length):
            #     self.files_to_return.append(arr_files[ind].hash)
        return arr_files

    def delete_files(self, list_of_files, my_trash):
        """Delete a list of files with checking for folders"""
        list_for_return = []
        try:
            checked_list = source.src.verification.check_for_files_and_links(list_of_files)
            length = len(checked_list)
            list_for_return = self.real_delete(checked_list, length, my_trash)
            for removing_file in checked_list:
                my_trash.rootLogger.info('Removing ' + removing_file + ' to trash')

        except source.src.my_exceptions.NotSuchFileError as e:
            logging.error('Error:' + str(e))
            sys.exit(1)

        except source.src.my_exceptions.PermissionError as e:
            logging.error('Error:' + str(e))
            sys.exit(2)

        except source.src.my_exceptions.NotFileError as e:
            logging.error('Error:' + str(e))
            sys.exit(3)

        except OSError as e:
            logging.error('Error' + str(e))

       # source.src.serialization.push_json(my_trash.arr_json_files, my_trash.database)
        return list_for_return


class RDCommand(Command):

    def __init__(self, my_trash):
        super(Command, self).__init__()
        self.dried = my_trash.dried
        self.trash = my_trash
        self.dirs_to_return = []

    def name(self, list_of_args):
        return 'Remove Directories'

    def execute(self, list_of_dirs):
        return self.delete_dir(list_of_dirs, self.trash)

    def cancel(self, list_of_files):
        self.trash.rootLogger.info('Cancel for rdc')
        temp_recover_command = bin_command.RecCommand(self.trash)
        temp_recover_command.execute(list_of_files)

    @dry_run
    def real_delete_dir(self, dirs_to_delete, length, my_trash):
        arr_dirs = [source.src.directory.Folder() for i in xrange(0, length)]
        for index, each_dir in enumerate(dirs_to_delete):
            source.src.directory.Folder.make_objects(arr_dirs[index], each_dir)
            os.rename(each_dir, str(arr_dirs[index].hash))
            shutil.move(str(arr_dirs[index].hash), my_trash.path_of_trash)
        return  arr_dirs

    def delete_dir(self, list_of_dirs, my_trash):
        """
        Delete a list of directories with checking
        :param list_of_dirs:
        :return:
        """
        checked_list_of_dirs = source.src.verification.check_for_dir(list_of_dirs, my_trash.path_of_trash)
        length = len(checked_list_of_dirs)
        list_for_return = self.real_delete_dir(checked_list_of_dirs, length, my_trash)
        for each_dir in checked_list_of_dirs:
            my_trash.rootLogger.info('Removing directory ' + each_dir + ' to trash')

        # except source.src.my_exceptions.NotSuchFileError as e:
        #     logging.error('Error:' + str(e))
        #     sys.exit(1)
        #
        # except source.src.my_exceptions.PermissionError as e:
        #     logging.error('Error:' + str(e))
        #     sys.exit(2)
        #
        # except source.src.my_exceptions.NotFileError as e:
        #     logging.error('Error:' + str(e))
        #     sys.exit(3)
        #
        # except source.src.my_exceptions.RemoveError as e:
        #     logging.error('Error:' + str(e) + '. It is a trash folder.')
        #     sys.exit(4)

        return list_for_return

class RRCommand(Command):

    def __init__(self, current_folder, my_trash):
        super(Command, self).__init__()
        self.cur_dir = current_folder
        self.dried = my_trash.dried
        self.trash = my_trash
        self.files_to_remove = []
        self.dirs_to_remove = []

    def execute(self, regex):
        self.delete_for_regex(self.cur_dir, regex, self.trash)
        return [self.files_to_remove, self.dirs_to_remove]

    def cancel(self, list_of_something):
        pass


    def delete_for_regex(self, cur_dir, regex, my_trash):

        """
        Removing for regular expression
        :param regex:
        :param cur_dir: current directory from which starts removing
        :return:
         """
        for name in os.listdir(cur_dir):
            path = os.path.join(cur_dir, name)
            if re.search(regex, name) and os.path.isfile(path):
                self.files_to_remove.append(path)
            elif os.path.isdir(path) and re.match(regex, name):
                self.dirs_to_remove.append(path)
            elif os.path.isdir(path) and not re.match(regex, name):
                self.delete_for_regex(path, regex, self.trash)


