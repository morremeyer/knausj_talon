from talon import app, Context, Module

mod = Module()
@mod.action_class
class Actions:  
    def desktop_down():
        """Go down a desktop"""
        
    def desktop_up():
        """Go up a desktop"""

    def move_window_desktop_down():
        """Move the currently focused window a down a desktop"""

    def move_window_desktop_up():
        """Move the currently focused window a up a desktop"""
