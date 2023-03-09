from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty

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
        self.data = [{'nombre': str(x)} for x in range(100)]

class ElementCard1(MDCard):
    nombre = StringProperty()
    pass

class TestApp(MDApp):
    def build(self):
        return RV()

TestApp().run()