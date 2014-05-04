#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from qwak_utils import make_request

__title__   = 'qwak'
__version__ = '0.2'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/qwak'
__license__ = 'Apache v2.0 License'

def public():
	"""Fetch public pool statistics."""
	d = make_request('public')
	return json.loads(d)


def pool_info():
	"""Get the information on pool settings."""
	d = make_request('getpoolinfo')
	return json.loads(d)


def pool_status():
	"""Fetch overall pool status."""
	d = make_request('getpoolstatus')
	return json.loads(d)


def pool_hashrate():
	"""Get current pool hashrate."""
	d = make_request('getpoolhashrate')
	return json.loads(d)


def hourly_hashrates():
	"""Get detailed pool hashrate history."""
	d = make_request('gethourlyhashrates')
	return json.loads(d)


def pool_sharerate():
	"""Get current pool share rate (shares/s)."""
	d = make_request('getpoolsharerate')
	return json.loads(d)


def block_last():
	"""Get time since last block found (seconds)."""
	d = make_request('gettimesincelastblock')
	return json.loads(d)


def block_count():
	"""Get current block height in blockchain."""
	d = make_request('getblockcount')
	return json.loads(d)


def blocks_found():
	"""Get last N blocks found as configured in admin panel."""
	d = make_request('getblocksfound')
	return json.loads(d)


def blocks_stats():
	"""Get pool block stats."""
	d = make_request('getblockstats')
	return json.loads(d)


def difficulty():
	"""Get current difficulty in blockchain."""
	d = make_request('getdifficulty')
	return json.loads(d)


def current_workers():
	"""Get amount of current active workers."""
	d = make_request('getcurrentworkers')
	return json.loads(d)


def top_contributors():
	"""Fetch top contributors data."""
	d = make_request('gettopcontributors')
	return json.loads(d)


def estimated_time():
	"""Get estimated time to next block based on pool hashrate (seconds)."""
	d = make_request('getestimatedtime')
	return json.loads(d)


def user_status():
	"""Fetch a users overall status."""
	d = make_request('getuserstatus')
	return json.loads(d)


def user_balance():
	"""Fetch a users balance."""
	d = make_request('getuserbalance')
	return json.loads(d)


def user_hashrate():
	"""Fetch a users hash rate."""
	d = make_request('getuserhashrate')
	return json.loads(d)


def user_sharerate():
	"""Fetch a users share rate	."""
	d = make_request('getusersharerate')
	return json.loads(d)


def user_transactions():
	"""Get a users transactions."""
	d = make_request('getusertransactions')
	return json.loads(d)


def user_workers():
	"""Fetch a users worker status."""
	d = make_request('getuserworkers')
	return json.loads(d)


def dashboard():
	"""Fetch all dashboard related information."""
	d = make_request('getdashboarddata')
	return json.loads(d)


def navbar():
	"""Get the data displayed on the navbar."""
	d = make_request('getnavbardata')
	return json.loads(d)
