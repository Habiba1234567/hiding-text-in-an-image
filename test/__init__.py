from PIL import Image

from src.decode import getDataFromImage
from src.encode import putDataInsideImage

def test_hiding_in_image(imgName, imgSecretName, dataSecretName, dataRecoverName):
    im = Image.open(imgName)
    with open(dataSecretName, "rb") as dataFile:  # Note that we open in binary mode
        secretData = dataFile.read()
    putDataInsideImage(im, secretData)
    im.save(imgSecretName)
    imOut = Image.open(imgSecretName)
    with open(dataRecoverName, "wb") as dataFile:  # Note that we open in binary mode
        dataFile.write(getDataFromImage(imOut))