from datetime import datetime

date1 = datetime(2025, 6, 10, 14, 30, 0)
date2 = datetime(2025, 6, 11, 16, 45, 30)

difference = abs((date2 - date1).total_seconds())

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", difference)