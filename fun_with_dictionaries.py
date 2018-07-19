
import matplotlib.pyplot as plt
import pandas as pd

weight = [4.56,5.22,6.78,7.3,7.5,7.6]
players = ["carl", "doug", "bob", "alex", "bill", "adam"]

print(len(weight))
print(len(players))

a_dictionary = {

"carl": 4.56,
"doug": 5.22,
"bob" : 6.78,
"alex": 7.3,
"bill": 7.5,
"adam": 7.6
    }

print(a_dictionary)

a_dictionary["drew"] = 7.34
print(a_dictionary)

print("drew" in a_dictionary)

d = "precaution"
print(d.replace("e","-"))

blurb = pd.DataFrame(a_dictionary , index=[0])
print(blurb)

print(2 <= 2)

print("3" < "chris")

print("%" < "^")
print("%" < "$")






