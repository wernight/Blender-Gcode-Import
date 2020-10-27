import bpy
from . import parser

from bpy.props import (StringProperty,
                       BoolProperty,
                       PointerProperty,
                       FloatProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )


from bpy_extras.io_utils import ImportHelper



class import_settings(PropertyGroup):

    # gcode_path: StringProperty(
    #     name = "Directory",
    #     description="Choose a directory:",
    #     default="",
    #     maxlen=1024,
    #     subtype='FILE_PATH'
    #     )

    split_layers: BoolProperty(
        name="Split Layers",
        description="Save every layer as single Objects in Collection",
        default = True
        )

    subdivide: BoolProperty(
        name="Subdivide",
        description="Only Subdivide gcode segments that are bigger than 'Segment length' ",
        default = False
        )

    max_segment_size: FloatProperty(
        name = "",
        description = "Only Segments bigger then this value get subdivided",
        default = 1,
        min = 0.1,
        max = 999.0
        )



# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class OBJECT_PT_CustomPanel(Panel):
    bl_label = "Gcode Import"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Gcode-Import"
    bl_context = "objectmode"   

    @classmethod
    def poll(cls, context):
        return context.mode in {'OBJECT', 'EDIT_MESH'}#with this poll addon is visibly even when no object is selected

    # @classmethod
    # def poll(self,context):
    #     return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        #layout.prop(mytool, "gcode_path")     
        layout.prop(mytool, "split_layers")
         
        
        layout.prop(mytool, "subdivide")
        col=layout.column(align=True)
        col = col.row(align=True)
        col.split()
        col.label(text="Segment length")
        
    
        col.prop(mytool, "max_segment_size")
        col.enabled =  mytool.subdivide
        col.separator()

        col=layout.column()
		#row=col.row()
        col.scale_y = 2.0
        col.operator("wm.gcode_import")


        


def import_gcode(context, filepath):
    print("running read_some_data...")

    #f = open(filepath, 'r', encoding='utf-8')
    #data = f.read()
    #f.close()

    scene = context.scene
    mytool = scene.my_tool
    import time
    then = time.time()

    parse = parser.GcodeParser()
    model = parse.parseFile(filepath)
    
    if mytool.subdivide:
        model.subdivide(mytool.max_segment_size)
    model.classifySegments()
    if mytool.split_layers:
        model.draw(split_layers=True)
    else:
        model.draw(split_layers=False)

    now=time.time()
    print("then", then)
    print("importing Gcode took", now-then)

    return {'FINISHED'}


class WM_OT_gcode_import(Operator, ImportHelper):
    """Import Gcode, travel lines don't get drawn"""
    bl_idname = "wm.gcode_import"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Import Gcode"

    # ImportHelper mixin class uses this
    filename_ext = ".txt"

    filter_glob: StringProperty(
        default="*.*",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )



    def execute(self, context):
        return import_gcode(context, self.filepath)


