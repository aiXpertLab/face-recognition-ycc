bicycles = ['trek', 'cannondale', 'redline', 'specialized','5th','6th bike']
message = f"my bike is {bicycles[2]}"
#print(bicycles[0].title())
#print(bicycles[-2].title())
#print(message)


motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles)

motorcycles[0] = 'ducati'
#print(motorcycles)

motorcycles.append('Havana')
#print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.insert(1, 'ducati')
#print(motorcycles)
del motorcycles[1]
#print(motorcycles)

popped_motorcycle = motorcycles.pop(1)
#print(motorcycles)
#print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)
motorcycles.remove('ducati')
#print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))

#cars.sort(reverse=True)
#print(cars)

cars.reverse()
print(cars)
print(len(cars))
