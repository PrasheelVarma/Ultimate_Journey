nums=list(map(int,input("Enter your list of numbers: ").split(",")))

print("The list of numbers is:  " + (nums))
target=int(input)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print("The two indices are: i=" + (i) + " j=" + (j))
            print("The two numbers are: " + nums[i] + " and " + nums[j])
        else:
            print("No two numbers found")

