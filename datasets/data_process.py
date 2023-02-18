import os
#import random


# 获取文件夹所有子文件
def get_file(path):
    all_files = []
    for home, dirs, files in os.walk(path):
        for filename in files:
            name = os.path.join(home, filename)
            name = name.replace('\\', '/')
            all_files.append(name)
    return all_files


if __name__ == "__main__":
    data_floder = 'image_train'
    data_list = get_file(data_floder)
    
    val_list = [data_list[i] for i in range(0, len(data_list), 10)]
    train_list = [i for i in data_list if i not in val_list]
    
    with open('train.txt', 'w') as f:
        for train_file in train_list:
            train_file = './datasets/' + train_file
            f.write('%s\t%s\n'%(train_file, train_file[:-3].replace('image_train', 'txt_train')+'txt'))
    f.close()
    
    with open('test.txt', 'w') as f:
        for val_file in val_list:
            val_file = './datasets/' + val_file
            f.write('%s\t%s\n'%(val_file, val_file[:-3].replace('image_train', 'txt_train')+'txt'))
    f.close()
