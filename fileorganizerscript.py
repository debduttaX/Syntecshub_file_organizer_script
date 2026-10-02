import os
import shutil
import logging
import argparse


# Log file setup
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def get_folder(extension):
    """Return folder name according to file extension."""

    extension = extension.lower()

    if extension in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
        return "Images"

    elif extension in [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"]:
        return "Documents"

    elif extension in [".mp3", ".wav", ".aac", ".flac"]:
        return "Audio"

    elif extension in [".mp4", ".mkv", ".avi", ".mov"]:
        return "Videos"

    elif extension in [".zip", ".rar", ".7z"]:
        return "Archives"

    elif extension in [".py", ".c", ".cpp", ".java", ".html", ".css", ".js"]:
        return "Programs"

    else:
        return "Others"


def get_new_name(folder, filename):
    """If same file already exists, create a new name."""

    path = os.path.join(folder, filename)

    if not os.path.exists(path):
        return path

    name, extension = os.path.splitext(filename)
    count = 1

    while True:
        new_name = name + "_" + str(count) + extension
        new_path = os.path.join(folder, new_name)

        if not os.path.exists(new_path):
            return new_path

        count += 1


def organize_files(folder_path, dry_run=False):

    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    print("\nScanning:", folder_path)
    print("-" * 40)

    moved = 0

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # Get file extension
        name, extension = os.path.splitext(file)

        if extension == "":
            continue

        folder_name = get_folder(extension)

        destination_folder = os.path.join(
            folder_path, folder_name
        )

        destination = get_new_name(
            destination_folder, file
        )

        # Dry run
        if dry_run:
            print(
                "[DRY RUN]",
                file,
                "->",
                folder_name
            )
            continue

        try:
            # Create folder if it doesn't exist
            os.makedirs(destination_folder, exist_ok=True)

            # Move the file
            shutil.move(file_path, destination)

            print(
                "Moved:",
                file,
                "->",
                folder_name
            )

            logging.info(
                "Moved %s to %s",
                file,
                folder_name
            )

            moved += 1

        except Exception as e:

            print("Error moving", file, ":", e)

            logging.error(
                "Error moving %s: %s",
                file,
                e
            )

    print("-" * 40)
    print("Total files moved:", moved)


def main():

    parser = argparse.ArgumentParser(
        description="Simple File Organizer"
    )

    parser.add_argument(
        "folder",
        help="Folder path"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show changes without moving files"
    )

    args = parser.parse_args()

    organize_files(
        args.folder,
        args.dry_run
    )


if __name__ == "__main__":
    main()