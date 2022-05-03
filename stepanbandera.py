
import requests
res_parse_list=[]

responce=requests.get("https://coinmarketcap.com/")

responce_text=responce.text

responce_parse=responce_text.split("<span>")

for parse_elem_1 in responce_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():

                res_parse_list.append(parse_elem_2)

bitcoin_exange_rate=res_parse_list[0]
print("Курс бітка: "+bitcoin_exange_rate)
