import pyzxing

# Initialize ZXing reader
reader = pyzxing.BarCodeReader()

# Decode the image
barcode = reader.decode('/home/thierry/robotics/decoding-codes/decoding/datamatrix_code.jpg')

if barcode:
    print("Decoded Data:", barcode[0]['raw'])
else:
    print("No Data Matrix code found.")
