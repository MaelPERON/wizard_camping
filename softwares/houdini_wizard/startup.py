# coding: utf-8
# Author: Leo BRUNEL
# Contact: contact@leobrunel.com

# Wizard modules
from houdini_wizard import wizard_tools
import wizard_debug

if wizard_debug.is_debugging():
    wizard_debug.connect()

wizard_tools.trigger_after_scene_openning_hook()
