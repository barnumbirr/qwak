#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests

config_file = '~/.qwak_config.py'
sys.path.append(os.path.dirname(os.path.expanduser(config_file)))

from qwak_config import config

__title__   = 'qwak'
__version__ = '0.2'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/qwak'
__license__ = 'Apache v2.0 License'


def make_request(api_action):
	payload = {
		'page': 'api',
		'action': api_action,
		'api_key': config['api_key'],
	}
	d = requests.get(config['pool_url'], params=payload)
	return d.text
