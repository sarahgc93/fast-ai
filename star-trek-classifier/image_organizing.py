from os import listdir, rename
import random

def train_test_move(image_path, train_perc, new_train_path, new_test_path):
    '''
    Purpose: This function randomly splits files into training and test subsets, and moves
        files corresponding to the expected directories for fast.ai
    
    Parameters:
        image_path: original location of images
        train_perc: percent of images you want in training set, in [0,1]
        new_train_path: location where training images will be stored
        new_test_path: location where test images will be stored
    
    '''
    # pull names of file paths from original location
    image_list = listdir(image_path)
    
    # calculate the number of images to be included in the training set    
    train_num = round(train_perc * len(image_list))
    
    # randomize the order of these image paths
    random.seed = 456
    random.shuffle(image_list)
    
    # create lists of train test images names
    train_images = image_list[:train_num]
    test_images = image_list[train_num:]
    
     # test that there are no images in both folders
    if (len(set(train_images) & set(test_images)) > 0 ):
        print ("Training set and test set are not distinct!")
    
    # move the train images to the train folder
    for i in train_images:
        rename(image_path + '/' + i, new_train_path + '/' + i)
    
    # move the test images to the test folder
    for i in test_images:
        rename(image_path + '/' + i, new_test_path + '/' + i)
    
    print("Images from " + image_path + " have been moved to train and test folders, which are respectively "
          + new_train_path + ' and ' + new_test_path)
    


# move the files for each species. note i already moved cardassians so if you're replicating my projet, do that too

train_test_move(image_path= 'downloads/ star trek andorian', train_perc = 0.75, new_train_path='images/train/andorian' , new_test_path='images/valid/andorian')

train_test_move(image_path= 'downloads/star trek ferengi', train_perc = 0.75, new_train_path='images/train/ferengi' , new_test_path='images/valid/ferengi')

train_test_move(image_path= 'downloads/star trek klingon', train_perc = 0.75, new_train_path='images/train/klingon' , new_test_path='images/valid/klingon')

train_test_move(image_path= 'downloads/star trek vulcan', train_perc = 0.75, new_train_path='images/train/vulcan' , new_test_path='images/valid/vulcan')
