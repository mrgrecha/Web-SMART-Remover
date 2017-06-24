
def clean_list(some_list, key):
    if key:
        return [some_file.encode('ascii', 'ignore')[1:] for some_file in
         some_list[key][0].replace('&#39;', '').replace('[', '').replace(']', '').split(
            ', ')]
    else:
        return [some_file.encode('ascii', 'ignore') for some_file in
        some_list[0].replace('&#39;', '').replace('[', '').replace(']', '').split(
             ', ')]


def from_list_to_string(some_list):
    return some_list[0]
