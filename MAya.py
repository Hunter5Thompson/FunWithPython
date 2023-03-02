import maya.cmds as cmds

#get all objects in the group
objects = cmds.ls("BigJunks")

#loop through the objects
for obj in objects:
#select the object
    cmds.select(obj)
#create a UV set for the object
    cmds.polyAutoProjection(ibd=1, cm=0, l=2, sc=1, o=1, p=4, ps=0.2)
#layout the UVs in a square, allow free rotations, scale uniformly
    cmds.polyMultiLayoutUV( scale=1, rotateForBestFit=2, layout=2 )