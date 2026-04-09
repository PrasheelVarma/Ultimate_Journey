import statistics
data=input("Enter numbers separated by spaces: ")
data=[int(x) for x in data.split(' ')]
mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
standard_deviation=statistics.stdev(data)
variance=statistics.variance(data)

#outputs
print(f"Mean:= {mean}")     #using formatted string literal
print(f"Median:", median)   #here f is useless
print("Mode:", mode)        #direct way to print without the use of f
print(f"Standard Deviation:", standard_deviation)   
print(f"Variance:", variance)
