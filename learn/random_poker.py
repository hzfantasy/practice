# import random
# sample = [i for i in range(1, 36)]
# r1 = random.sample(sample, k=5)
# print(r1)

import qrcode

a = qrcode.make("https://www.baidu.com")
a.save("test.png")

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.ERROR_CORRECT_Q,
#     box_size=4,
#     border=2
# )
# qr.add_data("http://www.baidu.com")
# qr.make(fit=True)
# img = qr.make_image(fill_color="yellow", back_color="blue")
# img.save("baidu.png")
