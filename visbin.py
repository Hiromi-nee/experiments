#usage python visbin.py inputfile output.png width
#example python visbin.py derp.elf lol.png 512
import struct
import sys
import Image, numpy

infile = sys.argv[1]
outfile = sys.argv[2]
width = int(sys.argv[3])
bytelist = []

def array2image(a):
    im = Image.Image()
    im = Image.fromarray(numpy.uint8(a))
    return im

fi = open(infile, 'rb')
print "Reading file..."
for abyte in fi.read():
    bytelist += struct.unpack('B', abyte)
fi.close()
print "File reading done."
n = width
print "Performing dark magic.."
vect = [bytelist[i:i+n] for i in range(len(bytelist)-n+1)]
print "Generating image..."
imeji = array2image(vect)
imeji.save(outfile)
print "Image generated."

