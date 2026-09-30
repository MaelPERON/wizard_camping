# coding: utf-8
# Wizard commands hook

import logging

import bpy
from blender_wizard import wizard_tools

logger = logging.getLogger(__name__)


def abc_command(export_GRP_list, export_file, frange):
    ''' This function is used to store 
    a default alembic export command.
    You can modify it from here
    Be carreful on what you are modifying'''
    wizard_tools.select_all_children(export_GRP_list)
    bpy.ops.wm.alembic_export(filepath=export_file,
                              selected=True,
                              export_custom_properties=True,
                              uvs=True,
                              orcos=True,
                              start=frange[0],
                              end=frange[1],
                              sh_open=-0.2,
                              sh_close=0.2)


def fbx_command(export_GRP_list, export_file, frange):
    ''' This function is used to store 
    a default fbx export command.
    You can modify it from here
    Be carreful on what you are modifying'''
    wizard_tools.select_all_children(export_GRP_list)
    bpy.ops.export_scene.fbx(filepath=export_file,
                             use_selection=True,
                             use_custom_props=True)


def usd_command(export_GRP_list, export_file,
                frange: tuple[int, int] = [0, 0]):
    ''' This function is used to store 
    a default usd export command.
    You can modify it from here
    Be carreful on what you are modifying'''
    context = bpy.context
    scene = context.scene
    orig_start = scene.frame_start
    orig_end = scene.frame_end

    # Override the scene frame range to match the export range
    scene.frame_start = frange[0]
    scene.frame_end = frange[1]

    wizard_tools.select_all_children(export_GRP_list)
    bpy.ops.wm.usd_export(
        filepath=export_file,
        selected_objects_only=True,
        export_animation=True,
        incremental_frames=0,
        export_hair=False,
        export_uvmaps=True,
        rename_uvmaps=True,
        export_mesh_colors=True,
        export_normals=True,
        export_materials=False,
        export_subdivision='BEST_MATCH',
        export_armatures=True,
        only_deform_bones=False,
        export_shapekeys=True,
        use_instancing=True,
        evaluation_mode='RENDER',
        generate_preview_surface=True,
        generate_materialx_network=False,
        convert_orientation=False,
        export_global_forward_selection='NEGATIVE_Z',
        export_global_up_selection='Y',
        export_textures_mode='NEW',
        overwrite_textures=False,
        relative_paths=True,
        xform_op_mode='TRS',
        root_prim_path='/root',
        export_custom_properties=True,
        custom_properties_namespace='',
        author_blender_name=True,
        convert_world_material=False,
        allow_unicode=True,
        export_meshes=True,
        export_lights=True,
        export_cameras=True,
        export_curves=True,
        export_points=True,
        export_volumes=True,
        triangulate_meshes=False,
        quad_method='SHORTEST_DIAGONAL',
        ngon_method='BEAUTY',
        usdz_downscale_size='KEEP',
        usdz_downscale_custom_size=128,
        merge_parent_xform=False,
        convert_scene_units='METERS',
        meters_per_unit=1.0)

    # Restore the original scene frame range
    scene.frame_start = orig_start
    scene.frame_end = orig_end
