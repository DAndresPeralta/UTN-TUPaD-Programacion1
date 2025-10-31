#  Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial1 = {60 , 72, 55, 85, 15, 63, 25}
parcial2 = {12, 55, 63, 85, 33, 25, 90}

aprobados1 = {nota for nota in parcial1 if nota >= 60}
aprobados2 = {nota for nota in parcial2 if nota >= 60}

ambos = aprobados1 & aprobados2
print("Aprobaron ambos parciales:", ambos)

soloUno = aprobados1 ^ aprobados2
print("Aprobaron solo uno de los dos:", soloUno)

alMenosUno = aprobados1 | aprobados2
print("Aprobaron al menos un parcial:", alMenosUno)