start = int(input("Enter start for the range: "))
end = int(input("Enter end for the range: "))

for i in range (start,end+1):
    count = 0
    for j in range(start,end+1):
        if(i % j == 0):
            count = count + 1
    if count == 2:
        print(i)