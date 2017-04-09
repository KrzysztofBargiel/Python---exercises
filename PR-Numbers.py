# NUMBER OF ALL PRS with severity S,A,B
total_number = raw_input("Enter the number of all PRs(numbers only): ")

try:
    # Checking if total_number contains only numbers
    int(total_number)

except ValueError:
    print "Invalid entry"
    exit(0)

else:
    # Double check if user enter 0 for total_number
    if int(total_number) < 1:
        print "Total numbers of PRs: 0"
        exit(0)

TotalS = raw_input("Enter number of failed PR with severity S: ")
TotalA = raw_input("Enter number of failed PR with severity A: ")
TotalB = raw_input("Enter number of failed PR with severity B: ")

try:
    # Another check if variables contains only numbers
    int(TotalS)
    int(TotalA)
    int(TotalB)

except ValueError:
    print "Invalid entry"
    exit(0)

precentPrS = float(TotalS) / float(total_number) * 100
precentPrA = float(TotalA) / float(total_number) * 100
precentPrB = float(TotalB) / float(total_number) * 100

print "Percent o failed PR with severity S = " + str(precentPrS) + " %"
print "Percent o failed PR with severity A = " + str(precentPrA) + " %"
print "Percent o failed PR with severity B = " + str(precentPrB) + " %"
