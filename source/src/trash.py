# -*- coding: utf-8 -*-
import ConfigParser
import datetime
import logging
import os
import pydoc
import shutil
import source.policies.count_policy as count_policy
import source.policies.memory_policy as memory_policy
import source.policies.time_policy as time_policy
import termcolor
import my_exceptions
import serialization
import singleton
import user_input
import verification


class Trash(object):

    def __init__(self, path_of_config=''):
        if os.path.exists(path_of_config):
            config = ConfigParser.RawConfigParser()
            config.read(path_of_config)
            self.path_of_trash = os.path.expanduser(config.get('Section_Custom', 'path'))
            self.database = os.path.expanduser(config.get('Section_Custom', 'database'))
            self.max_size = config.getint('Section_Custom', 'max_size')
            self.max_number = config.getint('Section_Custom', 'max_num')
            self.max_list_height = 50
            self.max_time = config.getint('Section_Custom', 'max_time')
            self.arr_json_files = serialization.load_json(self.database)
            self.policies = config.get('Section_Custom', 'policies')
            self.silent = config.getboolean('Section_Custom', 'silent')
            self.dried = config.getboolean('Section_Custom', 'dry_run')
        else:
            self.path_of_trash = os.path.expanduser('~/.MyTrash')
            self.database = os.path.expanduser('~/.DB.json')
            self.max_size = 500000000
            self.max_number = 1000
            self.max_list_height = 50
            self.max_time = 1000
            self.arr_json_files = serialization.load_json(self.database)
            self.policies = 'default'
            self.silent = False
            self.dried = False

        if not os.path.exists(self.path_of_trash):
            os.makedirs(self.path_of_trash)
        self.rootLogger = logging.getLogger()
        self.set_logger()
        self.update()
        self.check_policy()

    def go_dry_run(self):
        """
        Dry run mode on
        :return:
        """
        self.dried = True

    def go_silent_mode(self):
        """
        Silent mode on
        :return:
        """
        self.silent = True
        self.rootLogger.setLevel(logging.CRITICAL)


    def check_policy(self):
        """
        Choose policies for removing files
        :return:
        """
        list_of_removing_files_by_policies = set()
        if self.policies.count('time'):
            time_policy_instance = time_policy.TimePolicy()
            list_of_removing_files_by_policies = list_of_removing_files_by_policies.union(time_policy_instance.run(self))
        if self.policies.count('memory'):
            memory_policy_instance = memory_policy.MemoryPolicy()
            memory_policy_instance.run(self)
        if self.policies.count('count'):
            count_policy_instance = count_policy.CountPolicy()
            list_of_removing_files_by_policies = list_of_removing_files_by_policies.union(count_policy_instance.run(self))
        if self.policies.count('default'):
            pass
        self.remove_for_hash(list_of_removing_files_by_policies)

    def remove_for_hash(self, list_of_hashes):
        """
        Remove files for list of hashes
        :param list_of_hashes: list of file hashes
        :return:
        """
        for item in list(list_of_hashes):
            path_of_item = os.path.join(self.path_of_trash, item)
            try:
                os.remove(path_of_item)
            except OSError:
                shutil.rmtree(path_of_item)

    def set_logger(self):
        """
        Set logger in case of silent mode
        :return:
        """
        if self.silent:
            silentHandler = logging.StreamHandler()
            silentHandler.setLevel(logging.CRITICAL)
            self.rootLogger.addHandler(silentHandler)
        else:
            log_handler = logging.StreamHandler()
            log_handler.setFormatter(
                logging.Formatter('[%(levelname)s] %(asctime)s (%(processName)-10s) %(message)s')
            )
            logger = logging.getLogger()
            logger.handlers = []
            logger.addHandler(log_handler)
            logger.setLevel(logging.DEBUG)
            self.rootLogger.addHandler(log_handler)

    def full_show(self):
        """
        Demonstrating a list of files with full description in color format
        """
        if len(self.arr_json_files) == 0:
            logging.info('No files in trash')
        full_show_string = ''
        for index, each_file in enumerate(self.arr_json_files):
            full_show_string += '%d %s %s %s %s %d Bytes \n' % (
            index + 1, termcolor.colored(each_file['name'], 'red'), termcolor.colored(each_file['type'], 'green'), termcolor.colored(each_file['hash'], 'yellow'),
            termcolor.colored(datetime.datetime.fromtimestamp(each_file['time_of_life']).strftime('%Y-%m-%d %H:%M:%S'), 'blue'), each_file['size'])

        if len(self.arr_json_files) > self.max_list_height:
            pydoc.pager(full_show_string)
        else:
            logging.info(full_show_string)

    def bin_show(self):
        """
        Demonstrating a list of files in trash bin
        """
        if len(self.arr_json_files) == 0:
            logging.info('No files in trash')
        for ind, json_file in enumerate(self.arr_json_files):
            logging.info("{0}. {1}".format(ind + 1, json_file))

    def delete_for_name_from_trash(self, elems):
        """
        Remove files for their filenames
        :param elems: filename
        :return:
        """
        for elem in elems:
            path_of_elem = os.path.join(self.path_of_trash, elem)
            if os.path.isdir(path_of_elem):
                shutil.rmtree(path_of_elem)
            else:
                os.remove(path_of_elem)

    def update(self):
        """
        Update info about database and current items in trash
        :return:
        """
        try:
            verification.check_for_trash_files(self.arr_json_files, self.path_of_trash)
        except my_exceptions.TrashSetError as e:
            self.rootLogger.error('Error: Unknown %s' % termcolor.colored(e.get_list(), 'green'))
            answer = user_input.UserInput()
            list_of_elems = e.get_list()
            for elem in list_of_elems[:]:
                self.rootLogger.error('Delete %s?' % termcolor.colored(elem, 'red'))
                answer.ask()
                if answer.state == 'yes':
                    self.delete_for_name_from_trash([elem])
                    list_of_elems.remove(elem)
                elif answer.state == 'no':
                    list_of_elems.remove(elem)
                elif answer.state == 'yes_to_all':
                    self.delete_for_name_from_trash(list_of_elems)
                    break
                elif answer.state == 'no_to_all':
                    break
                elif answer.state == 'cancel':
                    break

        except my_exceptions.DatabaseSetError as e:
            list_of_elems = e.get_list()
            for elem in list_of_elems:
                for index, json_dict in enumerate(self.arr_json_files):
                    if elem == str(json_dict['hash']):
                        self.arr_json_files.remove(self.arr_json_files[index])

        serialization.push_json(self.arr_json_files, self.database)

    def get_hashes(self):
        """
        A function to get names of files in the database
        :return: list of names of files in Database
        """
        list_of_hashes = []
        for items in self.arr_json_files:
            list_of_hashes.append(items['hash'])
        return list_of_hashes
