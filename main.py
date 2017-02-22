import os, sys
from re import split
from ffmpy import FFmpeg
from PIL import Image
import mechanize

name = split('\.', sys.argv[1])
myOutput = os.getcwd() + '/' + name[0] + ' Frames/'
del name

#'''
if not os.path.exists(myOutput):
    os.makedirs(myOutput)

ff = FFmpeg(
    inputs={sys.argv[1]: None},
    outputs={None: [myOutput + "frame%04d.bmp"]}
)

ff.run()

for i in range(1, 9999):

    frame = myOutput + 'frame' + format(i, '04d')

    if os.path.isfile(frame + '.bmp'):
        # print(myOutput + 'frame' + format(i, '04d'))
        im = Image.open(frame + '.bmp')
        im.save(frame + '.jpg', quality=95)
        os.remove(frame + '.bmp')
    else:
        break
#'''
ff = FFmpeg(
    inputs={myOutput + 'frame%04d.jpg': ["-framerate", sys.argv[2]]},
    outputs={'test.mp4': None}
)

ff.run()
del ff
