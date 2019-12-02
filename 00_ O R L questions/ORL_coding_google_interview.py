
# in a sorted given collection (sample#) of numbers find all the pairs of numbers that summed together are equal to a given value ('sum')


sample1 = [1,2,3,9]
sample2 = [1,2,4,4]
sum = 8

index = 0
pairs = []
for n in collection:
    n = collection[index]
    rest_list = (collection[:index] + collection[index+1:])
    for item in rest_list:
        if n + item == sum:
            pair = (n, item)
            pairs.append(pair)
    index += 1


print (pairs)
