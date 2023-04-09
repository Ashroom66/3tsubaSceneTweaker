# PySimpleGUI使う
# 参考：https://fuji-pocketbook.net/pysimplegui/
import PySimpleGUI as sg

layout = [  [sg.Text("1行目")],
            [sg.Text("2行目")],
            [sg.Text("3行目"), sg.Text("これも3行目")]
        ]

window = sg.Window("title", layout)

event, values = window.read()
window.close()

