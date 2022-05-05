from time import sleep
from datetime import datetime
date = datetime.now().strftime("%d/%m/%Y/ %H:%M:%S")

print(f"{date}")
while True:
    date = datetime.now().strftime("%d/%m/%Y/ %H:%M:%S")
    print(date)
    sleep(1)

