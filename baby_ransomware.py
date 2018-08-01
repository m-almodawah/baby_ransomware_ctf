from twofish import Twofish
start='keykey'
end='11111'
flag = b'\x61\xd1\xd3\x3c\x8f\xcf\x28\xd6\xe3\xff\x8e\xd3\xab\x1d\x00\x6d'

for i in range(10000,100000):
    key = str.encode(start + str(i) + end)
    T = Twofish(key)
    out = T.decrypt(flag)
    try:
        outString = out.decode()
        if 'bank' in outString:
            print(outString + '   ' + key)
    except:
        pass
