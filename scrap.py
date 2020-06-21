# scrap v2

import os.path
import sys
import urllib.request

api_url = "http://scrap.hankapi.com"
scrap_key_filename = "scrap_key"

def get_key_from_file():
    if os.path.isfile(scrap_key_filename):
        f = open (scrap_key_filename, "r")
        key = f.read()
        f.close
        return key
    else:  
        print ("Error: scrap_key setup file does not exist. Invoke scrap.setup (key-name) from a python script to set.")
        return "ERROR"

def write(text):
    key = get_key_from_file()
    if key == "ERROR":
        return
    else:
        try:
            url = api_url + "/write/?key=" + key + "&text=" + text
            with urllib.request.urlopen(api_url + "/write/?key=" + key + "&text=" + text) as response:
                html = response.read()

        except:
            print ("scrap error")

def setup(key):
    f = open (scrap_key_filename, "w")
    f.write (key)
    f.close
    write ("New python client writing to scrap " + key)


