#Naudodami tą pačią Frankfurter API (kaip ir pirmoje užduotyje),
# sukurkite programą, kuri pagal parametruose pateiktas valiutų poras,
# periodo pradžios ir pabaigos datą surastų dienas kai kursas
# buvo aukščiausias ir kai kursas buvo žemiausias Maždaug taip:
#currency_pair_analysis('EUR', 'GBP', '2019-01-01', '2019-12-31')
# Valiutų poroje EUR-GBP, periode nuo 2019-01-01 iki 2019-12-31:
# Žemiausias kursas buvo 2019-12-09 - 0.84116
# Aukščiausias kursas buvo 2019-08-12 - 0.92203
import json
import requests

def currency_pair_analysis(from_currency, to_currency, from_date, to_date):
    amount = 1
    params = {
        ('amount', amount),
        ('from', from_currency),
        ('to', to_currency),
    }
    request = requests.get(f"https://api.frankfurter.app/{from_date}..{to_date}", params=params)
    dictionary = json.loads(request.text)
    print(f'In currency group {from_currency}-{to_currency}, period from {from_date} to {to_date}')
    print(dictionary['rates'])
    list_of_items = []
    for i, z in dictionary['rates'].items():
        result = i, z[to_currency]
        list_of_items.append(result)
    min_result = str(min(list_of_items, key=lambda x: x[1]))
    min_result = min_result.replace('(', '').replace(')', '').replace("'", "").replace(',', ' -')
    max_result = str(max(list_of_items, key=lambda x: x[1]))
    max_result = max_result.replace('(', '').replace(')', '').replace("'", "").replace(',', ' -')
    print(f'Lowest currency rate was {min_result}')
    print(f'Highest currency rate was {max_result}')
currency_pair_analysis('EUR', 'AUD', '2023-01-01', '2023-01-16')

#output
In currency group EUR-AUD, period from 2023-01-01 to 2023-01-16
{'2023-01-02': {'AUD': 1.5699}, '2023-01-03': {'AUD': 1.5708}, '2023-01-04': {'AUD': 1.5452}, '2023-01-05': {'AUD': 1.5515}, '2023-01-06': {'AUD': 1.559}, '2023-01-09': {'AUD': 1.5446}, '2023-01-10': {'AUD': 1.5616}, '2023-01-11': {'AUD': 1.5588}, '2023-01-12': {'AUD': 1.557}, '2023-01-13': {'AUD': 1.5586}, '2023-01-16': {'AUD': 1.5537}}
Lowest currency rate was 2023-01-09 - 1.5446
Highest currency rate was 2023-01-03 - 1.5708

Process finished with exit code 0
