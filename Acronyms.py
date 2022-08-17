User_input=str(input("Enter the phrase"))
text=User_input.split()
acro=''
for i in text:
    acro+=i[0].upper()
print(acro)
