import random
import array
max = 6
d=['0','1','2','3','4','5','6','7','8','9','10']
low=['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up=['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sym=['@','#','$','%','=',':','?','.','/','|','&','*','~','>','<']
com_list=d+low+up+sym
r_digit=random.choice(d)
r_upper=random.choice(up)
r_lower=random.choice(low)
r_symbol=random.choice(sym)
temp_pass=r_digit+r_upper+r_lower+r_symbol
for x in range(maximum-5):
  temp_pass=temp_pass+random.choice(com_list)
  temp_pass_list=array.array('u',temp_pass)
  random.shuffle(temp_pass_list)
password=" "
for x in temp_pass_list:
  password=password+x
print(password)