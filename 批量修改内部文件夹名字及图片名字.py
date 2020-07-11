import os
import cv2
from PIL import Image
outer_path = r"C:\Users\18327\Desktop\xie"
folderlist = os.listdir(outer_path)          #列举文件夹
out_dir = "C:/Users/18327/Desktop/label1/"


def load_image(path):
# cv2.cvtColor(p1,p2) 是颜色空间转换函数，p1是需要转换的图片，p2是转换成何种格式。
    # cv2.COLOR_BGR2RGB 将BGR格式转换成RGB格式
    # cv2.COLOR_BGR2GRAY 将BGR格式转换成灰度图片
    image = cv2.cvtColor(cv2.imread(path,-1), cv2.COLOR_BGR2RGB)
    return image
for folder in folderlist:     
	inner_path = os.path.join(outer_path, folder)
	total_num_folder = len(folderlist)       #文件夹的总数
	print ('total have %d folders' % (total_num_folder) )  #打印文件夹的总数
	filelist = os.listdir(inner_path)        #列举图片
	i = 0

	for item in filelist:
		total_num_file = len(filelist)  #单个文件夹内图片的总数
		if item.endswith('.png'):
			#
			# img = cv2.imread(inner_path + item)
			# Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			# ret, thresh = cv2.threshold(Grayimg, 0, 256, cv2.THRESH_BINARY)
			# cv2.imwrite(out_dir + item, thresh)
			# input_image = utils.load_image(train_input_names[id])


			# if item == img.png
			src = os.path.join(os.path.abspath(inner_path), item)           #原图的地址
			dst = os.path.join(os.path.abspath(inner_path), str(folder) +str(i) + '.png')
			#新图的地址（这里可以把str(folder) + '_' + str(i) + '.jpg'改成你想改的名称）
			# input_image = load_image(src)
			# cv2.imwrite(out_dir + item, input_image)

			# img = cv2.imread(src)
			# cv2.imwrite(out_dir, img)
			try:
				os.rename(src, dst)
				print ('converting %s to %s ...' % (src, dst))
				image = Image.open(dst)
				# out = os.path.join(os.path.abspath(out_dir), str(folder) +str(i) + '.png')
				image.save(out_dir)
				# i += 1
			except:
				continue
	print ('total %d to rename & converted %d jpgs' % (total_num_file, i))
