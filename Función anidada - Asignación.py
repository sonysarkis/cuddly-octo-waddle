def division(a,b):
    def validacion():
        if a > 0 and b > 0:
            return True
        else:
            return False
    print (validacion())
    if validacion() == True:
        return a/b 
    else:
        return None
        
resultado = division (10,4)
print(resultado)