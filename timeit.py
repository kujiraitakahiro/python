#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from timeit import timeit

def test_timeit(i):
	j=101
	times=100
	for j in range(i):

		print(timeit('test_timeit(i)', globals=globals(), number=times))
