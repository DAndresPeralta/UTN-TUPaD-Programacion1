# Contador Binario:
# Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria.
# Extensión: Utilicen un retardo (por ejemplo, con time.sleep) para simular el conteo de un circuito.

n = 0;
residuo = 0;

# En este primer bucle for se toma el numero  i del 0 al 15 y se guarda en la variable n
for i in range(16):
    n = i;
    # La variable "binario" almacenara el valor del numero en binario
    binario = ''
    # En este segundo bucle for se realiza la conversion del numero decimal n a binario
    for j in range(4):
        # Aqui se calcular el resto de dividir el numero n entre 2  y se almacena en la variable residuo
        residuo = n % 2;
        # En la variable "binario" se va formando el numero binario
        binario = str(residuo) + binario;
        # Se actualiza el valor de n dividiendolo entre 2
        n = n // 2;
    print(f'Decimal: {i} ---> Binario: {binario}');