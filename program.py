import PySimpleGUI as sg
import os


def create_new_inventory():
    layout = [[sg.Text('Create a new inventory:'), sg.InputText()],
              [sg.Submit('Create'), sg.Cancel("Exit")]]

    window = sg.Window('Create a new inventory', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif len(values[0]) > 0:
            f = open(os.path.abspath(os.path.join('.', 'inventories', "{}.json".format(values[0]))), "w")
            f.close()
            break
    window.close()


def update_inventory(inventories):
    layout = list()
    for inventory in inventories:
        layout.append([sg.Text(inventory, enable_events=True), sg.Button("Show")])
    layout.append([sg.Submit('New inventory'), sg.Cancel("Exit")])
    return layout


def show_layout(inventory):
    f = open(os.path.abspath(os.path.join('.', 'inventories', inventory)), 'r')
    data = f.read()
    print(data)


def show_list():
    inventories = os.listdir(os.path.abspath(os.path.join('.', 'inventories')))
    window = sg.Window('Create a new inventory', update_inventory(inventories))
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            window.close()
            break
        elif event == 'New inventory':
            window.close()
            create_new_inventory()
            window = sg.Window('Create a new inventory', update_inventory(inventories))
        elif event in inventories:
            print(event)
            window.close()
            show_layout(event)
            window = sg.Window('Create a new inventory', update_inventory(inventories))


def main():
    if len(os.listdir(os.path.abspath(os.path.join('.', 'inventories')))) == 0:
        create_new_inventory()
    show_list()


if __name__ == '__main__':
    main()
