
from os.path import expanduser
import maya.cmds as mc
import maya.mel as mel


def controlType(ctrltype, Name):  # initiate control types

    if ctrltype is "Box":
        mel.eval('curve -d 1 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -n ' + Name + ';')

    elif ctrltype is "Circle":
        mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -ch 1 -n ' + Name + ';')

    elif ctrltype is "Diamond":
        mel.eval('curve -d 1 -p 0.0 1 0 -p 0.0 0 1 -p 0.0 -1 0 -p 0.0 0 -1 -p 0.0 1 0 -p 1.0 0 0 -p 0.0 -1 0 -p -1.0 0 0 -p 0.0 1 0 -p 1.0 0 0 -p 0.0 0 1 -p -1.0 0 0 -p 0.0 0 -1 -p 1.0 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -n ' + Name + ' ;')

    elif ctrltype is "Arrow":
        mel.eval('curve -d 1 -p -1 0 1 -p -1 0 -2 -p 1 0 -2 -p 1 0 1 -p 2 0 1 -p 0 0 3 -p -2 0 1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7  -n ' + Name + ';')

    elif ctrltype is "Cross":
        mel.eval('curve -d 1 -p -1 0 1 -p -3 0 1 -p -3 0 2 -p -5 0 0 -p -3 0 -2 -p -3 0 -1 -p -1 0 -1 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 -1 -p 3 0 -1 -p 3 0 -2 -p 5 0 0 -p 3 0 2 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p 2 0 3 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -n ' + Name + ';')

    elif ctrltype is "rotate":
        crv1 = mel.eval('circle -nr 0 1 0 -c 0 0 0 -sw 180 -r 2 -n ' + Name + ' ;')
        crv2 = mel.eval('circle -nr 0 1 0 -c 0 0 0 -sw 180 -r 4 ;')
        arrow1 = mel.eval('curve -d 1 -p 0 0 -2 -p 0 0 -1 -p 2 0 -3 -p 0 0 -5 -p 0 0 -4 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
        arrow2 = mel.eval('curve -d 1 -p 0 0 2 -p 0 0 1 -p 2 0 3 -p 0 0 5 -p 0 0 4 -k 0 -k 1 -k 2 -k 3 -k 4  ;')

        relcrv1 = mc.listRelatives(crv1, shapes=True)
        relcrv2 = mc.listRelatives(crv2, shapes=True)
        relarrow1 = mc.listRelatives(arrow1, shapes=True)
        relarrow2 = mc.listRelatives(arrow2, shapes=True)

        mc.parent(relcrv2, crv1, shape=True, r=True)
        mc.parent(relarrow1, crv1, shape=True, r=True)
        mc.parent(relarrow2, crv1, shape=True, r=True)

        mc.delete(crv2, arrow1, arrow2)

        mc.rename(crv1, Name)

    elif ctrltype is "sphere":
        crv1 = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -ch 1  -n ' + Name + ';')
        crv2 = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -ch 1 ;')
        crv3 = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -ch 1 ;')

        mel.eval('rotate -r -os 90 0 0' + crv2 + ';')
        mel.eval('rotate -r -os 0 0 90' + crv3 + ';')
        mc.select(crv2, crv3)
        mel.eval('makeIdentity -apply 1 -t 1 -r 1 -s 1')

        relcrv2 = mc.listRelatives(crv2, shapes=True)
        relcrv3 = mc.listRelatives(crv3, shapes=True)

        mc.parent(relcrv2, crv1, shape=True, r=True)
        mc.parent(relcrv3, crv1, shape=True, r=True)
        mc.delete(crv2, crv3)

        mc.select(crv1)
        mel.eval('DeleteHistory;')
        pass

    return Name


def createArrowCtrlSetup():  # create Arrow Control
    selections = mc.ls(sl=True)
    if (len(selections) == 0):  # run this if there are no object selected
        mc.select(cl=True)
        # creates arrow curve
        ctrlName = ("ctrl_ARROW01")
        newCtrl = controlType("Arrow", ctrlName)
        # creates group
        grpName = ("grp_ARROW01")
        newGrp = mc.group(em=True, n=grpName)
        mc.parent(newCtrl, newGrp)
        # creates locator and move to object location
        locName = ("loc_ARROW01")
        newLoc = mc.spaceLocator(n=locName)
        mc.parent(newGrp, newLoc)
        mc.select(cl=True)
    else:
        for sel in selections:  # run this if there are object selected
            mc.select(cl=True)
            # creates arrow curve
            ctrlName = ("ctrl_" + sel)
            newCtrl = controlType("Arrow", ctrlName)
            # creates group
            grpName = ("grp_" + sel)
            newGrp = mc.group(em=True, n=grpName)
            mc.parent(newCtrl, newGrp)
            # creates locator and move to object location
            locName = ("loc_" + sel)
            newLoc = mc.spaceLocator(n=locName)
            mc.parent(newGrp, newLoc)
            mc.delete(mc.parentConstraint(sel, newLoc))
            mc.select(cl=True)

    if ctrlName:
        mc.confirmDialog(title='Confirm', message='Arrow Control Created.', button=['OK'], defaultButton='OK', dismissString='OK')

    else:
        pass


def createBoxCtrlSetup():  # create Arrow Control
    selections = mc.ls(sl=True)
    if (len(selections) == 0):  # run this if there are no object selected
        mc.select(cl=True)
        # creates arrow curve
        ctrlName = ("ctrl_BOX01")
        newCtrl = controlType("Box", ctrlName)
        # creates group
        grpName = ("grp_BOX01")
        newGrp = mc.group(em=True, n=grpName)
        mc.parent(newCtrl, newGrp)
        # creates locator and move to object location
        locName = ("loc_BOX01")
        newLoc = mc.spaceLocator(n=locName)
        mc.parent(newGrp, newLoc)
        mc.select(cl=True)
    else:
        for sel in selections:  # run this if there are object selected
            mc.select(cl=True)
            # creates arrow curve
            ctrlName = ("ctrl_" + sel)
            newCtrl = controlType("Box", ctrlName)
            # creates group
            grpName = ("grp_" + sel)
            newGrp = mc.group(em=True, n=grpName)
            mc.parent(newCtrl, newGrp)
            # creates locator and move to object location
            locName = ("loc_" + sel)
            newLoc = mc.spaceLocator(n=locName)
            mc.parent(newGrp, newLoc)
            mc.delete(mc.parentConstraint(sel, newLoc))
            mc.select(cl=True)

    if ctrlName:
        mc.confirmDialog(title='Confirm', message='Box Control Created.', button=['OK'], defaultButton='OK', dismissString='OK')

    else:
        pass


def createCircleCtrlSetup():  # create Arrow Control
    selections = mc.ls(sl=True)
    if (len(selections) == 0):  # run this if there are no object selected
        mc.select(cl=True)
        # creates arrow curve
        ctrlName = ("ctrl_CIRCLE01")
        newCtrl = controlType("Circle", ctrlName)
        # creates group
        grpName = ("grp_CIRCLE01")
        newGrp = mc.group(em=True, n=grpName)
        mc.parent(newCtrl, newGrp)
        # creates locator and move to object location
        locName = ("loc_CIRCLE01")
        newLoc = mc.spaceLocator(n=locName)
        mc.parent(newGrp, newLoc)
        mc.select(cl=True)
    else:
        for sel in selections:  # run this if there are object selected
            mc.select(cl=True)
            # creates arrow curve
            ctrlName = ("ctrl_" + sel)
            newCtrl = controlType("Circle", ctrlName)
            # creates group
            grpName = ("grp_" + sel)
            newGrp = mc.group(em=True, n=grpName)
            mc.parent(newCtrl, newGrp)
            # creates locator and move to object location
            locName = ("loc_" + sel)
            newLoc = mc.spaceLocator(n=locName)
            mc.parent(newGrp, newLoc)
            mc.delete(mc.parentConstraint(sel, newLoc))
            mc.select(cl=True)

    if ctrlName:
        mc.confirmDialog(title='Confirm', message='Circle Control Created.', button=['OK'], defaultButton='OK', dismissString='OK')

    else:
        pass


def createDiamondCtrlSetup():  # create Arrow Control
    selections = mc.ls(sl=True)
    if (len(selections) == 0):  # run this if there are no object selected
        mc.select(cl=True)
        # creates arrow curve
        ctrlName = ("ctrl_DIAMOND01")
        newCtrl = controlType("Diamond", ctrlName)
        # creates group
        grpName = ("grp_DIAMOND01")
        newGrp = mc.group(em=True, n=grpName)
        mc.parent(newCtrl, newGrp)
        # creates locator and move to object location
        locName = ("loc_DIAMOND01")
        newLoc = mc.spaceLocator(n=locName)
        mc.parent(newGrp, newLoc)
        mc.select(cl=True)
    else:
        for sel in selections:  # run this if there are object selected
            mc.select(cl=True)
            # creates arrow curve
            ctrlName = ("ctrl_" + sel)
            newCtrl = controlType("Diamond", ctrlName)
            # creates group
            grpName = ("grp_" + sel)
            newGrp = mc.group(em=True, n=grpName)
            mc.parent(newCtrl, newGrp)
            # creates locator and move to object location
            locName = ("loc_" + sel)
            newLoc = mc.spaceLocator(n=locName)
            mc.parent(newGrp, newLoc)
            mc.delete(mc.parentConstraint(sel, newLoc))
            mc.select(cl=True)

    if ctrlName:
        mc.confirmDialog(title='Confirm', message='Diamond Control Created.', button=['OK'], defaultButton='OK', dismissString='OK')

    else:
        pass


def createCrossCtrlSetup():  # create Arrow Control
    selections = mc.ls(sl=True)
    if (len(selections) == 0):  # run this if there are no object selected
        mc.select(cl=True)
        # creates arrow curve
        ctrlName = ("ctrl_CROSS01")
        newCtrl = controlType("Cross", ctrlName)
        # creates group
        grpName = ("grp_CROSS01")
        newGrp = mc.group(em=True, n=grpName)
        mc.parent(newCtrl, newGrp)
        # creates locator and move to object location
        locName = ("loc_CROSS01")
        newLoc = mc.spaceLocator(n=locName)
        mc.parent(newGrp, newLoc)
        mc.select(cl=True)
    else:
        for sel in selections:  # run this if there are object selected
            mc.select(cl=True)
            # creates arrow curve
            ctrlName = ("ctrl_" + sel)
            newCtrl = controlType("Diamond", ctrlName)
            # creates group
            grpName = ("grp_" + sel)
            newGrp = mc.group(em=True, n=grpName)
            mc.parent(newCtrl, newGrp)
            # creates locator and move to object location
            locName = ("loc_" + sel)
            newLoc = mc.spaceLocator(n=locName)
            mc.parent(newGrp, newLoc)
            mc.delete(mc.parentConstraint(sel, newLoc))
            mc.select(cl=True)

    if ctrlName:
        mc.confirmDialog(title='Confirm', message='Cross Control Created.', button=['OK'], defaultButton='OK', dismissString='OK')

    else:
        pass


def createRotateCtrlSetup():  # create Arrow Control
    selections = mc.ls(sl=True)
    if (len(selections) == 0):  # run this if there are no object selected
        mc.select(cl=True)
        # creates arrow curve
        ctrlName = ("ctrl_ROTATE01")
        newCtrl = controlType("rotate", ctrlName)
        # creates group
        grpName = ("grp_ROTATE01")
        newGrp = mc.group(em=True, n=grpName)
        mc.parent(newCtrl, newGrp)
        # creates locator and move to object location
        locName = ("loc_ROTATE01")
        newLoc = mc.spaceLocator(n=locName)
        mc.parent(newGrp, newLoc)
        mc.select(cl=True)
    else:
        for sel in selections:  # run this if there are object selected
            mc.select(cl=True)
            # creates arrow curve
            ctrlName = ("ctrl_" + sel)
            newCtrl = controlType("rotate", ctrlName)
            # creates group
            grpName = ("grp_" + sel)
            newGrp = mc.group(em=True, n=grpName)
            mc.parent(newCtrl, newGrp)
            # creates locator and move to object location
            locName = ("loc_" + sel)
            newLoc = mc.spaceLocator(n=locName)
            mc.parent(newGrp, newLoc)
            mc.delete(mc.parentConstraint(sel, newLoc))
            mc.select(cl=True)

    if ctrlName:
        mc.confirmDialog(title='Confirm', message='Rotate Control Created.', button=['OK'], defaultButton='OK', dismissString='OK')

    else:
        pass


def createSphereCtrlSetup():  # create Arrow Control
    selections = mc.ls(sl=True)
    if (len(selections) == 0):  # run this if there are no object selected
        mc.select(cl=True)
        # creates arrow curve
        ctrlName = ("ctrl_SPHERE01")
        newCtrl = controlType("sphere", ctrlName)
        # creates group
        grpName = ("grp_SPHERE01")
        newGrp = mc.group(em=True, n=grpName)
        mc.parent(newCtrl, newGrp)
        # creates locator and move to object location
        locName = ("loc_SPHERE01")
        newLoc = mc.spaceLocator(n=locName)
        mc.parent(newGrp, newLoc)
        mc.select(cl=True)
    else:
        for sel in selections:  # run this if there are object selected
            mc.select(cl=True)
            # creates arrow curve
            ctrlName = ("ctrl_" + sel)
            newCtrl = controlType("sphere", ctrlName)
            # creates group
            grpName = ("grp_" + sel)
            newGrp = mc.group(em=True, n=grpName)
            mc.parent(newCtrl, newGrp)
            # creates locator and move to object location
            locName = ("loc_" + sel)
            newLoc = mc.spaceLocator(n=locName)
            mc.parent(newGrp, newLoc)
            mc.delete(mc.parentConstraint(sel, newLoc))
            mc.select(cl=True)

    if ctrlName:
        mc.confirmDialog(title='Confirm', message='Sphere Control Created.', button=['OK'], defaultButton='OK', dismissString='OK')

    else:
        pass


def UI():
    path = expanduser("~") + '\\maya\\scripts\\icons'

    window = mc.window(name='controlCreator')
    mc.rowColumnLayout(numberOfRows=1)
    mc.iconTextButton(style='iconAndTextVertical', image1=path + '\\arrow.jpg', label='Arrow', c=createArrowCtrlSetup)
    mc.iconTextButton(style='iconAndTextVertical', image1=path + '\\box.jpg', label='Box', c=createBoxCtrlSetup)
    mc.iconTextButton(style='iconAndTextVertical', image1=path + '\\circle.jpg', label='Circle', c=createCircleCtrlSetup)
    mc.iconTextButton(style='iconAndTextVertical', image1=path + '\\diamond.jpg', label='Diamond', c=createDiamondCtrlSetup)
    mc.iconTextButton(style='iconAndTextVertical', image1=path + '\\cross.jpg', label='Cross', c=createSphereCtrlSetup)
    mc.showWindow(window)
