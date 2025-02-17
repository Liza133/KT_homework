from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

from PIL import Image

import cv2
from moviepy import VideoFileClip, TextClip, CompositeVideoClip

filename = "cutie_cats1.mp4"
width = 100
height = 100
name = Path(filename).stem
extension = Path(filename).suffix
if width and height and extension == '.jpg':
    image_path = f'images\\{filename}'
    img = Image.open(image_path)
    new_image = img.resize((width, height))  # изменяем размер
    new_image.save(f'previews\\{name}_({width}x{height}).jpg')  # сохранение картинки + добавить расширение в назавание
elif width and height and extension == '.mp4':
    video_clip = VideoFileClip(f'videos\\{filename}')
    frame = video_clip.get_frame(5)
    video_clip.close()
    img = Image.fromarray(frame)
    # img = Image.open(image_path)
    new_image = img.resize((width, height))  # изменяем размер
    # new_image.show()
    new_image.save(f'previews\\{name}_({width}x{height}).jpg')  # сохранение картинки + добавить расширение в назавание


















# showing a video, guess I don't need it...
# video_path = 'C:\\Users\\user\\dwhelper\\cutie_cats.mp4'
# video = cv2.VideoCapture(video_path)
# if video.isOpened():
#     print('Video Succefully opened')
# else:
#     print('Something went wrong check if the video name and path is correct')
#
#
# #define a scale lvl for visualization
# scaleLevel = 3 #it means reduce the size to 2**(scaleLevel-1)
#
#
# windowName = 'Video Reproducer'
# cv2.namedWindow(windowName)
# #let's reproduce the video
# while True:
#     ret, frame = video.read() #read a single frame
#     if not ret: #this mean it could not read the frame
#          print("Could not read the frame")
#          cv2.destroyWindow(windowName)
#          break
#
#     reescaled_frame  = frame
#     for i in range(scaleLevel-1):
#         reescaled_frame = cv2.pyrDown(reescaled_frame)
#
#     cv2.imshow(windowName, reescaled_frame )
#
#     waitKey = (cv2.waitKey(1) & 0xFF)
#     if waitKey == ord('q'): #if Q pressed you could do something else with other keypress
#          print("closing video and exiting")
#          cv2.destroyWindow(windowName)
#          video.release()
#          break


