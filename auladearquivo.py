import shutil
def escrever_arquivo(texto):
    diretorio = 'c:/user/wnasc/pycharmprojects/treinamento'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_doarquivo, texto):
    arquivo = open(nome_doarquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_doarquivo):
    arquivo = open(nome_doarquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_doarquivo):
    arquivo = open('notas.txt', 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') #split para criar uma lista.
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0) #retira um item da lista.
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(f'{aluno}: notas -> {lista_notas} | média -> {media(lista_notas)}')

def copia_arquivo(nome_doarquivo):
    shutil.copy(nome_doarquivo, 'c:/users/wnasc')

def move_arquivo(nome_doarquivo):
    shutil.move(nome_doarquivo, 'c:/users/wnasc/documents')





if __name__ == '__main__':
   
