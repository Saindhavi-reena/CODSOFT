#N<-Names, c_n<-contact_numbers, n<-number of names
Na=[]
contact=[]
n=int(input("Enter the number of contacts we need to save :"))
for i in range(n):
  Name=input("Name: ")
  C_N=int(input("Contact Number: "))
  Na.append(Name)
  contact.append(C_N)
print("\nName\t\t\tContact_number")
for i in range(n):
  print(Na[i],"\t\t\t",contact[i])

