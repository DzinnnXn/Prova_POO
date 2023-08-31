class ToDoList:
    def __init__(self):
        self.Tarefas = {}

    def adicionar_tarefa(self, indice, descricao):
        self.indice = indice
        self.descricao = descricao
        self.Tarefas[self.indice] = [self.descricao]
        
    def excluir_tarefas(self, indice):
        self.indice = indice
        for self.indice in self.Tarefas.items:
            self.Tarefas = delattr[self.indice]

    def listar_tarefas(self):
            print(self.Tarefas)