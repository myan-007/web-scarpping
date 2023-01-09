from bs4 import BeautifulSoup
import pandas as pd
import requests
url = "https://www.lidl.de/q/query/supersale"



r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')


total_products = int(soup.find('span',class_='s-page-heading__text').get_text().split()[0])
print(total_products)

pro_per_page= int(soup.find('div',class_='s-load-more__text').get_text().split()[2])
print(pro_per_page)


total_loop=int(total_products/pro_per_page)
remainder = total_products%pro_per_page

list_df =[]




for i in range(total_loop):
	temp_url = "https://www.lidl.de/q/query/supersale"+"?offset="+str(pro_per_page*i)
	temp_r = requests.get(temp_url)
	temp_htmlContent = temp_r.content
	temp_soup = BeautifulSoup(temp_htmlContent,'html.parser')
	# print(soup.title)
	products= temp_soup.find_all('div',class_='product-grid-box grid-box')
	# print(products[1].find('span',class_='m-price__rrp'))
	# exit()
	products_data = []
	for product in products:
	
		title = product.find('h2').get_text().strip()
		link = "https://www.lidl.de"+product.find('a').get('href')
	
		currentPrice = product.find('div',class_='m-price__price m-price__price--small').get_text().strip()
		if(product.find('span',class_='m-price__rrp')==None):
			previousPrice='n.a.'
		else:
			previousPrice = product.find('span',class_='m-price__rrp').get_text().strip()
		if(product.find('span',class_='rating-label__text')==None):
			reviews='n.a.'
		else:
			reviews = product.find('span',class_='rating-label__text').get_text()
		
		if(product.find('div',class_='m-price__label')==None):
			discount='n.a.'
		else:
			discount = product.find('div',class_='m-price__label').get_text().strip()
		rating = product.find_all('div',class_='rating-stars__clipmask')
		total_percentage=0
		for star in rating:
			total_percentage+=int(star['style'].split(":")[1].replace('%;',''))

		result_rating = format((total_percentage/100),'.1f')
		
		products_data.append({
		'title':title,
		'url':link ,
		'currentPrice':currentPrice,
		'previousPrice':previousPrice,
		'totalReviews':reviews,
		'discount':discount,
		'rating': result_rating
		})
	# print(products_data)
	t_df = pd.DataFrame(products_data)
	# print(url)
	# print(t_df)
	list_df.append(t_df)


df = pd.concat(list_df)	


df.to_excel("lidl.xlsx")


