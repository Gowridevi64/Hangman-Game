import os
import shutil
import logging
import argparse
from pathlib import Path

EXTENSIONS = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
}

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def organize_folder(folder, dry_run=False):
    scanned = 0
    moved = 0
    skipped = 0
    errors = 0

    folder = Path(folder)

    if not folder.is_dir():
        print(f"Folder not found: {folder}")
        return

    with os.scandir(folder) as entries:
        for entry in entries:
            if not entry.is_file(follow_symlinks=False):
                continue

            source = Path(entry.path)
            scanned += 1
            category = EXTENSIONS.get(source.suffix.lower())

            if category is None:
                logging.info("Skipped: %s", source.name)
                skipped += 1
                continue

            destination_folder = folder / category
            destination = destination_folder / source.name

            counter = 1
            while destination.exists():
                destination = destination_folder / (
                    f"{source.stem} ({counter}){source.suffix}"
                )
                counter += 1

            if dry_run:
                logging.info(
                    "Preview: %s -> %s",
                    source.name,
                    destination.relative_to(folder)
                )
                moved += 1
                continue

            try:
                destination_folder.mkdir(exist_ok=True)
                shutil.move(str(source), str(destination))
                logging.info("Moved: %s", source.name)
                moved += 1

            except PermissionError:
                logging.error("Permission denied: %s", source.name)
                errors += 1

            except (OSError, shutil.Error) as error:
                logging.error("Could not move %s: %s", source.name, error)
                errors += 1

    print("\n===== ORGANIZER SUMMARY =====")
    print(f"Files scanned   : {scanned}")
    print(f"Files relocated : {moved}" + (" (preview only)" if dry_run else ""))
    print(f"Files skipped   : {skipped}")
    print(f"Errors          : {errors}")
    print("=============================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Folder to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without moving files"
    )
    args = parser.parse_args()

    organize_folder(args.directory, args.dry_run)