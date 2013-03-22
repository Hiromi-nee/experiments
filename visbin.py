#usage python visbin.py inputfile output.png width
#example python visbin.py derp.elf lol.png 512
import struct
import sys
import Image, numpy

infile = sys.argv[1]
outfile = sys.argv[2]
try:
    width = int(sys.argv[3])
except IndexError:
    width = 128
vect = []

def array2image(a):
    im = Image.Image()
    im = Image.fromarray(numpy.uint8(a))
    return im

fi = open(infile, 'rb')
print "Reading file..."

count = 0
while True:
    piece = fi.read(width)
    if piece == "":
        break
    widthlist = []
    for abyte in piece:
        widthlist += struct.unpack('B', abyte)
    if count%2 !=0:
        widthlist.reverse()
    if len(widthlist) < width:
        for i in range(width-len(widthlist)):
            widthlist+=[0]                           
    vect.append(widthlist)
    
fi.close()

print "File reading done."
print "Generating image..."
imeji = array2image(vect)
imeji.save(outfile)
print "Image generated. Written to ",outfile

