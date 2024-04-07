# pip install barcode
from barcode import EAN13
from barcode.writer import ImageWriter

# 12 digit number which barcode you want to create
number = "787419958500"

# generat barcode
barcode = EAN13(number,writer=ImageWriter())

# save..
barcode.save("E:/PYTHON/PROJECTS/6_BARCODE_GENERATOR/mybarcode")
# no need to specify by defult it saved as 
# png but in case of qrcode we need to specify