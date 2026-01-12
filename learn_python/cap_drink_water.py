from plyer import notification
import time

while True:
    notification.notify(title="Please drink some water", message="You need to drink some water",)
    time.sleep(60)