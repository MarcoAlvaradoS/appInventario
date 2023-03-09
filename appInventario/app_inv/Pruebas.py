from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from firebase import firebase

Builder.load_string('''
<ElementCard1>:
    text: ''
    radius: '10dp'
    spacing: '10dp'
    padding: '10dp'
    line_color: 0,0,1,1
    ripple_behavior: True
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: root.nombre
            text_color: 'black'
            font_size: 50
            halign: 'center'
            
<RV>:
    viewclass: 'ElementCard1'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        global productos, departamentos, categorias, subcategorias, conn_prods
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

class ElementCard1(MDCard):
    nombre = StringProperty()
    pass

class TestApp(MDApp):
    def build(self):
        return RV()

TestApp().run()