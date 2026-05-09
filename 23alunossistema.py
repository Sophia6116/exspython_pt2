quantidade_cadastros=0
soma=0
# função para calcular a média
def media_turma(qtd_cadastro,soma_notas):
    media = soma_notas/qtd_cadastro
    return media
# biblioteca pra guardar os dados dos estudantes
infos = {
    "nomes" : [],
    "idades" : [],
    "notas" : [],
    "situacoes" : []
}
# loopão pra controlar as entradas
while True:
        # loops menores ppoder voltar na pergunta em questão
        while True:
            nome= str (input("Nome do aluno: "))
            infos["nomes"].append(nome)
            break
        while True:
            try:
                # peço a idade
                idade= int (input("Idade do aluno: "))
                # verifico se é maior q zero
                if idade<=0:
                    print ("Erro: Idade deve ser acima de 0")
                else:
                    # se for maior q zero, ele joga no final da lista idades na dict infos
                    infos["idades"].append(idade)
                    break
            except ValueError: 
                print("Erro! Valor inválido!")
        while True:
            try:
                nota= float(input("Nota do aluno: "))
                if nota<0 or nota>10:
                    print ("A nota deve ser entre 0 e 10")
                else:
                    infos["notas"].append(nota)
                    # para contar a quantidade de cadastrados
                    quantidade_cadastros+=1
                    # p já ir somando as notas cadastradas, p usar na média
                    soma += nota
                    break
            except ValueError:
                print ("Valor inválido! Tente novamente")
                # transforma e letra em minúsculo
        continuar= str(input("Deseja continuar? S/N: ")).lower()
        if continuar == "n":
            break
# função pra calcular as situações dos alunos
def situacao_turma(notas):
    # uma lista p ir armazenando as situações 
    situacao = []
    # contadores zerados
    aprovados=0
    recuperacao=0  
    reprovados=0
    # pega cada nota q tem na lista notas, e vai testando, contando e jogando no fim da lista de situacao
    for pegar in notas:
        if pegar >= 7:
            situacao.append("Aprovado")
            aprovados+=1
        elif pegar>4:
            situacao.append("Recuperação")
            recuperacao+=1
        else:
            situacao.append("Reprovado")
            reprovados+=1
    return aprovados, recuperacao, reprovados, situacao

# pega a lista de notas na dict infos, e taca na variavel notas da função
# pega oq está nas variaveis do return, e coloca nessas, na mesma ordem 
aprov, recup, reprov, situacao = situacao_turma(infos["notas"])
infos["situacoes"] = situacao
 
  
maior = max(infos["notas"])
menor = min(infos["notas"])
result= media_turma(quantidade_cadastros,soma)   

print (f"\nQuantidade de cadastros: {quantidade_cadastros}") 
print (f"Média da turma: {result:.1f}")
print (f"Maior nota da turma: {maior}\nMenor nota da turma: {menor}")
print (f"Aprovados: {aprov}\nRecuperação: {recup}\nReprovados: {reprov}\n")

mostrar_dados= input("Deseja exibir os dados dos alunos? S/N: \n").lower()
if mostrar_dados == "s":
    print (f"""     DADOS DOS ALUNOS     """)    
          
    for mostrar in range(quantidade_cadastros):
        print(f"""
        Nome: {infos["nomes"][mostrar]}
        Idade: {infos["idades"][mostrar]}
        Nota: {infos["notas"][mostrar]:.1f}
        Situação: {infos["situacoes"][mostrar]}
        """)
# as tres aspas serve serve para poder deixar as infos em linhas diferentes sem dar erro (tenta apagar as aspas), e na hr da apresentação o python separa como está aki tbm(usei p fazer um titulo em console, LGL NEH?)
else:
    exit()
    # pra sair do codigo, lgl neh?
    # eu coloquei p pedir p apresentar os dados dos alunos, e não direto, pq podem ter 1000 alunos, sla,
    # e carregaria tudo junto. Mas se quiser, é só tirar, e pode arrastar a formatação tbm 
    # (sobre o espaçamento dos dados, eu achei mais organizado)

   