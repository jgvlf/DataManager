from abc import abstractmethod, ABC


class PreProcess(ABC):

    def __init__(self, train_size, val_size, test_size):
        self._train_size = train_size
        self._val_size = val_size
        self._test_size = test_size

    @abstractmethod
    def split_data_folders(self, input_folder, output_folder):
        pass
