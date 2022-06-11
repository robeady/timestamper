import time
import os

def fmt_timestamp(timestamp, remark):
    # convert to hours, minutes and seconds
    hours = int(timestamp / 3600)
    hours_text = f"{hours}:" if hours else ""
    minutes = int((timestamp % 3600) / 60)
    seconds = int(timestamp % 60)
    return f"{hours_text}{minutes:02d}:{seconds:02d} {remark or ''}"

def main():
    timestamps = []

    filename = input("Enter a filename: ")
    if not filename.endswith(".txt"):
        filename += ".txt"
    desc = input("Enter a description: ")

    # warn if file already exists
    if os.path.exists(filename):
        print("Warning, file already exists")

    # start timing
    start = time.time()

    while True:
        # get key pressed by user
        line = input("Press 'q' to quit and save, r to reset, or a comment to stamp: ")
        if line == "q":
            # write timestamps to file then exit
            with open(filename, "w") as f:
                if desc:
                    f.write(desc + "\n")
                for (timestamp, remark) in timestamps:
                    f.write(fmt_timestamp(timestamp, remark) + "\n")
            return
        elif line == "r":
            print("Resetting")
            start = time.time()
            timestamps = []
        else:
            now = time.time()
            stamp = now - start
            timestamps.append((stamp, line))
            print(f"Stamp {len(timestamps)} - {fmt_timestamp(stamp, line)}")


if __name__ == "__main__":
    main()
