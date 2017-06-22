import src.trash as trash
import commands.remove_command
import src.dividing
import commands.bin_command
import multiprocessing
import src.serialization
import os

elems_for_deleting = ["tt.1", "tt.2", "tt.3", "tt.4", "tt.5", "tt.6", "tt.7", "tt.8", "tt.9", "tt.10"]
# remove_file_command = commands.remove_command.RFCommand(my_trash)
# remove_directory_command = commands.remove_command.RDCommand(my_trash)
# recover_command = commands.bin_command.RecCommand(my_trash)
# delete_command = commands.bin_command.DFTCommand(my_trash)


def high_remove_files(list_of_files, the_trash):
    remove_file_command = commands.remove_command.RFCommand(the_trash)
    processes = []
    manager = multiprocessing.Manager()
    manager_list = manager.list()
    # res = src.dividing.parallel_dividing(list_of_files)
    res = list_of_files

    def help_function_for_removing_files(list_for_manager, list_for_removing):
        list_of_objects_of_removed_files = remove_file_command.execute([list_for_removing])
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
    processes = []
    remove_directory_command = commands.remove_command.RDCommand(the_trash)
    manager = multiprocessing.Manager()
    manager_list = manager.list()
    # res = src.dividing.parallel_dividing(list_of_dirs, force_dividing=True)
    res = list_of_dirs

    def help_function_for_removing_dirs(list_for_manager, list_for_removing):
        list_of_objects_of_removed_dirs = remove_directory_command.execute([list_for_removing])
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



# #TODO fix bugs
# def help_function_for_recovering(list_for_manager, list_for_recovering):
#     list_of_objects_of_recovered_files = recover_command.execute(list_for_recovering)
#     for obj in list_of_objects_of_recovered_files:
#         list_for_manager.append(obj)
#
# def high_recover(list_of_files, the_trash):
#     processes = []
#     manager = multiprocessing.Manager()
#     manager_list = manager.list()
#     res = src.dividing.parallel_dividing(list_of_files, force_dividing=True)
#     for i in xrange(len(res)):
#         p = multiprocessing.Process(target=help_function_for_recovering, args=(manager_list, res[i]))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     for index, each_note in enumerate(the_trash.arr_json_files):
#         for manage_note in manager_list:
#             if each_note == manage_note:
#                 the_trash.arr_json_files.remove(the_trash.arr_json_files[index])
#
#     src.serialization.push_json(the_trash.arr_json_files, the_trash.database)
#
#
# def help_function_for_deleting_files_from_trash(list_for_manager, list_for_removing):
#     list_of_objects_of_removed_files = delete_command.execute(list_for_removing)
#     for obj in list_of_objects_of_removed_files:
#         list_for_manager.append(obj)
#
# def deleting_files_from_trash(list_of_files, the_trash):
#     processes = []
#     manager = multiprocessing.Manager()
#     manager_list = manager.list()
#     res = src.dividing.parallel_dividing(list_of_files)
#     for i in xrange(len(res)):
#         p = multiprocessing.Process(target=help_function_for_deleting_files_from_trash, args=(manager_list, res[i]))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     for index, each_note in enumerate(the_trash.arr_json_files):
#         for manage_note in manager_list:
#             if each_note == manage_note:
#                 the_trash.arr_json_files.remove(the_trash.arr_json_files[index])
#
#     src.serialization.push_json(the_trash.arr_json_files, the_trash.database)


if __name__ == '__main__':
    # temp = ["aa", "bb", "cc", "dd", "ee"]
    # high_remove_files(temp, my_trash)
    names = []
    names.append("155d0bc6-1286-4a2d-92ae-332f49b00ec9")
    names.append("ca8bbc34-c2d7-433d-b2ae-4be63f2cddd9")
