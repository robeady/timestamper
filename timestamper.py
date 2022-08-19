import time
import os
from global_hotkeys import register_hotkey, start_checking_hotkeys

def fmt_timestamp(timestamp, remark):
    # convert to hours, minutes and seconds
    hours = int(timestamp / 3600)
    hours_text = f"{hours}:" if hours else ""
    minutes = int((timestamp % 3600) / 60)
    seconds = int(timestamp % 60)
    return f"{hours_text}{minutes:02d}:{seconds:02d} {remark or ''}"


class Timestamper:

    def __init__(self):
        self.filename = input("Enter a filename: ")
        if not self.filename.endswith(".txt"):
            self.filename += ".txt"
        if os.path.exists(self.filename):
            print("Warning, file already exists")

        self.desc = input("Enter a description: ")

        self.reset_timing()

        # :KeepKeybindsSynced
        register_hotkey("s", ["control", "alt"], self.record_timestamp)
        register_hotkey("r", ["control", "alt"], self.reset_timing)
        start_checking_hotkeys()

    def reset_timing(self):
        if hasattr(self, "start"):
            print("Resetting")
        self.start = time.time()
        self.timestamps = []

    def record_timestamp(self, remark = None):
        now = time.time()
        stamp = now - self.start
        self.timestamps.append((stamp, remark))
        print(f"Stamp {len(self.timestamps)} - {fmt_timestamp(stamp, remark)}")

    def input_loop(self):
        print("global hotkeys")
        # :KeepKeybindsSynced
        print("ctrl alt s: record timestamp")
        print("ctrl alt r: reset timing")
        while True:
            # get key pressed by user
            line = input("Enter 'q' to quit and save, 'r' to reset, or a comment to stamp:\n")
            if line in ["q", "Q"]:
                # write timestamps to file then exit
                with open(self.filename, "w") as f:
                    if self.desc:
                        f.write(self.desc + "\n")
                    for (timestamp, remark) in self.timestamps:
                        f.write(fmt_timestamp(timestamp, remark) + "\n")
                print("Saved to", self.filename)
                return
            elif line in ["r", "R"]:
                self.reset_timing()
            else:
                self.record_timestamp(line)


if __name__ == "__main__":
    Timestamper().input_loop()
