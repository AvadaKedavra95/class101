import dropbox

class Transferdata :
    def __init__(self,access_token) :
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.A942rAX8CWMnfEGumEkT5k_XduGh6HEB5PoF6Z1Max6QAOHNUpj-w0ZGWIdYXaYq5dbYTd4vzjony6voP4F8yETmbw47qwtwxIA1g-8sTLoSTL0JaC_VjO14yp__CVLbGPGabdu5RyTs"
    transferdata=Transferdata(access_token)
    file_from=input("Enter the file path to transfer : ")
    file_to=input("Enter the path to upload to dropbox : ")
    transferdata.upload_file(file_from,file_to)
    print("files have been moved")

main()