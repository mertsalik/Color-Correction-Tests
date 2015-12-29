import operator
from PIL import Image


def equalize(im):
    h = im.convert("L").histogram()
    lut = []
    for b in range(0, len(h), 256):
        # step size
        step = reduce(operator.add, h[b:b + 256]) / 255
        # create equalization lookup table
        n = 0
        for i in range(256):
            lut.append(n / step)
            n = n + h[i + b]
    # map image through lookup table
    return im.point(lut * im.layers)


if __name__ == "__main__":
    img = Image.open("DSC00628.JPG")
    result = equalize(img)
    result.save("Result.JPG")
