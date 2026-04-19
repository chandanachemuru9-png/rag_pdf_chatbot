from fastapi import UploadFile, File
import shutil
import os
from ingest import process_pdf

UPLOAD_DIR = "data"

def save_file(file: UploadFile):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


def handle_upload(file: UploadFile):
    file_path = save_file(file)

    # process immediately
    process_pdf(file_path)

    return {"message": "File uploaded and processed"}