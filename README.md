# IKPoleAngles
Blender script to calculate pole angles for ik constraints

## HOWTO
After following these steps shift+ctrl+v to mirror paste a pose should work properly, and pole angles have correct values so chains bone rolls dont matter while creating the rig.
``
1. run blender from terminal to see script output
2. create FK rig
3. Set all bone rotation to euler in edit and pose mode
4. remove ik constraints if already setup
5. shift+n local x on bones in edit mode
6. put correct bone names in script (base_bone is last bone in ik chain)
7. run script
8. create ik constraints with pole angle values from script
9. Now u can create animations

``

![](rig.png)
