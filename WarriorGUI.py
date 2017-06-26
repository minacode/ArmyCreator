import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from Warrior import Warrior
from OptionGUI import OptionGUI


class WarriorGUI(Gtk.ListBoxRow):
    def __init__(self, warband_gui):
        Gtk.ListBoxRow.__init__(self)

        self.db = warband_gui.db
        self.army_list = warband_gui.army_list
        self.warband_gui = warband_gui

        self.warrior = None

        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        self.header_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)

        self.count_spin_button = Gtk.SpinButton.new_with_range(1, 12, 1)
        self.count_spin_button.connect('value-changed', self.set_count)
        self.count_spin_button.set_sensitive(False)

        warrior_combo_box = Gtk.ComboBoxText()
        warrior_combo_box.connect('scroll-event', lambda box, event: box.emit_stop_by_name('scroll-event'))
        for warrior in self.db.get_all_warriors_from_army(self.army_list):
            warrior_combo_box.append_text(warrior.name)
        warrior_combo_box.connect('changed', self.change_warrior)

        self.points_label = Gtk.Label()

        options_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        self.options_list_box = Gtk.ListBox()
        self.options_list_box.set_selection_mode(Gtk.SelectionMode.NONE)

        self.foreign_options_list_box = Gtk.ListBox()
        self.foreign_options_list_box.set_selection_mode(Gtk.SelectionMode.NONE)

        destroy_button = Gtk.Button.new_with_label('Delete Warrior')
        destroy_button.connect('clicked', self.destroy_gui)
      
        self.add(box)

        box.pack_start(self.header_box, False, False, 0)
        box.pack_start(options_box, False, False, 20)

        options_box.pack_start(self.options_list_box, False, False, 0)
        options_box.pack_start(self.foreign_options_list_box, False, False, 0)
       
        self.header_box.pack_start(warrior_combo_box, False, False, 5)
        self.header_box.pack_start(self.count_spin_button, False, False, 5)
        self.header_box.pack_end(destroy_button, False, False, 5)
        self.header_box.pack_start(self.points_label, False, False, 50)

    def destroy_gui(self, button):
        if self.warrior is not None:
            self.warband_gui.remove_warrior(self.warrior)
        self.destroy()

    def change_warrior(self, combo_box):
        old_warrior = self.warrior
        name = combo_box.get_active_text()
        self.warrior = self.db.get_warrior(name)
        self.warrior.count = self.count_spin_button.get_value_as_int()
        self.count_spin_button.set_sensitive(True)

        if old_warrior is not None:
            self.warband_gui.remove_warrior(old_warrior)
            self.remove_options()
        self.warband_gui.add_warrior(self.warrior)
        self.add_options()
        self.set_foreign_options()
        self.update_points()

    def set_count(self, spin_button):
        if self.warrior is not None:
            self.warrior.count = spin_button.get_value_as_int()
            self.update_warrior_count()
            self.update_points()

    def get_warrior(self):
        return self.warrior

    def update_warrior_count(self):
        self.warband_gui.update_warrior_count()

    def update_points(self):
        self.points_label.set_text(str(self.warrior.get_points()) + 'p')
        self.warband_gui.update_points()
        
    def add_options(self):
        for option in self.db.get_all_options_for_unit(self.warrior.name):
            self.warrior.add_option(option)
            gui = OptionGUI(self, option)
            self.options_list_box.add(gui)

    def set_foreign_options(self):
        if self.warrior is not None:
            self.remove_foreign_options()
            for foreign_option in self.db.get_all_foreign_options_for_unit(self.warrior.name):
                if foreign_option.giving_unit in (h.name for h in self.get_all_heroes()):
                    self.warrior.add_foreign_option(foreign_option)
                    gui = OptionGUI(self, foreign_option)
                    self.foreign_options_list_box.add(gui)
            self.show_all() 

    def remove_options(self):
        self.options_list_box.forall(lambda option_gui: option_gui.destroy())

    def remove_foreign_options(self):
        self.foreign_options_list_box.forall(lambda option_gui: option_gui.destroy())

    def get_all_heroes(self):
        return self.warband_gui.get_all_heroes()
