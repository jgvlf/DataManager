from DataManager import DataManager
if __name__ == '__main__':
    yolox_data = DataManager(train=.8, val=.1, test=.1)
    yolox_data.split_data_folders(input_folder="datasets", output_folder="out-datasets")