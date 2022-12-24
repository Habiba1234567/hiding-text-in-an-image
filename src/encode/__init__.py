def getDataBits(data):
    bits = []
    for byte in data:
        for b in range(0, 8):
            bits.append((byte >> b) & 0b1)
    return bits


def putDataInsideImage(im, data):
    dataBits = getDataBits(data)

    maxX = im.size[0]  # width of the image
    maxY = im.size[1]  # height of the image
    maxC = len(im.getpixel((0, 0)))  # number of channels in the image

    x = 0  # x coordinate of the pixel
    y = 0  # y coordinate of the pixel
    c = 0  # color channel of the pixel

    for bit in dataBits:
        color = list(im.getpixel((x, y)))
        color[c] = (color[c] & (~0b1)) | bit
        im.putpixel((x, y), tuple(color))

        c += 1  # we first iterate through the color channel
        if c >= maxC:
            c = 0
            x = x + 1  # then through the x coordinate
            if x >= maxX:
                x = 0
                y = y + 1  # and finally through the y coordinate
                if y >= maxY:
                    print("Not enough pixels!")
                    return
