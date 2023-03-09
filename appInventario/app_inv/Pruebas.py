from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from firebase import firebase
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

Builder.load_string('''
<ScreenManager1>:
    Ui:
        id: UiId
        
<ElementCard1>:
    orientation: 'vertical'
    pos_hint: {'center_x': .5, 'center_y':.5}
    size_hint: 1, 0.2
    height: '20dp'
    radius: '10dp'
    spacing: '10dp'
    padding: '10dp'
    line_color: 0,0,1,1
    ripple_behavior: True
    radius: 20
    on_release: app.root.presion(root.nombre, root.img, root.descripcion, root.Inventario, root.sku, root.color, root.precio, root._id, root.precio_compra)
    on_release: app.root.menu_item_dep(root.departamento, root.categoria, root.subcategoria)
    MDLabel:
        text: root.nombre
        halign:'center'
    FitImage:
        source: root.img
        size_hint_y: 3
        radius: '10dp'
    MDLabel:
        text: root.descripcion
        halign:'center'
    MDLabel:
        text: root.Inventario
        halign:'center'

<Ui>:
    name: 'Ui'
    MDScreen:        
        RV:
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
    img = StringProperty()
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
    pass

class ScreenManager1(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManager1, self).__init__(**kwargs)
    pass

class Ui(MDScreen):
    pass

class TestApp(MDApp):
    def build(self):
        return ScreenManager1()

TestApp().run()