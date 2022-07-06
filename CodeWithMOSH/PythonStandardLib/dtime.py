from datetime import datetime
import time

dt = datetime(2021, 1, 1)
dt = datetime.now()
datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())


print(f"{dt.year}/{dt.month}")
