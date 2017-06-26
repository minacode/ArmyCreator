import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class OptionGUI(Gtk.ListBoxRow):
    def __init__(self, parent, option):
        Gtk.ListBoxRow.__init__(self)
        
        self.parent = parent
        self.option = option
       
        box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        self.add(box)

        name_label = Gtk.Label(option.name)
        
        option_switch = Gtk.Switch()
        option_switch.connect("notify::active", self.option_toggle)
        option_switch.set_active(self.option.is_set)
        
        points_label = Gtk.Label(str(option.points) + 'p')
        
        box.pack_start(name_label, False, False, 3)
        box.pack_end(option_switch, False, False, 3)
        box.pack_end(points_label, False, False, 3)
        
    def option_toggle(self, switch, a):
        self.option.toggle_set()
        self.update_points()
        
    def update_points(self):
        self.parent.update_points()
