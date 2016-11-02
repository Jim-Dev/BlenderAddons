
####################################
# MakeEnvmap
#       v.0.2
#  (c)ishidourou 2014
####################################

#!BPY
import bpy
from bpy.props import *

bl_info = {
    "name": "MakeEnvmap",
    "author": "ishidourou",
    "version": (0, 1),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar and View3D",
    "description": "MakeEnvmap",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'Material'}

#   language(jp-eng)
class mes():
    title = ('Make Envmap','環境マップ一発作成ツール')
    btn1 = ('Make envmap','環境マップを作成')
    dst1 = ('Material Name:','マテリアル名:')

def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0
  
#    Menu in tools region
class MakeEnvmapPanel(bpy.types.Panel):
    lng = lang()
    bl_label = mes.title[lng]
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        self.layout.operator("make.envmap")

#---- main ------

def makeenv(matname):
    
    cobj = bpy.context.object
    if cobj == None or cobj.type != 'MESH':
        bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=1)
        cobj = bpy.context.object

    #bpy.ops.texture.envmap_clear()
    mat = bpy.data.materials.new(matname)
    cobj.data.materials.append(mat)
 
    cobj.data.materials[0] = mat
    cobj.active_material.diffuse_color = (0.5, 0.5, 0.5)
    cobj.active_material.specular_shader = 'WARDISO'

    tex = bpy.data.textures.new(matname+'_tex',type='ENVIRONMENT_MAP')

    mtex = mat.texture_slots.add()
    mtex.texture = tex
    mtex.texture.type = 'ENVIRONMENT_MAP'
    mtex.texture.environment_map.source = 'STATIC'
    mtex.texture.environment_map.viewpoint_object = cobj
    mtex.texture.filter_size = 0.1

    cotex = bpy.context.object.active_material.texture_slots[0]
    cotex.use_map_color_diffuse = False
    cotex.use_map_mirror = True
    cotex.texture_coords = 'REFLECTION'
    cotex.mirror_factor = 0.8
    cotex.mapping = 'CUBE'

def render():
    bpy.ops.render.render()

class MakeEnvmap(bpy.types.Operator):
    lng = lang()
    bl_idname = "make.envmap"
    bl_label = mes.btn1[lng]
    bl_options = {'REGISTER'}

    my_string = bpy.props.StringProperty(name = mes.dst1[lng] ,default = 'envmat')

    def execute(self, context):
        matname = self.my_string
        
        makeenv(matname)
        render()
        
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#	Registration

def register():
    bpy.utils.register_class(MakeEnvmapPanel)
    bpy.utils.register_class(MakeEnvmap)

def unregister():
    bpy.utils.unregister_class(MakeEnvmapPanel)
    bpy.utils.unregister_class(MakeEnvmap)

if __name__ == "__main__":
    register()