import os, shutil, random

# preparing the folder structure

full_img_path = 'imagess/'
full_label_path = 'labels/'
extension_allowed = '.png'
split_percentage = 90

parent_path = 'data'
images_path = 'data/images'
if os.path.exists(images_path):
    shutil.rmtree(images_path)
os.mkdir(parent_path)
if os.path.exists(parent_path):
    os.mkdir(images_path)
    
labels_path = 'data/labels/'
if os.path.exists(labels_path):
    shutil.rmtree(labels_path)
os.mkdir(labels_path)
    
training_images_path = images_path + '/training/'
validation_images_path = images_path + '/validation/'
training_labels_path = labels_path + '/training/'
validation_labels_path = labels_path +'/validation/'
    
os.mkdir(training_images_path)
os.mkdir(validation_images_path)
os.mkdir(training_labels_path)
os.mkdir(validation_labels_path)

files = []

ext_len = len(extension_allowed)

for r, d, f in os.walk(full_img_path):
    for file in f:
        if file.endswith(extension_allowed):
            strip = file[0:len(file) - ext_len]      
            files.append(strip)

random.shuffle(files)

size = len(files)                   

split = int(split_percentage * size / 100)

print("copying training data")
for i in range(split):
    strip = files[i]
                         
    image_file = strip + extension_allowed
    src_image = full_img_path + image_file
    shutil.copy(src_image, training_images_path) 
                         
    annotation_file = strip + '.txt'
    src_label = full_label_path + annotation_file
    shutil.copy(src_label, training_labels_path) 

print("copying validation data")
for i in range(split, size):
    strip = files[i]
                         
    image_file = strip + extension_allowed
    src_image = full_img_path + image_file
    shutil.copy(src_image, validation_images_path) 
                         
    annotation_file = strip + '.txt'
    src_label = full_label_path + annotation_file
    shutil.copy(src_label, validation_labels_path) 

print("finished")