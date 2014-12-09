<img src="https://raw.github.com/c0ding/qwak/master/doc/qwak.png" alt="qwak" title="qwak">

[![PyPi Version](http://img.shields.io/pypi/v/qwak.svg)](https://pypi.python.org/pypi/qwak/)   [![Downloads](http://img.shields.io/pypi/dm/qwak.svg)](https://pypi.python.org/pypi/qwak/)


**qwak** is an APACHE licensed library written in Python designed to provide a simple to use API wrapper for [MPOS](https://github.com/MPOS/php-mpos).

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install qwak

## Configuration:

Create a ```~/.qwak_config.py``` file and fill in your pool URL and API key like so:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

config = {
	'pool_url': 'http://example.com',
	'api_key' : '12345abcde'
}
```

## API Documentation:

**qwak** handles all the API calls MPOS provides. Examples kindly provided by [script.io](https://scrypt.io).

### Pool:

  - Public:

```
>>> import qwak
>>> qwak.public()
{
    "pool_name": "Scrypt.io | HBN Pool", 
    "last_block": 817675, 
    "workers": 33, 
    "shares_this_round": 20764, 
    "network_hashrate": 573459242.17, 
    "hashrate": 46773
}
```
  - Pool info:

```
>>> qwak.pool_info()
{
    "getpoolinfo": {
        "version": "1.0.0", 
        "data": {
            "coinname": "HoboNickels", 
            "algorithm": "scrypt", 
            "txfee": null, 
            "min_ap_threshold": 5, 
            "cointarget": "30", 
            "stratumport": "37373", 
            "payout_system": "prop", 
            "currency": "HBN", 
            "max_ap_threshold": 5000, 
            "fees": 0.5, 
            "coindiffchangetarget": 5
        }, 
        "runtime": 0.99682807922363
    }
}
```
  - Pool status:

```
>>> qwak.pool_status()
{
    "getpoolstatus": {
        "version": "1.0.0", 
        "data": {
            "nethashrate": 614243980.49, 
            "pool_name": "Scrypt.io | HBN Pool", 
            "nextnetworkblock": 817770, 
            "currentnetworkblock": 817769, 
            "estshares": 13180.24593408, 
            "workers": 34, 
            "networkdiff": 12.87133392, 
            "timesincelast": 2816, 
            "efficiency": 98.81, 
            "lastblock": 817675, 
            "esttime": 1160.4105424495, 
            "hashrate": 47640
        }, 
        "runtime": 5.7098865509033
    }
}
```
  - Pool hashrate:

```
>>> qwak.pool_hashrate()
{
    "getpoolhashrate": {
        "version": "1.0.0", 
        "data": 47591, 
        "runtime": 32.737016677856
    }
}
```
  - Pool sharerate:

```
>>> qwak.pool_sharerate()
{
    "gethourlyhashrates": {
        "version": "1.0.0", 
        "data": {
            "mine": false, 
            "pool": {
                "20": 41289, 
                "21": 40548, 
                "22": 38363, 
                "23": 40847, 
                "1": 38504, 
                "0": 38877, 
                "3": 38939, 
                "2": 37899, 
                "5": 39439, 
                "4": 39971, 
                "7": 40100, 
                "6": 40040, 
                "9": 39971, 
                "8": 40278, 
                "11": 40320, 
                "10": 40180, 
                "13": 39690, 
                "12": 39268, 
                "15": 38260, 
                "14": 40554, 
                "17": 41645, 
                "16": 38543, 
                "19": 39174, 
                "18": 12647
            }
        }, 
        "runtime": 1261.7139816284
    }
}
```
  - Pool workers:

```
>>> qwak.current_workers()
{
    "getcurrentworkers": {
        "version": "1.0.0", 
        "data": 32, 
        "runtime": 1.2381076812744
    }
}
```

  - Pool top contributors:

```
>>> qwak.top_contributors()
{
    "gettopcontributors": {
        "version": "1.0.0", 
        "data": {
            "hashes": {
                "account": "hip_Hobo", 
                "hashrate": 370.5
            }, 
            "shares": [
                {
                    "account": "SaschaAc", 
                    "shares": 731
                }, 
                {
                    "account": "unick", 
                    "shares": 353
                }, 
                {
                    "account": "ubuntufreak", 
                    "shares": 264
                }, 
                {
                    "account": "graymatter", 
                    "shares": 157
                }, 
                {
                    "account": "Meska", 
                    "shares": 109
                }, 
                {
                    "account": "splint9ka", 
                    "shares": 107
                }, 
                {
                    "account": "licocraft", 
                    "shares": 96
                }, 
                {
                    "account": "lepetitdiable", 
                    "shares": 82
                }, 
                {
                    "account": "interfuse", 
                    "shares": 67
                }, 
                {
                    "account": "anonymous", 
                    "shares": 56
                }, 
                {
                    "account": "goldfeverhobo", 
                    "shares": 50
                }, 
                {
                    "account": "fonky", 
                    "shares": 31
                }, 
                {
                    "account": "Eight", 
                    "shares": 22
                }, 
                {
                    "account": "hip_Hobo", 
                    "shares": 21
                }, 
                {
                    "account": "zelszels", 
                    "shares": 21
                }
            ]
        }, 
        "runtime": 2.6769638061523
    }
}
```

### Blocks:

  - Estimated time to next block:

```
>>> qwak.estimated_time()
{  
    "getestimatedtime": {  
        "version": "1.0.0",
        "data": 63541.382146264,
        "runtime": 2724.8191833496
    }
}
```

  - Time since last block:

```
>>> qwak.block_last()
{
    "gettimesincelastblock": {
        "version": "1.0.0", 
        "data": 3028, 
        "runtime": 1.3439655303955
    }
}
```

  - Block count:

```
>>> qwak.block_count()
{
    "getblockcount": {
        "version": "1.0.0", 
        "data": 817779, 
        "runtime": 1.6119480133057
    }
}
```

  - Blocks found on pool:

```
>>> qwak.blocks_found()
{
    "getblocksfound": {
        "version": "1.0.0", 
        "data": [
            {
                "estshares": 12862, 
                "worker_name": "SaschaAc.6", 
                "account_id": 226, 
                "blockhash": "000000000efea095fd26518b19820b870e9086e93855f4977e1766f7e9b711c0", 
                "is_anonymous": 0, 
                "shares": 1993, 
                "height": 817675, 
                "difficulty": 12.56077319, 
                "amount": 5, 
                "confirmations": 25, 
                "time": 1399218719, 
                "share_id": 85212233, 
                "id": 23245, 
                "finder": "SaschaAc", 
                "accounted": 1
            },
            ...
            {
                "estshares": 14183, 
                "worker_name": "SaschaAc.5", 
                "account_id": 226, 
                "blockhash": "0000000008898c8e8b613db2a7c83aa0f972de19826db8ec7b8bfbed8f4b477d", 
                "is_anonymous": 0, 
                "shares": 4951, 
                "height": 815667, 
                "difficulty": 13.85024985, 
                "amount": 5, 
                "confirmations": 25, 
                "time": 1399159614, 
                "share_id": 84650456, 
                "id": 23211, 
                "finder": "SaschaAc", 
                "accounted": 1
            }
        ], 
        "runtime": 1.2688636779785
    }
}
```
  - Block stats:

```
>>> qwak.block_stats()
{
    "getblockstats": {
        "version": "1.0.0", 
        "data": {
            "12MonthShares": "82306047", 
            "1HourEstimatedShares": 26298, 
            "1HourDifficulty": 25.6816834, 
            "7DaysShares": "6701309", 
            "7DaysDifficulty": 5816.95565409, 
            "12MonthAmount": 115530, 
            "TotalValid": "23106", 
            "24HourDifficulty": 642.6008193, 
            "24HourTotal": "48", 
            "TotalDifficulty": 71859.73857944, 
            "7DaysAmount": 2280, 
            "24HourValid": "48", 
            "4WeeksOrphan": "32", 
            "7DaysOrphan": "0", 
            "1HourAmount": 10, 
            "12MonthOrphan": "134", 
            "12MonthTotal": "23240", 
            "4WeeksTotal": "3047", 
            "1HourOrphan": "0", 
            "TotalEstimatedShares": 73584372, 
            "12MonthValid": "23106", 
            "24HourShares": "828972", 
            "4WeeksValid": "3015", 
            "12MonthEstimatedShares": 73584372, 
            "7DaysEstimatedShares": 5956563, 
            "12MonthDifficulty": 71859.73857944, 
            "TotalShares": "82306047", 
            "TotalAmount": 115530, 
            "24HourOrphan": "0", 
            "7DaysValid": "456", 
            "24HourEstimatedShares": 658023, 
            "4WeeksAmount": 15075, 
            "24HourAmount": 240, 
            "7DaysTotal": "456", 
            "1HourShares": "39467", 
            "1HourValid": "2", 
            "4WeeksDifficulty": 22239.12019247, 
            "1HourTotal": "2", 
            "4WeeksEstimatedShares": 22772859, 
            "4WeeksShares": "25594317", 
            "TotalOrphan": "134", 
            "Total": 23240
        }, 
        "runtime": 203.04179191589
    }
}

```

### Network:

  - Difficulty:

```
>>> qwak.difficulty()
{
    "getdifficulty": {
        "version": "1.0.0", 
        "data": 13.11145585, 
        "runtime": 1.8680095672607
    }
}
```

### User:

  - User status:

```
>>> qwak.user_status()
{
    "getuserstatus": {
        "version": "1.0.0", 
        "data": {
            "username": "username", 
            "sharerate": "1.27", 
            "hashrate": 5312.79, 
            "shares": {
                "username": "username", 
                "is_anonymous": 0, 
                "invalid": 1, 
                "donate_percent": 0, 
                "valid": 42, 
                "id": 40
            }
        }, 
        "runtime": 199.51820373535
    }
}
```

  - User balance:

```
>>> qwak.user_balance()
{
    "getuserbalance": {
        "version": "1.0.0", 
        "data": {
            "confirmed": 8.22416031, 
            "orphaned": 6.99071406, 
            "unconfirmed": 1.65332559
        }, 
        "runtime": 19.626140594482
    }
}
```

  - User hashrate:

```
>>> qwak.user_hashrate()
{
    "getuserhashrate": {
        "version": "1.0.0", 
        "data": 5474, 
        "runtime": 14.457941055298
    }
}
```

  - User sharerate:

```
>>> qwak.user_sharerate()
{
    "getusersharerate": {
        "version": "1.0.0", 
        "data": "1.42", 
        "runtime": 1.2180805206299
    }
}
```

  - User transactions:

```
>>> qwak.user_transactions()
{
    "getusertransactions": {
        "version": "1.0.0", 
        "data": {
            "transactionsummary": {
                "Fee": 482.61430904998, 
                "TXFee": 238.79999999999, 
                "Credit": 115545.00010462, 
                "Donation": 43.14081271, 
                "Debit_AP": 96526.28776731, 
                "Debit_MP": 16190.69451484
            }, 
            "transactions": [
                {
                    "username": "unick", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.00382566, 
                    "confirmations": 10, 
                    "height": 817836, 
                    "type": "Fee", 
                    "id": 898454
                }, 
                {
                    "username": "unick", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.76513133, 
                    "confirmations": 10, 
                    "height": 817836, 
                    "type": "Credit", 
                    "id": 898453
                }, 
                {
                    "username": "zelszels", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.00023474, 
                    "confirmations": 10, 
                    "height": 817836, 
                    "type": "Fee", 
                    "id": 898452
                }, 
                {
                    "username": "zelszels", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.04694836, 
                    "confirmations": 10, 
                    "height": 817836, 
                    "type": "Credit", 
                    "id": 898451
                }, 
                {
                    "username": "interfuse", 
                    "blockhash": null, 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:03:10", 
                    "txid": null, 
                    "amount": 0.1, 
                    "confirmations": null, 
                    "height": null, 
                    "type": "TXFee", 
                    "id": 898450
                }
            ]
        }, 
        "runtime": 1032.723903656
    }
}
```

  - User sharerate:

```
>>> qwak.user_sharerate()
{
    "getusersharerate": {
        "version": "1.0.0", 
        "data": "1.42", 
        "runtime": 1.2180805206299
    }
}
```

  - User transactions:

```
>>> qwak.user_transactions()
{
    "getusertransactions": {
        "version": "1.0.0", 
        "data": {
            "transactionsummary": {
                "Fee": 482.61430904998, 
                "TXFee": 238.79999999999, 
                "Credit": 115545.00010462, 
                "Donation": 43.14081271, 
                "Debit_AP": 96526.28776731, 
                "Debit_MP": 16190.69451484
            }, 
            "transactions": [
                {
                    "username": "unick", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.00382566, 
                    "confirmations": 13, 
                    "height": 817836, 
                    "type": "Fee", 
                    "id": 898454
                }, 
                {
                    "username": "unick", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.76513133, 
                    "confirmations": 13, 
                    "height": 817836, 
                    "type": "Credit", 
                    "id": 898453
                }, 
                {
                    "username": "zelszels", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.00023474, 
                    "confirmations": 13, 
                    "height": 817836, 
                    "type": "Fee", 
                    "id": 898452
                }, 
                {
                    "username": "zelszels", 
                    "blockhash": "000000000717fb23284487ffc964af5d39a25e58cf47ca30c44aef777e4aee57", 
                    "coin_address": null, 
                    "timestamp": "2014-05-04 19:09:05", 
                    "txid": null, 
                    "amount": 0.04694836, 
                    "confirmations": 13, 
                    "height": 817836, 
                    "type": "Credit", 
                    "id": 898451
                }, 
                {
                    "username": "interfuse", 
                    "blockhash": null, 
                    "coin_address": null,
                    "timestamp": "2014-05-04 19:03:10", 
                    "txid": null, 
                    "amount": 0.1, 
                    "confirmations": null, 
                    "height": null, 
                    "type": "TXFee", 
                    "id": 898450
                }
            ]
        }, 
        "runtime": 1028.6419391632
    }
}
```

  - User workers:

```
>>> qwak.user_workers()
{
    "getuserworkers": {
        "version": "1.0.0", 
        "data": [
            {
                "username": "username.5870x2", 
                "monitor": 0, 
                "count_all_archive": 7, 
                "difficulty": 128, 
                "count_all": 107, 
                "password": "x", 
                "id": 41, 
                "hashrate": 797
            }, 
            {
                "username": "username.6970", 
                "monitor": 0, 
                "count_all_archive": 1, 
                "difficulty": 128, 
                "count_all": 63, 
                "password": "x", 
                "id": 43, 
                "hashrate": 447
            }, 
            {
                "username": "username.2k", 
                "monitor": 0, 
                "count_all_archive": 0, 
                "difficulty": 0, 
                "count_all": 0, 
                "password": "x", 
                "id": 970, 
                "hashrate": 0
            }, 
            {
                "username": "username.6850", 
                "monitor": 0, 
                "count_all_archive": 3, 
                "difficulty": 128, 
                "count_all": 21, 
                "password": "x", 
                "id": 980, 
                "hashrate": 168
            }, 
            {
                "username": "username.2k2", 
                "monitor": 0, 
                "count_all_archive": 23, 
                "difficulty": 128, 
                "count_all": 287, 
                "password": "x", 
                "id": 1062, 
                "hashrate": 2167
            }, 
            {
                "username": "username.2", 
                "monitor": 0, 
                "count_all_archive": 31, 
                "difficulty": 128, 
                "count_all": 261, 
                "password": "x", 
                "id": 1078, 
                "hashrate": 2042
            }
        ], 
        "runtime": 23.391008377075
    }
}
```

  - Dashboard:

```
>>> qwak.user_dashboard()
{
    "getdashboarddata": {
        "version": "1.0.0", 
        "data": {
            "personal": {
                "sharedifficulty": 0, 
                "sharerate": 0, 
                "estimates": {
                    "payout": 0, 
                    "donation": 0, 
                    "fee": 0, 
                    "block": 0
                }, 
                "shares": {
                    "invalid_percent": 0, 
                    "unpaid": 0, 
                    "valid": 0, 
                    "invalid": 0
                }, 
                "hashrate": 0
            }, 
            "raw": {
                "personal": {
                    "hashrate": 0
                }, 
                "network": {
                    "nextdifficulty": 3.96825133, 
                    "esttimeperblock": 76.040271480616, 
                    "blocksuntildiffchange": 1, 
                    "hashrate": 621.58896191
                }, 
                "pool": {
                    "hashrate": 47074
                }
            }, 
            "system": {
                "load": [
                    1.35, 
                    1.21, 
                    1.17
                ]
            }, 
            "pool": {
                "info": {
                    "currency": "HBN", 
                    "name": "Scrypt.io | HBN Pool"
                }, 
                "workers": 35, 
                "shares": {
                    "invalid_percent": 1.35, 
                    "progress": 1.1, 
                    "valid": 3403, 
                    "estimated": 13139, 
                    "invalid": 690
                }, 
                "difficulty": 16, 
                "target_bits": 20, 
                "price": "0.00043614", 
                "hashrate": 0.723849
            }, 
            "network": {
                "blocksuntildiffchange": 1, 
                "esttimeperblock": 76.04, 
                "difficulty": 12.83067929, 
                "hashrate": 51.144842457, 
                "nextdifficulty": 3.96825133, 
                "block": 208173
            }
        }, 
        "runtime": 55.642127990723
    }
}
```

  - User navbar:

```
>>> qwak.user_navbar()
{
    "getnavbardata": {
        "version": "1.0.0", 
        "data": {
            "raw": {
                "workers": 30, 
                "pool": {
                    "hashrate": 47074
                }
            }, 
            "network": {
                "difficulty": 13.02524623, 
                "block": 817867, 
                "hashrate": 621.58896191
            }, 
            "pool": {
                "progress": 81.43, 
                "workers": 30, 
                "estimated": 13338, 
                "hashrate": 47074
            }
        }, 
        "runtime": 14.021873474121
    }
}

```

## License:

```
  Apache v2.0 License
  Copyright 2014 Martin Simon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
