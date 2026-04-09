import statistics
data=input("Enter numbers separated by spaces: ")
data=[int(x) for x in data.split(' ')]
mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
standard_deviation=statistics.stdev(data)
variance=statistics.variance(data)
