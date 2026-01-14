import qrcode

url_to_generate_qr_code_for = input("Please provide a url for which a qr code will be generated:\n")
qr_file_name = input("Please provide a name for the qr file:\n")

if not(qr_file_name.endswith(".png")):
    qr_file_name = qr_file_name + ".png"

img = qrcode.make(url_to_generate_qr_code_for)
img.save(qr_file_name)

