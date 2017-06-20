import os


def make_folder_for_configs():
    if not os.path.exists(os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm')):
        os.mkdir(os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm'))
    print 'well done!'
    
if __name__ == '__main__':
    make_folder_for_configs()