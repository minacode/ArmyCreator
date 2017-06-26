import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Warband import Warband
from WarriorGUI import WarriorGUI
from HeroGUI import HeroGUI


class WarbandGUI(Gtk.ListBoxRow):
    def __init__(self, army_list, db, parent):
        Gtk.ListBoxRow.__init__(self)

        self.warband = Warband(army_list)
        self.db = db
        self.army_list = army_list
        self.parent = parent

        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        self.add(self.box)

        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_fraction(0.0)

        self.header_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)

        army_name_label = Gtk.Label(self.warband.army_list)

        self.add_warrior_button = Gtk.Button.new_with_label('Add Warrior')
        self.add_warrior_button.connect('clicked', self.add_warrior_gui)
        self.add_warrior_button.set_sensitive(False)
        
        destroy_button = Gtk.Button.new_with_label('Delete Warband')
        destroy_button.connect('clicked', self.destroy_gui)
        
        hero_gui = HeroGUI(self)

        self.warriors_list_box = Gtk.ListBox()
        self.warriors_list_box.set_selection_mode(Gtk.SelectionMode.NONE)
        
        self.box.pack_start(self.header_box, False, False, 0)
        self.box.pack_start(self.progress_bar, False, False, 5)
        self.box.pack_start(hero_gui, False, False, 5)
        self.box.pack_start(self.warriors_list_box, False, False, 5)
        self.box.pack_end(self.add_warrior_button, False, False, 5)
        
        self.header_box.pack_start(army_name_label, True, True, 5)
        self.header_box.pack_end(destroy_button, False, False, 5)

    def destroy_gui(self, button):
        self.parent.remove_warband(self)
        self.destroy()

    def add_warrior_gui(self, button):
        warrior_gui = WarriorGUI(self)
        self.warriors_list_box.add(warrior_gui)
        self.show_all()

    def add_warrior(self, warrior):
        self.warband.add_warrior(warrior)
        self.update_warrior_count()
        self.update_points()

    def remove_warrior(self, warrior):
        self.warband.remove_warrior(warrior)
        self.update_warrior_count()
        self.update_points()

    def remove_warrior_guis(self):
        self.warriors_list_box.forall(lambda warrior_gui: warrior_gui.destroy())

    def update_warrior_count(self):
        self.progress_bar.set_fraction(self.warband.get_fill_fraction())

    def update_points(self):
        self.parent.update_points()

    def reset_foreign_options(self):
        self.warriors_list_box.forall(lambda w: w.set_foreign_options())
        #self.hero_gui.set_foreign_options()

    def set_hero(self, hero):
        self.warband.set_hero(hero)
        if hero.can_lead:
            self.add_warrior_button.set_sensitive(True)
        else:
            self.add_warrior_button.set_sensitive(False)
            self.warband.remove_all_warriors()
            self.remove_warrior_guis()
        self.update_warrior_count()
        self.update_points()
        self.parent.reset_foreign_options()

    def get_warband(self):
        return self.warband

    def get_all_heroes(self):
        return self.parent.get_all_heroes()
