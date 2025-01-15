numeroagua = input("cuantas tzas de agua necesitamos?")
numeroagua = float(numeroagua)
numeroharina = input("cuantas tzas de harina PAN necesitamos?")
numeroharina = float(numeroharina)
numerosal = input("cuantas cdtas de sal ecesitamos?")
numerosal = float(numerosal)
numeroaceite = input("cuantas cdas de aceite necesitamos?")
numeroaceite = float(numeroaceite) 
numerosal=numerosal/3
numerosal=numerosal/16
numeroaceite=numeroaceite/16
numerobol = numeroagua + numeroharina + numerosal + numeroaceite
numerobol=numerobol*0.9
print( f"tenemos {numerobol} de volumen de masa")
