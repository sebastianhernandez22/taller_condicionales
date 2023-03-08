#Programa que permita realizar un préstamo bancario, teniendo en cuenta que elpréstamo será otorgado solamente a personas con ingresos superiores a $945200 y que no posea ninguna otra deuda.

#input

ing= int(input("porfavor ingrese sus ingresos: "))
deuda= int(input("porfavor ingrese sus deudas: "))

#processing
if ing > 945200:
    if deuda==0:
        rta =("se aprueba el prestamo ")
    else:
        rta =("prestamo no aprobado ")
else:
    rta =("no se aprueba el prestamo ")            


#output
print(rta)
