def parallel_dividing(elems, force_dividing=False):
    max_number_of_elements_for_process = 20
    len_of_list_of_elems = len(elems)
    number_of_processes = len_of_list_of_elems / max_number_of_elements_for_process + 1
    processes = []
    for i in xrange(number_of_processes):
        processes.append([])
    if len_of_list_of_elems >= max_number_of_elements_for_process:
        for index, elem in enumerate(elems):
            processes[index % number_of_processes].append(elem)
    elif len_of_list_of_elems < max_number_of_elements_for_process and force_dividing is True:
        processes = [elems[1:(len_of_list_of_elems/2)], elems[(len_of_list_of_elems/2):]]
    else:
        processes = elems
    return processes

# if __name__ == '__main__':
#     res = parallel_dividing(range(10), force_dividing=True)
#     print res