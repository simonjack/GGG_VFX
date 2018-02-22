import maya.cmds as mc
import maya.mel as mel


def alignObjects()  # aligns the selected objects select the source object and then select the target objects

    sel = mc.ls(selection=True)

    source = sel[0]

    if len(sel) > 1:
        for idx, i in enumerate(sel):

            if idx != 0:
                mc.parentConstraint(source, i)
                mc.parentConstraint(source, i, e=True, rm=True)
            else:
                pass

    else:
        mc.confirmDialog(title='Confirm', message=' Select more than one object', button=['OK'], defaultButton='OK', dismissString='OK')


def alignPVT():  # aligns the pivot point of the selected object to the source object. select the source pivot object and then select the target objects

    sel = mc.ls(selection=True)

    source = sel[0]
    mc.spaceLocator(n='locationFinder')

    mc.parentConstraint(source, 'locationFinder')
    mc.parentConstraint(source, 'locationFinder', rm=True)

    position = mc.xform('locationFinder', ws=True, translation=True, q=True)
    # print position[0]

    rotation = mc.xform('locationFinder', ws=True, rotation=True, q=True)

    if len(sel) > 1:

        for idx, i in enumerate(sel):
            # print i

            if idx != 0:
                mc.setAttr(i + ".rotatePivotX", position[0])
                mc.setAttr(i + ".rotatePivotX", position[1])
                mc.setAttr(i + ".rotatePivotX", position[2])

                objParent = mc.listRelatives(i, p=True)
                mc.parent(i, 'locationFinder')

                mel.eval('makeIdentity -apply true -t 0 -r 1 -s 0 -n 0 ' + i + ';')

                if len(objParent) > 0:
                    mc.parent(i, objParent[0])
                else:
                    pass

    else:
        pass

    mc.delete('locationFinder')
