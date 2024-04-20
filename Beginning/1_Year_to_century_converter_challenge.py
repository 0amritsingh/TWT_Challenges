# The Main Code (95 char):
def yearToCentury(year):
 if str(year)[-2:]=="00":
  return(year//100)
 else:
  return(year//100)+1
   
# Output:
print(yearToCentury(2024))
 