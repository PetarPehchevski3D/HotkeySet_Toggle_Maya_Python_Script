import maya.cmds as cmds

"""Change the temporary names to the names of your hotkey sets. If the hotkey set names have spaces in them
you have to add an underscore in the script instead of the space"""

if cmds.hotkeySet(q=True, current=True) == "Second_HotkeySet_Name":
    cmds.hotkeySet("First_HotkeySet_Name", e=True, current=True)
    cmds.inViewMessage(amg="First_HotkeySet_Name", pos='midCenter', fade=True, fst=1000, ck=True)
elif cmds.hotkeySet(q=True, current=True) == "First_HotkeySet_Name":
    cmds.inViewMessage(amg="Second_HotkeySet_Name", pos='midCenter', fade=True, fst=1000, ck=True)
    cmds.hotkeySet("Second_HotkeySet_Name", e=True, current=True)
else:
    cmds.inViewMessage(amg="Second_HotkeySet_Name", pos='midCenter', fade=True, fst=1000, ck=True)
    cmds.hotkeySet("Second_HotkeySet_Name", e=True, current=True)
