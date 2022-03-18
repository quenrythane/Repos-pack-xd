import requests as req

url = "https://www.freecodecamp.org/learn"
cont = req.get(url).text
x1 = cont.find("Responsive")
print(x1)


