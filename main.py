import shutil

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

from PIL import Image
from moviepy import VideoFileClip
import uuid

from db import connection, table_creation, insert


conn = connection()


app = FastAPI()


@app.post("/upload/")
def upload_file(file: UploadFile):
    extension = Path(file.filename).suffix
    if extension == '.jpg':
        path = f'images\\{file.filename}'
        type = 'IMG'
        with open(path, "wb") as wf:
            shutil.copyfileobj(file.file, wf)
            file.file.close()  # удалаяет временный
    elif extension == '.mp4':
        path = f'videos\\{file.filename}'
        type = 'VID'
        with open(path, "wb") as wf:
            shutil.copyfileobj(file.file, wf)
            file.file.close()
    else:
        raise HTTPException(status_code=415)
    # создаем табличку если еще не создана
    table_creation(conn)
    # insert-им в нее данные
    insert(conn, str(uuid.uuid4()), path, type, file.size)
    return {"path": path}



@app.get("/download/{filename}")
def download_file(filename: str, width: int = None, height: int = None):
    name = Path(filename).stem
    extension = Path(filename).suffix
    if width and height and extension == '.jpg' and Path(f'images\\{filename}').exists():
        image_path = f'images\\{filename}'
        img = Image.open(image_path)
        new_image = img.resize((width, height))     # изменяем размер
        new_image.save(f'previews\\{name}_({width}x{height}).jpg')     # сохранение картинки + добавить расширение в назавание
        return FileResponse(path=f'previews\\{name}_({width}x{height}).jpg',
                            media_type='application/octet-stream')
    elif width and height and extension == '.mp4' and Path(f'videos\\{filename}').exists():
        video_clip = VideoFileClip(f'videos\\{filename}')
        frame = video_clip.get_frame(5)
        video_clip.close()
        img = Image.fromarray(frame)
        # img = Image.open(image_path)
        new_image = img.resize((width, height))  # изменяем размер
        new_image.save(f'previews\\{name}_({width}x{height}).jpg')  # сохранение картинки + добавить расширение в назавание
        return FileResponse(path=f'previews\\{name}_({width}x{height}).jpg',
                            media_type='application/octet-stream')
    else:
        if extension == '.jpg' and Path(f'images\\{filename}').exists():
            return FileResponse(path=f'images\\{filename}',
                                media_type='application/octet-stream')
        elif extension == '.mp4' and Path(f'videos\\{filename}').exists():
            return FileResponse(path=f'videos\\{filename}',
                                media_type='application/octet-stream')
    raise HTTPException(status_code=404)













