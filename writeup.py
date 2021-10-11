image = open('prob1.img','rb')
magic = image.read(4)
topoffset = image.read(4)

print("magic: ",magic)
print("offset:",topoffset)
image.seek(int.from_bytes(topoffset,'big'))

dirflag = image.read(1)
print("dirflag:", dirflag)

dirname = image.read(16)
print("dirname:", dirname)

dirnum = image.read(4)
print("dirnum:", dirnum)

filenum = image.read(4)
print("filenum:", filenum)

fileoffset = image.read(4)
print("fileoffset:", fileoffset)

image.seek(int.from_bytes(fileoffset,'big'))

fileflag = image.read(1)
print("fileflag:", fileflag)

filename = image.read(32)
print("filename:", filename)

filesize = image.read(4)
print("filesize:", filesize)

fileflag = int.from_bytes(fileflag,'big')

if fileflag & 0b10:
    print("encrypted file name detected.")

    #filename = [j for j in filename]

    key =  "xm4s!xm4s!xm4s!xm4s!xm4s!xm4s!xm4s!"
    key = [ord(j) for j in key]
    #flag = [ord(j) for j in flag]
    
    dec = [key[j] ^ filename[j] for j in range(len(filename))]
    dec = b''.join([j.to_bytes(1,byteorder='big') for j in dec])
    print(dec)
else:
    print(filename)
