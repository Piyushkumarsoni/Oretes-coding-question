import urllib.request
import json
import webbrowser
apodurl= "https://api.nasa.gov/planetary/apod?api_key=dWBpd85ub5hRRh1UfaV2iVig8QUs5uGrzYELXg63"
mykey= "dWBpd85ub5hRRh1UfaV2iVig8QUs5uGrzYELXg63"
apodurlobj =urllib.request.urlopen(apodurl + mykey)

apodread = apodurlobj.read()
decodeapod =json.loads(apodread.decode('utf-8'))

print("\nConverted Python data:-")
print(decodeapod)

input("\n Enter to open NASA Picture of the Day:-")
webbrowser.open(decodeapod['url'])