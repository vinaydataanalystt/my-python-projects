import qrcode
import cv2

text = input("Enter text or link: ")
img = qrcode.make(text)
img.save("my_qr.png")
print("QR code saved as my_qr.png")

img = cv2.imread("my_qr.png")
detector = cv2.QRCodeDetector()
data, points, _ = detector.detectAndDecode(img)
print("QR code says:", data)