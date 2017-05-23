import src.trash as trash
import commands.remove_command
import src.dividing
import os
import multiprocessing
import src.serialization

my_trash = trash.Trash()
elems_for_deleting = ["tt.1", "tt.2", "tt.3", "tt.4", "tt.5", "tt.6", "tt.7", "tt.8", "tt.9", "tt.10"]
remove_command = commands.remove_command.RFCommand(my_trash)

def help_function_for_removing_files(list_for_manager, list_for_removing):
    list_of_objects_of_removed_files = remove_command.execute(list_for_removing)
    for obj in list_of_objects_of_removed_files:
        list_for_manager.append(obj.__dict__)

def high_remove(list_of_files, the_trash):
    processes = []
    manager = multiprocessing.Manager()
    manager_list = manager.list()
    res = src.dividing.parallel_dividing(list_of_files)
    for i in xrange(len(res)):
        p = multiprocessing.Process(target=help_function_for_removing_files, args=(manager_list, res[i]))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    the_trash.arr_json_files += manager_list
    src.serialization.push_json(the_trash.arr_json_files, the_trash.database)


if __name__ == '__main__':
    names = []
    for i in xrange(1, 1001):
        names.append('dima' + str(i))
    high_remove(names, my_trash)
