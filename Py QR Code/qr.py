import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Data
genData = input("QR Code Content: ")

# Generate
qr = pyqrcode.create(genData)
qr.png(f'{genData}.png', scale=8)

# Generated message
if qr:
    print("Your QR Code Is Generated!")

# Read
readInput = input("Do you what to read your qr code? (y/n): ")
Yes = "y"
No = "n"
read = decode(Image.open(f'{genData}.png'))
readMsg = read[0].data.decode('ascii')
if readInput == Yes:
    print(f'Your qr code says: {readMsg}')    
elif readInput == No:
    print("Thank You!")
else:
    print("Your responce was invalid")
