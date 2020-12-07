from kedro.io.core import AbstractDataSet, DataSetError

from base64 import b64encode

class Base64DataSet(AbstractDataSet):
    def __init__(self, filepath):
        self._filepath = filepath

    def _save(self):
        with open(str(self._filepath), "w") as f:
            f.write(b64encode(binary_data).decode("utf8"))


    def _load(self):
        raise  DataSetError("Write Only Dataset")

    def _describe(self):
        return dic(filepath=self._filepath)