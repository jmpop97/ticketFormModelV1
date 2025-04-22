import subprocess
import logging
logging.basicConfig(filename='./log/main.log',level=logging.DEBUG)
cmdLine="cat sample.json"
file_path = 'sample.json'
errCatch ="{"

class JsonFile():
    def __init__(self,file_path,cmdLine,errCatch):
        self.file_path=file_path
        self.cmdLine=cmdLine.split(" ")
        self.errCatch = errCatch
        with open(file_path, 'r', encoding='utf-8') as f:
            self.lines = f.readlines()  # 각 줄이 리스트의 요소가 됨
    def changeFile(self):
        for lineI,line in enumerate(self.lines):
            if "#siteLoginInfo" in line:
                self.lines[lineI]=line.replace("#siteLoginInfo","siteLoginInfo")
                self.saveFile()
                self.cmd()
                self.lines[lineI]=line
    def saveFile(self):
        with open(self.file_path,"w",encoding="utf-8") as f:
            f.write("".join(self.lines))
    def cmd(self):
        result = subprocess.run(self.cmdLine, capture_output=True, text=True)
        print(result.stdout)
        if errCatch in result.stdout:
            logging.error(result.stdout)

JsonFile(file_path,cmdLine,errCatch).changeFile()