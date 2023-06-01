# Write a program to print T in all scales viz Celsius, Fahrenheit and Kelvin.

# Formula to convert from F to C is 
# C = (F-32)*5/9

# Formula to convert from K to C is 
# C = K - 273 

# input 
# 25C 
# Output 
# 25.0C 
# 77.0F
# 298.0K

temparature = input()   
unit = temparature[-1] 
value = temparature[:-1] 
if(unit=="C" or unit=="c"):
    celcius = float(value);
    print(str(round(celcius,2))+"C")
    print(str(round((celcius*9/5)+32,2))+"F")
    print(str(round(celcius+273.15,2))+"K")
elif(unit=="F" or unit=="f"):
    kelv = float(value)
    print(round(kelv-273.15,2),C)
    print(round((kelv-273.15)*9/5+32,2),F)
    print(round(kelv,2),K)
elif(unit=="K" or unit == "k"):
    fahr = float(value)
    print(round((fahr-32)*5/9,2),"C")
    print(round(fahr,2),"F")
    print(round((fahr-32)*5/9+273.15,2),"K")