
####################################
# MMCopy(メッシュミラーコピー)
#       v.1.01
#  (c)ishidourou 2014
####################################

#!BPY
import bpy
from bpy.props import *

bl_info = {
    "name": "MMCopy",
    "author": "ishidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar and View3D",
    "description": "MMCopy",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'MESH'}

#    メッセージ（英語,日本語）
class mes():
    title = ('Mesh Mirror Copy','メッシュミラーコピー')
    btn01 = ('xcopy','Xコピー')
    ermes = ('Changed Edit Mode.','編集モードに移行しました')
    selectmesh = ('Please Select Mesh Object','メッシュオブジェクトを選択してください')

def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0

mmc_wmessage  = 'Please Select Edges.'
class ErrorDialog(bpy.types.Operator):
    bl_idname = "error.dialog"
    bl_label = 'warning'
    bl_options = {'REGISTER'}

    my_message = 'warnig' 
    def execute(self, context):
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        global mmc_wmessage 
        self.layout.label(mmc_wmessage )

def error(message):
    global mmc_wmessage 
    mmc_wmessage  = message
    bpy.ops.error.dialog('INVOKE_DEFAULT')

#    Menu in tools region
class MMCopyPanel(bpy.types.Panel):
    lng = lang()
    bl_category = "Tools"
    bl_label = mes.title[lng]
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row(align=True)
        row.operator("mm.copyx",text='X')
        row.operator("mm.copyy",text='Y')
        row.operator("mm.copyz",text='Z')

#---- main ------

def mesh_mirror_copy(axis):
    obj = bpy.ops.object
    cobj = bpy.context.object
    cosp = bpy.context.space_data

    if cobj.type != 'MESH':
        error(mes.selectmesh[lang()])
        return -1 
    if cobj.mode != 'EDIT':
        obj.mode_set(mode='EDIT')
        error(mes.ermes[lang()])
        return -1

    obj.mode_set(mode='OBJECT')
    bpy.ops.view3d.snap_cursor_to_selected()
    obj.mode_set(mode='EDIT')

    pv = cosp.pivot_point
    cosp.pivot_point = 'CURSOR'

    bpy.ops.mesh.duplicate_move()
    if axis == 'x':
        bpy.ops.transform.mirror(constraint_axis=(True, False, False))
    elif axis == 'y':
        bpy.ops.transform.mirror(constraint_axis=(False, True, False))
    elif axis == 'z':
        bpy.ops.transform.mirror(constraint_axis=(False, False, True))
  
    bpy.ops.mesh.flip_normals()
    bpy.context.space_data.pivot_point = pv

class MMCopyX(bpy.types.Operator):
    lng = lang()
    bl_idname = "mm.copyx"
    bl_label = 'X'
    bl_options = {'REGISTER'}

    def execute(self, context):
        mesh_mirror_copy('x')
        return{'FINISHED'}

class MMCopyY(bpy.types.Operator):
    lng = lang()
    bl_idname = "mm.copyy"
    bl_label = 'Y'
    bl_options = {'REGISTER'}

    def execute(self, context):
        mesh_mirror_copy('y')
        return{'FINISHED'}

class MMCopyZ(bpy.types.Operator):
    lng = lang()
    bl_idname = "mm.copyz"
    bl_label = 'Z'
    bl_options = {'REGISTER'}

    def execute(self, context):
        mesh_mirror_copy('z')
        return{'FINISHED'}

#	Registration

def register():
    bpy.utils.register_class(MMCopyPanel)
    bpy.utils.register_class(MMCopyX)
    bpy.utils.register_class(MMCopyY)
    bpy.utils.register_class(MMCopyZ)
    bpy.utils.register_class(ErrorDialog)

def unregister():
    bpy.utils.unregister_class(MMCopyPanel)
    bpy.utils.unregister_class(MMCopyX)
    bpy.utils.unregister_class(MMCopyY)
    bpy.utils.unregister_class(MMCopyZ)
    bpy.utils.unregister_class(ErrorDialog)

if __name__ == "__main__":
    register()

