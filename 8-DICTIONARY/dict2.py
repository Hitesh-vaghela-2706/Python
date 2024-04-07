A = {   "ADA" : 56 ,
        "CN" : 48 ,
        "PE" : 64 ,
        "IPDC" : 54 ,
        "PDS" : 66 ,
        "SE" : 51
    }

# assending order
sortbyvalue = {v:k for k,v in sorted(A.items() , key = lambda v:v[1] )  }
print(sortbyvalue) #also able to write k:v it gives o/p as k:v
# v:k gives o/p in v:k form

#desending order
sortbyvalue = {v:k for k,v in sorted(A.items() , key = lambda v:v[1] , reverse=True )  }
print(sortbyvalue)

#sort by key
sortbykey = { k:v for k,v in sorted(A.items()) }
print(sortbykey)