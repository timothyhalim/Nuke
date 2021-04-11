import nuke
from subprocess import Popen
from os import path

def fileExplorer():
    n = nuke.selectedNode()
    if n.Class() == "Write" or n.Class() == "Read":
        file = n['file'].evaluate()
        if path.exists(file):
            Popen(r'explorer /select,'+file.replace("/", "\\"))
        elif path.exists(path.split(file)[0]):
            Popen(r'explorer '+(path.split(file)[0]).replace("/", "\\"))
        else:
            nuke.message("Folder Not Exist")
            
def main():
    fileExplorer()