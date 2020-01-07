from bs4 import BeautifulSoup
import requests

nbk_url = 'https://english.mubasher.info/markets/BK/stocks/NBK/profile'

nbk_page = requests.get(nbk_url)

nbk_soup = BeautifulSoup(nbk_page.text, 'html.parser')

nbk_stock_price = nbk_soup.find_all(class_="market-summary__last-price up-icon-only")[0].get_text()



khot_url = 'https://english.mubasher.info/markets/BK/stocks/KHOT/profile'

khot_page = requests.get(khot_url)

khot_soup = BeautifulSoup(khot_page.text, 'html.parser')

khot_stock_price = khot_soup.find_all(class_="market-summary__last-price up-icon-only")[0].get_text()




napesco_url = 'https://english.mubasher.info/markets/BK/stocks/NAPESCO/profile'

napesco_page = requests.get(napesco_url)

napesco_soup = BeautifulSoup(napesco_page.text, 'html.parser')

napesco_stock_price = napesco_soup.find_all(class_="market-summary__last-price down-icon-only")[0].get_text()



#National Petrolium Services NAPESCO 1.248
#url: https://english.mubasher.info/markets/BK/stocks/NAPESCO/profile
#element: <div class="market-summary__last-price up-icon-only">1,248.00</div>

hcc_url = 'https://english.mubasher.info/markets/BK/stocks/HCC/profile'

hcc_page = requests.get(hcc_url)

hcc_soup = BeautifulSoup(hcc_page.text, 'html.parser')

hcc_stock_price = hcc_soup.find_all(class_="market-summary__last-price unchanged-icon-only")[0].get_text()



# Hilal Cement HCC 100
#url: https://english.mubasher.info/markets/BK/stocks/HCC/profile
#element: <div class="market-summary__last-price unchanged-icon-only">100.00</div>

# Al kout industrial projects ALKOUT 850
#url: https://english.mubasher.info/markets/BK/stocks/ALKOUT/profile
#element: <div class="market-summary__last-price unchanged-icon-only">850.00</div>

alhout_url = 'https://english.mubasher.info/markets/BK/stocks/ALKOUT/profile'

alhout_page = requests.get(alhout_url)

alhout_soup = BeautifulSoup(alhout_page.text, 'html.parser')

alhout_stock_price = alhout_soup.find_all(class_="market-summary__last-price unchanged-icon-only")[0].get_text()



menu = '''
Options:
1. National Bank of Kuwait (NBK)
2.Kuwait Hotels (KHOT)
3. National Petroleum of Kuwait (NAPESCO)
4. Hilal Cement (HCC)
5. Al Kout Industrial Projects (ALKOUT)
6. Exit'''

while True:
	print('------------------------------')
	print(menu)
	choice = input('Choose a company by entering its number to show its stock price: ')
	if choice == '6':
		break
	elif choice == '1':
		print(nbk_stock_price)
	elif choice == '2':
		print(khot_stock_price)
	elif choice == '3':
		print(napesco_stock_price)
	elif choice == '4':
		print(hcc_stock_price)
	elif choice == '5':
		print(alhout_stock_price)




