from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.button import Button
from kivy.properties import StringProperty

Builder.load_string('''
<ElementCard@Button1>:
    text: root.nombre
            
<RV>:
    viewclass: 'ElementCard'
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

class Button1(Button):
    nombre = StringProperty()
    pass

class TestApp(App):
    def build(self):
        return RV()

TestApp().run()