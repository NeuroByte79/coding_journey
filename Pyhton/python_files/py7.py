# How will you identify which of the following is a string,list,tuple,dictonary,set,?
"""{10,20,30.5}
[1,2,3.14,'shyam']
{12:'simple',43:'complicated',13:'comlex'}
"check it out!"
(1,2,3,"shyam")
3 + 2j """

print(type({10,20,30.5}))
print(type([1,2,3.14,'shyam']))
print(type({12:'simple',43:'complicated',13:'complex'}))
print(type((1,2,3,'shyam')))
print(type("check it out!"))
print(type(3 + 2j))