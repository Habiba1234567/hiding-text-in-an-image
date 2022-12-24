from test import test_hiding_in_image

imgName = "data/image.png"
imgSecretName = "out/imgWithSecret.png"

dataSecretName = "data/data.txt"
dataRecoverName = "out/dataOut.txt"


test_hiding_in_image(imgName, imgSecretName, dataSecretName, dataRecoverName)