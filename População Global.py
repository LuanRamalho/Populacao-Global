# -*- coding: utf-8 -*-
p_Ásia = [0]*9999
p_África = [0]*9999
p_América = [0]*9999
p_Europa = [0]*9999
p_Oceania = [0]*9999

t_Ásia = [0]*9999
t_África = [0]*9999
t_América = [0]*9999
t_Europa = [0]*9999
t_Oceania = [0]*9999

i = 1
j = 0
ano = [0] * 9999

while(i>0):
    print("Digite o ano: ")
    ano[j] = int(input())
    
    print("")
    print("")
    
    print("Digite a população do continente da Ásia: ")
    Ásia = float(input())
    print("Digite a população do continente da África: ")
    África = float(input())
    print("Digite a população do continente da América: ")
    América = float(input())
    print("Digite a população do continente da Europa: ")
    Europa = float(input())
    print("Digite a população do continente da Oceania: ")
    Oceania = float(input())
    
    print("")
    print("")
    
    print("Digite o aumento percentual do população da Ásia: ")
    p_Ásia[j] = float(input())
    print("Digite o aumento percentual do população da África: ")
    p_África[j] = float(input())
    print("Digite o aumento percentual do população da América: ")
    p_América[j] = float(input())
    print("Digite o aumento percentual do população da Europa: ")
    p_Europa[j] = float(input())
    print("Digite o aumento percentual do população da Oceania: ")
    p_Oceania[j] = float(input())
    
    t_Ásia[j] = Ásia + (Ásia*p_Ásia[j])/100
    t_África[j] = África + (África*p_África[j])/100
    t_América[j] = América + (América*p_América[j])/100
    t_Europa[j] = Europa + (Europa*p_Europa[j])/100
    t_Oceania[j] = Oceania + (Oceania*p_Oceania[j])/100
    
    print("")
    print("")
    
    print("População do Continente da Ásia: %.0f" % t_Ásia[j])
    print("Aumento/Dimuniução da População da População da Ásia: %.2f " % p_Ásia[j])
    print("")
    
    print("População do Continente da África: %.0f" % t_África[j])
    print("Aumento/Dimuniução da População da População da África: %.2f" % p_África[j])
    print("")
    
    print("População do Continente da América: %.0f"%t_América[j])
    print("Aumento/Dimuniução da População da População da América: %.2f " % p_América[j])
    print("")
    
    print("População do Continente da Europa: %.0f" % t_Europa[j])
    print("Aumento/Dimuniução da População da População da Europa: %.2f " % p_Europa[j])
    print("")
    
    print("População do Continente da Oceania: %.0f" % t_Oceania[j])
    print("Aumento/Dimuniução da População da População da Oceania: %.2f " % p_Oceania[j])
    
    print("")
    print("")
    
    ano[j] = ano[j] + 10
    j = j + 1
    
    print("")
    print("")
    
    print("Digite 1 para continuar ou 0 para sair.")
    i = int(input())
    
print("")
print("")

a = 0
while(a<j):
    print("Ano: ",ano[a])
    print("População do Continente da Ásia: %.0f" % t_Ásia[a])
    print("Aumento/Dimuniução da População da População da Ásia: %.2f " % p_Ásia[a])
    print("")
    
    print("População do Continente da África: %.0f" % t_África[a])
    print("Aumento/Dimuniução da População da População da África: %.2f" % p_África[a])
    print("")
    
    print("População do Continente da América: %.0f"%t_América[a])
    print("Aumento/Dimuniução da População da População da América: %.2f " % p_América[a])
    print("")
    
    print("População do Continente da Europa: %.0f" % t_Europa[a])
    print("Aumento/Dimuniução da População da População da Europa: %.2f " % p_Europa[a])
    print("")
    
    print("População do Continente da Oceania: %.0f" % t_Oceania[a])
    print("Aumento/Dimuniução da População da População da Oceania: %.2f " % p_Oceania[a])
    print("")
    
    print("")
    print("")
    
    a = a + 1
input()