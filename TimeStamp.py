import datetime
print("\nInserisci il numero TimeStamp del quale vuoi sapere la data \n")
timestamp = int(input("# "))
value = datetime.datetime (1, 1, 1) + datetime.timedelta(seconds=timestamp/10000000)
print("Data > ",value.strftime('%d-%m-%Y'))
#print("Data & Ora > ",value.strftime('%d-%m-%Y %H:%M:%S')) #Se si vuole vedere anche l'orario
