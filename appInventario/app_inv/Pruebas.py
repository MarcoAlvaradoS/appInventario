from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from firebase import firebase
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
import pymongo

Builder.load_file('inv.kv')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        global productos, departamentos, categorias, subcategorias, conn_prods, firebase_mary
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

    def menu_item(self, dropdown, clase, dpn):
        self.menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "height": dp(56),
                "on_release": lambda x=f"{i}": self.set_item(x, dropdown, self.menu_dep if dpn == 1 else self.menu_cat if dpn == 2 else self.menu_subcat),
            } for i in clase
        ]

        if dpn == 1:
            self.menu_dep = MDDropdownMenu(
                caller=dropdown,
                items=self.menu_items,
                position="center",
                width_mult=4,
            )
            self.menu_dep.bind()
        if dpn == 2:
            self.menu_cat = MDDropdownMenu(
                caller=dropdown,
                items=self.menu_items,
                position="center",
                width_mult=4,
            )
            self.menu_cat.bind()
        if dpn == 3:
            self.menu_subcat = MDDropdownMenu(
                caller=dropdown,
                items=self.menu_items,
                position="center",
                width_mult=4,
            )
            self.menu_subcat.bind()

    def menu_item_dep(self, item_departamento, item_categoria, item_subcategoria):
        self.menu_item(self.ids.ProductoId.ids.PCId.ids.drop_item_departamento, departamentos, 1)
        self.ids.ProductoId.ids.PCId.ids.drop_item_departamento.ids.label_item.text = item_departamento
        self.menu_item(self.ids.ProductoId.ids.PCId.ids.drop_item_categoria, categorias, 2)
        self.ids.ProductoId.ids.PCId.ids.drop_item_categoria.ids.label_item.text = item_categoria
        self.menu_item(self.ids.ProductoId.ids.PCId.ids.drop_item_subcategoria, subcategorias, 3)
        self.ids.ProductoId.ids.PCId.ids.drop_item_subcategoria.ids.label_item.text = item_subcategoria

    def set_item(self, text_item, dropdown, menu):
        dropdown.set_item(text_item)
        menu.dismiss()

    def update_mongo(self):
        prod_id = '/my_endpoint/' + id_current_prod
        firebase_mary.put(prod_id, 'nombre', self.ids.ProductoId.ids.PCId.ids.nombre_id.text)
        firebase_mary.put(prod_id, 'descripcion', self.ids.ProductoId.ids.PCId.ids.descripcion_id.text)
        firebase_mary.put(prod_id, 'sku', self.ids.ProductoId.ids.PCId.ids.sku_id.text)
        firebase_mary.put(prod_id, 'color', self.ids.ProductoId.ids.PCId.ids.color_id.text)
        firebase_mary.put(prod_id, 'precio', self.ids.ProductoId.ids.PCId.ids.precio_id.text)
        firebase_mary.put(prod_id, 'Inventario', self.ids.ProductoId.ids.PCId.ids.inventario_id.text)
        firebase_mary.put(prod_id, 'precio_compra', self.ids.ProductoId.ids.PCId.ids.precio_compra_id.text)
        firebase_mary.put(prod_id, 'departamento', self.ids.ProductoId.ids.PCId.ids.drop_item_departamento.ids.label_item.text)
        firebase_mary.put(prod_id, 'categoria', self.ids.ProductoId.ids.PCId.ids.drop_item_categoria.ids.label_item.text)
        firebase_mary.put(prod_id, 'subcategoria', self.ids.ProductoId.ids.PCId.ids.drop_item_subcategoria.ids.label_item.text)

        productos_firebase = firebase_mary.get('/my_endpoint', '')
        productos = list(productos_firebase.values())

        for producto,_id in zip(productos, productos_firebase.keys()):
            producto['img'] = producto['img'].replace('C:/Users/Marco/Documents/Jarcieria/Imgs/', 'Imgs/')
            producto['_id'] = _id

        self.ids.UiId.ids.recyleview.data = productos

    def presion(self, nombre, img, des, inv, sku, col, precio, id, precio_compra):
        global id_current_prod
        self.current = 'Producto'
        self.ids.ProductoId.ids.PCId.nombre = nombre
        self.ids.ProductoId.ids.PCId.img = img
        self.ids.ProductoId.ids.PCId.descripcion = des
        self.ids.ProductoId.ids.PCId.Inventario = inv
        self.ids.ProductoId.ids.PCId.sku = sku
        self.ids.ProductoId.ids.PCId.color = col
        self.ids.ProductoId.ids.PCId.precio = precio
        self.ids.ProductoId.ids.PCId.precio_compra = precio_compra
        id_current_prod = id
    pass

class Ui(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def search(self):
        self.ids.recyleview.data = [i for i in productos if
                                    self.ids.InventarioSearch.text in i['nombre']]
    pass

class Menu(MDScreen):
    pass

class Producto(MDScreen):
    pass

class ProductoCard(MDCard):
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

class TestApp(MDApp):
    def build(self):
        return ScreenManager1()

TestApp().run()