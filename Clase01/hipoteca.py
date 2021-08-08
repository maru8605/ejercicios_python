saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
Pago_adicional = 1000
mes = 0
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    while mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual - Pago_adicional
        total_pagado = total_pagado + pago_mensual + Pago_adicional
        mes = mes + 1
        print(mes, round(total_pagado, 2), round(saldo, 2))
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    print(mes, round(total_pagado, 2), round(saldo, 2))
    if saldo < pago_mensual:
        saldo = saldo - saldo
        total_pagado = total_pagado + saldo
        print(mes, round(total_pagado, 2), round(saldo, 2))
print('mes:', mes, 'total pagado', round(
    total_pagado, 2), 'saldo adeudado:', round(saldo, 2))
