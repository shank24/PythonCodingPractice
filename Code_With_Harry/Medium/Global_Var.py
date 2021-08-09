#Global Scope
l=10

def function(n):
    #Local Scope
    #l=6
    global l
    l = l+50
    m=9
    print(m,l)
    print(n,"Via Function")

function("Calling function")