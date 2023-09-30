from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instr import *
from seconds import Seconds
from ruffier import test


def check_int(str_num):
    try:
        return int(str_num)
    except ValueError:
        return False




class InstructionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction, valign = 'top')
        inp1 = Label(text = txt_name)
        inp2 = Label(text = txt_age)
        line1 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        line2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        self.in_name = TextInput(hint_text = txt_hintname,multiline = False, width = '10sp')
        self.age = TextInput(hint_text = txt_hintage,multiline = False)
        self.but1 = Button(text = 'Далее', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.5})
        self.but1.on_press = self.next
        box = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        line1.add_widget(inp1)
        line1.add_widget(self.in_name)
        line2.add_widget(inp2)
        line2.add_widget(self.age)
        box.add_widget(instr)
        box.add_widget(line1)
        box.add_widget(line2)
        box.add_widget(self.but1)
        self.add_widget(box)
    def next(self):
        global in_name, age
        in_name = self.in_name.text
        age = check_int(self.age.text)
        # if age == False or age < 7:
        #     self.age.text = str()
        # else:
        self.manager.current = 'second'










class PulseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_test1, valign = 'top')
        inp1 = Label(text = 'Введите результат:')
        self.timer = Seconds(1)
        self.timer.bind(done=self.off)
        line1 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        line2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        self.pulse = TextInput(hint_text = txt_hintage,multiline = False, width = '10sp')
        self.pulse.set_disabled(True)
        self.but1 = Button(text = 'Начать', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.5})
        self.but1.on_press = self.next
        box = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        line1.add_widget(inp1)
        line1.add_widget(self.pulse)
        box.add_widget(instr)
        box.add_widget(self.timer)
        box.add_widget(line1)
        box.add_widget(line2)
        box.add_widget(self.but1)
        self.add_widget(box)
        self.next_screen = False
    def next(self):
        global pulse
        if self.next_screen:
            pulse = check_int(self.pulse.text)
            if pulse == False or pulse < 7:
                self.pulse.text = str()
            else:
                self.manager.current = 'third'
        else:
            self.timer.start()
            self.but1.set_disabled(True)
    def off(self,*args):
        self.next_screen = True
        self.but1.set_disabled(False)
        self.but1.text = 'Продолжить'
        self.pulse.set_disabled(False)





class SitsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = 'Выполните 30 приседаний за 45 секунд.', valign = 'top')
        but = Button(text = 'Далее', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.5})
        but.on_press = self.next
        box = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        box.add_widget(instr)
        box.add_widget(but)
        self.add_widget(box)
    def next(self):
        self.manager.current = 'fourth'




class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timer1 = Seconds(5,size_hint = (0.2, 0.2), pos_hint = {'center_x':0.5})
        self.timer2 = Seconds(5,size_hint = (0.2, 0.2), pos_hint = {'center_x':0.5})
        self.timer3 = Seconds(5,size_hint = (0.2, 0.2), pos_hint = {'center_x':0.5})
        self.timer1.bind(done=self.off1)
        self.timer2.bind(done=self.off2)
        self.timer3.bind(done=self.off3)
        instr = Label(text = txt_test3, valign = 'top')
        inp1 = Label(text = 'Результат:')
        inp2 = Label(text = 'Результат после отдыха:')
        line1 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        line2 = BoxLayout(size_hint = (0.8, None), height = '30sp')
        self.result = TextInput(hint_text = '0',multiline = False, width = '10sp')
        self.result1 = TextInput(hint_text = '0',multiline = False)
        self.result.set_disabled(True)
        self.result1.set_disabled(True)
        self.but1 = Button(text = 'Начать', size_hint = (0.2, 0.2), pos_hint = {'center_x':0.5})
        self.but1.on_press = self.next
        box = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        line1.add_widget(inp1)
        line1.add_widget(self.result)
        line2.add_widget(inp2)
        line2.add_widget(self.result1)
        box.add_widget(instr)
        box.add_widget(self.timer1)
        box.add_widget(self.timer2)
        box.add_widget(self.timer3)
        box.add_widget(line1)
        box.add_widget(line2)
        box.add_widget(self.but1)
        self.add_widget(box)
        self.next_screen = False
    def next(self):
        global pulse1, pulse2
        if self.next_screen:
            pulse1 = check_int(self.result.text)
            pulse2 = check_int(self.result1.text)
            if pulse1 == False:
                self.result.text = str()
            elif pulse2 == False:
                self.result1.text = str()
            else:
                self.manager.current = 'fifth'
        else:
            self.timer1.start()
            self.but1.set_disabled(True)
    def off1(self,*args):
        self.but1.text = 'Отдых'
        self.result.set_disabled(False)
        self.timer2.start()
    def off2(self,*args):
        self.but1.text = 'Продолжить'
        self.timer3.start()
    def off3(self,*args):
        self.next_screen = True
        self.but1.set_disabled(False)
        self.result1.set_disabled(False)




class ResultScreen(Screen):
    class Result(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
            self.instr = Label(text='')
            self.outer.add_widget(self.instr)
            self.add_widget(self.outer)
            self.on_enter = self.before

        def before(self):
            global name
            self.instr.text = name + '\n' + test(p1, p2, p3, age)



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstructionScreen(name='main'))
        sm.add_widget(PulseScreen(name='second'))
        sm.add_widget(SitsScreen(name='third'))
        sm.add_widget(Pulse2Screen(name='fourth'))
        sm.add_widget(ResultScreen(name='fifth'))
        return sm



app = MyApp()
app.run()
