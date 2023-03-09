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



Builder.load_string('''
#: import RiseInTransition kivy.uix.screenmanager.RiseInTransition

<ScreenManager1>:
    Menu:
        id: MenuId
    Ui:
        id: UiId
    Producto:
        id: ProductoId
    
<ProductoCard>:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '10dp'
    line_color: 0,0,1,1
    radius: 20
    rows: 2
    MDCard:
        size_hint: 1, 0.58
        orientation: 'vertical'
        pos_hint: {'center_x': .5, 'center_y':.5}
        rows:3
        MDCard:
            size_hint: 1, 0.3
            spacing: '10dp'
            orientation: 'horizontal'
            cols: 2
            #line_color: 0,0,1,1
            MDIconButton:
                icon: 'arrow-u-left-top-bold'
                on_release: app.root.current = 'Inventario'
            MDTextField:
                id: nombre_id
                adaptive_size: True
                text: root.nombre
                halign:'center'
                valign: 'bot'
        FitImage:
            adaptive_size: True
            source: root.img
            size_hint_y: 1
            size_hint_x: .5
            pos_hint: {'center_x': .5, 'center_y':.5}
            radius: '5dp'
        MDTextField:
            id: descripcion_id
            adaptive_size: True
            text: root.descripcion
            halign: 'center'
            valign: 'bot'
    MDCard:
        size_hint: 1, 0.42
        radius: '10dp'
        spacing: '10dp'
        padding: '10dp'
        orientation: 'horizontal'
        cols: 2
        line_color: 0,0,1,1
        MDBoxLayout:
            orientation: 'vertical'
            valign:'top'
            size_hint: .3, 1
            MDGridLayout:
                size_hint: 1, .33 #x,y
                cols: 1
                padding: '5dp'
                spacing: '5dp'
                MDLabel:
                    text: 'Departamento'
                    size_hint: 1, .5
                MDDropDownItem:
                    id: drop_item_departamento
                    on_release: app.root.menu_dep.open()
            MDGridLayout:
                size_hint: 1, .34 #x,y
                cols: 1
                padding: '5dp'
                spacing: '5dp'
                MDLabel:
                    text: 'Categoría'
                    size_hint: 1, .5
                MDDropDownItem:
                    id: drop_item_categoria
                    text: 'item 1'
                    on_release: app.root.menu_cat.open()
            MDGridLayout:
                size_hint: 1, .33 #x,y
                cols: 1
                padding: '5dp'
                spacing: '5dp'
                MDLabel:
                    text: 'Subcategoria'
                    size_hint: 1, .5
                MDDropDownItem:
                    id: drop_item_subcategoria
                    text: 'item 1'
                    on_release: app.root.menu_subcat.open()
        MDBoxLayout:
            orientation: 'vertical'
            pos_hint: {'center_x': .5, 'center_y':.5}
            MDBoxLayout:
                orientation: 'horizontal'
                MDLabel:
                    size_hint: .1, 1
                    text: 'SKU:'
                MDTextField:
                    id: sku_id
                    size_hint: .9, 1
                    halign:'left'
                    text: root.sku
            MDBoxLayout:
                orientation: 'horizontal'
                MDLabel:
                    size_hint: .1, 1
                    text: 'Color:'
                MDTextField:
                    id: color_id
                    size_hint: .9, 1
                    halign:'left'
                    text: root.color
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: '10dp'
                halign:'left'
                MDLabel:
                    size_hint: .2, 1
                    text: 'Precio venta:'
                MDTextField:
                    id: precio_id
                    size_hint: .2, 1
                    halign:'left'
                    text: root.precio
                MDLabel:
                    size_hint: .24, 1
                    text: 'Precio compra:'
                MDTextField:
                    id: precio_compra_id
                    size_hint: .36, 1
                    halign:'left'
                    text: root.precio_compra
            MDBoxLayout:
                orientation: 'horizontal'
                spacing: '10dp'
                MDLabel:
                    size_hint: .16, 1
                    text: 'Inventario:'
                MDTextField:
                    id: inventario_id
                    size_hint: .20, 1
                    text: root.Inventario
                MDRectangleFlatButton:
                    size_hint: .64, .8
                    text: 'Actualizar'
                    on_release: app.root.update_mongo()
                    
                    
<ElementCard@MDCard>:
    text: ''
    radius: '10dp'
    spacing: '10dp'
    padding: '10dp'
    line_color: 0,0,1,1
    ripple_behavior: True
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: root.text
            text_color: 'black'
            font_size: 50
            halign: 'center'
            
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
        
<Menu>:
    name: 'menu'
    MDScreen:
        name: 'Principal'
        MDBoxLayout:
            orientation: 'vertical'
            MDBoxLayout:
                size_hint: 1, .1 #x,y}
                MDCard:
                    radius: '10dp'
                    padding: '10dp'
                    line_color: 1,0,1,1
                    MDLabel:
                        text: 'Menú principal'
                        font_size: 50
                        halign: 'center'
            MDGridLayout:
                size_hint: 1, .9 #x,y
                cols: 1
                padding: '25dp'
                spacing: '25dp'

                ElementCard:
                    text: 'Productos'
                    on_release:
                        app.root.current = 'Ui'
                        root.manager.transition.direction = 'left'
                ElementCard:
                    text: 'Tienda'

<Ui>:
    name: 'Ui'
    MDScreen:
        MDBoxLayout:
            orientation: 'vertical'
            radius: '10dp'
            padding: '10dp'
            spacing: '10dp'

            MDLabel:
                size_hint: 1, .1 #x,y
                text: 'Inventario'
                font_size: 20
                halign: 'center'


            MDBoxLayout:
                orientation: 'horizontal'
                size_hint: .7, .12
                halign: 'left'
                MDTextField:
                    id: InventarioSearch
                    size_hint: .8, 1
                    hint_text: "Nombre del producto"
                    halign:'left'
                    valign:'top'
                    on_text: root.search()
                MDIconButton:
                    id: BotonInventarioBuscar
                    size_hint: .2, 1
                    icon: "database-search"
                    halign:'left'
                    valign:'top'
                    on_release: root.search()
            RV:
                viewclass: 'ElementCard1'
                id: recyleview
                RecycleGridLayout:
                    cols: 3
                    padding: '10dp'
                    spacing: '10dp'
                    default_size: None, '300dp'
                    default_size_hint: 1, None
                    size_hint_y: None
                    height: self.minimum_height
                    MDIconButton:
                
<Producto>:
    name: 'Producto'
    id: 'Producto'
    MDScreen:
        MDBoxLayout:
            orientation: 'vertical'
            radius: '10dp'
            padding: '10dp'
            spacing: '10dp'
            ProductoCard:
                id: PCId
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
        producto = conn_prods.find_one({'_id': id_current_prod})
        producto['nombre'] = self.ids.ProductoId.ids.PCId.ids.nombre_id.text
        producto['descripcion'] = self.ids.ProductoId.ids.PCId.ids.descripcion_id.text
        producto['sku'] = self.ids.ProductoId.ids.PCId.ids.sku_id.text
        producto['color'] = self.ids.ProductoId.ids.PCId.ids.color_id.text
        producto['precio'] = self.ids.ProductoId.ids.PCId.ids.precio_id.text
        producto['Inventario'] = self.ids.ProductoId.ids.PCId.ids.inventario_id.text
        producto['precio_compra'] = self.ids.ProductoId.ids.PCId.ids.precio_compra_id.text
        producto['departamento'] = self.ids.ProductoId.ids.PCId.ids.drop_item_departamento.ids.label_item.text
        producto['categoria'] = self.ids.ProductoId.ids.PCId.ids.drop_item_categoria.ids.label_item.text
        producto['subcategoria'] = self.ids.ProductoId.ids.PCId.ids.drop_item_subcategoria.ids.label_item.text
        conn_prods.update_one({'_id': id_current_prod}, {"$set": producto}, upsert=False)

        productos = conn_prods.find()
        productos = list(productos)
        #print(
        self.ids.InventarioId.ids.recyleview.data = productos
        #)
        # print(self.ids.ProductoId.ids.PCId.ids.drop_item_departamento.ids.label_item.text)

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