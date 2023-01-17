#Sukurkite programą, kuri duoda įvestos valiutų poros dabartinį kursą.
# Naudokitės https://api.frankfurter.app/.
# Dokumentaciją rasite Čia. Rezultatas galėtų atrodyti taip:
#get_rate('EUR', 'GBP')
# EUR-GBP:	0.84828
#get_rate('ZZZ', 'GBP')
# Neteisingai suvestos valiutos. Galimų variantų sąrašas:
# ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS', 'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
import requests
url = 'https://api.frankfurter.app/'
#url = requests.get('https://api.frankfurter.app/')
#print(url.status_code)
def get_currency_list():
    r = requests.get(f'{url}currencies')
    dictionary = r.json()
    currency_list = []
    for key in dictionary.keys():
        currency_list.append(key)
    return currency_list

def get_rate(base, to):
    if base in get_currency_list() and to in get_currency_list():
        payload = {'from': base, 'to': to}
        r = requests.get(f'{url}latest', params=payload)
        dictionary = r.json()
        print(f'{dictionary["base"]}-{to}:\t{dictionary["rates"][to]}')
    else:
        print(f'''
Neteisingai suvestos valiutos. Galimų variantų sąrašas:
{get_currency_list()}
''')
get_rate('EUR', 'PLN')
get_rate('AUD', 'GBP')
get_rate('PLN', 'HUF')

#output
EUR-PLN:	4.6935
AUD-GBP:	0.57127
PLN-HUF:	85.01

Process finished with exit code 0
