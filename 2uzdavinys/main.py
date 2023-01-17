#Naudodami tą pačią Frankfurter API (kaip ir pirmoje užduotyje),
# sukurkite programą, kuri pagal parametruose pateiktas valiutų poras,
# periodo pradžios ir pabaigos datą surastų dienas kai kursas
# buvo aukščiausias ir kai kursas buvo žemiausias Maždaug taip:
#currency_pair_analysis('EUR', 'GBP', '2019-01-01', '2019-12-31')
# Valiutų poroje EUR-GBP, periode nuo 2019-01-01 iki 2019-12-31:
# Žemiausias kursas buvo 2019-12-09 - 0.84116
# Aukščiausias kursas buvo 2019-08-12 - 0.92203
import requests
import json

url = 'https://api.frankfurter.app/'

def get_key(val, dct):
    """Little key by value extractor"""
    for k, v in dct.items():
        if val == v:
            return k


def currency_pair_analysis(base, to, start_date, end_date):
    payload = {'from': base, 'to': to}                                      # susikuriame parametrų žodyną
    r = requests.get(f'{url}{start_date}..{end_date}', params=payload)      # susikuriame užklausą pagal API dokumentaciją
    result = json.loads(r.text)                 # Atsakymą paverčiame Python žodynu
    new_dict = {}                               # Susikuriame tuščią žodyną
    for k, v in result['rates'].items():        # Užpildome jį reikšmėmis 'data': 'kursas'
        new_dict[k] = v[to]

    values_list = list(new_dict.values())       # Susikuriame kursų sąrašą
    min_value = min(values_list)                # Ištraukiame žemiausią reikšmę
    max_value = max(values_list)                # Ištraukiame aukščiausią reikšmę
    min_date = get_key(min_value, new_dict)     # Panaudojame pagalbinę funkciją rakto pagal reikšmę paieškai (gauname datą)
    max_date = get_key(max_value, new_dict)     # Gauname kitą datą
    ''' Formuojame Atsakymą:'''
    print(f'''
    Valiutų poroje {base}-{to}, periode nuo {start_date} iki {end_date}:
    Žemiausias kursas buvo {min_date} - {min_value}
    Aukščiausias kursas buvo {max_date} - {max_value}
    ''')
currency_pair_analysis('PLN', 'USD', '2023-01-01', '2023-01-17')
    # Valiutų poroje PLN-USD, periode nuo 2023-01-01 iki 2023-01-17:
    # Žemiausias kursas buvo 2023-01-06 - 0.22364
    # Aukščiausias kursas buvo 2023-01-13 - 0.23063
    
#output
Valiutų poroje PLN-USD, periode nuo 2023-01-01 iki 2023-01-17:
    Žemiausias kursas buvo 2023-01-06 - 0.22364
    Aukščiausias kursas buvo 2023-01-13 - 0.23063
    

Process finished with exit code 0
