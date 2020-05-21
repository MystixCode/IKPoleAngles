## A script that calculates pole angles for ik constraints in blender
## based on following stackexchange answer:
## https://blender.stackexchange.com/questions/19754/how-to-set-calculate-pole-angle-of-ik-constraint-so-the-chain-does-not-move/19755#19755

## HOWTO
## 1. run blender from terminal to see script output
## 2. create FK rig
## 3. Set all bone rotation to euler in edit and pose mode
## 4. remove ik constraints if already setup
## 5. shift+n local x on bones in edit mode
## 6. put correct bone names in script (base_bone is last bone in ik chain)
## 7. run script
## 8. create ik constraints with pole angle values from script
## 9. Now u can create animations
## shift+ctrl+v should work properly, and pole angles have correct values so chains bone rolls dont matter while creating the rig

print("############################")
print("##     IK Pole Angles     ##")
print("############################")

import bpy
from mathutils import *

def signed_angle(vector_u, vector_v, normal):
    # Normal specifies orientation
    angle = vector_u.angle(vector_v)
    if vector_u.cross(vector_v).angle(normal) < 1:
        angle = -angle
    return angle

def get_pole_angle(base_bone, ik_bone, pole_location):
    pole_normal = (ik_bone.tail - base_bone.head).cross(pole_location - base_bone.head)
    projected_pole_axis = pole_normal.cross(base_bone.tail - base_bone.head)
    return signed_angle(base_bone.x_axis, projected_pole_axis, base_bone.tail - base_bone.head)

#ARM LEFT
base_bone = bpy.context.active_object.pose.bones["upper_arm.L"]
ik_bone = bpy.context.active_object.pose.bones["arm_control.L"]
pole_bone = bpy.context.active_object.pose.bones["arm_pole.L"]
arm_l_pole_angle_in_radians = get_pole_angle(base_bone, ik_bone, pole_bone.matrix.translation)
arm_l_pole_angle_in_deg = round(180*arm_l_pole_angle_in_radians/3.141592, 3)
#ARM RIGHT
base_bone = bpy.context.active_object.pose.bones["upper_arm.R"]
ik_bone = bpy.context.active_object.pose.bones["arm_control.R"]
pole_bone = bpy.context.active_object.pose.bones["arm_pole.R"]
arm_r_pole_angle_in_radians = get_pole_angle(base_bone, ik_bone, pole_bone.matrix.translation)
arm_r_pole_angle_in_deg = round(180*arm_r_pole_angle_in_radians/3.141592, 3)
#LEG LEFT
base_bone = bpy.context.active_object.pose.bones["thigh.L"]
ik_bone = bpy.context.active_object.pose.bones["leg_control.L"]
pole_bone = bpy.context.active_object.pose.bones["leg_pole.L"]
leg_l_pole_angle_in_radians = get_pole_angle(base_bone, ik_bone, pole_bone.matrix.translation)
leg_l_pole_angle_in_deg = round(180*leg_l_pole_angle_in_radians/3.141592, 3)
#LEG RIGHT
base_bone = bpy.context.active_object.pose.bones["thigh.R"]
ik_bone = bpy.context.active_object.pose.bones["leg_control.R"]
pole_bone = bpy.context.active_object.pose.bones["leg_pole.R"]
leg_r_pole_angle_in_radians = get_pole_angle(base_bone, ik_bone, pole_bone.matrix.translation)
leg_r_pole_angle_in_deg = round(180*leg_r_pole_angle_in_radians/3.141592, 3)

print("arm_pole.L: " + str(arm_l_pole_angle_in_deg))
print("arm_pole.R: " + str(arm_r_pole_angle_in_deg))
print("leg_pole.L: " + str(leg_l_pole_angle_in_deg))
print("leg_pole.R: " + str(leg_r_pole_angle_in_deg))
