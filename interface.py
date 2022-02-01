
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
        
             
def estudante():
    sg.theme('DarkGreen6')
    linha=[
        [sg.Text('Nome'),sg.Input(key='aluno')],
        [sg.Text('Matricula'),sg.Input(key='matricula')],
        [sg.Text('CPF'),sg.Input(key='CPF')],
        [sg.Checkbox('Confirmar')],
        [sg.Button('Cadastrar'),sg.Button('Disciplina')],
        [sg.Output(size=(60,10))]
    ]
    return sg.Window('Aluno',linha,finalize=True)

def materia():
    sg.theme('DarkGreen6')
    linha=[
        [sg.Text('Nome'),sg.Input(key='Nome')],
        [sg.Text('Codigo'),sg.Input(key='Codigo')],
        [sg.Text('Nota1'),sg.Input(key='Nota1')],
        [sg.Text('Nota2'),sg.Input(key='Nota2')],
         [sg.Text('Nota3'),sg.Input(key='Nota3')],

        [sg.Button('Adicionar'),sg.Button('Retornar')],
        [sg.Output(size=(60,10))]
        ]
    return sg.Window('Disciplina',linha,finalize=True) 

janela1,janela2=aluno(),None

while True:
    window,evento,valores=sg.read_all_windows()

    if window==janela1 and evento == sg.WIN_CLOSED:
        
     break
    if window==janela2 and evento == sg.WIN_CLOSED:
        
     break
    if window==janela1 and evento=='Disciplina':
        janela2= materia()
        janela1.hide()
    if window==janela2 and evento=='Retornar':
         janela2.hide()
         janela1.un_hide()
    if window==janela1 and evento=='Cadastrar':
        Cadastro()
            
