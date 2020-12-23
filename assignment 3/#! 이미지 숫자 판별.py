def read_img(img_name):
    with open(img_name,'rb') as f:
        data = f.read()
        img = data[-512:]
    img_num = list(img)
    det_list = img_num[272:288]
    det_string = ''
    for i in range(len(det_list)):
         det_string += str(det_list[i])
    middle_det = det_string.split('0')
    last_det = 0
    for i in range(len(middle_det)):
        if middle_det[i]:
            last_det += 1
    if last_det == 3:
        return 0
    else:
        return 1
print(read_img("C:\doit\\t1.bmp"))
print(read_img("C:\doit\\t2.bmp"))
print(read_img("C:\doit\\t3.bmp"))
print(read_img("C:\doit\\t4.bmp"))
print(read_img("C:\doit\\t5.bmp"))