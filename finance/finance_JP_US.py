#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas_datareader.data as web
from datetime import datetime
start = datetime(2000, 1, 1)
end = datetime(2018, 9, 12)
f = web.DataReader('DEXJPUS', 'fred', start, end)
print(f.head(1))
print(f.tail(1))
today = datetime(2018, 9, 12)
f2 = web.DataReader('DEXJPUS', 'fred', start, today)
print(f2.tail(1))
