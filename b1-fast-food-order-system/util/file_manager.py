import pandas as pd


class CSVFileManager:
    # Lectura CSV
    def __init__(self, file_path: str):
        self.file_path = file_path

    # CSV a DataFrame
    def read(self):
        return pd.read_csv(self.file_path)

    def write(self, data_frame):
        data_frame.to_csv(self.file_path, index=False)