# scrap requires a total of three lines of python code for you to use

import scrap  # this needs to be done on every script you write to a scrap from

### Link this folder to a scrap key
# This command only needs to be invoked once for each project directory you work in - it will save the key to a file for use going forward
# but there's no harm in running it each time if you prefer - it will overwrite nicely
scrap.setup("scrap-testing")

# Then you write to your scrap with the following command:
scrap.write("Hello world")

# It will appear immediately at your scrap on the web

# That's all


print ("A string has been written to " + scrap.get_key_from_file())
print ("Go check it out at http://scrap.hankapi.com/read?key=" + scrap.get_key_from_file())