#add-on name = ShakeObjects
#id name = shake.objects
#category = 3D View
#author = ishidourou

####################################
# Shake Mesh Objects
#       v.1.0
#  (c)ishidourou 2014
####################################

#!BPY
import bpy

bl_info = {
    "name": "ShakeObjects",
    "author": "ishidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar and View3D",
    "description": "ShakeObjects",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": '3D View'}

class mes():
    title = ('Measures to particles for 2.7','2.7 パーティクルバグ？対策')
    btn1 = ('Shake Selected Mesh Objects','選択したメッシュＯＢを揺らします')

def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0

#    Menu in tools region
class ShakeObjectsPanel(bpy.types.Panel):
    lng = lang()
    bl_label = mes.title[lng]
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        self.layout.operator("shake.objects")

#---- Measures to bug in 2.7 ----

def shakeobjects():
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.transform.translate(value=(0.1, 0, 0))
    bpy.ops.transform.translate(value=(-0.1, 0, 0))

#---- main ------
class ShakeObjects(bpy.types.Operator):
    lng = lang()
    bl_idname = "shake.objects"
    bl_label = mes.btn1[lng]
    bl_options = {'REGISTER'}

    def execute(self, context):
        slist = bpy.context.selected_objects

        for i in slist:
             if i.type == 'MESH':
                shakeobjects()
        
        return{'FINISHED'}

#	Registration

def register():
    bpy.utils.register_class(ShakeObjectsPanel)
    bpy.utils.register_class(ShakeObjects)

def unregister():
    bpy.utils.unregister_class(ShakeObjectsPanel)
    bpy.utils.unregister_class(ShakeObjects)

if __name__ == "__main__":
    register()