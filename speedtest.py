'''
speedtest.py

A simple speedtest to check the performance of a new M1 macbook pro

Macbook Pro 14" 2021 M1 Pro 16GB                            113s
Macbook Pro 16" 2019 2.6GHz 6-core Intel i7 16GB            180s
Macbook Pro 15" mid 2014 2.2GHz Quad core Intel i7 16GB     205s


'''
import random
from datetime import datetime

print('speedtest.py')
print('Starting test...')

time_start = datetime.now()

data = [random.randrange(100, 999) for i in range(100000000)]

squared = [x**2 for x in data]
sqrt = [x**0.5 for x in data]
mul = [x * y for x, y in zip(squared, sqrt)]
div = [x / y for x, y in zip(squared, sqrt)]
int_div = [x // y for x, y in zip(squared, sqrt)]

time_end = datetime.now()

print('...test complete.')
print(f'TOTAL TIME = {(time_end - time_start).seconds} seconds')
