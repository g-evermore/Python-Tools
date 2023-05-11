import os, glob

class FileManipulator:

    def __init__(self):
        self.target_path = ""
        self.target_folder = ""
    
    def getPath(self, input_path):        
        x = input_path.rindex("\\")+1
        self.target_path = input_path[:x]
        self.target_folder = input_path[x:]
    
    
    def renameFiles(self, path, folder_name):
        for count, filename in enumerate(self.getListOfFiles(path, folder_name)):
            self.rename(path, folder_name, filename, count, padding="XXX")
        for count, filename in enumerate(self.getListOfFiles(path, folder_name)):
            self.rename(path, folder_name, filename, count)

    def renameFilesDrill(self, path, folder_name):
        dirs = os.listdir(f"{path}{folder_name}")
        for file in dirs:
            if (file.find(".")<0):
                self.renameFilesDrill(f"{path}{folder_name}", f"\\{file}")
        self.renameFiles(path, folder_name)        

    def rename(self, path, folder_name, file_name, count, padding=""):
        file_extention = file_name[file_name.rindex("."):]
        new_name = f"{folder_name}_{padding}{str(count)}{file_extention}"
        final_name = f"{path}{folder_name}/{new_name}"
        os.rename(file_name, final_name)

    def getListOfFiles(self, path, folder_name):
        list_of_files = filter( os.path.isfile, glob.glob(f"{path}{folder_name}" + '\\*') )
        list_of_files = sorted( list_of_files, key = os.path.getmtime)
        return list_of_files

    def begin(self, input_path, drill=False):
        self.getPath(input_path)
        if drill==True:
            self.renameFilesDrill(self.target_path, self.target_folder)
        else:
            self.renameFiles(self.target_path, self.target_folder)
