#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from qwak_utils import make_request

__title__   = 'qwak'
__version__ = '0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/qwak'
__license__ = 'Apache v2.0 License'

def public():
	d = make_request('public')
	return json.loads(d)

def user_status():
	d = make_request('getuserstatus')
	return json.loads(d)


def user_balance():
	d = make_request('getuserbalance')
	return json.loads(d)


def user_hashrate():
	d = make_request('getuserhashrate')
	return json.loads(d)


def user_sharerate():
	d = make_request('getusersharerate')
	return json.loads(d)


def user_transactions():
	d = make_request('getusertransactions')
	return json.loads(d)


def user_workers():
	d = make_request('getuserworkers')
	return json.loads(d)


def user_dashboard():
	d = make_request('getdashboarddata')
	return json.loads(d)


def user_navbar():
	d = make_request('getnavbardata')
	return json.loads(d)
