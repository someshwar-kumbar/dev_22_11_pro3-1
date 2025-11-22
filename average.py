import sys

if len(sys.argv) != 6:
    print("Usage: python3 average.py <sub1> <sub2> <sub3> <sub4> <sub5>")
    sys.exit(1)

sub1 = int(sys.argv[1])
sub2 = int(sys.argv[2])
sub3 = int(sys.argv[3])
sub4 = int(sys.argv[4])
sub5 = int(sys.argv[5])

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
