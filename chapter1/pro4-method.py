#write a function istrcmp to compare two strings,ignoring the case
def istrcmp(x,y):
 if x.upper()==y.upper():
  return True
 else:
  return False

print istrcmp('python','Python')
print istrcmp('LaTex','latex')
print istrcmp('a','b')
