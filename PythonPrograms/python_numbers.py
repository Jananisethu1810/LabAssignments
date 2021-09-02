import math
import random
#Absolute Value (abs)

print ("abs(-45) = ",abs(-45));

#ceil()

print("ceil(-45.90)=", math.ceil(-45.90))
print("ceil(100.01)=", math.ceil(100.01))

#floor()

print("floor(-45.90)=", math.floor(-45.90))
print("floor(100.72)=", math.floor(100.72))

#log(), log10()

print("log(100.12)=", math.log(100.12))
print("log10(100.12)=", math.log10(100.12))

#max(), min()

print("max(34, -90, 45, 67)=", max(34, -90, 45, 67))
print("min(34, -90, 45, 67)=", min(34, -90, 45, -167))

#modf()

print ("math.modf(100.12) : ", math.modf(100.12))

#pow(), round()

print("math.pow(100, 2) : ", math.pow(100, 2))
print("round((80.23456, 2) : ", round(80.23456, 2))

#Random Functions

print("random.choice([1,2,3,4,5]) = ", random.choice([1,2,3,4,5]))
print("random.choice('A String') = ", random.choice('A String'))

print ("randrange(100, 1000, 2) = ", random.randrange(100, 1000, 2))
