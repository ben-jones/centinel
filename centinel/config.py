import os
import getpass
import logging
import json


class Configuration():

    def __init__(self,):

        self.params = {}

        # centinel user
        user_info = {}
        user_info['current_user']  = getpass.getuser()
        user_home          = os.path.expanduser('~' + user_info['current_user'])
        user_info['centinel_home'] = os.path.join(user_home, '.centinel')
        self.params['user'] = user_info

        # directory structure
        dirs = {}
        dirs['experiments_dir'] = os.path.join(os.path.dirname(__file__),
                                               "experiments")
        dirs['data_dir']        = os.path.join(os.path.dirname(__file__),
                                               "data")
        dirs['results_dir']     = os.path.join(self.params['user']['centinel_home'],
                                               'results')
        self.params['dirs'] = dirs

        # logging
        self.params['log'] = {}
        self.params['log']['log_level'] = logging.INFO
        self.params['log']['log_file'] = None
        # an alternative is os.path.join(centinel_home,
        # "centinel.log")
        self.params['log']['log_format'] = '%(levelname)s: %(message)s'

        # server
        servers = {}
        servers['server_url'] = "http://127.0.0.1:5000"
        servers['login_file'] = os.path.join(self.params['user']['centinel_home'],
                                             'login')
        self.params['server'] = servers

        # proxy
        proxy = {}
        proxy['proxy_type'] = None  # "socks" or "http"
        proxy['proxy_url']  = None  # "http://127.0.0.1:9050"
        proxy['proxy'] = None
        if proxy['proxy_type']:
            proxy['proxy']  = {proxy['proxy_type']: proxy['proxy_url']}
        self.params['proxy'] = proxy

    def parse_config(self, config_file):
        """Given a configuration file, read in and interpret the results"""

        with open(config_file, 'r') as f:
            config = json.load(f)
        self.params = config
        if self.params['proxy_type']:
            self.params['proxy']  = {self.params['proxy_type']:
                                     self.params['proxy_url']}

    def write_out_config(self, config_file):
        """Write out the configuration file

        Note: this will erase all comments from the config file

        """
        with open(config_file, 'w') as f:
            json.dump(self.params, f)
