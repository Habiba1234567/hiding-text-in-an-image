from PIL import Image

imgName = "image.png"
imgSecretName = "imgWithSecret.png"

dataSecretName = "data.txt"
dataRecoverName = "dataOut.txt"


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


def getBitsFromImage(im, maxBits=0):
    bits = []

    maxC = len(im.getpixel((0, 0)))
    for y in range(0, im.size[1]):
        for x in range(0, im.size[0]):
            for c in range(0, maxC):
                bits.append(im.getpixel((x, y))[c] & 0b1)
                if maxBits != 0 and len(bits) >= maxBits:
                    return bits

    return bits


def bitsToBytes(dataBits):
    dataBytes = []
    for i in range(0, len(dataBits), 8):
        if i + 7 >= len(dataBits):
            break

        currByte = 0
        for b in range(0, 8):
            currByte = currByte | (dataBits[i + b] << b)

        dataBytes.append(currByte)

    return bytes(dataBytes)


def getDataFromImage(im):
    dataBits = getBitsFromImage(im)
    return bitsToBytes(dataBits)


# knowing the order in which we save the bits is important when recovering the data from the image

im = Image.open(imgName)
with open(dataSecretName, "rb") as dataFile:  # Note that we open in binary mode
    secretData = dataFile.read()
putDataInsideImage(im, secretData)
im.save(imgSecretName)


imO = Image.open(imgSecretName)
with open(dataRecoverName, "wb") as dataFile:  # Note that we open in binary mode
    dataFile.write(getDataFromImage(im))
