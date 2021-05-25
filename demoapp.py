import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class NailGrid(GridLayout):
    def __init__(self,**kwargs):
        super(NailGrid, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Customer Name:"))

        self.c_name = TextInput()
        self.add_widget(self.c_name)

        self.add_widget(Label(text="Nail Size:"))
        self.n_size = TextInput()
        self.add_widget(self.n_size)

        self.add_widget(Label(text="Customer Gender"))
        self.c_gender = TextInput()
        self.add_widget(self.c_gender)

        self.press = Button(text="Enter")
        self.press.bind(on_press=self.enter_)
        self.add_widget(self.press)

    def enter_(self,instance):
        print("You have entered your details succesfully")
        print("Name of student is "+self.c_name.text)
        print("Nail size is "+self.n_size.text)
        print("Gender of Customer is "+self.c_gender.text)




class NailBar(App):
    def build(self):
        return NailGrid()




if __name__ =="__main__":
    NailBar().run()

