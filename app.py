import pyttsx3
import PySimpleGUI as sg
from regex import W


tema = "DarkPurple4"

fonte = "Helvitica 15 bold italic"



def criar_janela():
    sg.theme(tema)

    layout = [
        [sg.Text("Escreva algo interessante:")],
        [sg.Input("", key="-FRASE-", border_width=5, pad=(0,16))],
        [sg.Button("Falar", size=(7, 1), border_width=5)]
    ]

    return sg.Window("PYTHON FALANTE", layout=layout, finalize=True, element_justification="center", font=fonte, margins=(10, 10))


def falar():
    robo = pyttsx3.init("sapi5")
    msg_robo = values["-FRASE-"]
    robo.setProperty("voice", "brazil")
    robo.setProperty("rate", 120)
    robo.setProperty("volume", 1.)
    robo.say(msg_robo)

    return robo.runAndWait()
    


janela = criar_janela()

while True:
    window, event, values = sg.read_all_windows(timeout=1)

    if window == janela and event == sg.WIN_CLOSED:
        break
    if window == janela and event == "Falar":
        falar()
    

    