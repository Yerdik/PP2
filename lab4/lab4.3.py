from datetime import datetime

current_time = datetime.now()
clean_time = current_time.replace(microsecond=0)

print("Original datetime:", current_time)
print("Datetime without microseconds:", clean_time)