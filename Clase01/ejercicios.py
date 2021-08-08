saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
Pago_adicional = 1000
mes = 0
total_pagado = 0.0

while saldo > 0:
    while mes < 12:
        saldo = saldo * (1+tasa/12) - pago_mensual - Pago_adicional
        total_pagado = total_pagado + pago_mensual + Pago_adicional
        mes = mes + 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))
f'total pagad0 = ${total_pagado} cantidad de meses= ${mes}'

# =============================================================================
#calcula el total de letras O 
# =============================================================================
total = 0
cadena = "Ejemplo con for"
for c in cadena:
    if c == 'o':
        total = total + 1
print('existen:', total, 'o')

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
frutas.lower() 