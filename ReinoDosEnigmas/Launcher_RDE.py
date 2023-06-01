import PySimpleGUI as sg
import subprocess
import pygetwindow as gw

# Definindo o layout da janela
layout = [
    [sg.Text("Reino dos enigmas", size=(20, 1), font=("Modern No. 20", 20), text_color="black", background_color="white")],
    [sg.Button("Iniciar", size=(9, 1), button_color=("black", "white"), border_width=3), sg.Button("Sair", size=(9, 1), button_color=("black", "white"), border_width=3)]
]

# Definindo as configurações da janela
window_config = {
    "background_color": "white",
    "element_padding": (5, 5),
    "auto_size_buttons": True,
    "default_button_element_size": (12, 2),
    "text_justification": "center"
}

# Definindo o ícone da janela
sg.set_options(icon='ReinoDosEnigmas\logoRDE.ico')

# Criando a janela
window = sg.Window("Launcher Reino Dos Enigmas", layout, **window_config)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    
    if event == "Iniciar":
        file_path = "ReinoDosEnigmas\ReinoDosEnigmas.py"
        try:
            subprocess.Popen(["python", file_path], shell=True)
            launcher_window = gw.getWindowsWithTitle("Launcher Reino Dos Enigmas")[0]
            launcher_window.minimize()
        except Exception as e:
            sg.popup_error(f"Ocorreu um erro ao executar o jogo:\n{str(e)}")
    
window.close()
