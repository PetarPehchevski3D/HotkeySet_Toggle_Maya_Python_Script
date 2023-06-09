import maya.cmds as cmds
import maya.mel as mel

aTimeSlider = mel.eval('$tmpVar=$gPlayBackSlider')
timeRange = cmds.timeControl(aTimeSlider, q=True, rangeArray=True)

startingFrame = cmds.playbackOptions(q=True, ast=True)
endingFrame = cmds.playbackOptions(q=True, aet=True)

croppedStartFrame = cmds.playbackOptions(q=True, min=True)
croppedEndFrame = cmds.playbackOptions(q=True, max=True)


if croppedStartFrame != startingFrame or croppedEndFrame != endingFrame:
    cmds.playbackOptions(e=True, max=endingFrame)
    cmds.playbackOptions(e=True, min=startingFrame)
    
elif timeRange[1] - timeRange[0] > 1:
    cmds.playbackOptions(e=True, min=timeRange[0])
    cmds.playbackOptions(e=True, max=timeRange[1] - 1)
    selection = cmds.ls(sl=True)
    cmds.select(cl=True)
    cmds.select(selection)
    
else:
    cmds.inViewMessage(amg="<hl>Select a timeline range to crop - hold Shift + Left Click drag select<hl>", pos='midCenter', fade=True, fst=4000, ck=True)