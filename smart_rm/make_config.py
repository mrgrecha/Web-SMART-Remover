import os
import ConfigParser

def make_config(name_of_trash_bin, path_of_trash_bin, policies, dried, silent, max_size, max_num, max_time):
    config = ConfigParser.RawConfigParser()
    config_name = 'config_of_' + name_of_trash_bin + '.cfg'
    path_of_config = os.path.join(os.path.expanduser('~'), '.Configs_for_web_rm', config_name)
    if not os.path.exists(config_name):
        with open(path_of_config, 'w+'):
            pass
    config.add_section('Section_Custom')
    config.set('Section_Custom', 'path', path_of_trash_bin + '_' + name_of_trash_bin)
    config.set('Section_Custom', 'database', '~/.Configs_for_web_rm/' + name_of_trash_bin + '.json')
    config.set('Section_Custom', 'max_size', max_size)
    config.set('Section_Custom', 'max_time', max_time)
    config.set('Section_Custom', 'max_num', max_num)
    config.set('Section_Custom', 'dry_run', dried)
    config.set('Section_Custom', 'silent', silent)
    config.set('Section_Custom', 'policies', policies)

    with open(path_of_config, 'wb') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    make_config(name_of_trash_bin='one_trash', path_of_trash_bin='/Users/Dima', policies='213', max_num=100, max_time=25, max_size=123, silent=True, dried=False)