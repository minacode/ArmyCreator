import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Hero import Hero
from OptionGUI import OptionGUI


class HeroGUI(Gtk.Box):
    def __init__(self, warband_gui):
        Gtk.Box.__init__(self, orientation = Gtk.Orientation.VERTICAL)

        self.db = warband_gui.db
        self.army_list = warband_gui.army_list
        self.warband_gui = warband_gui

        self.hero = None

        header_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)

        hero_combo_box = Gtk.ComboBoxText()
        hero_combo_box.connect('scroll-event', lambda box, event: box.emit_stop_by_name('scroll-event'))
        for hero in self.db.get_all_heroes_from_army(self.army_list):
            hero_combo_box.append_text(hero.name)
        hero_combo_box.connect('changed', self.change_hero)
        
        self.points_label = Gtk.Label()
        
        self.options_list_box = Gtk.ListBox()
        self.options_list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        
        header_box.pack_start(hero_combo_box, False, False, 5)
        header_box.pack_start(self.points_label, False, False, 50)
        
        self.pack_start(header_box, False, False, 0)
        self.pack_start(self.options_list_box, False, False, 20)
        

    def change_hero(self, combo_box):
        old_hero = self.hero
        self.remove_options()
        name = combo_box.get_active_text()
        self.hero = self.db.get_hero(name)
        self.points_label.set_text(str(self.hero.get_points()) + 'p')
        self.warband_gui.set_hero(self.hero)
        self.add_options()
        self.update_points()
        
    def get_hero(self):
        return self.hero

    def update_points(self):
        self.points_label.set_text(str(self.hero.get_points()) + 'p')
        self.warband_gui.update_points()
        
    def add_options(self):
        for option in self.db.get_all_options_for_unit(self.hero.name):
            self.hero.add_option(option)
            gui = OptionGUI(self, option)
            self.options_list_box.add(gui)
        self.show_all()
            
    def remove_options(self):
        self.options_list_box.forall(lambda option_gui: option_gui.destroy())
