#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas_datareader.data as web
from datetime import datetime
start = datetime(2000, 1, 1)
end = datetime(2018, 9, 12)
j = web.DataReader('GDP', 'fred', start, end)
print(j.head(1))
print(j.tail(1))
