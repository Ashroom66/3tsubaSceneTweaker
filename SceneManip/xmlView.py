import PySimpleGUI as sg
import mitsuba as mi
import numpy as np
import io
import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# variant
mi.set_variant('llvm_ad_rgb')

# Styles
sg.theme('Green')

def mk_renderFig():
    # ここにMitsubaのレンダリング
    original_image = mi.render(mi.load_file(values["-RenderPath-"]), spp=128)
    image = original_image ** (1.0/2.2)

    dpi =72
    fig = plt.figure(figsize=(image.shape[0]/dpi, image.shape[1]/dpi))
    ax = fig.add_subplot(1,1,1)
    plt.axis('off')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.imshow(image)
    return fig
    


def update_renderWindow():
    # update sg window
    fig = mk_renderFig()
    item = io.BytesIO()
    plt.savefig(item, format="png")
    plt.clf()
    imgPanel = window["-Image-"]
    imgPanel.update(data=item.getvalue(),size=(fig.get_size_inches()*fig.dpi))
    

render_canvas = [sg.Image(key="-Image-",size=(640,480))]

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
