from DataManager import DataManager

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-ts', '--train_size', type=float)
parser.add_argument('-vs', '--val_size', type=float)
parser.add_argument('-tts', '--test_size', type=float)
parser.add_argument('-inf', '--input_name_folder', type=str)

args = parser.parse_args()

if __name__ == '__main__':
    yolox_data = DataManager(train=args.train_size if args.train_size is not None else .8,
                             val=args.val_size if args.val_size is not None else .1,
                             test=args.test_size if args.test_size is not None else .1)
    yolox_data.split_data_folders(input_folder=args.input_name_folder if args.input_name_folder is not None else "datasets", output_folder="out-datasets")