bl_info = {
    "name": "Gcode Import",
    "description": "",
    "author": "Heinz Löpmeier",
    "version": (0, 0, 3),
    "blender": (2, 83, 0),
    "location": "3D View > Gcode Import",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}


from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )



if "bpy" in locals():
    import importlib
    importlib.reload(ui) 
    importlib.reload(parser) 


else:
    from . import ui
    from . import parser

import bpy
	


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    ui.import_settings,
    ui.OBJECT_PT_CustomPanel,
    ui.WM_OT_gcode_import
    
)

def register():
	#bpy.utils.register_class(ui.import_settings)
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        bpy.types.Scene.my_tool = PointerProperty(type=ui.import_settings)

def unregister():
	#bpy.utils.unregister_class(ui.import_settings)
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()