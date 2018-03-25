import maya.cmds as mc
import os
import maya.mel as mel


mc.loadPlugin("GGGMayaToolUpdaterPlugin2018.mll")  # Load GGG
hitWords = ['Animations', 'animations', 'once.mb', 'loop.mb']


class GGGMayaUtil():

    def __init__(self):

        pass

    def pathOperations(self, *args):
        global finalPath, pathToOpen
        filePath = mc.file(q=True, sn=True)
        keyWords = str.split(str(filePath), ".")
        cwd = str.split(str(keyWords[0]), "/")[-1]
        finalPath = keyWords[0].replace(cwd, "", 1)

        constructPath = str.split(finalPath, "/Art")

        if len(constructPath) < 1:
            constructPath = str.split(finalPath, "/art")

        binExtension = constructPath[1].replace('/', '\\')
        binPath = constructPath[0].replace('C:/SVNs', 'C:\\SVNs\\bin\\client\\Art')

        pathToOpen = binPath + binExtension

        # os.startfile(pathToOpen)

        return pathToOpen, finalPath

    def binOpen(self, *args):
        constructedPath = self.pathOperations()[0]
        os.startfile(constructedPath)

    def artOpen(self, *args):
        constructedPath = self.pathOperations()[1]
        os.startfile(constructedPath)

    def cleanBin(self, *args):
        pathToClean = self.pathOperations()[0]
        files = os.listdir(pathToClean)

        if len(files) == 0:
            mc.confirmDialog(title='Confirm', message='No files to clear', button=['OK'], defaultButton='OK', dismissString='OK')

        else:
            for i in files:
                os.remove(pathToClean + "\\" + i)

    def exportGGG(self, *args):
        path = self.pathOperations()[1]

        items = os.listdir(path)

        if len(items) <= 1 and "Animations" not in items:
            mel.eval('GGG - exportSelected false')

        elif len(items) > 1:

            for i in items:
                if i.endswith('rig.mb'):
                    pass
                else:
                    key = i.split(" ")
                    # print key
                    if len(key) > 1 and key[1] in hitWords:
                        fullPath = path + i
                        print fullPath
                        #mc.file(fullPath, open=True, f=True, iv=True)
                        mel.eval('GGG - exportSelected false')
                        mel.eval('ggg_exportAnimationSet false')
                        exitID = exitID + 1

                        if exitID == 1:
                            break

        elif "Animations" in items and len(items) > 1:
            mel.eval('ggg_exportAnimationSet false')

        elif "animations" in items and len(items) > 1:
            mel.eval('ggg_exportAnimationSet false')

        elif "animation" in items and len(items) > 1:
            mel.eval('ggg_exportAnimationSet false')

        else:
            pass

    def UIElements(self):

        window = mc.window(title="gggUtil_tools")

        if(mc.window('gggUtil_tools', exists=True)):
            mc.deleteUI('GGGExportUtil')

        mc.gridLayout(numberOfColumns=4, cellWidthHeight=(100, 50))
        mc.button(label='Open Art', c=self.artOpen)
        mc.button(label='Open Bin', c=self.binOpen)
        mc.button(label='Clean Bin', c=self.cleanBin)
        mc.button(label='Export Rig/Anim', c=self.exportGGG)
        mc.setParent("..")

        mc.showWindow(window)
