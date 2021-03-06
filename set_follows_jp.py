﻿#﻿
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

####################################
# SetFollows 日本語版
#       v.1.0j
#  (c)ishidourou 2014
####################################

#ブログ　http://stonefield.cocolog-nifty.com/higurashi/2014/01/blenderaddonset.html
#使い方　https://www.youtube.com/watch?v=33WXDDXXBnc#t=1


#!BPY
import bpy
import random
from bpy.props import *

bl_info = {
    "name": "SetFollows_JP",
    "author": "ishidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar",
    "description": "SetFollows_JP",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'Animation'}
  
#    Menu in tools region
class SetFollowsPanel(bpy.types.Panel):
    bl_label = "追従パス設定ツール"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        self.layout.operator("set.follows")
        self.layout.operator("trans.follows")

def objselect(objct,selection):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True
    
def meshseparate(obj):
    if obj.type != 'MESH':
        return
    objselect(obj,'ADD')
    msh = bpy.ops.mesh
    bpy.ops.object.mode_set(mode = 'EDIT')
    msh.select_all(action='SELECT')
    msh.separate(type = 'LOOSE')
    bpy.ops.object.mode_set(mode = 'OBJECT')

def editcurve(obj,pttype,pframe,frandom,rev,ow):
    crv = bpy.ops.curve
    if ow == False:
        pframe = bpy.context.object.data.path_duration
    pframe = int(pframe - pframe*frandom*random.random())
    if pframe < 1:
        pframe = 1    
    bpy.context.object.data.path_duration = pframe

    bpy.ops.object.mode_set(mode = 'EDIT')
    #crv.spline_type_set(type = 'BEZIER')
    crv.select_all(action='SELECT')
    if pttype != 'KEEP':
        if pttype == 'AUTO':
            crv.handle_type_set()
        else:
            crv.handle_type_set(type=pttype)
    if rev == True:
        crv.switch_direction()
    bpy.ops.object.mode_set(mode = 'OBJECT')
        
def setcurve(obj,aobj):
    global wmessage
    if obj.type != 'MESH' and obj.type != 'CURVE':
        print('can not set curve')
        wmessage = "Prease Select Mesh or Curve Objects."
        bpy.ops.error.dialog('INVOKE_DEFAULT')
        return

    crv = bpy.ops.curve

    obj.name = 'Curve'

    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    if obj.type == 'MESH':
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.delete(type='ONLY_FACE')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.convert(target='CURVE')
        bpy.ops.object.mode_set(mode = 'EDIT')
        crv.spline_type_set(type = 'BEZIER')
        crv.select_all(action='SELECT')

    cyclic = 0
    for s in obj.data.splines:
        if s.use_cyclic_u == True:
            cyclic = 1
            break

    bpy.ops.object.mode_set(mode = 'EDIT')
    if cyclic == 1:
        bpy.ops.curve.cyclic_toggle(direction='CYCLIC_U')

    crv.select_all(action='DESELECT')
    
    obj.data.splines[0].bezier_points[0].select_control_point = True
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.mode_set(mode = 'OBJECT')

    objselect(aobj,'ONLY')
    bpy.ops.object.duplicate_move_linked()
    cobj = bpy.context.object
    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
    cobj.constraints["Follow Path"].target = bpy.data.objects[obj.name]
    bpy.ops.constraint.followpath_path_animate(constraint="Follow Path", owner='OBJECT', frame_start=1, length=100)
    bpy.ops.view3d.snap_selected_to_cursor()
    cobj.constraints["Follow Path"].use_curve_follow = True
    cobj.constraints["Follow Path"].forward_axis = 'TRACK_NEGATIVE_Y'

    objselect(obj,'ONLY')
    bpy.ops.object.mode_set(mode = 'EDIT')
    if cyclic == 1:
        bpy.ops.curve.cyclic_toggle(direction='CYCLIC_U')
    bpy.ops.object.mode_set(mode = 'OBJECT')

wmessage = 'パス用と追従するオブジェクトを選択してください'

class ErrorDialog(bpy.types.Operator):
    bl_idname = "error.dialog"
    bl_label = "Warning:"
    bl_options = {'REGISTER'}
        
    my_message = StringProperty(name="message",default='パス用と追従するオブジェクトを選択してください')    

    def execute(self, context):
        message = self.my_message
        print(message)
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        global wmessage
        self.layout.label(wmessage)

def error(message):
    global wmessage
    wmessage = message
    bpy.ops.error.dialog('INVOKE_DEFAULT')
  
  #---- main ------

class SetFollows(bpy.types.Operator):

    bl_idname = "set.follows"
    bl_label = "追従パスを設定"
    bl_options = {'REGISTER'}

    def execute(self, context):

        global wmessage
        
        aobj = bpy.context.active_object
 
        bpy.context.area.type = 'VIEW_3D'
        slist = bpy.context.selected_objects

        ct = 0
        for i in slist:
            if i != aobj and i.type != 'MESH' and i.type != 'CURVE':
                error("メッシュまたはカーブオブジェクトを選択してください")
                return{'FINISHED'}
            ct += 1
        if ct < 2:
            error("パス用と追従するオブジェクトを選択してください")
            return{'FINISHED'}
  
        for i in slist:
            if i != aobj:
                meshseparate(i)
           
        nslist = bpy.context.selected_objects
             
        for i in nslist:
            objselect(i,'ONLY')
            if i != aobj:
                setcurve(i,aobj)
                
        return{'FINISHED'}

class TransFollows(bpy.types.Operator):

    bl_idname = "trans.follows"
    bl_label = "追従パスを編集"
    bl_options = {'REGISTER'}

    my_pttype = EnumProperty(name="ハンドルタイプ",
        items = [('AUTO','Automatic','0'),
                 ('VECTOR','Vector','1'),
                 ('KEEP','変更しない','2')],
                 #('ALIGNED','Aligned','2'),
                 #('FREE_ALIGN','Free','3')],
                 default = 'KEEP')
    my_rev = BoolProperty(name="向きを反転",default = False)
    my_pframe = bpy.props.IntProperty(name="パスフレーム（速度）",min= 0,default = 0)
    my_frandom = bpy.props.FloatProperty(name="速度のランダム率",min=0,max=1,default = 0)

    def execute(self, context):
        pttype = self.my_pttype
        pframe = self.my_pframe
        frandom = self.my_frandom
        rev = self.my_rev
               
        cvlist = []
        #global wmessage

        if pframe == 0:
            ow = False
            pframe = 1
        else:
            ow = True
        
        aobj = bpy.context.active_object
 
        bpy.context.area.type = 'VIEW_3D'
        slist = bpy.context.selected_objects

        ct = 0
        for i in slist:
            if i.type == 'CURVE':
                cvlist.append(i)
                ct += 1
        if ct == 0:
            error("カーブオブジェクトを選択してください")
            return{'FINISHED'}

        for i in cvlist:
            objselect(i,'ADD')
            editcurve(i,pttype,pframe,frandom,rev,ow)
                
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#	Registration

def register():
    bpy.utils.register_class(SetFollowsPanel)
    bpy.utils.register_class(SetFollows)
    bpy.utils.register_class(TransFollows)
    bpy.utils.register_class(ErrorDialog)

def unregister():
    bpy.utils.unregister_class(SetFollowsPanel)
    bpy.utils.unregister_class(SetFollows)
    bpy.utils.unregister_class(TransFollows)
    bpy.utils.unregister_class(ErrorDialog)

if __name__ == "__main__":
    register()