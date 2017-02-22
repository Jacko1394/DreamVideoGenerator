from os import remove

from ffmpy import FFmpeg

from PIL import Image

myInput = 'IMG_0697.mov'
myOutput = '/frames/'

print('hi')

ff = FFmpeg(
    inputs={myInput: None},
    outputs={None: ["frame%04d.bmp"]}
)

ff.run()
del ff

im = Image.open('frame0400.bmp')
im.save('frame2.jpg', quality=95)
