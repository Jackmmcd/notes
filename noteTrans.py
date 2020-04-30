import PIL
#import pytesseract as pyt
import cv2 

img= cv2.imread('notes.jpg')

def detect_text(img):
  text= pyt.image_to_string(Image, ('creepy-notes-1.png'))
  return text

detect_text(img)

while str(text)== True:
  file= open('notes.txt', "a")
  file.write(text)
  file.close()
file_text = open('notes.txt',"a")
