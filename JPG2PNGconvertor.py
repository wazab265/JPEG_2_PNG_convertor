from PIL import Image
import sys
import os
target=r'{}'.format(sys.argv[1])
depository=r'{}'.format(sys.argv[2])
parent_dir=r'C:\Users\mega\Desktop'
path=os.path.join(parent_dir,depository)
os.mkdir(path)
tar_path=os.path.join(parent_dir,target)
for filename in os.listdir(tar_path):
	img_loc=os.path.join(tar_path,filename)
	fp=Image.open(img_loc)
	print(fp)
	new_filename=filename.replace('.jpg','.png')
	fp.save(path+ new_filename,'png')




