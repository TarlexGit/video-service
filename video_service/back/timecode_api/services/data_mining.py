import os, pathlib
import pandas as pd
from .checks import data_verification

class Collector:
    """Collect data from files folder"""

    def __init__(self, path) -> None:
        self.path = pathlib.Path(path)
        self.data_path = pathlib.Path.cwd() / self.path
        self.folders = {}

    def scann_folder_with_data(self):
        for root_dir in os.scandir(self.path):
            if not root_dir.name.startswith(".") and root_dir.is_dir():
                x_dirs = os.listdir(root_dir.path)
                df = pd.read_csv(root_dir.path/pathlib.Path('labels.txt'))
                if data_verification(df):
                    self.folders.update({root_dir.name: x_dirs})
                else:
                    continue
                

    def get_csv_path_from_folder(self, folder:str):
        for file_name in self.folders[str(folder)]:
            match file_name.split('.')[1]:
                case 'txt':
                    return self.path/folder/file_name

    def get_timecodes_data(self, folder):
        timecodes = pd.read_csv(folder)
        json_codes = timecodes.to_json()
        return json_codes


if __name__ == "__main__":
    c = Collector()
    c.scann_folder_with_data()
    from checks import check_on_match
    print("\n", c.data_path, "\n", )
    i = 0
    csv_one = c.get_csv_path_from_folder('3')
    timecodes = c.get_timecodes_data(csv_one)
    print(timecodes)