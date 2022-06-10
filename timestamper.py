import time
import os

def fmt_timestamp(timestamp):
    return f"{int(timestamp) // 60}:{(timestamp % 60):04.1f}"

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
        key = input("Press 'q' to quit and save, or return to stamp: ")
        if key == "q":
            # write timestamps to file then exit
            with open(filename, "w") as f:
                if desc:
                    f.write(f"{desc}\n")
                for timestamp in timestamps:
                    f.write(fmt_timestamp(timestamp) + "\n")
            return

        elif key == "":
            now = time.time()
            stamp = now - start
            timestamps.append(stamp)
            print(f"Stamp {len(timestamps)}: {fmt_timestamp(stamp)}")

        elif key == "r":
            print("Resetting")
            start = time.time()
            timestamps = []


if __name__ == "__main__":
    main()
