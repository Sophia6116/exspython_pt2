try:
    preco= float (input("Digite o preço: "))
    qtd= int (input("Digite a quantidade: "))
    result= preco*qtd
    print (f"Preço final: R${result}")
except:
    print ("Erro: Valor inválido")