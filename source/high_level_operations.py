import src.trash as trash
import commands.remove_command
import src.dividing
import commands.bin_command
import multiprocessing
import src.serialization
import os



def high_remove_files(list_of_files, the_trash):
    print 'fiiiles:', list_of_files
    remove_file_command = commands.remove_command.RFCommand(the_trash)
    processes = []
    manager = multiprocessing.Manager()
    manager_list = manager.list()
    if len(list_of_files) == 1:
        res = src.dividing.parallel_dividing([list_of_files])
    else:
        res = src.dividing.parallel_dividing(list_of_files)

    def help_function_for_removing_files(list_for_manager, list_for_removing):
        list_of_objects_of_removed_files = remove_file_command.execute(list_for_removing)
        for obj in list_of_objects_of_removed_files:
            list_for_manager.append(obj.__dict__)

    for i in xrange(len(res)):
        p = multiprocessing.Process(target=help_function_for_removing_files, args=(manager_list, res[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    the_trash.arr_json_files += manager_list
    src.serialization.push_json(the_trash.arr_json_files, the_trash.database)

def high_remove_dirs(list_of_dirs, the_trash):
    print 'Dirs: ', list_of_dirs
    processes = []
    remove_directory_command = commands.remove_command.RDCommand(the_trash)
    manager = multiprocessing.Manager()
    manager_list = manager.list()

    if len(list_of_dirs) == 1:
        res = src.dividing.parallel_dividing([list_of_dirs])
    else:
        res = src.dividing.parallel_dividing(list_of_dirs)

    def help_function_for_removing_dirs(list_for_manager, list_for_removing):
        list_of_objects_of_removed_dirs = remove_directory_command.execute(list_for_removing)
        for obj in list_of_objects_of_removed_dirs:
            list_for_manager.append(obj.__dict__)

    for i in xrange(len(res)):
        p = multiprocessing.Process(target=help_function_for_removing_dirs, args=(manager_list, res[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    the_trash.arr_json_files += manager_list
    src.serialization.push_json(the_trash.arr_json_files, the_trash.database)

def high_remove(list_of_files_and_dirs, the_trash):
    files = []
    dirs = []
    for each_item in list_of_files_and_dirs:
        if os.path.isdir(each_item):
            dirs.append(each_item)
        else:
            files.append(each_item)
    high_remove_files(files, the_trash)
    high_remove_dirs(dirs, the_trash)


def high_regular_removing(start_folder, pattern, the_trash):
    remove_regex_command = commands.remove_command.RRCommand(start_folder, the_trash)
    files, dirs = remove_regex_command.execute(pattern)
    high_remove_files(files, the_trash)
    high_remove_dirs(dirs, the_trash)



def high_recover(list_of_files, the_trash):
    recover_command = commands.bin_command.RecCommand(the_trash)
    processes = []
    manager = multiprocessing.Manager()
    manager_list = manager.list()
    if len(list_of_files) == 1:
        res = src.dividing.parallel_dividing([list_of_files])
    else:
        res = src.dividing.parallel_dividing(list_of_files)

    def help_function_for_recovering(list_for_manager, list_for_recovering):
        list_of_objects_of_recovered_files = recover_command.execute(list_for_recovering)
        for obj in list_of_objects_of_recovered_files:
            list_for_manager.append(obj)

    for i in xrange(len(res)):
        p = multiprocessing.Process(target=help_function_for_recovering, args=(manager_list, res[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for index, each_note in enumerate(the_trash.arr_json_files):
        for manage_note in manager_list:
            if each_note == manage_note:
                the_trash.arr_json_files.remove(the_trash.arr_json_files[index])

    the_trash.update()
    src.serialization.push_json(the_trash.arr_json_files, the_trash.database)




def high_deleting_files_from_trash(list_of_files, the_trash):
    delete_command = commands.bin_command.DFTCommand(the_trash)
    processes = []
    manager = multiprocessing.Manager()
    manager_list = manager.list()

    if len(list_of_files) == 1:
        res = src.dividing.parallel_dividing([list_of_files])
    else:
        res = src.dividing.parallel_dividing(list_of_files)
    def help_function_for_deleting_files_from_trash(list_for_manager, list_for_removing):
        list_of_objects_of_removed_files = delete_command.execute(list_for_removing)
        for obj in list_of_objects_of_removed_files:
            list_for_manager.append(obj)

    for i in xrange(len(res)):
        p = multiprocessing.Process(target=help_function_for_deleting_files_from_trash, args=(manager_list, res[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    for index, each_note in enumerate(the_trash.arr_json_files):
        for manage_note in manager_list:
            if each_note == manage_note:
                the_trash.arr_json_files.remove(the_trash.arr_json_files[index])

    the_trash.update()
    src.serialization.push_json(the_trash.arr_json_files, the_trash.database)


if __name__ == '__main__':
   pass
