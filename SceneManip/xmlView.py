import PySimpleGUI as sg
import mitsuba as mi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# variant
mi.set_variant('llvm_ad_rgb')

# Styles
plt.axis('off')
sg.theme('Green')

def mk_render():
    fig = plt.figure()
    # ここにMitsubaのレンダリング
    original_image = mi.render(mi.load_file(values["-RenderPath-"]), spp=128)
    return plt.imshow(original_image ** (1.0/2.2))
    


def update_renderWindow():
    # update sg window
    imgPanel = window["-Image-"]
    imgPanel.update(data=mk_render().tobytes())
    

render_canvas = [sg.Image(key="-Image-")]

layout = [
    [sg.Text("シーンファイル"), sg.InputText(key="-RenderPath-"), sg.FileBrowse(key="-Browse-")],
    [sg.Button("保存(WIP)"), sg.Button("レンダー", key="-Render-")],
    [render_canvas]
]
window = sg.Window("MitsubaXMLviewer(ver.0.01)", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-Render-":
        update_renderWindow()

window.close()
