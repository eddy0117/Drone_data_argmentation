import bpy
import os
import numpy as np
import math

def setup_camera():

    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.type == 'CAMERA':
            obj.select_set(True)
    bpy.ops.object.delete()


    bpy.ops.object.camera_add(location=(0, -7, 2))
    camera = bpy.context.object
 
    camera.rotation_euler = (1.3, 0, 0)  
    bpy.context.scene.camera = camera  
def setup_model(rotation: tuple):

 
    model.rotation_euler.x = math.radians(rotation[0]) 
    model.rotation_euler.y = math.radians(rotation[1]) 
    model.rotation_euler.z = math.radians(rotation[2])  
    
    
if __name__ == "__main__":


    bpy.context.scene.render.film_transparent = True


    bpy.context.scene.render.image_settings.file_format = 'PNG'
    bpy.context.scene.render.image_settings.color_mode = 'RGBA'
    
    bpy.context.scene.render.resolution_x = 768
    bpy.context.scene.render.resolution_y = 768


    model_name = "dji.fbx"
    model_obj_name = "Default"
    model_path = os.path.join('model', model_name)

    if not os.path.exists(os.path.join('E:/Programs/Drone_data_argmentation/img', model_name)):
        os.makedirs(os.path.join('E:/Programs/Drone_data_argmentation/img', model_name.split('.')[0]))
        

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    if model_path.endswith('.obj'):
        bpy.ops.wm.obj_import(filepath=model_path)
    elif model_path.endswith('.fbx'):
        bpy.ops.import_scene.fbx(filepath=model_path)

    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.name == model_obj_name:
            obj.select_set(True)
      
    model = bpy.context.selected_objects[0]
 

    deg_list = list(np.arange(0, 360, 45))

    setup_camera()
    for x_idx, x_deg in enumerate(deg_list):
        for y_idx, y_deg in enumerate(deg_list):
            for z_idx, z_deg in enumerate(deg_list):
                setup_model((x_deg, y_deg, z_deg))
           
                output_path = os.path.join('E:/Programs/Drone_data_argmentation/img', model_name, f"{str(x_deg)}_{str(y_deg)}_{str(z_deg)}.png")
                bpy.context.scene.render.filepath = output_path
                bpy.ops.render.render(write_still=True)
       


