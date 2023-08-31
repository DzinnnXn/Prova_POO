import os
from classesprova import *

def main():
    taskId = 0
    sair = False
    tasks = ToDoList()
    while sair == False:
        try:
            print("---LISTA DE TAREFAS---")
            print("1 - Adicionar Tarefas")
            print("2 - Remover Tarefas")
            print("3 - Listar Tarefas")
            print("4 - Sair")
            menu = int(input("Selecione: "))
            match menu:
                case 1:
                    os.system("cls")
                    taskId += 1
                    indice = taskId
                    print("---ADICIONAR TAREFA---")
                    descricao = input("Qual a nova tarefa?: ")
                    tasks.adicionar_tarefa(indice, descricao)
                    print("Tarefa Adicionada!!")
                    os.system("pause")

                case 2:
                    os.system("cls")
                    print("---REMOVER TAREFA---")
                    print("---Para remover selecione o indice da tarefa---")
                    tasks.listar_tarefas()
                    indice = int(input("Qual tarefa deseja remover?: "))
                    tasks.excluir_tarefas(indice)
                    print("Tarefa Removida!!")
                    os.system("pause")


                case 3:
                    os.system("cls")
                    print("---TAREFAS---")
                    tasks.listar_tarefas()
                    print("Essas são suas tarefas")
                    os.system("pause")

                case 4:
                    sair = True
        
        except Exception as erro:
            print("Erro Encontrado!!", erro)