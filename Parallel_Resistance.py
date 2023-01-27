#JEROME WALTERS 
#INTERNET OF THINGS 
#LAB 1

#finind the total resistance of a network of 2 or more resistors
import math
def parallel(list_of_resistors):

    total_resistance = 0
    for resistors in list_of_resistors:
        total_resistance = total_resistance + 1/resistors
    
    return (1/total_resistance)

list_of_resistors = [1000, 1000,1000]
print(parallel(list_of_resistors), " ohms")




#Finding the voltage drops across resistors in series
def potential_divider(voltage_supply , series_resistance):
    total_resistance = sum(series_resistance)
    total_current = voltage_supply/total_resistance
     
    for resistors in series_resistance:
        voltage_drop = total_current * resistors
        print (voltage_drop,"v")
        

potential_divider(9,[1000,1000])




def temperature_check(temp,unit):

    if unit == "c" or unit=="C":

        if temp <= 36: 
            print ("The patientent is hypothermic")

        elif temp == 37:
            print ("The patient's temperature is normal")

        elif temp >= 38:
            print ("The patient is hyperthermic")

    if unit == "f" or unit=="F":
        #coversion = temp * 1.8 + 32
        if temp <= 98.5: 
            print ("The patientent is hypothermic")

        elif temp == 98.6:
            print ("The patient's temperature is normal")

        elif temp >= 98.7:
            print ("The patient is hyperthermic")
      
temperature_check(98.6,"f")