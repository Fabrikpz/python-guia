print("ingrese cantidad de magia del tesoro:")
magia = int(input())
def determinar(magia):
  if magia > 1500:
    print("posees un gran tesoro")
  else:
    print("menuda basura, tira eso al carrer")

determinar(magia)