#! /bin/python

from Database import Database
from ArmyList import ArmyList
from WarbandGUI import WarbandGUI
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

db = Database('database.db')
 
class MyWindow(Gtk.Window):
    def __init__(self, db, army_list):
        Gtk.Window.__init__(self, title="Hobbit Army List Tool")

        self.db = db
        self.army_list = army_list
   
        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        self.set_titlebar(header_bar)
   
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        self.points_label = Gtk.Label('0p')

        add_warband_button = Gtk.Button.new_with_label('Add Warband')
        add_warband_button.connect('clicked', self.add_warband)

        self.army_combo_box = Gtk.ComboBoxText()
        self.army_combo_box.connect('scroll-event', lambda box, event: box.emit_stop_by_name('scroll-event'))
        for army in db.get_all_armies():
            self.army_combo_box.append_text(army.name)

        self.warbands_list_box = Gtk.ListBox()
        self.warbands_list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        
        self.add(scrolled_window)
        scrolled_window.add(self.warbands_list_box)
        
        header_bar.pack_start(self.army_combo_box)
        header_bar.pack_start(add_warband_button)
        header_bar.pack_start(self.points_label)
        
        scrolled_window.show_all()

    def update_points(self):
        self.points_label.set_text(str(self.army_list.get_points()) + 'p') 

    def add_warband(self, button):
        army = self.army_combo_box.get_active_text()
        if army is not None:
            gui = WarbandGUI(army, self.db, self)
            self.warbands_list_box.add(gui)
            self.show_all()
            self.army_list.add_warband(gui.get_warband())
        self.update_points()

    def remove_warband(self, warband_gui):
        self.army_list.remove_warband(warband_gui.get_warband())
        self.update_points()

    def get_all_heroes(self):
        return self.army_list.get_all_heroes()

    def reset_foreign_options(self):
        self.warbands_list_box.forall(lambda w: w.reset_foreign_options())


army_list = ArmyList()
win = MyWindow(db, army_list)
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
