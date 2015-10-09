import os
ROOT_PATH = '/var/www/html/xyjie/xyjie/static/imgs/img-fall/'
imgs = os.listdir(ROOT_PATH)
index=1
for fileName in imgs:
	targetName=str(index)+'.jpg'
	os.rename(os.path.join(ROOT_PATH, fileName), os.path.join(ROOT_PATH, targetName))
	print fileName, '==>', targetName
	index=index+1
