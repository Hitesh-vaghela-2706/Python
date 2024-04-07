import qrcode
# pip install qrcode
url = "https://www.instagram.com/hitesh_818/"
img = qrcode.make(url)
img.save("E:/PYTHON/PROJECTS/5_QR_CODE_GENERATER/my_insta_qrcode.png")

url2 = "https://www.youtube.com/c/ThunderLover"
img = qrcode.make(url2)
img.save("E:/PYTHON/PROJECTS/5_QR_CODE_GENERATER/my_youtube_qrcode.png")