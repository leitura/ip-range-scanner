try:
  import requests as r
  import ipaddress, sys
  from os import system as s
  import time
  from datetime import datetime
  from requests.exceptions import Timeout

except ModuleNotFoundError:
  print('\npip install -r req.txt\n')

s('clear')
cg='\033[92m'
cp='\033[35m'
clb='\033[94m'
cb='\033[34m'
k='\033[0m'
clr='\033[91m'
ver = '@Ver 1.0 LTS'
aaa = datetime.now().strftime(' %d/%m/%y')

print()

print(f'''
		 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$${clr} COOL-CODER {k}$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$${cg} IP RANGE SCANNER {k}$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
  u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
  $$$$$$$$$$""""           ""$$$$$$$$$$$"
   "$$$$$"                      ""$$$$""
     $$$"                         $$$$"
					  {cb}@Ver {ver}{k}
___________________________________________________
  Noob       |  sem dinheiro    |  Plataforma  |  Data
———————————————|—————————————|————————————|———————————
{clr}「Sofre」{k} |  @OMentalista |  Telegram  |{aaa}''')

print()
print(f'{clb}[ {cp}obs {clb}]{k} A conexão de dados fornece resultados mais precisos')
#range = '104.18.6.0/24'
try:
  range = input(f'{clb}[ {cp}obs {clb}]{k} Digite Ip e intervalo no formato " 192.0.0.0/24 " \n{cg}|\n└──{k}IP ~{cg}#{k} ')
  if range == '':
    print('Noob sofre')
    sys.exit(1)
except:
  print('mando pegar o pacote você ferra tudo')
  sys.exit(1)

try:
  net4 = ipaddress.ip_network(range)
except ValueError as e:
  print(f'\n{clr}fodeu{k}: ' + str(e))
  print()
  sys.exit(1)

v = 0
for x in net4.hosts():
  v = v + 1

print(f'\n{clb}DIGITALIZANDO{k}: {range}\n{clb}Total de hosts no intervalo{k}: {v}\n')

strt = time.time()
c = 0

for host in net4.hosts():

  h1 = f'http://{host}'
  h2 = h1

  try:
    x = r.get(h2, timeout=5)
    x = x.status_code
    print(str(f'{cg}{host}{k}') + ' | vivo - status ' + str(x))
    c = c + 1

  except Timeout:
    print(str(f'{clr}{host}{k}') + ' | Inacessível ')

  except KeyboardInterrupt:
    print('\nCTRL + C detectou\nSaindo ...')
    sys.exit(1)

  except:
    print(str(f'{clr}{host}{k}') + ' | fodeu ')

print()
en = time.time()
print(f'Tempo gasto: {en-strt} segundos\n')
print(f'{cp}Hits{k}: {cg}{c}{k}/{v}\n')
