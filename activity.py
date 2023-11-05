import dropbox

class Transfer_data:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        data = open(file_from,'rb')
        dbx.files_upload(data.read(), file_to)

def main():
    access_token = 'sl.BpR12CkvrEVCWoQjil9aIUDUY_xFBT9PC7e1avXMnS2D_3-ToNyvhPK-gR1lP5qcyrLn1N_f7F2uTk9i7iqWKbQwYO_ZBtUZdTX4uShklX507FVO9j41_PlEk_qxBWOWkobfH18zBugOVYtt78dRm9E'
    dby = Transfer_data(access_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the file path to be entered:")
    dby.upload_files(file_from, file_to)

main()
