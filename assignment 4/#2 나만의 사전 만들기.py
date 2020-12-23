from urllib.request import urlopen
import re

def make_dictionary(document):
    document = document.replace('.',' ')
    document = document.replace(',',' ')
    dickey = document.split()
    mydict = {}
    for key in dickey:
        with urlopen('http://114.71.103.80/dict.html?query={0}'.format(key)) as f:
            txt = f.read()
        retxt = txt.decode('utf-8')
        txt1 = retxt.split('Definition')[1]
        txt2 = txt1.split('<td>')[1]
        txt3 = txt2.split("</td>")[0]
        mydict[key] = txt3
    return mydict

data = "first, solve the problem. then, write the code."
print(make_dictionary(data))
