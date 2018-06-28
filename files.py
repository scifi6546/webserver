import os
from config import config
class Files:
    def is_extension(self,temp_ext):
        ret=False
        for i in range(0,len(self.extensions)):
            if self.extensions[i]==temp_ext:
                ret=True
        return ret
    def __init__(self,num):
        tempfiles=os.listdir(config['upload_folder'])
        self.extensions=[]
        self.files=[]

        temp_extensions=os.listdir("static/icons")
        for i in range(0,len(temp_extensions)):
            temp = temp_extensions[i].split('.svg')
            self.extensions.append(temp[0])


        for i in range(0,len(tempfiles)):
            temp_file_name=tempfiles[i]
            temp=tempfiles[i].split('.')
            
            tempext="icons/?.svg"
            
            if self.is_extension(temp[1]):
                tempext="icons/"
                tempext+=temp[1]
                
            self.files.append({"name":temp_file_name, "extension":tempext+ ".svg"})
        print("files: " + str(self.files))
    def getFiles(self):
        return self.files
    def notifyUploaded(self,file_name):
        temp=file_name.split('.')
        tempext="icons/?.svg"
        if self.is_extension(temp[1]):
            tempext="icons/"
            tempext+=temp[1] + ".svg"
        self.files.append({"name":file_name,"extension": tempext})
    

