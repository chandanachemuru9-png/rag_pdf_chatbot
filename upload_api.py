from fastapi import FastAPI, UploadFile, File
import shutil
import os
import subprocess

app = FastAPI()

UPLOAD_FOLDER = "data"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    subprocess.run(["python", "ingest.py"])

    return {"message": "PDF uploaded and indexed"}