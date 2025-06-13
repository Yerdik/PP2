import time
import math
number = 25100
delay_ms = 2123
print(f"Calculating square root of {number} after {delay_ms} milliseconds...")
time.sleep(delay_ms / 1000)  
result = math.sqrt(number)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
