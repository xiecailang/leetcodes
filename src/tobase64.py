import base64
f = open('H:\\lyangblog\\img\\0904.png', 'rb')
ls_f = base64.b64encode(f.read())
f.close()
print(ls_f)
