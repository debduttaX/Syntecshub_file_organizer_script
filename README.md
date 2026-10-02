# File Organizer Script

A simple Python automation tool that organizes files into different folders based on their file extensions.

## Features

- Scans a selected folder
- Organizes files by extension
- Creates folders automatically
- Handles duplicate file names
- Supports Dry Run mode
- Maintains a log file
- Includes error handling
- Can be scheduled using Windows Task Scheduler or cron

## Technologies Used

- Python
- os
- shutil
- logging
- argparse

## File Categories

| Extension Type | Folder |
|---|---|
| JPG, PNG, GIF | Images |
| PDF, DOCX, TXT | Documents |
| MP3, WAV | Audio |
| MP4, MKV | Videos |
| PY, C, CPP, JAVA | Programs |
| ZIP, RAR | Archives |
| Other files | Others |

## How to Run

```bash
python fileorganizerscript.py "TestFiles"