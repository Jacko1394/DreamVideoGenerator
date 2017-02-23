import os, sys
from re import split
from ffmpy import FFmpeg
from PIL import Image


name = split('\.', sys.argv[1])
myOutput = os.getcwd() + '/' + name[0] + '_Frames/'
del name
print(myOutput)
'''
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
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import contextlib
from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of


def wait_for_page_load(self, timeout=30):
    old_page = self.find_element_by_tag_name('html')
    yield
    WebDriverWait(self, timeout).until(staleness_of(old_page))

driver = webdriver.Firefox()

driver.implicitly_wait(20)

driver.get('https://deepdreamgenerator.com/generator')


elem = driver.find_element_by_name('email')
elem.clear()
elem.send_keys('jacko1394@me.com')
elem = driver.find_element_by_name('password')
elem.clear()
elem.send_keys('VFy-LHd-25E-duR')
elem = driver.find_element_by_class_name('btn')
elem.click()

# wait_for_page_load(driver, timeout=10)
# wait_for_page_load(driver, timeout=10)

#WebDriverWait(driver, 15)
elem = driver.find_element_by_id('image-for-dream')
#elem.click()
elem.send_keys('/Users/AllEqualsNothing/Documents/DreamVideoGenerator/IMG_0697_Frames/frame0300.jpg')

#elem.send_keys(Keys.RETURN)

#driver.get('https://deepdreamgenerator.com/generator-style')

#assert "No results found." not in driver.page_source
driver.close()

'''
ff = FFmpeg(
    inputs={myOutput + 'frame%04d.jpg': ["-framerate", sys.argv[2]]},
    outputs={'test.mp4': None}
)

ff.run()
del ff
'''
