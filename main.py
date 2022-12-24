from PIL import Image

from src.decode import getDataFromImage
from src.encode import putDataInsideImage

imgName = "image.png"
imgSecretName = "imgWithSecret.png"

dataSecretName = "data.txt"
dataRecoverName = "dataOut.txt"

# knowing the order in which we save the bits is important when recovering the data from the image

im = Image.open(imgName)
with open(dataSecretName, "rb") as dataFile:  # Note that we open in binary mode
    secretData = dataFile.read()
putDataInsideImage(im, secretData)
im.save(imgSecretName)


imO = Image.open(imgSecretName)
with open(dataRecoverName, "wb") as dataFile:  # Note that we open in binary mode
    dataFile.write(getDataFromImage(im))