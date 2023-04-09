# PySimpleGUI使う
# 参考：https://fuji-pocketbook.net/pysimplegui/
import PySimpleGUI as sg

layout = [  [sg.Text("name?"), sg.Input(key="-NAME-")],
            [sg.Text("", key="-ACT-")],
            [sg.Button("Confirm"), sg.Button("Exit")]
        ]

window = sg.Window("title", layout)

while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
                break
        if event == "Confirm":
                window["-ACT-"].update(f"Hi {values['-NAME-']}!")

window.close()