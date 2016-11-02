#
#The MIT License (MIT)
#
#Copyright (c) 2014 ishidourou
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#
#(参考日本語訳：http://sourceforge.jp/projects/opensource/wiki/licenses%2FMIT_licenseより）
#
#Copyright (c) 2014 ishidourou
#
##以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）
#の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。
#これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、
#および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も
#無制限に含まれます。

#上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載
#するものとします。

#ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく
#提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害に
#ついての保証も含みますが、それに限定されるものではありません。 作者または著作権者は、
#契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいは
#ソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務に
#ついて何らの責任も負わないものとします。
#
#
#####################################
# Add Mirror Modifier(日本語版)
#       v.2.1
#  (c)isidourou 2014
####################################

#!BPY
import bpy
import random
from bpy.types import Menu, Panel

bl_info = {
    "name": "Add Mirror Modifier",
    "author": "isidourou",
    "version": (2, 1),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar",
    "description": "AddMirrorModifierJ",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'Object'}
    
#    メッセージ（英語,日本語）
class mes():
    title = ('Add Mirror Modifier','ミラーモディファイアツール')
    axis = ('axis of symmetry','対称軸')
    mmname = ('Mirror','ミラー')

def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0

def mode_interpret(emode):
    if emode == 'PAINT_TEXTURE':
        return 'TEXTURE_PAINT'
    if emode == 'SCULPT':
        return 'SCULPT'
    if emode == 'PAINT_VERTEX':
        return 'VERTEX_PAINT'
    if emode == 'PAINT_WEIGHT':
        return 'WEIGHT_PAINT'
    if emode == 'OBJECT':
        return 'OBJECT'
    if emode == 'POSE':
        return 'POSE'
    if emode=='EDIT_MESH' or emode=='EDIT_ARMATURE' or emode=='EDIT_CURVE' or emode=='EDIT_TEXT' or emode=='EDIT_METABALL' or emode=='EDIT_SURFACE':
        return 'EDIT'

class AddMmPanelj(bpy.types.Panel):

    system = bpy.context.user_preferences.system
    axis = mes.axis[lang()]

    bl_label = mes.title[lang()]
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.label(text=self.axis)
        row = col.row(align=True)
        row.operator("add.mmx", text="X")
        row.operator("add.mmy", text="Y")     
        row.operator("add.mmz", text="Z")     
        row = col.row(align=True)
        row.operator("add.mmmx", text="-X")
        row.operator("add.mmmy", text="-Y")     
        row.operator("add.mmmz", text="-Z")     

#add mirror modifier
def add_mm(direction):

    emode = bpy.context.mode
    emode = mode_interpret(emode)
    obj = bpy.ops.object
    cobj = bpy.context.object
    mesh = cobj.data
    obj.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    obj.mode_set(mode='OBJECT')
    exist = False
    
    system = bpy.context.user_preferences.system
    mmname = mes.mmname[lang()] 
    for i in cobj.modifiers:
        s = i.name
        if s.find(mmname) != -1:
            exist = True
            break

    if exist == False:
        obj.modifier_add(type='MIRROR')

    if direction == 'X':
        for vertex in mesh.vertices:
            if (vertex.co.x < -0.000001):
                vertex.select = True
                cobj.modifiers[mmname].use_x = True
                if exist == False:
                    cobj.modifiers[mmname].use_y = False
                    cobj.modifiers[mmname].use_z = False
    if direction == '-X':
        for vertex in mesh.vertices:
            if (vertex.co.x > 0.000001):
                vertex.select = True
                cobj.modifiers[mmname].use_x = True
                if exist == False:
                    cobj.modifiers[mmname].use_y = False
                    cobj.modifiers[mmname].use_z = False
    if direction == 'Y':
        for vertex in mesh.vertices:
            if (vertex.co.y < -0.000001):
                vertex.select = True
                cobj.modifiers[mmname].use_y = True
                if exist == False:
                    cobj.modifiers[mmname].use_x = False
                    cobj.modifiers[mmname].use_z = False

    if direction == '-Y':
        for vertex in mesh.vertices:
            if (vertex.co.y > 0.000001):
                vertex.select = True
                cobj.modifiers[mmname].use_y = True
                if exist == False:
                    cobj.modifiers[mmname].use_x = False
                    cobj.modifiers[mmname].use_z = False
    if direction == 'Z':
        for vertex in mesh.vertices:
            if (vertex.co.z < -0.000001):
                vertex.select = True
                cobj.modifiers[mmname].use_z = True
                if exist == False:
                    cobj.modifiers[mmname].use_x = False
                    cobj.modifiers[mmname].use_y = False
    if direction == '-Z':
        for vertex in mesh.vertices:
            if (vertex.co.z > 0.000001):
                vertex.select = True
                cobj.modifiers[mmname].use_z = True
                if exist == False:
                    cobj.modifiers[mmname].use_x = False
                    cobj.modifiers[mmname].use_y = False
    cobj.modifiers[mmname].use_clip = True
    obj.mode_set(mode='EDIT')
    bpy.ops.mesh.delete(type='VERT')
    
    bpy.ops.mesh.select_all(action='SELECT')
    obj.mode_set(mode='OBJECT')
    if emode != 'OBJECT':
        bpy.ops.object.mode_set(mode=emode)

class AddMmx(bpy.types.Operator):
    bl_idname = "add.mmx"
    bl_label = "AddMmx"
    def execute(self, context):
        if bpy.context.object.type == 'MESH':
            add_mm('X')
        return{'FINISHED'}
class AddMm_x(bpy.types.Operator):
    bl_idname = "add.mmmx"
    bl_label = "AddMmx"
    def execute(self, context):
        if bpy.context.object.type == 'MESH':
            add_mm('-X')
        return{'FINISHED'}
class AddMmy(bpy.types.Operator):
    bl_idname = "add.mmy"
    bl_label = "AddMmx"
    def execute(self, context):
        if bpy.context.object.type == 'MESH':
            add_mm('Y')
        return{'FINISHED'}
class AddMm_y(bpy.types.Operator):
    bl_idname = "add.mmmy"
    bl_label = "AddMmx"
    def execute(self, context):
        if bpy.context.object.type == 'MESH':
            add_mm('-Y')
        return{'FINISHED'}
class AddMmz(bpy.types.Operator):
    bl_idname = "add.mmz"
    bl_label = "AddMmx"
    def execute(self, context):
        if bpy.context.object.type == 'MESH':
            add_mm('Z')
        return{'FINISHED'}
class AddMm_z(bpy.types.Operator):
    bl_idname = "add.mmmz"
    bl_label = "AddMmx"
    def execute(self, context):
        if bpy.context.object.type == 'MESH':
            add_mm('-Z')
        return{'FINISHED'}

#	Registration

def register():
    bpy.utils.register_class(AddMmPanelj)
    bpy.utils.register_class(AddMmx)
    bpy.utils.register_class(AddMm_x)
    bpy.utils.register_class(AddMmy)
    bpy.utils.register_class(AddMm_y)
    bpy.utils.register_class(AddMmz)
    bpy.utils.register_class(AddMm_z)

    
def unregister():
    bpy.utils.unregister_class(AddMmPanelj)
    bpy.utils.unregister_class(AddMmx)
    bpy.utils.unregister_class(AddMm_x)
    bpy.utils.unregister_class(AddMmy)
    bpy.utils.unregister_class(AddMm_y)
    bpy.utils.unregister_class(AddMmz)
    bpy.utils.unregister_class(AddMm_z)

if __name__ == "__main__":
    register()
