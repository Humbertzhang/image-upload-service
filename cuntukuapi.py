import requests
import os

def upload():
    key = "584bf3b4398f4e01f695cc0c50253110"
    source = input(">Input Source:")
    source = str(source)

    #if os.path.isfile(source):
    #    f = open(source,"r")
        
    r = requests.post("https://cuntuku.com/api/1/upload/?key=" + key + "&source=file://" + source + "&format=json/")
     
    print(r.status_code)
    print(r.json())
    #f.close()
    

if __name__ == "__main__":
    upload()
