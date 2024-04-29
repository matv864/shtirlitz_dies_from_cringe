from fastapi import UploadFile
from fastapi.responses import FileResponse

import os
from asyncio import sleep
import aiofiles

from time import time

STORAGE_PATH = f"{os.getcwd()}/storage"


async def generate_name(filename: str):
    await sleep(0.0000001)
    suffix = filename.split(".")[-1]
    return f"{time():10.7f}".replace(".", "") + f".{suffix}"


async def check_folder(id: int):
    pathfolder = f"{STORAGE_PATH}/pets_media/{id}"
    if not os.path.exists(pathfolder):
        os.mkdir(pathfolder)


async def save_file(card_id: int, file: UploadFile):
    await check_folder(card_id)
    filename = await generate_name(file.filename)
    pathfile = f"{STORAGE_PATH}/pets_media/{card_id}/{filename}"
    async with aiofiles.open(pathfile, 'wb') as out_file:
        while content := await file.read(1024):  # async read chunk
            await out_file.write(content)  # async write chunk
    return filename


async def delete_file(card_id: int, filename: str):
    full_path = f"{STORAGE_PATH}/pets_media/{card_id}/{filename}"
    if os.path.isfile(full_path):
        os.remove(full_path)


async def get_file(card_id: int, filename: str):
    return FileResponse(f"{STORAGE_PATH}/pets_media/{card_id}/{filename}")
