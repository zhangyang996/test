from PIL import Image
import os
import cv2
input_dir = "C:/Users/18327/Desktop/xie"
out_dir = "C:/Users/18327/Desktop/label1/"
b = os.listdir(input_dir)
for j in b:
    inner_path = os.path.join(input_dir, j)
    a = os.listdir(inner_path)

    for i in a:
        if i.endswith('0.png'):

            print(i)
            c = os.path.join(inner_path, i)
            img = cv2.imread(c)
            Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(Grayimg, 0, 256, cv2.THRESH_BINARY)
            cv2.imwrite(out_dir+i, thresh)
        # I = Image.open(input_dir+i)
        # L = I.convert('L')
        # L.save(out_dir+i)