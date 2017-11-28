#connect2dPlacement node to fileTexture

#Select the 2dPlacementNode, then select the fileTextures and run this!!!

import maya.cmds as mc
sel = mc.ls(selection = True)
connexList = []

def connectMe():
    
    connexList = mc.ls(selection = True)
    idx = len(connexList)
    print connexList
    for i in range(idx):
        if i == 0:
            pass
        else:     
            mc.connectAttr ( connexList[0]+".mirrorU", connexList[i]+".mirrorU", f = True)
            mc.connectAttr ( connexList[0]+".mirrorV", connexList[i]+".mirrorV", f = True) 
            mc.connectAttr ( connexList[0]+".stagger", connexList[i]+".stagger", f = True) 
            mc.connectAttr ( connexList[0]+".wrapU", connexList[i]+".wrapU", f = True)
            mc.connectAttr ( connexList[0]+".wrapV", connexList[i]+".wrapV", f = True) 
            mc.connectAttr (  connexList[0]+".repeatUV", connexList[i]+".repeatUV", f = True) 
            mc.connectAttr ( connexList[0]+".vertexUvOne", connexList[i]+".vertexUvOne", f = True) 
            mc.connectAttr ( connexList[0]+".vertexUvTwo", connexList[i]+".vertexUvTwo", f = True) 
            mc.connectAttr ( connexList[0]+".vertexUvThree", connexList[i]+".vertexUvThree", f = True) 
            mc.connectAttr ( connexList[0]+".vertexCameraOne", connexList[i]+".vertexCameraOne", f = True) 
            mc.connectAttr ( connexList[0]+".noiseUV", connexList[i]+".noiseUV", f = True) 
            mc.connectAttr ( connexList[0]+".offset", connexList[i]+".offset", f = True)
    
    
