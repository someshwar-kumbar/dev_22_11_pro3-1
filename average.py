sub1=int(input("enter 1 st subject marks"))
sub2=int(input("enter 2 st subject marks"))
sub3=int(input("enter 3st subject marks"))
sub4=int(input("enter 4st subject marks"))
sub5=int(input("enter 5 st subject marks"))
avg=sub1+sub2+sub3+sub4+sub5/5

if(avg>80):
  print("A grade")
elif(avg>60 or avg<80):
  print("B grade")
elif(avg>40 or avg<60):
  print("C grade")
elif(avg>30 or avg>40):
  print("D grade")
else:
  print("fail")

