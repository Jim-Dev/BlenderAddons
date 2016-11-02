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
#以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）
#の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。
#これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、
#および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も
#無制限に含まれます。
#
#上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載
#するものとします。
#
#ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく
#提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害に
#ついての保証も含みますが、それに限定されるものではありません。 作者または著作権者は、
#契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいは
#ソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務に
#ついて何らの責任も負わないものとします。
#
#

####################################
# Set Particle Beams 日英版
#       v.1.0
#  (c)ishidourou 2014
####################################

#ブログ　http://stonefield.cocolog-nifty.com/higurashi



#!BPY
import bpy
import bmesh
import random
from bpy.props import *
from copy import *

bl_info = {
    "name": "Set Particle Beams EJ",
    "author": "ishidourou",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "View3D > Toolbar",
    "description": "SetparticlebeamEJ",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": 'Animation'}
    
#    Menu in tools region

class mes():

    #toolbar
    title = ('Set Particle Beams','パーティクルビームツール')
    btn1 = ('Set Particle Beams','パーティクルビームを付加')
    btn2 = ('Edit Particle Beams','ビーム設定を編集')
    btn3 = ('Add Beam Node','ビーム用ノードを追加')
    btn4 = ('Repair incorrect particle\'s moving','不正なパーティクル対策')

    #add particle beams
    ap_target = ('Name','名前')
    ap_dupemitter = ('Dup Emitter Polygons','エミッタ部を複製')
    ap_sepemitter = ('Split Emitter Polygons','エミッタポリゴン分離')
    ap_addshapekey = ('Add ShapeKey','シェイプキーを追加')
    ap_addmaterial = ('Add Material','マテリアルを追加')
    ap_velocity = ('Velocity','速度')
    ap_geometry = ('Geometry','発射方向')
    ap_geometry_item = ('Normal','ノーマル')
    ap_makenode = ('Create Beam Node','ビーム用ノードを作成')
    ap_bake = ('Bake Cache','全ベイク')
    ap_render = ('item','ビームの形状')
    ap_render_item = (('Line','ライン'),('IcoSphere','ICO球'),('Cube','立方体'))
    ap_error = ('Prease Select Mesh Object.','メッシュオブジェクトを選択してください')
    
    #edit particle beams
    ep_target = ('Target','編集対象名') 
    ep_start = ('Start','開始フレーム') 
    ep_orandom = ('Random','ランダム')
    ep_pcopy = ('Copy Other Parameters','パラメータをコピー') 
    ep_bake = ('Bake Cache','全ベイク')
    ep_label = ('Start frame','開始フレーム')
    ep_error = ('Preale Select Active Mesh Object had Beam Particles.','ビームを設定したオブジェクトを選択してください')

    #set beam node
    sn_new = ('New','新規に作成') 

    warning = ('Warning:','ウォーニング:')
    
def lang():
    system = bpy.context.user_preferences.system
    if system.use_international_fonts:
        if system.language == 'ja_JP':
            return 1
    return 0
         
class SetparticlebeamPanel(bpy.types.Panel):

    lng = lang()
    bl_label = mes.title[lng]
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
 
    def draw(self, context):
        self.layout.operator("set.particlebeam")
        self.layout.operator("edit.particlebeam")
        self.layout.operator("set.beamnode")
        self.layout.operator("shake.objects")

wmessage = 'Dummy'
class ErrorDialog(bpy.types.Operator):
    bl_idname = "error.dialog"
    bl_label = mes.warning[lang()]
    bl_options = {'REGISTER'}

    my_message = 'warnig'       
    def execute(self, context):
        print(self.my_message)
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

def objselect(objct,selection):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    if (selection == 'ONLY'):
        bpy.ops.object.select_all(action='DESELECT')
    bpy.context.scene.objects.active = objct
    objct.select = True
 
#---- main ------
   

def addvertexgroup(target):
    mode = bpy.context.mode
    if mode != 'EDIT_MESH':
        bpy.ops.object.editmode_toggle()
    obj = bpy.context.object
    bpy.ops.object.vertex_group_add()
    group = obj.vertex_groups.active
    group.name = target
    bpy.context.scene.tool_settings.vertex_group_weight = 1
    bpy.ops.object.vertex_group_assign()
    if mode != 'EDIT_MESH':
        bpy.ops.object.editmode_toggle()
    return(group.name)

def simple_dup():
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.ops.mesh.duplicate_move()
    bpy.ops.object.mode_set(mode = 'OBJECT')
    
def face_trans(tmode, sepem):
    bpy.ops.object.mode_set(mode = 'EDIT')
    bpy.context.tool_settings.mesh_select_mode = (False, False, True) 

    if sepem:
        obj = bpy.context.active_object
        bm = bmesh.from_edit_mesh(obj.data)
        bmselect = []

        for i in bm.faces:
            bmselect.append(i.select)
        
        bpy.ops.mesh.select_all(action='DESELECT')

        ct = 0
        for i in bmselect:
            if i == True:
                bm.faces[ct].select = True
                if tmode == 'DUP':
                    bpy.ops.mesh.duplicate_move()
                if tmode == 'SCALE':
                    bpy.ops.transform.resize(value=(0.001, 0.001, 0.001))
                bpy.ops.mesh.hide(unselected=False)
            ct += 1
        bpy.ops.mesh.reveal()
        bmesh.update_edit_mesh(obj.data)
        
    elif not sepem:
        if tmode == 'DUP':
            bpy.ops.mesh.duplicate_move()
        if tmode == 'SCALE':
            bpy.ops.transform.resize(value=(0.001, 0.001, 0.001))

def add_shapekey(sepem,target):
    cobj = bpy.context.object
    bpy.ops.object.mode_set(mode = 'OBJECT')
    for skey in bpy.data.shape_keys:
        sname = skey.name
    bpy.ops.object.shape_key_add()
    ask = cobj.active_shape_key
    if ask.name == 'Basis':
        bpy.ops.object.shape_key_add()
    ask = cobj.active_shape_key
    ask.name = target
    face_trans('SCALE',sepem)
    bpy.ops.object.mode_set(mode = 'OBJECT')

def mod_name():
    mod = bpy.context.object.modifiers
    ct = 0
    for i in mod:
        ct += 1
    return mod[ct-1].name

def add_maskmod(groupname):
    bpy.ops.object.modifier_add(type='MASK')
    cobj = bpy.context.object
    name = mod_name()
    cobj.modifiers[name].vertex_group = groupname
    cobj.modifiers[name].invert_vertex_group = True
    cobj.modifiers[name].show_viewport = False
    

def add_mat(target):
    obj = bpy.context.object
    ct = 0
    for i in obj.material_slots:
        ct += 1
    if ct == 0:
        mat = bpy.data.materials.new('Material')
        obj.data.materials.append(mat)
        
    mat = bpy.data.materials.new(target)
    obj.data.materials.append(mat)
    ct = -1
    for i in obj.material_slots:
        ct += 1
    obj.active_material_index = ct
    bpy.ops.object.material_slot_assign()
    amat = obj.active_material
    amat.diffuse_color = (1,1,1)
    amat.use_shadeless = True
    amat.pass_index = 1
    amat.use_raytrace = False
    amat.use_shadows = False
    amat.use_cast_buffer_shadows = False
    return ct

def make_ico(primitive,target):
    bpy.ops.object.mode_set(mode = 'OBJECT')
    if primitive == 'ICO':
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, size=1, location=(random.random()*10-5, random.random()*10, 0),layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True))
    else:
        bpy.ops.mesh.primitive_cube_add(radius=1, location=(random.random()*10-5, random.random()*10, 0), rotation=(0, 0, 0), layers=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True))
    obj = bpy.context.object
    mat = bpy.data.materials.new(target)
    obj.data.materials.append(mat)
    mat.use_shadeless = True
    mat.pass_index = 1
    mat.use_raytrace = False
    mat.use_shadows = False
    mat.use_cast_buffer_shadows = False
    obj.draw_type = 'WIRE'
    return obj
    
def addparticle(idx,dupem,velo,geo,render,target,bake,ico):
    bpy.ops.object.particle_system_add()
    particle = bpy.context.object.particle_systems.active
    particle.name = target
    pset = particle.settings
    pset.count = 1000
    pset.name = target

    pset.use_rotations = True
    pset.rotation_mode = 'NOR'

    if geo == 'NORMAL':
        pset.normal_factor = velo
    else:
        pset.normal_factor = 0
    if geo == 'X':
        pset.object_align_factor[0] = velo
    if geo == 'Y':
        pset.object_align_factor[1] = velo
    if geo == 'Z':
        pset.object_align_factor[2] = velo

    pset.effector_weights.gravity = 0
    pset.distribution = 'RAND'
    pset.use_even_distribution = False
    if render != 'LINE':
        cobj = bpy.context.object
        #ico = make_ico(render,target)
        objselect(cobj,'ONLY')
        pset.dupli_object = ico
        pset.particle_size = 0.07
        render = 'OBJECT'
        
    pset.render_type = render
    pset.line_length_tail = 0
    pset.line_length_head = 1
    pset.material = idx

    frame = bpy.context.scene.frame_current
    pset.frame_start = frame
    pset.frame_end = frame + 200
    pset.lifetime = 200

    groupname = addvertexgroup(target)
    if dupem:
        add_maskmod(groupname)

    particle.vertex_group_density = groupname
    particle.point_cache.name = target
    particle.point_cache.frame_step = 1
    if bake:
        bpy.context.scene.frame_current = 1
        bpy.ops.ptcache.free_bake_all()
        bpy.ops.ptcache.bake_all(bake=True)

class Particlebean(bpy.types.Operator):
    lng = lang()
    bl_idname = "set.particlebeam"
    bl_label = mes.btn1[lng]
    bl_options = {'REGISTER'}

    my_target = StringProperty(name=mes.ap_target[lng],default = 'Beam') 
    my_dupemitter = BoolProperty(name=mes.ap_dupemitter[lng],default = True)
    my_sepemitter = BoolProperty(name=mes.ap_sepemitter[lng],default = False)
    my_addshapekey = BoolProperty(name=mes.ap_addshapekey[lng],default = False)
    my_addmaterial = BoolProperty(name=mes.ap_addmaterial[lng],default = True)
    my_velocity = FloatProperty(name=mes.ap_velocity[lng],default = 100)
    my_geometry = EnumProperty(name=mes.ap_geometry[lng],
        items = [('NORMAL',mes.ap_geometry_item[lng],'0'),
                 ('X','X','1'),
                 ('Y','Y','2'),
                 ('Z','Z','3')],
                 default = 'NORMAL')
    my_makenode = BoolProperty(name=mes.ap_makenode[lng],default = False)
    #my_bake = BoolProperty(name=mes.ap_bake[lng],default = False)
    my_render = EnumProperty(name=mes.ap_render[lng],
        items = [('LINE',mes.ap_render_item[0][lng],'0'),
                 ('ICO',mes.ap_render_item[1][lng],'1'),
                 ('CUBE',mes.ap_render_item[2][lng],'2')],
                 default = 'LINE')

    def execute(self, context):
        
        target = self.my_target
        dupem = self.my_dupemitter
        sepem = self.my_sepemitter
        addsk = self.my_addshapekey
        addmt = self.my_addmaterial
        velo = self.my_velocity
        geo = self.my_geometry
        render = self.my_render
        makenode = self.my_makenode
        #bake = self.my_bake
        bake = False
        
        aobj = bpy.context.active_object
        mlist = []
        slist = bpy.context.selected_objects
        bmselect = []

        bpy.ops.object.mode_set(mode = 'OBJECT')
        for i in slist:
            if i.type == 'MESH':
                mlist.append(i)

        if len(mlist) == 0:
            error(mes.ap_error[lang()])
            return{'FINISHED'}

        bpy.ops.object.select_all(action='DESELECT')            
        for i in mlist:
            objselect(i,'ADD')
        bpy.ops.object.make_single_user(object=True, obdata=True)
                
        ico = bpy.context.object
        if render != 'LINE':
             ico = make_ico(render,target)

        for i in mlist:
            objselect(i,'ADD')
            bpy.ops.object.mode_set(mode = 'EDIT')
            bm = bmesh.from_edit_mesh(i.data)
            bmselect = []

            for ii in bm.faces:
                bmselect.append(ii.select)
            
            if dupem:
                face_trans('DUP',sepem)
                if addsk == True:
                    add_shapekey(sepem,target)
            ct = 1
            if addmt:
                ct = add_mat(target)
            addparticle(ct+1,dupem,velo,geo,render,target,bake,ico)

            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_all(action='DESELECT')

            c = 0
            bm = bmesh.from_edit_mesh(i.data)
            for ii in bmselect:
                bm.faces[c].select = ii
                c += 1
 
        if makenode:
            set_passes()
            set_node('NEW',False)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        for i in slist:
            objselect(i,'ADD')
        objselect(aobj,'ADD')
        return{'FINISHED'}    

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = col.row()
        row.prop(self,"my_target")
        row = col.row()
        row.prop(self, "my_dupemitter")
        row.prop(self, "my_sepemitter")
        row = col.row()
        row.prop(self, "my_addshapekey")
        row.prop(self, "my_addmaterial")
        row = col.row()
        row.prop(self, "my_geometry")
        row = col.row()
        row.prop(self, "my_velocity")
        row = col.row()
        row.prop(self, "my_render")
        row = col.row()
        #row.label("Render")
        row.prop(self, "my_makenode")
        row.prop(self, "my_bake")
        

#--------- edit particle beam ------------

def chk_had_beam(obj,target):
    objselect(obj,'ADD')
    if obj.type != 'MESH':
        return False
    p = obj.particle_systems
    for i in p:
        if i.name == target:
            return True
    return False
   
def copy_pp(sobj,dobj,target):
    ap = sobj.particle_systems[target]
    aps = ap.settings
    p = dobj.particle_systems[target]
    ps = p.settings
    
    ps.count = aps.count
    ps.frame_start = aps.frame_start
    ps.frame_end = aps.frame_end
    ps.lifetime = aps.lifetime
    ps.lifetime_random = aps.lifetime_random
    
    ps.emit_from = aps.emit_from
    ps.use_emit_random = aps.use_emit_random
    ps.use_even_distribution = aps.use_even_distribution
    ps.use_modifier_stack = aps.use_modifier_stack
    
    ps.normal_factor = aps.normal_factor
    ps.object_align_factor = aps.object_align_factor
    ps.tangent_factor = aps.tangent_factor
    ps.tangent_phase = aps.tangent_phase
    ps.object_factor = aps.object_factor
    ps.factor_random = aps.factor_random

    ps.use_rotations = aps.use_rotations
    ps.rotation_mode = aps.rotation_mode
    ps.rotation_factor_random = aps.rotation_factor_random
    ps.phase_factor = aps.phase_factor
    ps.angular_velocity_mode = aps.angular_velocity_mode
    ps.angular_velocity_factor = aps.angular_velocity_factor
    ps.use_dynamic_rotation = aps.use_dynamic_rotation

    ps.physics_type = aps.physics_type    
    ps.mass = aps.mass
    ps.use_multiply_size_mass = aps.use_multiply_size_mass
    ps.brownian_factor = aps.brownian_factor
    ps.drag_factor = aps.drag_factor
    ps.damping = aps.damping
    ps.integrator = aps.integrator
    ps.timestep = aps.timestep
    ps.subframes = aps.subframes
    ps.use_size_deflect = aps.use_size_deflect
    ps.use_die_on_collision = aps.use_die_on_collision
    
    ps.material = aps.material
    ps.use_render_emitter = aps.use_render_emitter
    ps.show_unborn = aps.show_unborn
    ps.use_parent_particles = aps.use_parent_particles
    ps.use_dead = aps.use_dead
    ps.render_type = aps.render_type
    ps.line_length_tail = aps.line_length_tail
    ps.line_length_head = aps.line_length_head
    ps.trail_count = aps.trail_count
    ps.use_velocity_length = aps.use_velocity_length
 
    if aps.render_type == 'OBJECT':
        ps.dupli_object = aps.dupli_object
        ps.dupli_group = aps.dupli_group
        ps.use_global_dupli = aps.use_global_dupli
        ps.use_rotation_dupli = aps.use_rotation_dupli
        ps.use_scale_dupli = aps.use_scale_dupli
    ps.particle_size = aps.particle_size
    ps.size_random = aps.size_random
    
    ps.path_end = aps.path_end
    ps.length_random = aps.length_random
    
    ps.effector_weights.gravity = aps.effector_weights.gravity
    ps.effector_weights.wind = aps.effector_weights.wind

class EditBeam(bpy.types.Operator):
    lng = lang()
    bl_idname = "edit.particlebeam"
    bl_label = mes.btn2[lng]
    bl_options = {'REGISTER'}

    my_target = StringProperty(name=mes.ep_target[lng],default = 'Beam') 
    my_start = FloatProperty(name=mes.ep_start[lng],min=0,default = 0) 
    my_orandom = FloatProperty(name=mes.ep_orandom[lng],min=0,max=1,default = 0)
    my_pcopy = BoolProperty(name=mes.ep_pcopy[lng],default = False) 
    #my_bake = BoolProperty(name=mes.ep_bake[lng],default = False)
    

    def execute(self, context):
        target = self.my_target
        start = self.my_start
        orandom = self.my_orandom
        pcopy = self.my_pcopy
        #bake = self.my_bake
        bake = False
        
        scene = bpy.context.scene
        startframe = scene.frame_start
        endframe = scene.frame_end
        fcount = endframe - startframe

        mlist = []
        aobj = bpy.context.active_object
        slist = bpy.context.selected_objects
        
        if not chk_had_beam(aobj,target):
            error(mes.ep_error[lang()])
            return{'FINISHED'}

        for i in slist:
             if chk_had_beam(i,target) == True:
                mlist.append(i)

        apset = aobj.particle_systems[target].settings

        dframe = apset.frame_end - apset.frame_start
        if start != 0:
            bpy.ops.ptcache.free_bake_all()
            apset.frame_start = start
            apset.frame_end = start + dframe
 
        if len(mlist) != 0:
            for i in mlist:
                if i != aobj:
                    bpy.ops.screen.frame_jump()
                    pset = i.particle_systems[target].settings
                    if pcopy == True:
                        copy_pp(aobj,i,target)

                    if start != 0:
                        pset.frame_start = start + (0.5-random.random())*orandom*fcount*2
                        if pset.frame_start < 1:
                            pset.frame_start = 1
                        pset.frame_end = pset.frame_start + dframe
                    else:
                        pset.frame_start += (0.5-random.random())*orandom*fcount*2
                        if pset.frame_start < 1:
                            pset.frame_start = 1
                        pset.frame_end = pset.frame_start + dframe
                   
        objselect(aobj,'ADD') 
        if bake:
            bpy.ops.ptcache.free_bake_all()
            bpy.ops.ptcache.bake_all(bake=True)
        return{'FINISHED'}    

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = col.row()
        row.prop(self,"my_target")
        row = col.row()
        row.label(mes.ep_label[lang()])
        row = col.row()
        row.prop(self, "my_start")
        row.prop(self, "my_orandom")
        row = col.row()
        row.prop(self, "my_pcopy")
        #row.prop(self, "my_bake")

#---------- set beam node -------------
def set_passes():
    cl = bpy.context.scene.render.layers
    for i in cl:
        i.use_pass_vector = True
        i.use_pass_material_index = True

def clear_node(tree):
    for n in tree.nodes:
        tree.nodes.remove(n)

def add_node(tree,nodeset,x,y):
    node = tree.nodes.new(nodeset)
    node.location = x*150,y*100
    return node
    
def set_node(mode,hide):
    scene = bpy.context.scene
    scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    links = tree.links
    c = 'CompositorNode'
    idmct = 0

    chk = False    

    japanese = False
    for i in tree.nodes:
        if i.name == 'コンポジット':
            japanese = True
            break
        
    if mode == 'ADD':
        if japanese:
            for i in tree.nodes:
                if i.name == 'レンダーレイヤー':
                    chk = True
                    rl = i
                if i.name[:4] == 'ミックス':
                    lastmix = i
                if i.name[:5] == 'IDマスク':
                    idmct += 1
                if i.name == 'コンポジット':
                    comp = i
                if i.name == 'ビューアー':
                    viewer = i
        else:
            for i in tree.nodes:
                if i.name == 'Render Layers':
                    chk = True
                    rl = i
                if i.name[:3] == 'Mix':
                    lastmix = i
                if i.name[:7] == 'ID Mask':
                    idmct += 1
                if i.name == 'Composite':
                    comp = i
                if i.name == 'Viewer':
                    viewer = i
    if not chk:
        mode = 'NEW'
    yy = idmct * -5
    if mode != 'ADD':
        yy = 0
        clear_node(tree)
        rl = add_node(tree,c+'RLayers',0,2)
    
        vb = add_node(tree,c+'VecBlur',2,4)
        vb.factor = 0.5
        vb.use_curved = True
        links.new(rl.outputs[0],vb.inputs[0])
        links.new(rl.outputs[2],vb.inputs[1])
        links.new(rl.outputs[5],vb.inputs[2])

    idm = add_node(tree,c+'IDMask',2,-1+yy)
    idm.index = idmct + 1
    links.new(rl.outputs[15],idm.inputs[0])

    vb_idm = add_node(tree,c+'VecBlur',3.5,-1+yy)
    vb_idm.factor = 0.6
    if mode == 'ADD':
        vb_idm.hide = hide
    vb_idm.use_curved = True
    links.new(idm.outputs[0],vb_idm.inputs[0])
    links.new(rl.outputs[2],vb_idm.inputs[1])
    links.new(rl.outputs[5],vb_idm.inputs[2])
    
    bl_idm = add_node(tree,c+'Blur',5,-1+yy)
    bl_idm.size_x = 3
    bl_idm.size_y = 3
    if mode == 'ADD':
        bl_idm.hide = hide
    links.new(vb_idm.outputs[0],bl_idm.inputs[0])

    cb_idm = add_node(tree,c+'ColorBalance',6.5,-1+yy)
    cb_idm.gamma = random.random(),random.random(),random.random()
    n = int(3*random.random())
    cb_idm.gamma[n] = 1
    cb_idm.gain = 0.9,0.9,0.9
    links.new(bl_idm.outputs[0],cb_idm.inputs[1])

    glare = add_node(tree,c+'Glare',10,-1+yy)
    glare.fade = 0.85
    glare.threshold = 0
    glare.streaks = 3
    if mode == 'ADD':
        glare.hide = hide
    links.new(cb_idm.outputs[0],glare.inputs[0])
    
    mix_add = add_node(tree,c+'MixRGB',12,2+yy)
    mix_add.blend_type = 'ADD'
    if mode == 'ADD':
        mix_add.hide = hide
    mix_add.inputs[0].default_value = 2
    links.new(glare.outputs[0],mix_add.inputs[2])
    if mode != 'ADD':
        links.new(vb.outputs[0],mix_add.inputs[1])
    else:
        links.new(lastmix.outputs[0],mix_add.inputs[1])


    if mode != 'ADD':
        comp = add_node(tree,c+'Composite',14.5,4)
        viewer = add_node(tree,c+'Viewer',14.5,1)

    links.new(mix_add.outputs[0],comp.inputs[0])
    links.new(mix_add.outputs[0],viewer.inputs[0])
       
class SetBeamNode(bpy.types.Operator):
    lng = lang()
    bl_idname = "set.beamnode"
    bl_label = mes.btn3[lng]
    bl_options = {'REGISTER'}

    my_new = BoolProperty(name=mes.sn_new[lng],default = False) 

    def execute(self, context):
        new = self.my_new 

        set_passes()
        if new:
            set_node('NEW',False)
        else:
            set_node('ADD',True)

        return{'FINISHED'}    

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

#------------- shake objects --------------

def shakeobjects():
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.transform.translate(value=(0.1, 0, 0))
    bpy.ops.transform.translate(value=(-0.1, 0, 0))

class ShakeObjects(bpy.types.Operator):
    lng = lang()
    bl_idname = "shake.objects"
    bl_label = mes.btn4[lng]
    bl_options = {'REGISTER'}

    def execute(self, context):
        slist = bpy.context.selected_objects

        for i in slist:
             if i.type == 'MESH':
                shakeobjects()
        
        return{'FINISHED'}


#	Registration

def register():
    bpy.utils.register_class(SetparticlebeamPanel)
    bpy.utils.register_class(Particlebean)
    bpy.utils.register_class(EditBeam)
    bpy.utils.register_class(SetBeamNode)
    bpy.utils.register_class(ShakeObjects)
    bpy.utils.register_class(ErrorDialog)

def unregister():
    bpy.utils.unregister_class(SetparticlebeamPanel)
    bpy.utils.unregister_class(Particlebean)
    bpy.utils.unregister_class(EditBeam)
    bpy.utils.unregister_class(SetBeamNode)
    bpy.utils.unregister_class(ShakeObjects)
    bpy.utils.unregister_class(ErrorDialog)

if __name__ == "__main__":
    register()