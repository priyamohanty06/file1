import datetime
import time
from plyer import notification

while True:
    notification.notify(
        title="Flipkart".format(datetime.date.today()),
        message="Up to 50% Off on Juice Mixer Grinders... \nPrices slashed on top brands like Bajaj, Phillips, Kent, Pigeon & more top brands.Bring one home today!",
        app_icon="E:/Python Sync Project/noti.ico",
        timeout=10)

    time.sleep(60*60*2)
