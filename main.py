# import sys

import ffmpy

print('hi')

ff = ffmpy.FFmpeg(
    inputs={'input.mp4': None},
    outputs={'output.avi': None}
)

ff.run()