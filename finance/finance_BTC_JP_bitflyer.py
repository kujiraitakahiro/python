#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
r = requests.get('https://api.bitflyer.jp/v1/ticker?product_code=BTC_JPY')
json = r.json()
print(json)
print(json["ltp"])
