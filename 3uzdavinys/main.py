#Sukurkite programą, kuri atspausdintų jūsų rytdienos horoskopą, naudokite šį resursą.
import requests
params=(('sign','aries'),('day','tomorrow'))
r=requests.post('https://aztro.sameerkumar.website/',params=params)
print(r.content)
r_json=r.json()
for iterator in r_json:
    print(iterator, ":", r_json[iterator])

#output
b'{"date_range": "Mar 21 - Apr 20", "current_date": "January 18, 2023", "description": "Wasting precious hours over things that are either unimportant or out of your control (or possibly both)? Well, waste no longer. Take a few deep breaths and shake it off. You\'ve got bigger fish to fry.", "compatibility": "Pisces", "mood": "Relaxed", "color": "Yellow", "lucky_number": "77", "lucky_time": "6pm"}\n'
date_range : Mar 21 - Apr 20
current_date : January 18, 2023
description : Wasting precious hours over things that are either unimportant or out of your control (or possibly both)? Well, waste no longer. Take a few deep breaths and shake it off. You've got bigger fish to fry.
compatibility : Pisces
mood : Relaxed
color : Yellow
lucky_number : 77
lucky_time : 6pm

Process finished with exit code 0
