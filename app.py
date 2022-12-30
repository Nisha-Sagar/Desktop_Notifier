# Desktop Notifier using python

import time
from plyer import notification

while True:
    notification.notify(
        title = "Take a Break!",
        message = "Drink some water",
        app_icon = "C:\SYNC TASK\TASK_1_NOTIFIRE\coffee-break.ico",
        timeout = 5
    )
    time.sleep(3600)                # 3600 seconds = 1hr
