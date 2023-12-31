from fastapi import *
import os
from serverBE import serverBE

flash_file_name = "testflash.txt"

storage_path = os.path.join(os.getcwd(), "storage")
router = APIRouter()

@router.get("/getdemo/")
async def getDemo():
    file_name = "demofile.pptx"
    file_path = os.path.join(storage_path, file_name)
    return responses.FileResponse(path=file_path, filename=file_name)

@router.get("/getfile/")
async def getFile(file_name = "demofile.pptx"):
    file_path = os.path.join(storage_path, file_name)
    return responses.FileResponse(path=file_path, filename=file_name)

@router.get("/getfilesize/")
async def getFileSize(file_name = "demofile.pptx"):
    file_path = os.path.join(storage_path, file_name)
    return {"size": os.path.getsize(file_path),
            "unit": "byte"}

@router.get("/deleteall/")
async def getFileSize():
    for filename in os.listdir(storage_path):
        file_path = os.path.join(storage_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return {"result":"done"}

@router.get("/deletefile/")
async def getFileSize(file_name = "demofile.pptx"):
    for filename in os.listdir(storage_path):
        if filename != file_name:
            continue
        file_path = os.path.join(storage_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return {"result":"done"}

# to be used

@router.get("/getupdateversion/")
async def getversion():
    data = await serverBE.read()
    print(data)
    if not data["ready"]:
        raise HTTPException(status_code=500, detail="Download file is having issue, please wait.")
    file_path = os.path.join(storage_path, flash_file_name)
    return {
        "version":data["version"],
        "size":os.path.getsize(file_path)
    }

@router.get("/getflash/")
async def getFlash():
    file_path = os.path.join(storage_path, flash_file_name)
    return responses.FileResponse(path=file_path, filename=flash_file_name)
