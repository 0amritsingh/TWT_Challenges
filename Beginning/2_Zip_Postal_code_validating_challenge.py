# The Main Code (378 char):
def validate(n):
 m = str(n)
 if len(m)>5:
  exit()
 if m[0]==m[1] or m[0]==m[2]:
  print(False)
  exit()
 if m[1]==m[0] or m[1]==m[2] or m[1]==m[3]:
  print(False)
  exit()
 if m[2]==m[0] or m[2]==m[1] or m[2]==m[3] or m[2]==m[4]:
  print(False)
  exit()
 if m[3]==m[1] or m[3]==m[2] or m[3]==m[4]:
  print(False)
  exit()
 if m[4]==m[2] or m[4]==m[3]:
  print(False)
  exit()
 else:
  print(True)

# Output:
validate(12345)