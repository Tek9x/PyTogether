import PySimpleGUI27 as sg
import simplejson
import untangle

menu_def = [['[F]ile', ['Open', 'Save','---','Edit Mode']],['[P]atchs', ['!Seasonal Events']],['[A]bout']]

tab_farm = [[sg.Text('Farm Name:'), sg.In(disabled=True,key='_name_')],
            [sg.Text('Farm Style:'), sg.Input(disabled=True,key='_style_')],
            [sg.Text('Last Saved: '), sg.Input(disabled=True,key='_saved_')],
            [sg.Text('Season:'), sg.Input(disabled=True, key='_season_')],
            [sg.Text('Weather:'),sg.Input(disabled=True,key='_weather_')],
            [sg.Text('Weather Seed'), sg.Input(disabled=True,key='_seed_')]]

tab_character = [[sg.Text('body:'),sg.Input(size=[15,0],disabled=True,key='_body_'),
                  sg.Text('body type:'),sg.Input(size=[15,0],disabled=True,key='_bodytype_')],
                 [sg.Text('emote0:'), sg.Input(size=[15,0],disabled=True,key='_e0_'),
                  sg.Text('emote1:'),sg.Input(size=[15,0],disabled=True,key='_e1_')],
                 [sg.Text('emote2:'),sg.Input(size=[15,0],disabled=True,key='_e2_'),
                  sg.Text('emote3:'),sg.Input(size=[15,0],disabled=True,key='_e3_')],
                 [sg.Text('eye Color:'),sg.Input(size=[15,0],disabled=True,key='_eyes_'),
                  sg.Text('glasses:'),sg.Input(size=[15,0],disabled=True,key='_glasses_')],
                 [sg.Text('head:'),sg.Input(size=[15,0],disabled=True,key='_head_'),
                  sg.Text('backpack:'),sg.Input(size=[15,0],disabled=True,key='_backpack_')],
                 [sg.Text('Hair:'),sg.Input(size=[15,0],disabled=True,key='_hair_'),
                  sg.Text('Hair Color:'),sg.Input(size=[15,0],disabled=True,key='_haircolor_')]]


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
        window.Element('_body_').Update(obj.Farms.Avatar.Avatar['body'])
        window.Element('_bodytype_').Update(obj.Farms.Avatar.Avatar['bodyType'])
        window.Element('_e0_').Update(obj.Farms.Avatar.Avatar['emote0'])
        window.Element('_e1_').Update(obj.Farms.Avatar.Avatar['emote1'])
        window.Element('_e2_').Update(obj.Farms.Avatar.Avatar['emote2'])
        window.Element('_e3_').Update(obj.Farms.Avatar.Avatar['emote3'])
        window.Element('_eyes_').Update(obj.Farms.Avatar.Avatar['eyeColor'])
        window.Element('_glasses_').Update(obj.Farms.Avatar.Avatar['glasses'])
        window.Element('_head_').Update(obj.Farms.Avatar.Avatar['head'])
        window.Element('_backpack_').Update(obj.Farms.Avatar.Avatar['backpack'])
        window.Element('_hair_').Update(obj.Farms.Avatar.Avatar['hair'])
        window.Element('_haircolor_').Update(obj.Farms.Avatar.Avatar['hairColor'])

    if event == 'Edit Mode':
        window.Element('_name_').Update(disabled=False)
        window.Element('_style_').Update(disabled=False)
        window.Element('_season_').Update(disabled=False)
        window.Element('_weather_').Update(disabled=False)
        window.Element('_seed_').Update(disabled=False)







