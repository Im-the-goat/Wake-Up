#solicitar ao usuario que digite um numero
numero = float (input ( "digite um numero:"))
#verificar se o numero e positivo, negativo ou zero
if numero > 0:
    print ("o numero e positivo")
elif numero < 0:
    print ("o numero e negativo")
else:
    print ("o numero e zero")