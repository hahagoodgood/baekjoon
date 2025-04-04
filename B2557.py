'''
import sys
import time

s = time.perf_counter()
sys.stdout.write("Hello World!\n")
e = time.perf_counter()
execution_time = e - s
print(f"1:{execution_time}")

s = time.perf_counter()
print("Hello World!")
e = time.perf_counter()
execution_time = e - s
print(f"2:{execution_time}")
'''

import sys
sys.stdout.write("Hello World!\n")