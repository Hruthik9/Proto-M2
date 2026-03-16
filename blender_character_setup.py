import bpy
import os

def setup_hyper_realistic_materials():
    """
    Automates the creation of hyper-realistic PBR materials for a character.
    Includes SSS skin, procedural wool, and stainless steel.
    """
    
    # 1. Skin Material (SSS + Surface Detail)
    if "Skin_Material" not in bpy.data.materials:
        skin_mat = bpy.data.materials.new(name="Skin_Material")
    else:
        skin_mat = bpy.data.materials["Skin_Material"]
        
    skin_mat.use_nodes = True
    nodes = skin_mat.node_tree.nodes
    nodes.clear()
    
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = (0.8, 0.5, 0.4, 1.0)
    bsdf.inputs['Subsurface Weight'].default_value = 0.4
    bsdf.inputs['Subsurface Radius'].default_value = (1.0, 0.2, 0.1) # Human Skin R/G/B scattering
    bsdf.inputs['Roughness'].default_value = 0.35
    
    output = nodes.new(type='ShaderNodeOutputMaterial')
    skin_mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

    # 2. Suit Material (Procedural Navy Blue Wool)
    if "Suit_Material" not in bpy.data.materials:
        suit_mat = bpy.data.materials.new(name="Suit_Material")
    else:
        suit_mat = bpy.data.materials["Suit_Material"]
        
    suit_mat.use_nodes = True
    suit_nodes = suit_mat.node_tree.nodes
    suit_nodes.clear()
    
    suit_bsdf = suit_nodes.new(type='ShaderNodeBsdfPrincipled')
    suit_bsdf.inputs['Base Color'].default_value = (0.01, 0.05, 0.15, 1.0) # Deep Navy
    suit_bsdf.inputs['Roughness'].default_value = 0.85
    
    # Procedural Twill Weave logic
    noise = suit_nodes.new(type='ShaderNodeTexNoise')
    noise.inputs['Scale'].default_value = 1000.0
    noise.inputs['Detail'].default_value = 15.0
    
    suit_mat.node_tree.links.new(noise.outputs['Fac'], suit_bsdf.inputs['Roughness'])
    
    suit_output = suit_nodes.new(type='ShaderNodeOutputMaterial')
    suit_mat.node_tree.links.new(suit_bsdf.outputs['BSDF'], suit_output.inputs['Surface'])

    # 3. Hardware Material (Polished Stainless Steel)
    if "Metal_Material" not in bpy.data.materials:
        metal_mat = bpy.data.materials.new(name="Metal_Material")
    else:
        metal_mat = bpy.data.materials["Metal_Material"]
        
    metal_mat.use_nodes = True
    m_nodes = metal_mat.node_tree.nodes
    m_nodes.clear()
    
    m_bsdf = m_nodes.new(type='ShaderNodeBsdfPrincipled')
    m_bsdf.inputs['Metallic'].default_value = 1.0
    m_bsdf.inputs['Roughness'].default_value = 0.05
    m_bsdf.inputs['Base Color'].default_value = (0.9, 0.9, 0.9, 1.0)
    
    m_output = m_nodes.new(type='ShaderNodeOutputMaterial')
    metal_mat.node_tree.links.new(m_bsdf.outputs['BSDF'], m_output.inputs['Surface'])

    print("Hyper-realistic materials initialized successfully.")

if __name__ == "__main__":
    setup_hyper_realistic_materials()
