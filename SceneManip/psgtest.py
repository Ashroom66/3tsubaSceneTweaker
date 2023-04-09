# PySimpleGUI使う
# 参考：https://fuji-pocketbook.net/pysimplegui/
import PySimpleGUI as sg

layout = [  [sg.Text("name?"), sg.Input()],
            [sg.Text("sex?"), sg.Input("mare")],
            [sg.Button("Confirm"), sg.Button("Exit"), sg.Button(), sg.Button('はい', key='-YES-')]
        ]

window = sg.Window("title", layout)

event, values = window.read()
window.close()

print(f"event:\t{event}")
print(f"values:\t{values}")
# event:  Confirm
# values: {0: 'aaaaa', 1: 'mare'}

# event:  Exit
# values: {0: 'asdfas', 1: 'mare'}

# event:
# values: {0: '', 1: 'mare'}

# event:  -YES-
# values: {0: 'aaaaa', 1: 'mare'}