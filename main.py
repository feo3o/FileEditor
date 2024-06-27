def write(text):
    with open("file.txt", "a") as file:
        file.write(text)

def read():
    with open("file.txt", "r") as file:
        r = file.read()
        print("*** {} ***".format(r))

def retrieve(word):
    with open("file.txt", "r") as file:
        retrieve = file.read()
        str(retrieve)
        if word in retrieve:
            print("O valor {} existe".format(word))
        return retrieve
    
def delete():
    with open("file.txt", "w") as file:
        file.write("")

while True:
    print("O que você deseja fazer?")
    print("1 - Inserir ")
    print("2 - Deletar ")
    print("3 - Ler ")
    print("4 - Pesquisar se alguma palavra existe")

    answer = int(input(" "))

    match (answer):
        case 1:
            print("Insira o texto: ")
            io = input()
            write(io)
        case 2:
            delete()
        case 3:
            read()
        case 4:
            print("Digite a palavra: ")
            io = input()
            retrieve(io)