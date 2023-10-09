import os
import time
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

load_dotenv()

REPORT_FILES = ["xls", "xlsx", "ods"]
DOCUMENT_FILES = ["doc", "docx", "txt", "pdf", "rtf", "html", "htm", "odt"]
PRESENTATION_FILES = ["ppt", "pptx"]
VIDEO_FILES = ["mkv", "vob", "avi", "mov", "wmv", "asf", "mp4", "m4p", "m4v",
               "mpg", "mpeg", "m2v", "m4v", "mxf", "flv", "f4v"]
AUDIO_FILES = ["mp4a", "flac", "mp3", "wav", "wma", "aac", "m4a", "wv"]
IMAGE_FILES = ["bmp", "dpx", "gif", "ico", "jpeg", "jpg", "png", "svg", "tiff", "psd", "webp"]

FOLDER_TO_WATCH = os.getenv("FOLDER_WATCHED")
DESTINATION_FOLDER = os.getenv("DESTINATION_FOLDER")


def file_handler(event, file_name):
    if file_name.split(".")[-1] in REPORT_FILES:
        reports_folder = DESTINATION_FOLDER + "\\Reports"
        new_path = os.path.join(reports_folder, file_name)
        os.rename(event.src_path, new_path)
        return
    if file_name.split(".")[-1] in DOCUMENT_FILES:
        documents_folder = DESTINATION_FOLDER + "\\Documents"
        new_path = os.path.join(documents_folder, file_name)
        os.rename(event.src_path, new_path)
        return
    if file_name.split(".")[-1] in PRESENTATION_FILES:
        presentations_folder = DESTINATION_FOLDER + "\\Presentations"
        new_path = os.path.join(presentations_folder, file_name)
        os.rename(event.src_path, new_path)
        return
    if file_name.split(".")[-1] in VIDEO_FILES:
        videos_folder = DESTINATION_FOLDER + "\\Videos"
        new_path = os.path.join(videos_folder, file_name)
        os.rename(event.src_path, new_path)
        return
    if file_name.split(".")[-1] in AUDIO_FILES:
        audio_folder = DESTINATION_FOLDER + "\\Audio"
        new_path = os.path.join(audio_folder, file_name)
        os.rename(event.src_path, new_path)
        return
    if file_name.split(".")[-1] in IMAGE_FILES:
        images_folder = DESTINATION_FOLDER + "\\Images"
        new_path = os.path.join(images_folder, file_name)
        os.rename(event.src_path, new_path)
        return


class FolderWatcher(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return
        file_name = os.path.basename(event.src_path)
        print(f"Handling: {file_name}")

        max_retries = 5
        retry_count = 0
        while retry_count < max_retries:
            try:
                file_handler(event, file_name)
                break
            except PermissionError as ex:
                print(f"File Used. Retry {retry_count}")
                time.sleep(1)
                retry_count += 1


if __name__ == "__main__":
    event_handler = FolderWatcher()
    observer = Observer()
    observer.schedule(event_handler, path=FOLDER_TO_WATCH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt as e:
        observer.stop()
    observer.join()
