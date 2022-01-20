import json
import requests
requests.packages.urllib3.disable_warnings()
import urllib.parse
from prettytable import PrettyTable

print ("1.Obtener los id de las organizaciones ")

api_url="http://api.meraki.com/api/v1/organizations"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

resp = requests.get(api_url,headers=headers,verify=False)
print("Request status:",resp.status_code)

response_json = resp.json()



table = PrettyTable(["Id","Organizaciones"])
for Organiz in response_json:
    table.add_row([Organiz["id"],Organiz["name"]])

print(table)





IdOrg = response_json[3]["id"]



main_api="https://api.meraki.com/api/v1/organizations/"
headers={"X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}


print ("2.Obteniendo las redes a partir del id de la organizacion" ,IdOrg)
api_url2=main_api+(IdOrg)+'/networks'





resp2 = requests.get(api_url2,headers=headers,verify=False)
print("Request status:",resp2.status_code)

response_json2 = resp2.json()



tableRedes = PrettyTable(["id","Redes"])
for redes in response_json2:
    
    tableRedes.add_row([redes["id"],redes["name"]])

print(tableRedes)









IdNet = response_json2[0]["id"]
print ("3.Obteniendo los dispositivos  Red a con network  id",IdNet)
main_api2="https://api.meraki.com/api/v1/networks/"


api_url3=main_api2+(IdNet)+'/devices'


resp3 = requests.get(api_url3,headers=headers,verify=False)
print("Request status:",resp3.status_code)
response_json3 = resp3.json()


tableDisp = PrettyTable(["Direccion","Nroserie"])
for Dispositivos in response_json3:
    
    tableDisp.add_row([Dispositivos["address"],Dispositivos["serial"]])

print(tableDisp)



IdNet = response_json2[0]["id"]

print ("4.Obteniendo los datos Red con el network id",IdNet)

main_api2="https://api.meraki.com/api/v1/networks/"

api_url4=main_api2+(IdNet)

resp4 = requests.get(api_url4,headers=headers,verify=False)
print("Request status:",resp4.status_code)
response_json4 = resp4.json()
Redes1=response_json4["name"]
Redes2=response_json4["timeZone"]



tableDatosRed = PrettyTable(["Nombre","Zona Horaria"])
   
tableDatosRed.add_row([Redes1,Redes2])

print(tableDatosRed)




IdSerie = response_json3[0]["serial"]


print ("Obtengo informacion de un dispositivo con serial ID",IdSerie)

api_url5=main_api2+(IdNet)+'/devices/'+(IdSerie)


resp5 = requests.get(api_url5,headers=headers,verify=False)
print("Request status:",resp4.status_code)
response_json5 = resp5.json()


 

tableNetSerie = PrettyTable(["Direccion","modelo"])
Serie1=response_json5["address"]
Serie2=response_json5["model"] 

    
tableNetSerie.add_row([Serie1,Serie2])

print(tableNetSerie)






print ("Obtengo los SSID para la la Red Id" ,IdNet  )

api_url6=main_api2+(IdNet)+'/wireless/ssids'


resp6 = requests.get(api_url6,headers=headers,verify=False)


response_json6 = resp6.json()
Ssid=response_json6


tableWlan = PrettyTable(["Nombre","Seleccion de banda ", "visible"])
for Wlan in Ssid:    
    tableWlan.add_row([Wlan["name"],Wlan["bandSelection"],Wlan["visible"]])

print(tableWlan)








