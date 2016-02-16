import urllib
import xmltodict

def intention(tweet):
	op=urllib.urlopen('http://www.aiaioo.com/apis/vakintent/?key=brl8oHNrwHjD_guest@aiaioo.com_xN6xqqVaLdg9&text='+tweet)
	xml=op.read(op)
	doc=xmltodict.parse(xml)
	intention=doc['api']['result']['documents']['document']['intention']
	return intention