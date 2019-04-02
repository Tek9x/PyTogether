import PySimpleGUI27 as sg
import simplejson
import untangle

menu_def = [['[F]ile', ['Open', 'Save','---','Edit Mode']],['[P]atchs'],['[A]bout']]

tab_farm = [[sg.Text('Farm Name:'), sg.In(disabled=True,key='_name_')],
            [sg.Text('Farm Style:'), sg.Input(disabled=True,key='_style_')],
            [sg.Text('Last Saved: '), sg.Input(disabled=True,key='_saved_')],
            [sg.Text('Season:'), sg.Input(disabled=True, key='_season_')],
            [sg.Text('Weather:'),sg.Input(disabled=True,key='_weather_')],
            [sg.Text('Weather Seed'), sg.Input(disabled=True,key='_seed_')]]

tab_character = [[sg.Text('character')]]

tab_pet = [[sg.Text('pet')]]

tab_money = [[sg.Text('money')]]

layout = [[sg.MenuBar(menu_def)
              , sg.TabGroup([[sg.Tab('Farm Information', tab_farm)
                                 , sg.Tab('Character', tab_character)
                                 , sg.Tab('Pet', tab_pet)]])]]

window = sg.Window('Pytogether').Layout(layout)

def seasonparser():
    if db['Season'] is 0:
        return 'no specific season'
    if db['Season'] is 1:
        return 'spring'
    if db['Season'] is 2:
        return 'summer'
    if db['Season'] is 4:
        return 'fall'
    if db['Season'] is 8:
        return 'winter'

def weatherparser():
    if db['Weather'] is 0:
        return 'normal'
    if db['Weather'] is 1:
        return 'rain'
    if db['Weather'] is 2:
        return 'snow'
    if db['Weather'] is 3:
        return 'rain'

while True:
    event, value = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'Open':
        filename = sg.PopupGetFile('Open File',no_window=True, file_types=(("Uncompressed File", "*.uc"),))
        with open(filename) as f:
            db = simplejson.load(f)
        obj = untangle.parse('farms.xml')
        window.Element('_name_').Update(obj.Farms.Farms.Farm['name'])
        window.Element('_style_').Update(db['FarmStyle'])
        window.Element('_saved_').Update(db['SaveDate'])
        window.Element('_season_').Update(seasonparser())
        window.Element('_weather_').Update(weatherparser())
        window.Element('_seed_').Update(db['WeatherRandom'])






