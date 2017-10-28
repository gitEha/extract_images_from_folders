import os
from shutil import copyfile

PATH_TO_IMAGES_TO_EXTRACT = '' #Example: 'E:\\Users\\User\\Desktop\\Machine Learning\\images\\randomimages\\101_ObjectCategories\\'
PATH_TO_EXTRACT_TO = '' #Example: 'E:\\Users\\User\\Desktop\\Machine Learning\\images\\train_cat_or_not\\'

for subdir, dirs, files in os.walk(PATH_TO_IMAGES_TO_EXTRACT):
    for num, file in enumerate(files):
        img_path = os.path.join(subdir, file)
        extract_path = os.path.join(PATH_TO_EXTRACT_TO, 'notcat.' + str(num) + '.jpg')
        copyfile(img_path, extract_path)
