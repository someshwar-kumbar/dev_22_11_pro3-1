sub1 = int(input("Enter 1st subject marks: "))
sub2 = int(input("Enter 2nd subject marks: "))
sub3 = int(input("Enter 3rd subject marks: "))
sub4 = int(input("Enter 4th subject marks: "))
sub5 = int(input("Enter 5th subject marks: "))

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print("Average =", avg)

if avg >= 80:
    print("A grade")
elif avg >= 60:
    print("B grade")
elif avg >= 40:
    print("C grade")
elif avg >= 30:
    print("D grade")
else:
    print("Fail")
