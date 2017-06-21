import os
import ConfigParser
import shutil

def make_config(name_of_trash_bin, path_of_trash_bin, policies, dried, silent, max_size, max_num, max_time):
    config = ConfigParser.RawConfigParser()
    config_name = 'config_of_' + name_of_trash_bin + '.cfg'
    path_of_config = os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm', config_name)
    if not os.path.exists(config_name):
        with open(path_of_config, 'w+'):
            pass
    config.add_section('Section_Custom')
    config.set('Section_Custom', 'path', path_of_trash_bin + '/' + '.' + name_of_trash_bin)
    config.set('Section_Custom', 'database', '~/.Configs_for_web_rm/' + name_of_trash_bin + '.json')
    config.set('Section_Custom', 'max_size', max_size)
    config.set('Section_Custom', 'max_time', max_time)
    config.set('Section_Custom', 'max_num', max_num)
    config.set('Section_Custom', 'dry_run', dried)
    config.set('Section_Custom', 'silent', silent)
    config.set('Section_Custom', 'policies', policies)

    with open(path_of_config, 'wb') as configfile:
        config.write(configfile)

def remove_trash_bin(name_of_trash_bin):
    config_name = 'config_of_' + name_of_trash_bin.get_name() + '.cfg'
    path_of_config = os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm', config_name)
    config = ConfigParser.RawConfigParser()
    config.read(path_of_config)
    path_of_trash_bin = os.path.expanduser(config.get('Section_Custom', 'path'))
    os.remove(path_of_config)
    # os.remove(os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm', name_of_trash_bin.get_name() + '.json'))
    # shutil.rmtree(path_of_trash_bin + '_' + name_of_trash_bin.get_name())


if __name__ == '__main__':
  pass