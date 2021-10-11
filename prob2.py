image = open('prob2.img','wb')

image.write(b'\xde\xad\xbe\xaf')
image.write(b'\x00\x00\x00\x08')
image.write(b'\x00')
image.write(b'mydir2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x01')
offset = (image.tell()+4).to_bytes(4,byteorder='big')
image.write(offset)
image.write(b'\x00')
image.write(b'flag.txt' + b'\x00' * (32 - 8))
image.write(b'\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x00')
image.write(b'\x00\x00\x00\x00')

key =  "xm4s!xm4s!xm4s!xm4s!xm4s!xm"
flag = "xm4s{you_find_a_file_name!}"
key = [ord(j) for j in key]
flag = [ord(j) for j in flag]

enc = [key[j] ^ flag[j] for j in range(len(flag))]
enc = b''.join([j.to_bytes(1,byteorder='big') for j in enc])
