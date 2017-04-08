# @author : Trevor Darley
# @Description : Search files with regex
import os, sys,re
import regex 
def listFiles(path, regex):
    try:
        dirs = os.listdir(path)
    except:
        return
    for file in dirs:
        if os.path.isfile(path+"/"+file):
            try:
                fl = open(path+"/"+file)
                lineNum = 0
                matches = 0  
                for line in fl.readlines():
                    res = regex.search(line)
                    if res:
                        if( matches == 0):
                            print path+"/"+file+" : ",
                        matches+=1
                        print lineNum,
                    lineNum+=1
                if(matches > 0):
                    print ""
            except:
                x=2
        elif os.path.isdir(path+"/"+file):
            listFiles(path+"/"+file, regex)
               
def main():
    reg = regex.menu() 
    print "Regex Generated : "+reg
    listFiles(raw_input('Enter directory to search:'),re.compile(reg))

if __name__ == "__main__":
    main( )
