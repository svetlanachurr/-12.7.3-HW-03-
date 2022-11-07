per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму денег ")
money = float(money)

deposits = []

deposits.append(money * (100+per_cent["ТКБ"]) / 100.0)
deposits.append(money * (100+per_cent["СКБ"]) / 100.0)
deposits.append(money * (100+per_cent["ВТБ"]) / 100.0)
deposits.append(money * (100+per_cent["СБЕР"]) / 100.0)

print(deposits)

max(deposits)
print( "Максимальная сумма, которую вы можете заработать —", max(deposits))
