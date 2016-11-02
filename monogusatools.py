####################################
# MonogusaTools
#       v.1.0
#  (c)isidourou 2013
####################################

#!BPY
import bpy
import random
from bpy.types import Menu, Panel

bl_info = {
    "name": "Monogusa Tools",
    "author": "isidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar",
    "description": "MonogusaTools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'CTNAME'}
    
atobj = None

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
    
def check_active():
    count = 0
    slist = bpy.context.selected_objects
    for i in slist:
        count += 1
    return count

def check_mode():
    emode = bpy.context.mode
    if emode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    return emode
 
#    Menu in tools region
class MonogusaToolsPanel(bpy.types.Panel):
    bl_label = "Monogusa Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        layout = self.layout
#3D Cursor
        col = layout.column(align=True)
        col.label(text="3d cursor:")
        row = col.row(align=True)
        row.operator("to.selected", text="to Selected")
        row.operator("to.cursor", text="to Cursor")
#select
        col = layout.column(align=True)
        col.label(text="Select:")
        row = col.row(align=True)
        row.operator("select.type", text="Type")
        row.operator("select.group", text="Group")
        row.operator("select.obdata", text="OBData")
        row.operator("select.mat", text="Mat")
        row = col.row(align=True)
        row.operator("select.invert", text="Invert")
        row.operator("select.all", text="  All")
        row.operator("deselect.all", text="Deselect")
#execute
        #col = layout.column(align=True)
        col.label(text="Execute:")
        row = col.row(align=True)
        row.operator("hide.selected", text="Hide")
        row.operator("unhide.all", text="Unhide")
        row.operator("execute.delete", text="Delete")
#sendlayer layer        
        col.label(text="Move to Layer:")
        row = col.row(align=True)
        row.operator("sendlayer.l00",text=' ')
        row.operator("sendlayer.l01",text=' ')
        row.operator("sendlayer.l02",text=' ')
        row.operator("sendlayer.l03",text=' ')
        row.operator("sendlayer.l04",text=' ')
        row.operator("sendlayer.l05",text=' ')
        row.operator("sendlayer.l06",text=' ')
        row.operator("sendlayer.l07",text=' ')
        row.operator("sendlayer.l08",text=' ')
        row.operator("sendlayer.l09",text=' ')
        row = col.row(align=True)
        row.operator("sendlayer.l10",text=' ')
        row.operator("sendlayer.l11",text=' ')
        row.operator("sendlayer.l12",text=' ')
        row.operator("sendlayer.l13",text=' ')
        row.operator("sendlayer.l14",text=' ')
        row.operator("sendlayer.l15",text=' ')
        row.operator("sendlayer.l16",text=' ')
        row.operator("sendlayer.l17",text=' ')
        row.operator("sendlayer.l18",text=' ')
        row.operator("sendlayer.l19",text=' ')
#convert
        col = layout.column(align=True)
        col.label(text="Convert:")
        row = col.row(align=True)
        row.operator("convert.tomesh", text="to Mesh")
        row.operator("convert.tocurve", text="to Curve")
#subdivide
        col = layout.column(align=True)
        col.label(text="Sub Divide:")
        row = col.row(align=True)
        row.operator("div.simple", text="Simple Divide")
        row = col.row(align=True)
        row.operator("div.smooth", text="Smooth Div")
        row.operator("div.rand", text="Random Div")
        row = col.row(align=False)
        row.operator("ver.smooth", text="Smoothing  Vertex / Points")      
 #add mirror modifire
        col = layout.column(align=True)
        col = layout.column(align=True)
        col.label(text="Add Mirror Modifier:")
        row = col.row(align=True)
        row.operator("add.mmx", text="X")
        row.operator("add.mmy", text="Y")     
        row.operator("add.mmz", text="Z")     
        row = col.row(align=True)
        row.operator("add.mmmx", text="-X")
        row.operator("add.mmmy", text="-Y")     
        row.operator("add.mmmz", text="-Z")     
 #add mirror modifire
        col = layout.column(align=True)
        col.label(text="Set Template Empty:")
        row = col.row(align=True)
        row.operator("temp.single", text="Single")
        row.operator("temp.separate", text="3D Separate")     
        row.operator("temp.contact", text="3D Contact")     
#---- main ------

#select
class SelectType(bpy.types.Operator):
    bl_idname = "select.type"
    bl_label = "SelectType"
    def execute(self, context):
        check_mode()
        if check_active() == 0:
            return{'FINISHED'}
        bpy.ops.object.select_grouped(type='TYPE')
        return{'FINISHED'}

class SelectGroup(bpy.types.Operator):
    bl_idname = "select.group"
    bl_label = "SelectGroup"
    def execute(self, context):
        check_mode()
        if check_active() == 0:
            return{'FINISHED'}
        bpy.ops.object.select_grouped(type='GROUP')
        return{'FINISHED'}

class SelectObjdata(bpy.types.Operator):
    bl_idname = "select.obdata"
    bl_label = "SelectObjdata"
    def execute(self, context):
        check_mode()
        if check_active() == 0:
            return{'FINISHED'}
        bpy.ops.object.select_linked(type='OBDATA')
        return{'FINISHED'}

class SelectMat(bpy.types.Operator):
    bl_idname = "select.mat"
    bl_label = "SelectMat"
    def execute(self, context):
        check_mode()
        if check_active() == 0:
            return{'FINISHED'}
        bpy.ops.object.select_linked(type='MATERIAL')
        return{'FINISHED'}

class SelectInvert(bpy.types.Operator):
    bl_idname = "select.invert"
    bl_label = "SelectInvert"
    def execute(self, context):
        cobj = bpy.context.object
        if cobj == None:
            return{'FINISHED'}
        objtype = cobj.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if objtype == 'MESH':
            if emode == 'EDIT':
                bpy.ops.mesh.select_all(action='INVERT')
        if objtype == 'CURVE' or objtype == 'SURFACE':
            if emode == 'EDIT':
                bpy.ops.curve.select_all(action='INVERT')
        if objtype == 'ARMATURE':
            if emode == 'POSE':
                bpy.ops.pose.select_all(action='INVERT')
            if emode == 'EDIT':
                bpy.ops.armature.select_all(action='INVERT')
        if objtype == 'META':
            if emode == 'EDIT':
                bpy.ops.mball.select_all(action='INVERT')
        if emode == 'OBJECT':
            bpy.ops.object.select_all(action='INVERT')
        return{'FINISHED'}

class SelectAll(bpy.types.Operator):
    bl_idname = "select.all"
    bl_label = "SelectAll"
    def execute(self, context):
        cobj = bpy.context.object
        if cobj == None:
            return{'FINISHED'}
        objtype = cobj.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if objtype == 'MESH':
            if emode == 'EDIT':
                bpy.ops.mesh.select_all(action='SELECT')
        if objtype == 'CURVE' or objtype == 'SURFACE':
            if emode == 'EDIT':
                bpy.ops.curve.select_all(action='SELECT')
        if objtype == 'ARMATURE':
            if emode == 'POSE':
                bpy.ops.pose.select_all(action='SELECT')
            if emode == 'EDIT':
                bpy.ops.armature.select_all(action='SELECT')
        if objtype == 'META':
            if emode == 'EDIT':
                bpy.ops.mball.select_all(action='SELECT')
        if emode == 'OBJECT':
            bpy.ops.object.select_all(action='SELECT')
        return{'FINISHED'}

class DeselectAll(bpy.types.Operator):
    bl_idname = "deselect.all"
    bl_label = "DeselectAll"
    def execute(self, context):
        cobj = bpy.context.object
        if cobj == None:
            return{'FINISHED'}
        objtype = cobj.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if objtype == 'MESH':
            if emode == 'EDIT':
                bpy.ops.mesh.select_all(action='DESELECT')
        if objtype == 'CURVE' or objtype == 'SURFACE':
            if emode == 'EDIT':
                bpy.ops.curve.select_all(action='DESELECT')
        if objtype == 'ARMATURE':
            if emode == 'POSE':
                bpy.ops.pose.select_all(action='DESELECT')
            if emode == 'EDIT':
                bpy.ops.armature.select_all(action='DESELECT')
        if objtype == 'META':
            if emode == 'EDIT':
                bpy.ops.mball.select_all(action='DESELECT')
        if emode == 'OBJECT':
            bpy.ops.object.select_all(action='DESELECT')
        return{'FINISHED'}

#execute
class HideSelected(bpy.types.Operator):
    bl_idname = "hide.selected"
    bl_label = "HideSelected"
    def execute(self, context):
        global atobj
        cobj = bpy.context.object
        if cobj == None:
            return{'FINISHED'}
        objtype = cobj.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if objtype == 'MESH':
            if emode == 'EDIT':
                bpy.ops.mesh.hide(unselected=False)
        if objtype == 'CURVE' or objtype == 'SURFACE':
            if emode == 'EDIT':
                bpy.ops.curve.hide(unselected=False)
        if objtype == 'ARMATURE':
            if emode == 'POSE':
                bpy.ops.pose.hide(unselected=False)
            if emode == 'EDIT':
                bpy.ops.armature.hide(unselected=False)
        if objtype == 'META':
            if emode == 'EDIT':
                bpy.ops.mball.hide_metaelems(unselected=False)
        if emode == 'OBJECT':
            bpy.ops.object.hide_view_set(unselected=False)
        atobj = cobj
        return{'FINISHED'}
class UnhideAll(bpy.types.Operator):
    bl_idname = "unhide.all"
    bl_label = "UnhideAll"
    def execute(self, context):
        global atobj
        cobj = bpy.context.object
        if cobj == None:
                bpy.context.scene.objects.active = atobj
                obj=bpy.context.object
                obj.select = True

        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if emode == 'OBJECT':
            #bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.hide_view_clear()
            return{'FINISHED'}
        objtype = bpy.context.object.type
        if objtype == 'MESH':
            if emode == 'EDIT':
                bpy.ops.mesh.reveal()
        if objtype == 'CURVE' or objtype == 'SURFACE':
            if emode == 'EDIT':
                bpy.ops.curve.reveal()
        if objtype == 'ARMATURE':
            if emode == 'POSE':
                bpy.ops.pose.reveal()
            if emode == 'EDIT':
                bpy.ops.armature.reveal()
        if objtype == 'META':
            if emode == 'EDIT':
                bpy.ops.mball.reveal_metaelems()
        return{'FINISHED'}
class ExecuteDelete(bpy.types.Operator):
    bl_idname = "execute.delete"
    bl_label = "ExecuteDelete"
    def execute(self, context):
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if emode == 'OBJECT':
            bpy.ops.object.delete(use_global=False)
            return{'FINISHED'}
        objtype = bpy.context.object.type
        if objtype == 'MESH':
            if emode == 'EDIT':
                bpy.ops.mesh.delete()
        if objtype == 'CURVE' or objtype == 'SURFACE':
            if emode == 'EDIT':
                bpy.ops.curve.delete()
        if objtype == 'ARMATURE':
            if emode == 'POSE':
                bpy.ops.object.editmode_toggle()
                bpy.ops.armature.delete()
                bpy.ops.object.posemode_toggle()
            if emode == 'EDIT':
                bpy.ops.armature.delete()
        if objtype == 'META':
            if emode == 'EDIT':
                bpy.ops.mball.delete_metaelems()
        return{'FINISHED'}

#move to Layer
class Send00(bpy.types.Operator):
    bl_idname = "sendlayer.l00"
    bl_label = "Send00"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(True,False,False,False,False,False,False,False,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send01(bpy.types.Operator):
    bl_idname = "sendlayer.l01"
    bl_label = "Send01"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,True,False,False,False,False,False,False,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send02(bpy.types.Operator):
    bl_idname = "sendlayer.l02"
    bl_label = "Send02"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,True,False,False,False,False,False,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send03(bpy.types.Operator):
    bl_idname = "sendlayer.l03"
    bl_label = "Send03"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,True,False,False,False,False,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send04(bpy.types.Operator):
    bl_idname = "sendlayer.l04"
    bl_label = "Send04"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,True,False,False,False,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send05(bpy.types.Operator):
    bl_idname = "sendlayer.l05"
    bl_label = "Send05"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,True,False,False,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send06(bpy.types.Operator):
    bl_idname = "sendlayer.l06"
    bl_label = "Send06"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,True,False,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send07(bpy.types.Operator):
    bl_idname = "sendlayer.l07"
    bl_label = "Send07"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,True,False,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send08(bpy.types.Operator):
    bl_idname = "sendlayer.l08"
    bl_label = "Send08"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,True,False,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send09(bpy.types.Operator):
    bl_idname = "sendlayer.l09"
    bl_label = "Send09"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,True,
                False,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send10(bpy.types.Operator):
    bl_idname = "sendlayer.l10"
    bl_label = "Send10"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                True,False,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send11(bpy.types.Operator):
    bl_idname = "sendlayer.l11"
    bl_label = "Send11"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,True,False,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send12(bpy.types.Operator):
    bl_idname = "sendlayer.l12"
    bl_label = "Send12"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,True,False,False,False,False,False,False,False))
        return{'FINISHED'}
class Send13(bpy.types.Operator):
    bl_idname = "sendlayer.l13"
    bl_label = "Send13"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,False,True,False,False,False,False,False,False))
        return{'FINISHED'}
class Send14(bpy.types.Operator):
    bl_idname = "sendlayer.l14"
    bl_label = "Send14"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,False,False,True,False,False,False,False,False))
        return{'FINISHED'}
class Send15(bpy.types.Operator):
    bl_idname = "sendlayer.l15"
    bl_label = "Send15"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,False,False,False,True,False,False,False,False))
        return{'FINISHED'}
class Send16(bpy.types.Operator):
    bl_idname = "sendlayer.l16"
    bl_label = "Send16"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,False,False,False,False,True,False,False,False))
        return{'FINISHED'}
class Send17(bpy.types.Operator):
    bl_idname = "sendlayer.l17"
    bl_label = "Send17"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,False,False,False,False,False,True,False,False))
        return{'FINISHED'}
class Send18(bpy.types.Operator):
    bl_idname = "sendlayer.l18"
    bl_label = "Send18"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,False,False,False,False,False,False,True,False))
        return{'FINISHED'}
class Send19(bpy.types.Operator):
    bl_idname = "sendlayer.l19"
    bl_label = "Send19"
    def execute(self, context):
        check_mode()
        bpy.ops.object.move_to_layer(
        layers=(False,False,False,False,False,False,False,False,False,False,
                False,False,False,False,False,False,False,False,False,True))
        return{'FINISHED'}

#3D cursor
class ToSelected(bpy.types.Operator):
    bl_idname = "to.selected"
    bl_label = "ToSelected"
    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        return{'FINISHED'}
class ToCursor(bpy.types.Operator):
    bl_idname = "to.cursor"
    bl_label = "ToCursor"
    def execute(self, context):
        bpy.ops.view3d.snap_selected_to_cursor()
        return{'FINISHED'}

#subdivide
class DivSimple(bpy.types.Operator):
    bl_idname = "div.simple"
    bl_label = "DivSimple"
    def execute(self, context):
        objtype = bpy.context.object.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if objtype == 'MESH':
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.subdivide(smoothness=0)
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode=emode)
        if objtype == 'ARMATURE':
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.armature.subdivide()
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode=emode)
        if objtype == 'CURVE':
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.curve.subdivide()
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode=emode)

        return{'FINISHED'}
class DivSmooth(bpy.types.Operator):
    bl_idname = "div.smooth"
    bl_label = "DivSmooth"
    def execute(self, context):
        objtype = bpy.context.object.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if bpy.context.object.type == 'MESH':
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.subdivide(smoothness=1)
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode=emode)
        return{'FINISHED'}
class DivRand(bpy.types.Operator):
    bl_idname = "div.rand"
    bl_label = "DivRand"
    def execute(self, context):
        objtype = bpy.context.object.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if bpy.context.object.type == 'MESH':
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            frc = random.random()*6
            sed = int(random.random()*10)
            bpy.ops.mesh.subdivide(smoothness=0, fractal=frc, seed=sed)
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode=emode)
        return{'FINISHED'}
class VerSmooth(bpy.types.Operator):
    bl_idname = "ver.smooth"
    bl_label = "DivSmooth"
    def execute(self, context):
        objtype = bpy.context.object.type
        emode = bpy.context.mode
        emode = mode_interpret(emode)
        if bpy.context.object.type == 'MESH':
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.vertices_smooth()
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode=emode)
        if objtype == 'CURVE':
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.curve.smooth()
            if emode != 'EDIT':
                bpy.ops.object.mode_set(mode=emode)
        return{'FINISHED'}

#convert
class ConverttoMesh(bpy.types.Operator):
    bl_idname = "convert.tomesh"
    bl_label = "ConverttoMesh"
    def execute(self, context):
        objtype = bpy.context.object.type
        emode = bpy.context.mode
        if emode == 'SCULPT' or emode.find('PAINT') != -1:
            return{'FINISHED'}            
        emode = mode_interpret(emode)
        if objtype == 'CURVE' or objtype == 'FONT' or objtype == 'META' or objtype == 'SURFACE':
            if emode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.convert(target='MESH')
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.object.editmode_toggle()
            if emode != 'OBJECT':
                bpy.ops.object.mode_set(mode=emode)
        return{'FINISHED'}
class ConverttoCurve(bpy.types.Operator):
    bl_idname = "convert.tocurve"
    bl_label = "ConverttoCurve"
    def execute(self, context):
        objtype = bpy.context.object.type
        emode = bpy.context.mode
        if emode == 'SCULPT' or emode.find('PAINT') != -1:
            return{'FINISHED'}            
        emode = mode_interpret(emode)
        if objtype == 'MESH' or objtype == 'FONT':
            if emode != 'OBJECT':
                bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.convert(target='CURVE')
            if emode != 'OBJECT':
                bpy.ops.object.mode_set(mode=emode)
        return{'FINISHED'}
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
    ct = 0
    exist = False
    for i in cobj.modifiers:
        s = cobj.modifiers[ct].name
        if s.find('Mirror') != -1:
            exist = True
            break
    if exist == False:
        obj.modifier_add(type='MIRROR')

    if direction == 'X':
        for vertex in mesh.vertices:
            if (vertex.co.x < -0.000001):
                vertex.select = True
                cobj.modifiers["Mirror"].use_x = True
                if exist == False:
                    cobj.modifiers["Mirror"].use_y = False
                    cobj.modifiers["Mirror"].use_z = False
    if direction == '-X':
        for vertex in mesh.vertices:
            if (vertex.co.x > 0.000001):
                vertex.select = True
                cobj.modifiers["Mirror"].use_x = True
                if exist == False:
                    cobj.modifiers["Mirror"].use_y = False
                    cobj.modifiers["Mirror"].use_z = False
    if direction == 'Y':
        for vertex in mesh.vertices:
            if (vertex.co.y < -0.000001):
                vertex.select = True
                cobj.modifiers["Mirror"].use_y = True
                if exist == False:
                    cobj.modifiers["Mirror"].use_x = False
                    cobj.modifiers["Mirror"].use_z = False

    if direction == '-Y':
        for vertex in mesh.vertices:
            if (vertex.co.y > 0.000001):
                vertex.select = True
                cobj.modifiers["Mirror"].use_y = True
                if exist == False:
                    cobj.modifiers["Mirror"].use_x = False
                    cobj.modifiers["Mirror"].use_z = False
    if direction == 'Z':
        for vertex in mesh.vertices:
            if (vertex.co.z < -0.000001):
                vertex.select = True
                cobj.modifiers["Mirror"].use_z = True
                if exist == False:
                    cobj.modifiers["Mirror"].use_x = False
                    cobj.modifiers["Mirror"].use_y = False
    if direction == '-Z':
        for vertex in mesh.vertices:
            if (vertex.co.z > 0.000001):
                vertex.select = True
                cobj.modifiers["Mirror"].use_z = True
                if exist == False:
                    cobj.modifiers["Mirror"].use_x = False
                    cobj.modifiers["Mirror"].use_y = False
    cobj.modifiers["Mirror"].use_clip = True
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

#set template empty
def objselect(objct,selection):
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True
def makecenterempty():
    bpy.ops.object.empty_add(type='PLAIN_AXES', 
                        view_align=False, 
                        location=(0, 0, 0))
    centerempty = bpy.context.object
    centerempty.name = 'CenterEmpty'
    return centerempty
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
        #sn = bpy.context.scene
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
        #sn = bpy.context.scene
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
        #sn = bpy.context.scene
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
    bpy.utils.register_class(MonogusaToolsPanel)
    #select
    bpy.utils.register_class(SelectType)
    bpy.utils.register_class(SelectGroup)
    bpy.utils.register_class(SelectObjdata)
    bpy.utils.register_class(SelectMat)
    bpy.utils.register_class(SelectInvert)
    bpy.utils.register_class(SelectAll)
    bpy.utils.register_class(DeselectAll)
    #execute
    bpy.utils.register_class(HideSelected)
    bpy.utils.register_class(UnhideAll)
    bpy.utils.register_class(ExecuteDelete)
    #move to layer
    bpy.utils.register_class(Send00)
    bpy.utils.register_class(Send01)
    bpy.utils.register_class(Send02)
    bpy.utils.register_class(Send03)
    bpy.utils.register_class(Send04)
    bpy.utils.register_class(Send05)
    bpy.utils.register_class(Send06)
    bpy.utils.register_class(Send07)
    bpy.utils.register_class(Send08)
    bpy.utils.register_class(Send09)
    bpy.utils.register_class(Send10)
    bpy.utils.register_class(Send11)
    bpy.utils.register_class(Send12)
    bpy.utils.register_class(Send13)
    bpy.utils.register_class(Send14)
    bpy.utils.register_class(Send15)
    bpy.utils.register_class(Send16)
    bpy.utils.register_class(Send17)
    bpy.utils.register_class(Send18)
    bpy.utils.register_class(Send19)
   #3d cursor
    bpy.utils.register_class(ToSelected)
    bpy.utils.register_class(ToCursor)
   #subdvide
    bpy.utils.register_class(DivSimple)
    bpy.utils.register_class(DivSmooth)
    bpy.utils.register_class(DivRand)
    bpy.utils.register_class(VerSmooth)
    bpy.utils.register_class(ConverttoMesh)
    bpy.utils.register_class(ConverttoCurve)
    bpy.utils.register_class(AddMmx)
    bpy.utils.register_class(AddMm_x)
    bpy.utils.register_class(AddMmy)
    bpy.utils.register_class(AddMm_y)
    bpy.utils.register_class(AddMmz)
    bpy.utils.register_class(AddMm_z)
   #set template empty
    bpy.utils.register_class(TempSingle)
    bpy.utils.register_class(TempSeparate)
    bpy.utils.register_class(TempContact)
    
def unregister():
    bpy.utils.unregister_class(MonogusaToolsPanel)
    #select
    bpy.utils.unregister_class(SelectType)
    bpy.utils.unregister_class(SelectGroup)
    bpy.utils.unregister_class(SelectObjdata)
    bpy.utils.unregister_class(SelectMat)
    bpy.utils.unregister_class(SelectInvert)
    bpy.utils.unregister_class(SelectAll)
    bpy.utils.unregister_class(DeselectAll)
    #execute
    bpy.utils.unregister_class(HideSelected)
    bpy.utils.unregister_class(UnhideAll)
    bpy.utils.unregister_class(ExecuteDelete)
    #move to layer
    bpy.utils.unregister_class(Send00)
    bpy.utils.unregister_class(Send01)
    bpy.utils.unregister_class(Send02)
    bpy.utils.unregister_class(Send03)
    bpy.utils.unregister_class(Send04)
    bpy.utils.unregister_class(Send05)
    bpy.utils.unregister_class(Send06)
    bpy.utils.unregister_class(Send07)
    bpy.utils.unregister_class(Send08)
    bpy.utils.unregister_class(Send09)
    bpy.utils.unregister_class(Send10)
    bpy.utils.unregister_class(Send11)
    bpy.utils.unregister_class(Send12)
    bpy.utils.unregister_class(Send13)
    bpy.utils.unregister_class(Send14)
    bpy.utils.unregister_class(Send15)
    bpy.utils.unregister_class(Send16)
    bpy.utils.unregister_class(Send17)
    bpy.utils.unregister_class(Send18)
    bpy.utils.unregister_class(Send19)
    #3d cursor
    bpy.utils.unregister_class(ToSelected)
    bpy.utils.unregister_class(ToCursor)
   #subdvide
    bpy.utils.unregister_class(DivSimple)
    bpy.utils.unregister_class(DivSmooth)
    bpy.utils.unregister_class(DivRand)
    bpy.utils.unregister_class(VerSmooth)
    bpy.utils.unregister_class(ConverttoMesh)
    bpy.utils.unregister_class(ConverttoCurve)
    bpy.utils.unregister_class(AddMmx)
    bpy.utils.unregister_class(AddMm_x)
    bpy.utils.unregister_class(AddMmy)
    bpy.utils.unregister_class(AddMm_y)
    bpy.utils.unregister_class(AddMmz)
    bpy.utils.unregister_class(AddMm_z)
   #set template empty
    bpy.utils.unregister_class(TempSingle)
    bpy.utils.unregister_class(TempSeparate)
    bpy.utils.unregister_class(TempContact)

if __name__ == "__main__":
    register()