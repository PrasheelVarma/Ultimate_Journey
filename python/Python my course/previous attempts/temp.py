import statistics
data=input("Enter the values separated by spaces: ")
data=[int (x) for x in data.split(' ')]

print(f"mean={statistics.mean(data)}")
print("mode=",statistics.mode(data))
print("median=",statistics.median(data))
print(f"standard deviation={statistics.stdev(data):.2f}")
print(f"variance={statistics.variance(data):.2f}")