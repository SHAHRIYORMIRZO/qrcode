import qrcode
import image

qr = qrcode.QRCode(
  version=15,
  box_size=5,
  border=5,
)
data="https://mirzoportfolio.netlify.app"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fillcolor='green', back_color="white")
img.save('qrcode/test.png')