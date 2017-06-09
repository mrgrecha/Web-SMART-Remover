import os

def get_info_for_one_level(current_path):
    files = os.listdir(current_path)
    list_of_files = []
    print 'files one level', files
    for file in files:
        path_of_file = os.path.join(current_path, file)
        print 'path_of_file :', path_of_file
        if os.path.isdir(path_of_file):
            cur_file = {"id": path_of_file, "text": file}
        else:
            cur_file = {"id": path_of_file, "text": file, "icon": "glyphicon glyphicon-file"}
        list_of_files.append(cur_file)
        print list_of_files
    return list_of_files

def get_info(current_path):
    if os.path.exists(current_path):
        files = os.listdir(current_path)
        list_of_files = []
        for file in files:
            path_of_file = os.path.join(current_path, file)
            if os.path.isdir(path_of_file):
                if os.listdir(path_of_file) != '':
                    #cur_file = {"id" : path_of_file, "text" : file,  "type" : "Folder", "children" : get_info_for_one_level(path_of_file)}
                    cur_file = {"id" : path_of_file, "text" : file,  "type" : "Folder", "children" : get_info(path_of_file)}
                else:
                    cur_file = {"id" : path_of_file, "text" : file,  "type" : "Folder"}
            else:
                cur_file = {"id" : path_of_file, "text" : file,  "type" : "file",  "icon" : "glyphicon glyphicon-file"}
            list_of_files.append(cur_file)
        return list_of_files
    else:
        raise BaseException



if __name__ == '__main__':
    pass