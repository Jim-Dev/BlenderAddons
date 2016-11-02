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

#####################################
# Set Template Empty EJ(日英版)
#       v.1.0
#  (c)isidourou 2014
####################################

#!BPY
import bpy
from bpy.types import Menu, Panel

bl_info = {
    "name": "Set Template Empty EJ",
    "author": "isidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar",
    "description": "SetTemplateEmpty",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "", 
    "about_this":  "http://stonefield.cocolog-nifty.com",
    "category": '3D View'}
  
def objselect(objct,selection):
    if objct == None:
        return
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True

title = "Set Template Empty"
button1 = "Single"
button2 = "3D Separate"
button3 = "3D Contact"
admm = "add Mirror Modifier"


def lang():

    global title,button1,button2,button3,admm
    
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            title = "テンプレートツール"
            button1 = "一面図 単独"
            button2 = "三面図 分離タイプ"
            button3 = "三面図 密集タイプ"
            admm = "ミラーモディファイアを付加"
    
#    Menu in tools region
class SetTemplatePanelj(bpy.types.Panel):

    global title,button1,button2,button3,admm
    lang()
    bl_label = title
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        global title,button1,button2,button3,admm
        obj = context.object

        layout = self.layout
        col = layout.column(align=False)
        row = col.row(align=True)
        row.operator("temp.single", text=button1)
        row = col.row(align=True)
        row.operator("temp.separate", text=button2)     
        row = col.row(align=True)
        row.operator("temp.contact", text=button3)     
        row = layout.row()
        row.prop(obj, "adMm", text=admm)

#---- main ------

def makecenterempty():
    obj = bpy.ops.object
    addmm = bpy.context.object.adMm
    bpy.ops.mesh.primitive_circle_add(vertices=8,location=(0, 0, 0))
    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=5.05447)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    cobj = bpy.context.object
    if addmm:
        mesh = cobj.data
        obj.modifier_add(type='MIRROR')
        #bpy.context.object.modifiers[0].use_clip = True
        obj.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        obj.mode_set(mode='OBJECT')

        for vertex in mesh.vertices:
            if (vertex.co.x < -0.000001):
                vertex.select = True

        obj.mode_set(mode='EDIT')
        bpy.ops.mesh.delete(type='VERT')
        obj.mode_set(mode='OBJECT')
 
    return cobj

def makeempty(loc,rot):
    bpy.ops.object.empty_add(type='PLAIN_AXES',
                        view_align=False,
                        location= loc,
                        rotation= rot
                        )
    empty = bpy.context.object
    empty.empty_draw_type = 'IMAGE'
    empty.empty_draw_size = 10
    empty.name = 'Template Empty'
    empty.color[3] = 0.3   #Transparency
    empty.show_x_ray = True
    return empty

class TempSingle(bpy.types.Operator):
    bl_idname = "temp.single"
    bl_label = "TempSingle"
    def execute(self, context):
        pi = 3.141595
        pq = pi/2
        erot = [(pq, 0, 0),(pq, 0, pq),(0, 0, 0)]
        eloc = [(-5, 0, -5),(0, -5, -5),(-5, -5, 0)]
        cempty = makecenterempty()
        bpy.ops.group.create(name="TemplateEmpty")
        empty = makeempty(eloc[0],erot[0])
        bpy.ops.object.group_link(group='TemplateEmpty')
        objselect(cempty,'ADD')
        bpy.ops.object.parent_set(type='OBJECT')
        objselect(cempty,'ONLY')
        bpy.ops.view3d.snap_selected_to_cursor()
        return{'FINISHED'}

class TempSeparate(bpy.types.Operator):
    bl_idname = "temp.separate"
    bl_label = "TempSeparate"
    def execute(self, context):
        pi = 3.141595
        pq = pi/2
        erot = [(pq, 0, 0),(pq, 0, pq),(0, 0, 0)]
        eloc = [(-5, 5, -5),(-5, -5, -5),(-5, -5, -5)]

        cempty = makecenterempty()
        bpy.ops.group.create(name="TemplateEmpty")
        for i in range(3):
            empty = makeempty(eloc[i],erot[i])
            bpy.ops.object.group_link(group='TemplateEmpty')
            objselect(cempty,'ADD')
            bpy.ops.object.parent_set(type='OBJECT')
        objselect(cempty,'ONLY')
        bpy.ops.view3d.snap_selected_to_cursor()
        return{'FINISHED'}
class TempContact(bpy.types.Operator):
    bl_idname = "temp.contact"
    bl_label = "TempContact"
    def execute(self, context):
        pi = 3.141595
        pq = pi/2
        erot = [(pq, 0, 0),(pq, 0, pq),(0, 0, 0)]
        eloc = [(-5, 0, -5),(0, -5, -5),(-5, -5, 0)]
        cempty = makecenterempty()
        bpy.ops.group.create(name="TemplateEmpty")
        for i in range(3):
            empty = makeempty(eloc[i],erot[i])
            bpy.ops.object.group_link(group='TemplateEmpty')
            objselect(cempty,'ADD')
            bpy.ops.object.parent_set(type='OBJECT')
        objselect(cempty,'ONLY')
        bpy.ops.view3d.snap_selected_to_cursor()
        return{'FINISHED'}
            
#	Registration

def register():
    bpy.types.Object.adMm = bpy.props.BoolProperty()
    
    bpy.utils.register_class(SetTemplatePanelj)
    bpy.utils.register_class(TempSingle)
    bpy.utils.register_class(TempSeparate)
    bpy.utils.register_class(TempContact)
    
def unregister():
    bpy.utils.unregister_class(SetTemplatePanelj)
    bpy.utils.unregister_class(TempSingle)
    bpy.utils.unregister_class(TempSeparate)
    bpy.utils.unregister_class(TempContact)

if __name__ == "__main__":
    register()