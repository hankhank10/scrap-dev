# scrap v2

import os.path
import sys
import urllib.request
import urllib.parse

api_url = "http://scrap.hankapi.com"
scrap_key_filename = "scrap_key"

def get_key_from_file():
    if os.path.isfile(scrap_key_filename):
        with open ("scrap_key", "r") as f:
            key = f.read()

        return key
    else:  
        print ("Error: scrap_key setup file does not exist. Invoke scrap.setup (key-name) from a python script to set.")
        return "ERROR"

def write(text):
    key = get_key_from_file()
    if key == "ERROR":
        return
    else:
        url = api_url + "/write?key=" + key + "&text=" + text
        url = urllib.parse.quote (url,safe=":/&?=")
        print (url)
        try:
            with urllib.request.urlopen(url) as output:
                print (output.read), 
        except Exception as e:
            print (e.message, e.args)

def setup(key):
    with open ("scrap_key", "w") as f:
        f.write (key)

    #f = open (scrap_key_filename, "w")
    #f.write (key)
    #f.close
    write ("New python client writing to scrap " + key)


