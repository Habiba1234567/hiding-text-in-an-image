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


def getDataFromImage(im):
    dataBits = getBitsFromImage(im)
    return bitsToBytes(dataBits)
