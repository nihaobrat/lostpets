import qrcode

def qrcreate():
    # import url
    res = str(input())
    img = qrcode.make(res)
    type(img)
#Enter image № for creating qr code
    img.save("qr7.png")



qrcreate()
