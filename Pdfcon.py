import PySimpleGUI as sg
from convertermetres import ft_inch_to_m


ftinch_label = sg.Text("Enter ft and inc: ")
ftinch_input_box = sg.InputText(key="ftinch")

layout = 0

m_label = sg.Text("Value in metres: ")
m_input_box = sg.InputText(key="metres")

convert_btn = sg.Button("Convert", key="Convert")
leave_btn = sg.Button("leave", key="leave")

window = sg.Window(title="feet and inches to metres converter", layout=[[ftinch_label, ftinch_input_box],
                   [m_label, m_input_box],
                   [convert_btn, leave_btn]])

while True:

    event, values = window.read()
    match event:
        case 'convert':
            meters = ft_inch = values["ftinch"]
            window[("metres")].update(meters)
            ft_inch_to_m(ft_inch)
        case 'exit':
            exit()

    window.close()
    .