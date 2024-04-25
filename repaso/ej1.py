def calc_imc(peso, altura):
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura * altura)
    if imc <= 18.5:
        return print("IMC:", imc, "Talla S, desnutrido")
    elif imc <= 24.9:
        return print("IMC:", imc, "Talla M, peso normal")
    elif imc <= 29.9:
        return print("IMC:", imc, "Talla L, sobrepeso")
    else:
        return print("IMC:", imc, "Talla XL, obeso")
    
peso = input("Ingrese su peso en kg: ")
altura = input("Ingrese su altura en metros: ")
calc_imc(peso, altura)
