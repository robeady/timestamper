# Timestamper

This is a small interactive windows program which records timestamps as you enter them.

It is designed to help you catch interesting moments when you are recording a video.

## Installation

Create and activate a virtualenv and `pip install requirements.txt`

## Usage

Start the program from the command line

    python timestamper.py

Enter a file name to record timestamps in, and optionally a description at the prompt.

Then the following commands are available:
- `r` to reset the timer, in case you did not start recording at the same time as you started the program. This deletes all recorded timestamps.
- `q` to save the timestamps recorded to a text file and exit.
- any other text to save a timestamp at the current moment, with the given text as a remark.

Global hotkeys `ctrl-alt-r` and `ctrl-alt-t` are also available for resetting and saving a timestamp, in case you are in another full screen application.
