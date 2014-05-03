#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from qwak_config import config

def make_request(api_action):
	payload = {
		'page': 'api',
		'action': api_action,
		'api_key': config['api_key'],
	}
	d = requests.get(config['pool_url'], params=payload)
	return d.text
