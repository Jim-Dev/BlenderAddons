###################################
# Bones Fixer
#       v.1.0
#  (c)Ishidourou 2013
###################################

#!BPY

bl_info = {
    "name": "Bones Fixer",
    "author": "ishidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar and View3D",
    "description": "Bones Fixer",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'Rigging'}

import bpy
from bpy.props import *

obj = bpy.ops.object
scale = 2
join = True
fixmode = 'PARENT'
#fixmode = 'COPYTRANS'
groupname = 'BoneGroup'
direction = 'Z'


#    Menu in tools region
class BonesFixerPanel(bpy.types.Panel):
    bl_label = "Bones Fixer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        self.layout.operator("bones.fixer")
        
def objselect(objct,selection):
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    if (selection != 'POSE'):
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.scene.objects.active = objct
    objct.select = True
    
def select_check():

    keyword = 'testtesttestjohoooahg'
    checkname = keyword
    for i in bpy.context.selected_objects:
        checkname = i.name
    if checkname == keyword:
        print('Please select some Object.')
        return False
    return True

def add_ctbone(fixmode,join,scale,direction):

    if select_check() == False:
        return {'ERROR'}
    
    ct = 0
    for i in bpy.context.selected_objects:
        lc = i.location
        rc = i.rotation_euler
        obj.armature_add(location=(lc.x,lc.y,lc.z),rotation=(rc.x,rc.y,rc.z))

        if direction == 'X':
            bpy.ops.transform.rotate(value=-1.5708, axis=(0, 0, 1))
        if direction == 'Z':
            bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0))
        if direction == '-X':
            bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1))
        if direction == '-Y':
            bpy.ops.transform.rotate(value=1.5708*2, axis=(0, 0, 1))
        if direction == '-Z':
            bpy.ops.transform.rotate(value=-1.5708, axis=(1, 0, 0))

        if ct == 0:    
            bpy.ops.group.create(name=groupname)
        bpy.ops.object.group_link(group=groupname)

        armtr = bpy.context.object
        armtr.show_x_ray = True

        obj.mode_set(mode='EDIT')
        bpy.context.object.data.edit_bones[0].tail = (0, scale*i.scale.x, 0)
        bpy.ops.armature.select_all(action='SELECT')
        obj.mode_set(mode='OBJECT')
       
        if fixmode == 'COPYTRANS':
            bpy.ops.object.posemode_toggle()
            bpy.ops.pose.select_all(action='SELECT')
            bpy.ops.pose.constraint_add(type='COPY_TRANSFORMS')
            bpy.context.object.pose.bones["Bone"].constraints["Copy Transforms"].target = bpy.data.objects[i.name]
            bpy.ops.object.posemode_toggle()

        if fixmode == 'PARENT':
            objselect(i, 'ONLY')
            objselect(armtr, 'ADD')            
            bpy.ops.object.parent_set(type='BONE', xmirror=False, keep_transform=False)
        ct += 1
        
    objselect(armtr, 'ONLY')
    bpy.ops.object.select_grouped(type='GROUP')
 
    if (join == True):
            bpy.ops.object.join()
            
    objselect(armtr, 'ONLY')
    bpy.ops.object.select_grouped(type='GROUP')
    bpy.ops.group.objects_remove()

    return armtr

class BonesFixer(bpy.types.Operator):
    bl_idname = "bones.fixer"
    bl_label = "Fix Bones"
    bl_options = {'REGISTER'}

    my_fixmode = EnumProperty(name="Recording Type:",
        items = [
                 ('PARENT','Fix as Parent','1'),
                 ('COPYTRANS','Fix with CopyTransforms','2'),
                 ('NONFIX','Not Fix','3')],
                 default= fixmode)
    my_join = BoolProperty(name="Join Bones",default= join)
    my_scale = bpy.props.FloatProperty(name="Bone Size:",min=0.001,max=100,default = scale)
    my_direction = EnumProperty(name="Direction (Parent Fix Only):",
        items = [
                 ('X','X','1'),
                 ('Y','Y','2'),
                 ('Z','Z','3'),
                 ('-X','-X','4'),
                 ('-Y','-Y','5'),
                 ('-Z','-Z','6')],
                 default= direction)
   

    def execute(self, context):
        scale = self.my_scale
        join = self.my_join
        fixmode = self.my_fixmode
        direction = self.my_direction
        
        add_ctbone(fixmode,join,scale,direction)

        print ('Finished!')
        return{'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#	Registration

def register():
    bpy.utils.register_class(BonesFixerPanel)
    bpy.utils.register_class(BonesFixer)

def unregister():
    bpy.utils.unregister_class(BonesFixerPanel)
    bpy.utils.unregister_class(BonesFixer)

if __name__ == "__main__":
    register()