import random
min_Value=1
max_Value=6
Roll=True
while Roll:
    print("Rolling...")
    value1=random.randint(min_Value,max_Value)
    print("The Value is:",value1)
    if(value1==6):
        continue
    else:
        Roll=False

