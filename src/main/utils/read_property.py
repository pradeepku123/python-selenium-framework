import configparser

config = configparser.RawConfigParser()
config.read('./src/main/config/config.ini')


class ReadProperty:
    '''
    Read Property Value From Config.ini File
    '''
    @staticmethod
    def get_application_url():
        return config.get('base_line', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('base_line', 'username')

    @staticmethod
    def get_user_password():
        return config.get('base_line', 'password')
