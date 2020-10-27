from puzle1 import *
import threading
import gi

gi.require_version("Gtk","3.0")
from gi.repository import GLib, Gtk, Gdk


class MiVentana(Gtk.Window):
    def __init__(self):

        #Creación de la ventana
        Gtk.Window.__init__(self, title="Puzle 2")
        self.set_default_size(400, 100)
        self.set_position(True)

        #Instancia de argumentos
        self.uid = ""
        self.rf=RfidPN532()

        #Creación de la Box donde colocaremos los elementos de la ventana
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.box.set_homogeneous(False)
        self.add(self.box)

        #Creación de una EventBox para la estilización
        self.eventbox = Gtk.EventBox()
        self.eventbox.override_background_color(0, Gdk.RGBA(0.1, 0.8, 0.1, 1))

        #css = b'* {background-color: #555be6; color: #ffffff} button {color: #ffffff; }'  Esta opción es descartada, porque a mi juicio queda mejor con el EventBox
        css = b'* {color: #0010ff }'
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css)
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION) 

        #Creación del label inicial
        self.label=Gtk.Label()
        self.label.set_markup("Please, login with your <i>university card</i>")
        self.eventbox.add(self.label)

        #Creación y conexión del boton clear
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.eventbox, True, True, 0)
        self.box.pack_start(self.button, True, True, 0)
    
    
    def on_button_clicked(self, widget):
        self.label.set_markup("Please, login with your <i>university card</i>")
        self.eventbox.override_background_color(0, Gdk.RGBA(0.1, 0.8, 0.1, 1))
        if(threading.active_count()==1):
            thread = threading.Thread(target = self.lector_targeta, daemon = True)
            thread.start()
        

    def cambio_color(self):
        self.eventbox.override_background_color(0, Gdk.RGBA(0.8, 0.1, 0.1 ,1))
    
    def mostrar_uid(self):
        self.label.set_markup("UID: <b> " + self.uid + "</b>")

    def lector_targeta(self):
         self.uid=self.rf.read_uid()
         GLib.idle_add(self.mostrar_uid,)
         GLib.idle_add(self.cambio_color,)

#Código principal programa            
def app_main():
     
     ventana = MiVentana()
     ventana.connect("destroy", Gtk.main_quit)
     ventana.show_all()

     thread = threading.Thread(target = ventana.lector_targeta, daemon = True)
     thread.start()
     
         
if __name__=="__main__":
    app_main()
    Gtk.main()
    
                
