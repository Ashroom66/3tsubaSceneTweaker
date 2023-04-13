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

# mitsuba data
scene = ""
params = ""

def mk_renderFig():
    global scene, params
    # ここにMitsubaのレンダリング
    original_image = mi.render(scene, spp=128)
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
    print(fig.get_size_inches())
    window["-Params-"].set_size=(300, fig.get_size_inches()[1]*fig.dpi)

def update_parameter():
    print("update")
    global params
    prop_key = values["-Params-"][0]
    try:
        params[prop_key] = eval(values["-Property-"])
        params.update()
        print("property changed")
    except Exception as e:
        print ('=== ERROR ===')
        print ('type:' + str(type(e)))
        print ('args:' + str(e.args))
        print ('e自身:' + str(e))
        print ('=============')
        pass

def update_propCanvas():
    # propへ選択中のkeyの内容を表示
    prop_key = values["-Params-"][0]
    prop_canvas.update(params[prop_key])
    print(type(params[prop_key]))
    print(params[prop_key])

def read_XML():
    # XMLファイルからパラメータ一覧を取り出す
    # menu_contentsにパラメータ一覧を登録する
    global scene, params, menu_contents, window
    scene = mi.load_file(values["-RenderPath-"])
    params = mi.traverse(scene)
    menu_contents = [i for i in params.keys()]
    window["-Params-"].update(menu_contents)

menu_contents = []  # str array
render_canvas = sg.Image(key="-Image-",size=(640,480))
params_canvas = sg.Listbox(values=[], key="-Params-", size=(30, 20), enable_events=True)
prop_canvas = sg.Multiline(default_text="", key="-Property-", size=(30, 7), enable_events=True)
parameters_column = sg.Column(layout=[[params_canvas], [sg.HorizontalSeparator()], [prop_canvas]])

layout = [
    [sg.Text("シーンファイル"), sg.InputText(key="-RenderPath-", enable_events=True), sg.FileBrowse(key="-Browse-")],
    [sg.Button("保存(WIP)"), sg.Button("レンダー", key="-Render-")],
    [render_canvas, sg.VerticalSeparator(), parameters_column]
]
window = sg.Window("MitsubaXMLviewer(ver.0.4)", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-Render-":
        update_renderWindow()
    elif event == "-RenderPath-":
        read_XML()
    elif event == "-Params-":
        update_propCanvas()
    elif event == "-Property-":
        update_parameter()

window.close()
