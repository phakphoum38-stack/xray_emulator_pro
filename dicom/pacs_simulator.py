import os

class PACSServer:

    def __init__(self):

        self.storage = "pacs_storage"

        os.makedirs(self.storage, exist_ok=True)

    def store(self, dicom_file):

        import shutil

        dst = os.path.join(self.storage, dicom_file)

        shutil.copy(dicom_file, dst)

        print("[PACS] stored:", dst)
