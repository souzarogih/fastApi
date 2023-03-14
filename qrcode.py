import pyqrcode
import png
from PIL import Image


def generate_qr_code(data):
    print("Chegou no generate")
    qr_code = pyqrcode.create(data)
    qr_code_resp = qr_code.png("QRCode.png", scale=5)
    print(Image.open("QRCode.png"))
    return qr_code_resp


print(generate_qr_code("testando"))
