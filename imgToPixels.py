from PIL import Image
import numpy as np
import os
import csv

# default format can be changed as needed
def createFileList(myDir, format='.jpeg'):
    fileList = []
    labels = []
    names = []
    keywords = {"food" : "1","not": "0",} #if its f - picture of a foodtruck and if not it isn't a foodtruck
    for root, dirs, files in os.walk(myDir, topdown=True):
            for name in files:
                if name.endswith(format):
                    fullName = os.path.join(root, name)
                    fileList.append(fullName)
                for keyword in keywords:
                    if keyword in name:
                        labels.append(keywords[keyword])
                    else:
                        continue
                names.append(name)
    return fileList, labels, names

# load the original image
myFileList, labels, names  = createFileList('./Data')

with open('dataset.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(["label", "pixels"])

for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # img_file.show()

# get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

# Make image Greyscale
    img_grey = img_file.convert('L')
    #img_grey.save('result.png')
    #img_grey.show()

# Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((width, height))
    value = value.flatten()
    value = np.append(value,labels[-1])
    print(value[-1])
    
    with open('dataset.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow([value[-1], ' '.join(value[:-1])])
    