import gi
import time
import threading

gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello world")

        #self.button = Gtk.Button(label="Click Here")
        self.label = Gtk.Label(label="Buenas")
        #self.button.connect("clicked", self.on_button_clicked)
#       self.add(self.button)
        self.add(self.label)
        

    def on_button_clicked(self,widget):
        print("Hello world")

def funcion_thread():
    time.sleep(4)
    win.label.set_text("tardes")


win = MyWindow()
win.connect("destroy",Gtk.main_quit)
win.show_all()

thread=threading.Thread(target=funcion_thread, daemon=True)
thread.start()

Gtk.main()
