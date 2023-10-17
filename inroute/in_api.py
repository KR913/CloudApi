from fastapi import *
import os
import multiprocessing

from serverBE import serverBE

lockLoad = multiprocessing.Lock()

secured_password = "abctest"
flash_file_name = "testflash.txt"

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

@router.post("/uploadflash/")
async def create_upload_flash_file(file: UploadFile, password="", version = 0):
    if password!= secured_password:
        raise HTTPException(status_code=401, detail="You have no authority to update this")
    with lockLoad:
        fpath = os.path.join(storage_path, flash_file_name)
        try:
            contents = file.file.read()
            with open(fpath, 'wb') as f:
                f.write(contents)
        except Exception:
            data = serverBE.read()
            await serverBE.write({
                "version":data["version"],
                "ready":False
                            })
            raise HTTPException(status_code=500, detail="Server error.")
        finally:
            file.file.close()
        await serverBE.write({
            "version":version,
            "ready":True
                        })
    return {"message": "Successfully uploaded"}
