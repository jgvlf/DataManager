from .pre_process import PreProcess


class DataManager(PreProcess):

    def __init__(self, train: float, val: float, test: float):
        self._train_size = train
        self._val_size = val
        self._test_size = test
        super().__init__(self._train_size, self._val_size, self._test_size)

    def split_data_folders(self, input_folder, output_folder):
        from splitfolders import ratio
        ratio(input_folder, output=output_folder, ratio=(self._train_size, self._val_size, self._test_size))
