from stegano.lsbset import generators
from stegano import lsbset
from stegano import lsb
import numpy as np

#image files for steganography
inIMGpng='dexterLab.png'
outIMGpng='topSecret.png'

def convertToSteg():
      print("Encoding text data to image")
      with open('passlist.txt', 'r+', encoding="utf-8") as source:
            content= source.read()
      lsb.hide(inIMGpng, message=content).save(outIMGpng) #hide message in image

def RevealData():
      outmess= lsb.reveal(outIMGpng)
      with open('reveal.txt','a') as dest:
            dest.write(outmess)

