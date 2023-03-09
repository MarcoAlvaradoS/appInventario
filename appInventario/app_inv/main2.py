from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from firebase import firebase
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy import platform

from kivy.lang import Builder

Builder.load_file('app.kv')

class ScreenManager1(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManager1, self).__init__(**kwargs)
    def get_data(self):
        self.ids.UiId.ids.recyleview.data = productos
        #self.ids.InventarioId.ids.recyleview.data = productos
    pass


    # def menu_item(self, dropdown, clase, dpn):
    #     self.menu_items = [
    #         {
    #             "viewclass": "OneLineListItem",
    #             "text": f"{i}",
    #             "height": dp(56),
    #             "on_release": lambda x=f"{i}": self.set_item(x, dropdown, self.menu_dep if dpn == 1 else self.menu_cat if dpn == 2 else self.menu_subcat),
    #         } for i in clase
    #     ]
    #
    #     if dpn == 1:
    #         self.menu_dep = MDDropdownMenu(
    #             caller=dropdown,
    #             items=self.menu_items,
    #             position="center",
    #             width_mult=4,
    #         )
    #         self.menu_dep.bind()
    #     if dpn == 2:
    #         self.menu_cat = MDDropdownMenu(
    #             caller=dropdown,
    #             items=self.menu_items,
    #             position="center",
    #             width_mult=4,
    #         )
    #         self.menu_cat.bind()
    #     if dpn == 3:
    #         self.menu_subcat = MDDropdownMenu(
    #             caller=dropdown,
    #             items=self.menu_items,
    #             position="center",
    #             width_mult=4,
    #         )
    #         self.menu_subcat.bind()
    #
    # def menu_item_dep(self, item_departamento, item_categoria, item_subcategoria):
    #     self.menu_item(self.ids.ProductoId.ids.PCId.ids.drop_item_departamento, departamentos, 1)
    #     self.ids.ProductoId.ids.PCId.ids.drop_item_departamento.ids.label_item.text = item_departamento
    #     self.menu_item(self.ids.ProductoId.ids.PCId.ids.drop_item_categoria, categorias, 2)
    #     self.ids.ProductoId.ids.PCId.ids.drop_item_categoria.ids.label_item.text = item_categoria
    #     self.menu_item(self.ids.ProductoId.ids.PCId.ids.drop_item_subcategoria, subcategorias, 3)
    #     self.ids.ProductoId.ids.PCId.ids.drop_item_subcategoria.ids.label_item.text = item_subcategoria
    #
    # def set_item(self, text_item, dropdown, menu):
    #     dropdown.set_item(text_item)
    #     menu.dismiss()
    #
    # def update_mongo(self):
    #     producto = conn_prods.find_one({'_id': id_current_prod})
    #     producto['nombre'] = self.ids.ProductoId.ids.PCId.ids.nombre_id.text
    #     producto['descripcion'] = self.ids.ProductoId.ids.PCId.ids.descripcion_id.text
    #     producto['sku'] = self.ids.ProductoId.ids.PCId.ids.sku_id.text
    #     producto['color'] = self.ids.ProductoId.ids.PCId.ids.color_id.text
    #     producto['precio'] = self.ids.ProductoId.ids.PCId.ids.precio_id.text
    #     producto['Inventario'] = self.ids.ProductoId.ids.PCId.ids.inventario_id.text
    #     producto['precio_compra'] = self.ids.ProductoId.ids.PCId.ids.precio_compra_id.text
    #     producto['departamento'] = self.ids.ProductoId.ids.PCId.ids.drop_item_departamento.ids.label_item.text
    #     producto['categoria'] = self.ids.ProductoId.ids.PCId.ids.drop_item_categoria.ids.label_item.text
    #     producto['subcategoria'] = self.ids.ProductoId.ids.PCId.ids.drop_item_subcategoria.ids.label_item.text
    #     conn_prods.update_one({'_id': id_current_prod}, {"$set": producto}, upsert=False)
    #
    #     productos = conn_prods.find()
    #     productos = list(productos)
    #     #print(
    #     self.ids.InventarioId.ids.recyleview.data = productos
        #)
        # print(self.ids.ProductoId.ids.PCId.ids.drop_item_departamento.ids.label_item.text)
    # def presion(self, nombre, img, des, inv, sku, col, precio, id, precio_compra):
    #     global id_current_prod
    #     self.current = 'Producto'
    #     self.ids.ProductoId.ids.PCId.nombre = nombre
    #     self.ids.ProductoId.ids.PCId.img = img
    #     self.ids.ProductoId.ids.PCId.descripcion = des
    #     self.ids.ProductoId.ids.PCId.Inventario = inv
    #     self.ids.ProductoId.ids.PCId.sku = sku
    #     self.ids.ProductoId.ids.PCId.color = col
    #     self.ids.ProductoId.ids.PCId.precio = precio
    #     self.ids.ProductoId.ids.PCId.precio_compra = precio_compra
    #     id_current_prod = id

class Inventario(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # def search(self):
    #     self.ids.recyleview.data = [i for i in productos if
    #                                 self.ids.InventarioSearch.text in i['nombre']]
        #self.extract_data()
    pass

class Ui(Screen):
    pass

class Tienda(Screen):
    pass

class CustomRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.productos = None


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

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = ScreenManager1()
        global productos, departamentos, categorias, subcategorias, conn_prods
        # conn = pymongo.MongoClient("mongodb+srv://Jarcieria_Mary:8d37s9X0Ec8JbJRX@clusterjar.pp4z5hn.mongodb.net/?retryWrites=true&w=majority")
        # conn_prods = conn.get_database('Jarcieria').Productos
        # productos = conn_prods.find()
        # productos = list(productos)
        firebase_mary = firebase.FirebaseApplication('https://jarcieria-mary-default-rtdb.firebaseio.com/', None)
        productos_firebase = firebase_mary.get('/my_endpoint', '')
        productos = list(productos_firebase.values())
        departamentos = ['Plasticos', 'Limpieza']
        categorias = ['Baño', 'Ropa', 'Casa', 'Jardin', 'Personal']
        subcategorias = ['Lazos', 'Zacates', 'Pinzas', 'Termos', 'Macetas', 'Tuppers', 'Recipientes', 'Atomizadores',
                         'Fibras', 'Utensilios', 'Coladores', 'Escobas', 'Escobetillas', 'Recogedores', 'Ganchos',
                         'Lavabo', 'Cocina', 'Habitacion']
        for producto, _id in zip(productos, productos_firebase.keys()):
            producto['img'] = producto['img'].replace('C:/Users/Marco/Documents/Jarcieria/Imgs/', 'Imgs/')
            producto['_id'] = _id



    def build(self):
        return self.screen

MainApp().run()
