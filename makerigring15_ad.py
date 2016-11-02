###################################
# Make Rigidbody Ring (addon-full)
#       v.1.5 (addon full ver.)
#  (c)Ishidourou 2013
###################################

#!BPY

bl_info = {
    "name": "Make Rig Ring15f",
    "author": "ishidourou",
    "version": (1, 5),
    "blender": (2, 65, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Make Rigidbody Ring Full version",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"}


import bpy
import random
from bpy.props import *
from math import *

#-------- default parameters ------------

g_rigset = True
g_primitive = 'ICOSPHERE' # SELECTED PLANE CUBE UVSPHERE ICOSPHERE CLYNDER CONE MONKEY TORUS
g_comscale = 0.2
g_usecomscale = True
g_obscale_x = 0.15
g_obscale_y = 0.05
g_obscale_z = 0.4
g_divcount = 60
g_ringradius = 3.0
g_zlocation = 5.0
g_randloc = True
g_rot_x = False
g_rot_y = False
g_pempty = False

g_rigtype = 'ACTIVE'  # ACTIVE , PASSIVE
g_dynamic = True
g_anim = False
g_mass = 1.0
g_cshape = 'MESH'     # MESH CONVEX_HULL CUBE CYLINDER CAPSULE SPHERE BOX
g_friction = 0.5
g_bounciness = 0
g_usemargin = False   
g_margin = 0.04
g_colgroup = 0        # min:0  max:19
g_deact = False
g_stdeact = False
g_dmptrans = 0.04
g_dmprot = 0.1
g_linearvel = 0.4
g_angularvel = 0.5
g_ctype = 'HINGE'     #FIXED POINT HINGE SLIDER PISTON GENERIC GENERIC_SPRING MOTOR
g_c_enable = True
g_d_collisions = True
g_breakable = False
g_threshold = 10
g_override = False
g_iterations = 10
g_use_z_limit = True
g_z_lower = -45.0
g_z_upper = 45.0

#----------------------------------------
obj = bpy.ops.object


pi = 3.14159

def degree(dg):
    dgr = 2*pi/360*dg
    return dgr

def objselect(objct):
    obj.mode_set(mode='OBJECT')
    bpy.context.scene.objects.active = objct
    objct.select = True

def set_rigconst(                
                rigtype,
                dynamic,
                anim,
                mass,
                cshape,
                friction,
                bounciness,
                usemargin,
                margin,
                colgroup,
                deact,
                stdeact,
                dmptrans,
                dmprot,
                linearvel,
                angularvel,
                ctype,
                c_enable,
                d_collisions,
                oldname,
                newname,
                breakable,
                threshold,
                override,
                iterations,
                use_z_limit,
                z_lower,
                z_upper
                ):
    bpy.ops.rigidbody.object_add(type=rigtype)
    bpy.ops.rigidbody.constraint_add(type='FIXED')
    bpy.context.object.rigid_body.enabled = dynamic
    bpy.context.object.rigid_body.kinematic = anim
    bpy.context.object.rigid_body.mass = mass
    bpy.context.object.rigid_body.collision_shape = cshape
    bpy.context.object.rigid_body.friction = friction
    bpy.context.object.rigid_body.restitution = bounciness
    bpy.context.object.rigid_body.use_margin = usemargin
    bpy.context.object.rigid_body.collision_margin = margin
    bpy.context.object.rigid_body.collision_groups[colgroup] = True
    bpy.context.object.rigid_body.use_deactivation = deact
    bpy.context.object.rigid_body.use_start_deactivated = stdeact
    bpy.context.object.rigid_body.linear_damping = dmptrans
    bpy.context.object.rigid_body.angular_damping = dmprot
    bpy.context.object.rigid_body.deactivate_linear_velocity = linearvel
    bpy.context.object.rigid_body.deactivate_angular_velocity = angularvel
    bpy.context.object.rigid_body_constraint.type = ctype
    bpy.context.object.rigid_body_constraint.enabled = c_enable
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects[oldname]
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects[newname]
    bpy.context.object.rigid_body_constraint.use_breaking = breakable
    bpy.context.object.rigid_body_constraint.breaking_threshold = threshold
    bpy.context.object.rigid_body_constraint.use_override_solver_iterations = override
    bpy.context.object.rigid_body_constraint.solver_iterations = iterations
    bpy.context.object.rigid_body_constraint.use_limit_ang_z = use_z_limit
    bpy.context.object.rigid_body_constraint.limit_ang_z_lower = degree(z_lower)
    bpy.context.object.rigid_body_constraint.limit_ang_z_upper = degree(z_upper)
    

class MakeRigRing(bpy.types.Operator):

    bl_idname = "object.makerigring"
    bl_label = "Make Rigidbody Ring"
    bl_options = {'REGISTER', 'UNDO'}
    
    my_rigset = BoolProperty(name="Add Rigid Body",default= g_rigset)
    my_primitive = EnumProperty(name="Duplicate Object:",
        items = [('SELECTED','Selected','0'),
                 ('PLANE','Plane','1'),
                 ('CUBE','Cube','2'),
                 ('UVSPHERE','UVSphere','3'),
                 ('ICOSPHERE','IcoSphere','4'),
                 ('CLYNDER','Cylinder','5'),
                 ('CONE','Cone','6'),
                 ('MONKEY','Monkey','7'),
                 ('TORUS','Torus','8')],
                 default= g_primitive)
    my_comscale = FloatProperty(name="         Common scale:",min=0.001,max=10,default = g_comscale)
    my_usecomscale = BoolProperty(name="Use Common Scale",default=g_usecomscale)
    my_obscale_x = FloatProperty(name="         Scale X:",min=0.001,max=10,default = g_obscale_x)
    my_obscale_y = FloatProperty(name="         Scale Y:",min=0.001,max=10,default = g_obscale_y)
    my_obscale_z = FloatProperty(name="         Scale Z:",min=0.001,max=10,default = g_obscale_z)


    my_divcount = IntProperty(name="Ring Divisions:",min=3,default=g_divcount)
    my_ringradius = FloatProperty(name="         Radius:",default = g_ringradius)
    my_zlocation = FloatProperty(name="         Location Z:",default = g_zlocation)
    my_randloc = BoolProperty(name="Random Location",default=g_randloc)
    my_rot_x = BoolProperty(name="Rotate X:90",default= g_rot_x)
    my_rot_y = BoolProperty(name="Rotate Y:90",default= g_rot_y)
    my_pempty = BoolProperty(name="Use Parent Empty",default= g_pempty)

    my_rigtype = EnumProperty(name="Rigid Body Type:",
        items = [('ACTIVE','Active','un'),
                 ('PASSIVE','Passive','deux')],
                 default= g_rigtype)
    my_dynamic = BoolProperty(name="Dynamic", default = g_dynamic)
    my_anim = BoolProperty(name="Animated",default=g_anim)
    my_mass = FloatProperty(name="         Mass:",min=0.001,max=10000,default = g_mass)
    my_cshape = EnumProperty(name="         Shape:",
        items = [('MESH','Mesh','0'),
                 ('CONVEX_HULL','Convex Hull','1'),
                 ('CONE','Cone','3'),
                 ('CYLINDER','Cylinder','4'),
                 ('CAPSULE','Capsule','5'),
                 ('SPHERE','Sphere','6'),
                 ('BOX','Box','7')],
                 default= g_cshape)
    my_friction = FloatProperty(name="         Friction:",min=0,max=1,default = g_friction)
    my_bounciness = FloatProperty(name="         Bounciness:",min=0,max=1,default = g_bounciness)
    my_usemargin = BoolProperty(name="Collision Margin",default= g_usemargin)
    my_margin = FloatProperty(name="         Margin:",min=0,max=1,default = g_margin)
    my_colgroup = IntProperty(name="         CollisionGroups:",min=0,max=19,default= g_colgroup)
    my_deact = BoolProperty(name="Enable Deactivation",default= g_deact)
    my_stdeact = BoolProperty(name="Start Deactivated",default= g_stdeact)
    my_dmptrans = FloatProperty(name="         Damping Translation:",min=0,max=1,default = g_dmptrans)
    my_dmprot = FloatProperty(name="         Damping Rotation:",min=0,max=1,default = g_dmprot)
    my_linearvel = FloatProperty(name="         Linear Vel:",min=0,max=10000,default = g_linearvel)
    my_angularvel = FloatProperty(name="         Angular Vel:",min=0,max=10000,default = g_angularvel)

    my_ctype = EnumProperty(name="         Constraint Type:",
        items = [('FIXED','Fixed','0'),
                 ('POINT','Point','1'),
                 ('HINGE','Hinge','2'),
                 ('SLIDER','Slider','3'),
                 ('PISTON','Piston','4'),
                 ('GENERIC','Generic','5'),
                 ('GENERIC_SPRING','Generic Spring','6'),
                 ('MOTOR','Motor','7')],
                 default= g_ctype)
    my_c_enable = BoolProperty(name="Enable Deactivation",default= g_c_enable)
    my_d_collisions = BoolProperty(name="Disable Collisions",default= g_d_collisions)
    my_breakable = BoolProperty(name="breakable",default= g_breakable)
    my_threshold = FloatProperty(name="         Threshold:",min=0,max=1000,default = g_threshold)
    my_override = BoolProperty(name="Override Iterations",default= g_override)
    my_iterations = IntProperty(name="         Iterations:",min=1,max=100,default= g_iterations)
    my_use_z_limit = BoolProperty(name="Use Limit:Z Angle",default= g_use_z_limit)
    my_z_lower = FloatProperty(name="         Lower:",min=-360.0,max=360.0,default = g_z_lower)
    my_z_upper = FloatProperty(name="         Upper:",min=-360.0,max=360.0,default = g_z_upper)


    def execute(self, context):
        scn = bpy.context.scene
        cobj = bpy.context.object

        bpy.context.scene.frame_current = 1
        distance = -1*self.my_ringradius
        
        bpy.context.scene.layers[0] = True
        bpy.context.scene.layers[14] = False

        if (self.my_primitive == 'SELECTED'):
            bpy.ops.transform.translate(value=(0, distance, 0))
        else:
            obj.select_all(action='DESELECT')
        if (self.my_primitive == 'PLANE'):
            bpy.ops.mesh.primitive_plane_add(location=(0, distance, 0), rotation=(0, 0, 0))
        if (self.my_primitive == 'CUBE'):
            bpy.ops.mesh.primitive_cube_add(location=(0, distance, 0))
        if (self.my_primitive == 'UVSPHERE'):
            bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=8, size=1, location=(0, distance, 0), rotation=(0, 0, 0))
        if (self.my_primitive == 'ICOSPHERE'):
            bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, size=1, location=(0, distance, 0), rotation=(0, 0, 0))
        if (self.my_primitive == 'CLYNDER'):
            bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1, depth=2, end_fill_type='NGON', view_align=False, enter_editmode=False, location=(0, distance, 0))
        if (self.my_primitive == 'CONE'):
            bpy.ops.mesh.primitive_cone_add(vertices=16, radius1=1, radius2=0, depth=2, end_fill_type='NGON', view_align=False, enter_editmode=False, location=(0, distance, 0), rotation=(0, 0, 0))
        if (self.my_primitive == 'MONKEY'):
            bpy.ops.mesh.primitive_monkey_add(view_align=False, enter_editmode=False, location=(0, distance, 0), rotation=(0, 0, 0))
        if (self.my_primitive == 'TORUS'):
            bpy.ops.mesh.primitive_torus_add(location=(0, distance, 0), view_align=False, rotation=(0, 0, 0), major_radius=1, minor_radius=0.25, major_segments=24, minor_segments=6, use_abso=False, abso_major_rad=1, abso_minor_rad=0.5)

        if (self.my_usecomscale == True):
            self.my_obscale_x = self.my_comscale
            self.my_obscale_y = self.my_comscale
            self.my_obscale_z = self.my_comscale

        obj.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.resize(value=(self.my_obscale_x, self.my_obscale_y, self.my_obscale_z))
        obj.mode_set(mode='OBJECT')

        basecube = bpy.context.object
        oldname = basecube.name

        bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
        empty = bpy.context.object

        obj.select_all(action='DESELECT')
        objselect(basecube)

        for i in range(self.my_divcount-1):
            bpy.ops.object.duplicate_move_linked()
            cube = bpy.context.object
            newname = cube.name

            objselect(cube)
            if (self.my_rigset == True):
                set_rigconst(                
                            self.my_rigtype,
                            self.my_dynamic,
                            self.my_anim,
                            self.my_mass,
                            self.my_cshape,
                            self.my_friction,
                            self.my_bounciness,
                            self.my_usemargin,
                            self.my_margin,
                            self.my_colgroup,
                            self.my_deact,
                            self.my_stdeact,
                            self.my_dmptrans,
                            self.my_dmprot,
                            self.my_linearvel,
                            self.my_angularvel,
                            self.my_ctype,
                            self.my_c_enable,
                            self.my_d_collisions,
                            oldname,
                            newname,
                            self.my_breakable,
                            self.my_threshold,
                            self.my_override,
                            self.my_iterations,
                            self.my_use_z_limit,
                            self.my_z_lower,
                            self.my_z_upper
                            )
            obj.select_all(action='DESELECT')

            objselect(cube)
            objselect(empty)
            bpy.ops.object.parent_set(type='OBJECT')
    
            obj.select_all(action='DESELECT')
            objselect(empty)
            bpy.ops.transform.rotate(value=2*pi/self.my_divcount, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='ENABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), release_confirm=False)
            print(oldname,newname)
            obj.select_all(action='DESELECT')
            objselect(basecube)
            oldname = newname
        
        if (self.my_rigset == True):
            set_rigconst(                
                    self.my_rigtype,
                    self.my_dynamic,
                    self.my_anim,
                    self.my_mass,
                    self.my_cshape,
                    self.my_friction,
                    self.my_bounciness,
                    self.my_usemargin,
                    self.my_margin,
                    self.my_colgroup,
                    self.my_deact,
                    self.my_stdeact,
                    self.my_dmptrans,
                    self.my_dmprot,
                    self.my_linearvel,
                    self.my_angularvel,
                    self.my_ctype,
                    self.my_c_enable,
                    self.my_d_collisions,
                    oldname,
                    basecube.name,
                    self.my_breakable,
                    self.my_threshold,
                    self.my_override,
                    self.my_iterations,
                    self.my_use_z_limit,
                    self.my_z_lower,
                    self.my_z_upper
                    )
        objselect(empty)
        bpy.ops.object.parent_set(type='OBJECT')
        obj.select_all(action='DESELECT')
        objselect(empty)

        for i in range(0,3):
            bpy.context.object.rotation_euler[i] = 0 

        if (self.my_rot_x == True):
            bpy.context.object.rotation_euler[0] = degree(90) 
        if (self.my_rot_y == True):
            bpy.context.object.rotation_euler[1] = degree(90) 
        
        bpy.context.object.location[2] = self.my_zlocation
        
        if (self.my_randloc == True):
            xxx = (random.random()-0.5)*5
            yyy = (random.random()-0.5)*5
            zzz = (random.random()-0.5)*5
            print(xxx,yyy,zzz)
            bpy.context.object.location[0] = xxx
            bpy.context.object.location[1] = yyy
            bpy.context.object.location[2] = self.my_zlocation + zzz

        if (self.my_pempty == False):
            obj.select_grouped(extend=False, type='CHILDREN_RECURSIVE')
            obj.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            obj.select_all(action='DESELECT')
            objselect(empty)
            obj.delete()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)




#bpy.utils.register_class(MakeRigRing)

# test call
#bpy.ops.object.dialog_operator('INVOKE_DEFAULT')
#bpy.ops.object.makerigring('INVOKE_DEFAULT')

# Registration

def add_object_button(self, context):
    self.layout.operator(
        MakeRigRing.bl_idname,
        text="Rigidbody Ring_f",
        icon='PLUGIN')

def register():
    bpy.utils.register_class(MakeRigRing)
    bpy.types.INFO_MT_mesh_add.append(add_object_button)
    #bpy.types.VIEW3D_MT_object.append(add_object_button)
    
def unregister():
    bpy.utils.unregister_class(MakeRigRing)
    bpy.types.INFO_MT_mesh_add.remove(add_object_button)
    #bpy.types.VIEW3D_MT_object.append(add_object_button)


if __name__ == "__main__":
    register()