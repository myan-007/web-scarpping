import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com"

#Step 1 get the html 

r = requests.get(url)
htmlContent = r.content

#Step 2 parse the html

soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)




'''
Step 3 html tree traversal
1. Tag
 print(type(title))
2. NavigableString
 print(type(title.string))
3. BeautifulSoap
 print(type(soup)) 
4. Comment
markup = "<p><!-- thios is comment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

'''



title = soup.title #get the title of html page

paras = soup.find_all('p')#get all paras of html page
# print(paras)



#get class of first element only 
# print(soup.find('p')['class'])

#find all the elements with class lead
# print(soup.find_all('p',class_="lead"))


#get the text from the tags/soup
# print(soup.find('p').get_text())


anchors = soup.find_all('a')#get all anchor tags of html page
# print(anchors)

all_links = set()
#get all the link from the anchors text
for link in anchors:
	if(link.get('href')!='#'):
		if(link.get('href').__contains__('https')==False):
			all_links.add("https://codewithharry.com"+link.get('href'))
		else:
			all_links.add(link.get('href'))

# print(all_links)
 
  





