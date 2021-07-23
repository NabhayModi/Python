import dropbox


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)


def main():
    access_token = "FLua0-WtPjoAAAAAAAAAAbBCsUTDLJXYg1ZzIjtMM8ezb0pNer_HJOAJuVyPnT2_"
    transferData = TransferData(access_token)
    file_from = input("Enter File Name")
    file_to = input("Enter File Path to upload to dropbox")
    transferData.upload_file(file_from, file_to)
    print("FILE HAS BEEN MOVE!!!CONGRATULATION")
