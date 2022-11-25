import qrcode
a=qrcode.QRCode(version=1,box_size=50,border=2)
a.add_data("STUDENT ATTENDANCE SYSTEM")
a.make(fit=True)
b=a.make_image(fill_color="BLACK",back_color="white")
b.save("avi.png")
