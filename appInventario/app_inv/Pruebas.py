from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from firebase import firebase
from kivymd.uix.card import MDCard
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.screenmanager import MDScreenManager

Builder.load_file('inv.kv')


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class ScreenManager1(MDScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManager1, self).__init__(**kwargs)

    pass


class PreviousMDIcons(MDScreen):

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )
            self.ids.search_field.text = productos[0]['nombre']

        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

class Inventario(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    #def search(self):
    #    self.ids.recyleview.data = [i for i in productos if
    #                                self.ids.InventarioSearch.text in i['nombre']]
        #self.extract_data()
    pass

class ElementCard1(MDCard):
    nombre = StringProperty()
    #img = StringProperty()
    descripcion = StringProperty()
    Inventario = StringProperty()
    departamento = StringProperty()
    categoria = StringProperty()
    subcategoria = StringProperty()
    color = StringProperty()
    precio = StringProperty()
    precio_compra = StringProperty()
    sku = StringProperty()
    _id = StringProperty()

class CustomRecycleView(MDRecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global productos, departamentos, categorias, subcategorias, conn_prods
        #conn = pymongo.MongoClient("mongodb+srv://Jarcieria_Mary:8d37s9X0Ec8JbJRX@clusterjar.pp4z5hn.mongodb.net/?retryWrites=true&w=majority")
        #conn_prods = conn.get_database('Jarcieria').Productos
        #productos = conn_prods.find()
        #productos = list(productos)
        firebase_mary = firebase.FirebaseApplication('https://jarcieria-mary-default-rtdb.firebaseio.com/', None)
        productos_firebase = firebase_mary.get('/my_endpoint', '')
        productos = list(productos_firebase.values())
        departamentos = ['Plasticos', 'Limpieza']
        categorias = ['Baño', 'Ropa', 'Casa', 'Jardin', 'Personal']
        subcategorias = ['Lazos', 'Zacates', 'Pinzas', 'Termos', 'Macetas', 'Tuppers', 'Recipientes', 'Atomizadores',
                        'Fibras', 'Utensilios', 'Coladores', 'Escobas', 'Escobetillas', 'Recogedores', 'Ganchos',
                        'Lavabo', 'Cocina', 'Habitacion']
        for producto,_id in zip(productos, productos_firebase.keys()):
            producto['img'] = producto['img'].replace('C:/Users/Marco/Documents/Jarcieria/Imgs/', 'Imgs/')
            producto['_id'] = _id
        self.data = productos
        #print(productos)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        global productos
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()
        firebase_mary = firebase.FirebaseApplication('https://jarcieria-mary-default-rtdb.firebaseio.com/', None)
        productos_firebase = firebase_mary.get('/my_endpoint', '')
        productos = list(productos_firebase.values())
        print(productos[0])
        #return kv

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()


MainApp().run()