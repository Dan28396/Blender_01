import bpy

import pathlib
path = pathlib.Path(__file__).parent.absolute()


bpy.context.scene.render.engine = 'RPR'
for i in bpy.data.materials:
    bpy.data.materials.remove(i)
mat = 'Mball'

mat_ball = bpy.data.materials.new(name = mat)

bpy.data.materials[mat].use_nodes = True
bpy.data.materials[mat].node_tree.nodes.new("RPRShaderNodeUber")
bpy.data.materials[mat].node_tree.links.clear()
bpy.data.materials[mat].node_tree.links.new(bpy.data.materials[mat].node_tree.nodes["RPR Uber"].outputs["Shader"],
bpy.data.materials[mat].node_tree.nodes["Material Output"].inputs["Surface"])

bpy.data.materials[mat].node_tree.nodes["RPR Uber"].inputs[1].default_value = (0.8, 0.00171068, 0.00717472, 1)
bpy.data.materials[mat].node_tree.nodes["RPR Uber"].inputs[7].default_value = (0.104418, 0.132618, 1, 1)

bpy.ops.object.metaball_add(type='BALL', radius=1, enter_editmode=False, location=(0, 0, 0))
mesh = bpy.context.object.data
mesh.materials.append(mat_ball)

bpy.context.scene.render.filepath = str(path) + '\output.jpg'
bpy.ops.render.render(write_still = True)