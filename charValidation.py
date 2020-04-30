import PIL
#import pytesseract as pyt
import cv2 

img = cv2.imread('creepy-notes-1.png')
def charSeg(img):
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
  im2,ctrs, hier = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
  cv2.CHAIN_APPROX_SIMPLE)
  sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
  for i, ctr in enumerate(sorted_ctrs):
      x, y, w, h = cv2.boundingRect(ctr)
      roi = img[y:y+h, x:x+w]
      #cv2.imwrite('roi_imgs.png', roi)
      #cv2.imshow('character'+str(i), roi)
      #cv2.rectangle(img,(x,y),( x + w, y + h ),(90,0,255),2)
      file= open('lower_case', "a")
      file.write(roi)

fileText=charSeg(img)      
charArray= fileText.split()
noSpace=[]

for i in charArray:
  str(i).replace(' ', '')
  noSpace.append(i)

sent= "t h e q u i c k b r o w n f o x j u m p s o v e r t h e l a z y d o g"
new=sent.split()

letters=[]
for i in new:
  str(i).replace(' ', '')
  letters.append(i)

for i in noSpace:
  num=0
  num+=1
  if noSpace[num]!= letters[num]:
    noSpace.relace(noSpace[num], letters[num])
  else:
    break

fileText2=charSeg(img2)      
charArray2= fileText2.split()
noSpace2=[]

for i in charArray:
  str(i).replace(' ', '')
  noSpace2.append(i)

sent2= "T H E Q U I C K B R O W N F O X J U M P S O V E R T H E L A Z Y D O G"
new2=sent.split()

letters2=[]
for i in new2:
  str(i).replace(' ', '')
  letters2.append(i)

for i in noSpace2:
  num=0
  num+=1
  if noSpace2[num]!= letters2[num]:
    noSpace2.replace(noSpace2[num], letters2[num])
  else:
    break


