
import matplotlib.pyplot as plt

weight = [4.56,5.22,6.78,7.3,7.5,7.6]
height = [2,3,4,4,5,6]
#no good.
#weight2 = weight*2.5
#print(weight2)

print(height)
print(weight)
#plt.scatter(weight, height)
plt.plot(weight, height)
#plt.show()


plt.xscale('log')
#plt.scatter(weight, height)
#plt.show()

plt.clf()

plt.hist(height,2)
#plt.show()

plt.clf()
plt.xlabel('height')
plt.ylabel('population')
plt.title('hi jared')
plt.scatter(height,weight)
plt.show()

#plt.hist(weight,3)
#plt.show()

