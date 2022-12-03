import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def generate_qrcode(data):
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=4)
	qr.add_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
	image = qr.make_image(fill_color="black", back_color="white")
	image.save("qrcode.png")

def Decode_Qrcode(file_name):
	result = decode(Image.open(file_name))
	print("Data:", result[0][0].decode())

generate_qrcode("Hello this is just a test hehe")
Decode_Qrcode("qrcode.png")
