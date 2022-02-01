
from PySimpleGUI import PySimpleGUI as sg
from model.Aluno import Aluno
from model.Testte import Testte

def Cadastro():
             nome = str(valores['aluno'])
             telefone = str(valores['matricula'])
             aluno = Aluno(id=None, nome=nome, telefone=telefone)
             print(aluno,telefone)
             dao = Testte()
             dao.cadastrar(aluno) 
             print('Deu certo')
        
             
sg.theme('DarkGreen6')
linha=[
        [sg.Text('Nome'),sg.Input(key='aluno')],
        [sg.Text('Matricula'),sg.Input(key='matricula')],
        [sg.Text('CPF'),sg.Input(key='CPF')],
        [sg.Checkbox('Confirmar')],
        [sg.Button('Cadastrar'),sg.Button('Disciplina')],
        [sg.Output(size=(60,10))]
        
    ]


janela=sg.Window('Aluno',linha)
while True:
    eventos,valores = janela.read()  
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos=='Cadastrar':
        Cadastro()
            
