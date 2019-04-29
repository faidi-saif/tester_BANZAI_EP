

class logger:

    def __init__(self):
        pass


    def open(self,arg_file):
        file = open(arg_file,"w+")
        return file


    def write(self,arg_file,arg_data):
        file = self.open(arg_file)
        file.write(arg_data)
        self.close(file)

    def close(self,arg_file):
       arg_file.close()




    def __del__(self):
        pass
