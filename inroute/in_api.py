from fastapi import *
import os

storage_path = os.path.join(os.getcwd(), "storage")
router = APIRouter()

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    fpath = os.path.join(storage_path, file.filename)
    try:
        contents = file.file.read()
        with open(fpath, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return {"message": "Successfully uploaded"}


