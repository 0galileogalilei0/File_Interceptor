import os
import pyinotify
import time

# Whitebeard Skull with Mustache Banner
SKULL_ASCII = """
        ______
     .-'      `-.
    /            \\
   |              |
   |,  .-.  .-.  ,|
   | )(_o/  \\o_)( |
   |/     /\\     \\|
   (_     ^^     _)
    \\__|IIIIII|__/
     | \\IIIIII/ |
     \\          /
      `--------`
   ⚡ Whitebeard’s File Interceptor ⚡
"""
print(SKULL_ASCII)

# Log File Path
LOG_FILE = "file_interceptor.log"


class EventHandler(pyinotify.ProcessEvent):
    """Handles file events"""

    def process_IN_CREATE(self, event):
        log_event(f"[+] File Created: {event.pathname}")

    def process_IN_DELETE(self, event):
        log_event(f"[-] File Deleted: {event.pathname}")

    def process_IN_MODIFY(self, event):
        log_event(f"[!] File Modified: {event.pathname}")

    def process_IN_MOVED_FROM(self, event):
        log_event(f"[*] File Moved Out: {event.pathname}")

    def process_IN_MOVED_TO(self, event):
        log_event(f"[→] File Moved In: {event.pathname}")


def log_event(event_message):
    """Logs events with timestamps"""
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {event_message}\n"

    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

    print(log_entry.strip())


def start_monitoring(path="/home"):
    """Start monitoring files"""
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, EventHandler())

    wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True, auto_add=True)

    print(f"⚡ Monitoring Directory: {path} ⚡")
    print("👀 Watching for file changes...")

    notifier.loop()


if __name__ == "__main__":
    start_monitoring("/home")  # Change directory if needed
