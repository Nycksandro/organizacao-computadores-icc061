#Aluno: Nycksandro Lima dos Santos
#Matricula: 22351228

import sys

def memoria_p_arquivo(memoria,arquivo): #Transforma uma memoria em formato de lista em um arquvino no formato .m

    assert len(memoria) <= 256
    with open(arquivo, 'w') as arquivo:
        arquivo.write("v3.0 hex words addressed\n")
        for i in range(len(memoria)):
            string = f'{i:02x}: ' + str(memoria[i] + "\n")
            arquivo.write(string)

def comando_p_hex(arq_instrucoes): #Transforma comandos de asm em uma memoria no formato de lista

    def verificaBase(lista): #Verifica em qual base está o número e converte para Hexadecimal
        if(len(lista) == 2): #Caso especial quando o número possui duas casas e a primeira casa é um 0, a função int() não consegue reconhecer
            if (lista[0] == "0"):
                lista = lista[1]
        numero = int(lista,0)
        if (numero < 16):
            numero = '0' + hex(numero)[2:]
        else:
            numero = hex(numero)[2:]
        return numero
    
    def complementa_memoria(memoria): #complementa a memória com endereços "00" até completar os 256
        while(len(memoria) <= 255):
            memoria.append("00")
        return memoria
    
    dicionario_instrucao = {"ld":"0", "st":"1", "data":"2", "jmpr":"3", "jmp":"40", "jcaez":"5f","jcae":"5e","jcaz":"5d","jca":"5c","jcez":"5b", "jce":"5a","jcz":"59","jc":"58","jaez":"57","jae":"56","jaz":"55","ja":"54","jez":"53","je":"52","jz":"51","j":"50","clf":"60","add":"8","shr":"9","shl":"a","not":"b","and":"c","or":"d","xor":"e","cmp":"f"}
    
    dicionario_registradores = {"r0,r0":"0", "r0,r1":"1","r0,r2":"2","r0,r3":"3","r1,r0":"4","r1,r1":"5","r1,r2":"6","r1,r3":"7","r2,r0":"8","r2,r1":"9","r2,r2":"a","r2,r3":"b","r3,r0":"c","r3,r1":"d","r3,r2":"e","r3,r3":"f"}

    dicionario_instrucoes_in = {"data,r0":"70","data,r1":"71", "data,r2":"72","data,r3":"73","addr,r0":"74","addr,r1":"75","addr,r2":"76","addr,r3":"77"}

    dicionario_instrucoes_out = {"data,r0":"78","data,r1":"79", "data,r2":"7a","data,r3":"7b","addr,r0":"7c","addr,r1":"7d","addr,r2":"7e","addr,r3":"7f"}
    
    dicionario_data = {"r0,":"0","r1":"1","r2":"2","r3":"3"}

      
    memoria = []
    
    with open(arq_instrucoes, 'r') as arq_instrucoes:
        endereco = 0
        for linha in arq_instrucoes: #percorre as linhas do arquivo
            if (linha):
                linha = [' '.join(elm.strip().split()) for elm in linha.splitlines() if elm.strip()] # retira os espaços em brancos no inicio e no final e também retira quando há mais de um
                linha = [x.lower() for x in linha] # torna minusculo os comandos
                linha = [x.split(' ') for x in linha] #separa a string
                lista_aux = [x for lista in linha for x in lista] #separa as strings em listas
    
                for i in range(len(lista_aux)):

                    if(len(lista_aux) > 2): #verifica se está escrito errado, se tiver, é ajeitado
                        lista_aux[1] = ''.join(lista_aux[1:])

                    if (lista_aux[i] == "data"):
                        memoria.append(dicionario_instrucao[lista_aux[i]] + (lista_aux[i+1][1]))
                        memoria.append(verificaBase(lista_aux[i+1][3:])) 
                        endereco += 2

                    elif (lista_aux[i] == "jmpr"):
                        memoria.append(dicionario_instrucao[lista_aux[i]] + dicionario_data[lista_aux[i+1]])
                        endereco += 1

                    elif (lista_aux[i] == "jmp"):
                        memoria.append(dicionario_instrucao[lista_aux[i]])
                        memoria.append(verificaBase(lista_aux[i+1]))
                        endereco += 2

                    elif (lista_aux[i] == "clf"):
                        memoria.append(dicionario_instrucao[lista_aux[i]])
                        endereco += 1

                    elif (lista_aux[i] == "jcaez") or (lista_aux[i] == "jcae") or (lista_aux[i] == "jcaz") or (lista_aux[i] == "jca") or (lista_aux[i] == "jcez") or (lista_aux[i] == "jce") or (lista_aux[i] == "jcz") or (lista_aux[i] == "jc") or (lista_aux[i] == "jaez") or (lista_aux[i] == "jae") or (lista_aux[i] == "jaz") or (lista_aux[i] == "ja") or (lista_aux[i] == "jez") or (lista_aux[i] == "je") or (lista_aux[i] == "jz") or (lista_aux[i] == "j"):
                        memoria.append(dicionario_instrucao[lista_aux[i]])
                        memoria.append(verificaBase(lista_aux[i+1]))
                        endereco += 2

                    elif (lista_aux[i] == "add") or (lista_aux[i] == "shr") or (lista_aux[i] == "shl") or (lista_aux[i] == "not") or (lista_aux[i] == "and") or (lista_aux[i] == "or") or (lista_aux[i] == "xor") or (lista_aux[i] == "cmp") or (lista_aux[i] == "ld") or (lista_aux[i] == "st"):
                        memoria.append(dicionario_instrucao[lista_aux[i]] + dicionario_registradores[lista_aux[i+1]])
                        endereco += 1

                    elif(lista_aux[i] == "out"):
                        memoria.append(dicionario_instrucoes_out[lista_aux[i+1]])
                        endereco += 1

                    elif(lista_aux[i] == "in"):
                        memoria.append(dicionario_instrucoes_in[lista_aux[i+1]])
                        endereco += 1

                    elif(lista_aux[i] == "halt"): #Acaba o programa no logisim
                        memoria.append(dicionario_instrucao["jmp"])
                        memoria.append((verificaBase(hex(endereco))))
                        endereco += 2
                    elif(lista_aux[i] == "swap"): #Troca o conteudo de dois registradores
                        ra = lista_aux[i+1][:2]
                        rb = lista_aux[i+1][3:]
                        memoria.append(dicionario_instrucao["xor"] + dicionario_registradores[(ra + ',' + rb)])
                        memoria.append(dicionario_instrucao["xor"] + dicionario_registradores[(rb + ',' + ra)])
                        memoria.append(dicionario_instrucao["xor"] + dicionario_registradores[(ra + ',' + rb)])
                        endereco += 3
        
                    
    complementa_memoria(memoria)        
    return memoria

# execução do arquivo
memoria = comando_p_hex(sys.argv[1])
memoria_p_arquivo(memoria, sys.argv[2])
