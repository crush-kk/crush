from abc import  abstractmethod, ABC
class ProcessStrategy(ABC):

    @abstractmethod
    def process_file(self, filepath):
        pass
class ExcelStrategy(ProcessStrategy):
    def process_file(self, filepath):
        print("Processing Excel file.")
class CSVStrategy(ProcessStrategy):
    def process_file(self, filepath):
        print("Processing CSV file.")


class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_type = file_path.split(".")[-1]
    def process_file(self):
        if self.file_type == "csv":
            ExcelStrategy().process_file(self.file_path)
        elif self.file_type == "xlsx":
            ExcelStrategy().process_file(self.file_path)
if __name__ == '__main__':
    file_processor = FileProcessor("file.xlsx")
    file_processor.process_file()