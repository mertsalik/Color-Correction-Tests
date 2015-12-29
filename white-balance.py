from SimpleCV import Image

__author__ = 'mertsalik'


def test_whiteBalance():
    img = Image("BadWB2.jpg")
    output = img.whiteBalance()
    output2 = img.whiteBalance(method="GrayWorld")
    output.save("BadWB2_1.jpg")
    output2.save("BadWB2_2.jpg")


test_whiteBalance()
