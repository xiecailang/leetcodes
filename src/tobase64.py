import base64
f = open('J:\\imgs\\0920.png', 'rb')
ls_f = base64.b64encode(f.read())
f.close()
print(ls_f)
