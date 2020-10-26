from puzle1 import *
import threading
import gi

gi.require_version("Gtk","3.0")
from gi.repository import GLib, Gtk, Gdk


class MiVentana(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzle 2")
        self.set_default_size(400, 100)
        self.set_position(True)

        self.uid = ""
        self.rf=RfidPN532()
        "buenas"
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.box.set_homogeneous(False)
        self.add(self.box)
        
        self.label = Gtk.Label(label="Please, login with your university card")
        self.box.pack_start(self.label, True, True, 0) 
        
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)
    
    
    def on_button_clicked(self, widget):
        self.label.set_text("Please, login with your university card")
        if(threading.active_count()==1):
            thread = threading.Thread(target = self.lector_targeta, daemon = True)
            thread.start()
        

    def lector_targeta(self):
         self.uid=self.rf.read_uid()
         GLib.idle_add(self.label.set_text, self.uid)
             
def app_main():
     
     ventana = MiVentana()
     ventana.connect("destroy", Gtk.main_quit)
     ventana.show_all()

     thread = threading.Thread(target = ventana.lector_targeta, daemon = True)
     thread.start()
     
         
if __name__=="__main__":
    app_main()
    Gtk.main()
    
                
