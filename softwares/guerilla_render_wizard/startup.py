# coding: utf-8
# Author: Leo BRUNEL
# Contact: contact@leobrunel.com

# Python modules
import os

# Wizard modules
from guerilla_render_wizard import wizard_menu
from guerilla_render_wizard import wizard_tools
import wizard_debug

if wizard_debug.is_debugging():
    wizard_debug.connect()

wizard_menu.menu()
wizard_tools.trigger_after_scene_openning_hook()
