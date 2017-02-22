import os
from ffmpy import FFmpeg
from PIL import Image
#import mechanize

myInput = 'IMG_0697.mov'
myOutput = os.getcwd() + '/Frames/'

print('sup')
'''
if not os.path.exists(myOutput):
    os.makedirs(myOutput)

ff = FFmpeg(
    inputs={myInput: None},
    outputs={None: [myOutput + "frame%04d.bmp"]}
)

ff.run()
del ff

for i in range(1, 9999):

    frame = myOutput + 'frame' + format(i, '04d')

    if os.path.isfile(frame + '.bmp'):
        # print(myOutput + 'frame' + format(i, '04d'))
        im = Image.open(frame + '.bmp')
        im.save(frame + '.jpg', quality=95)
        os.remove(frame + '.bmp')
    else:
        break
'''
ff = FFmpeg(
    inputs={myOutput + 'frame%04d.jpg': None},
    outputs={'test.mp4': ['-r', "60"]}
)

ff.run()
del ff
