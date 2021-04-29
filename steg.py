from stegano.lsbset import generators
from stegano import lsbset
from stegano import lsb
import numpy as np

#define reading from text file function
with open('secret.txt', 'r+', encoding="utf-8") as source:
      content= source.read()
      print(content)
      
#resources
inIMGpng='dexterLab.png'
outIMGpng='topSecret.png'


#hide message in image
lsb.hide(inIMGpng, message=content).save(outIMGpng)

#reveal message
outmess= lsb.reveal(outIMGpng)

print(F'Reveal Message : {outmess}')