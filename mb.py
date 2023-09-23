from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='main'))
        sm.add_widget(SecondScreen(name='second'))
        return sm
    


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = 'привет')
        but1 = ScreenButton(self,text = 'экран2',direction='left',goal='second')
        but2 = ScreenButton(self,text = 'экран3',direction='up',goal='third')
        box = BoxLayout()
        box.add_widget(txt)
        box.add_widget(but1)
        box.add_widget(but2)
        self.add_widget(box)



class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        but1 = Button(text = 'привет')
        but2 = ScreenButton(self,text = 'экран1')
        box = BoxLayout()
        box.add_widget(but1)
        box.add_widget(but2)
        self.add_widget(box)



class ScreenButton(Button):
    def __init__(self,screen,direction='right',goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal




class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout()
        but2 = ScreenButton(self,text = 'назад')
        box.add_widget(but2)
        txt = 'текст'*100
        self.text = Label(text = txt,font_size = '24sp',halign = 'left',valign = 'top') 
    def resize(self,*args):
        self.text.text_size = (self.text.width, None)
        self.text.texture_update()
        self.text.height = self.text.texture_size[1]






def func():
    print('hello world')
    

app = MyApp()
app.run()