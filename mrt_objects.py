import maya.cmds as cmds
import maya.mel as mel
import os

def clearParentSwitchControlList():
    global parentSwitchControls
    parentSwitchControls = []

def createRawControlSurface(transformName, modHandleColour, createWithTransform=False):
    if createWithTransform:
        handleParent = cmds.createNode('transform', name=transformName+'_control')
        handleShape = cmds.createNode('nurbsSurface', name=handleParent+'Shape', parent=handleParent)
    else:
        handleParent = transformName
        handleShape = cmds.createNode('nurbsSurface', name=handleParent+'_controlShape', parent=handleParent)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', modHandleColour)
    cmds.setAttr('.overrideShading', 0)
    cmds.setAttr('.castsShadows', 0)
    cmds.setAttr('.receiveShadows', 0)
    cmds.setAttr('.motionBlur', 0)
    cmds.setAttr('.primaryVisibility', 0)
    cmds.setAttr('.smoothShading', 0)
    cmds.setAttr('.visibleInReflections', 0)
    cmds.setAttr('.visibleInRefractions', 0)
    cmds.setAttr('.curvePrecision', 3)
    cmds.setAttr('.curvePrecisionShaded', 3)
    mel.eval("""setAttr ".cached" -type "nurbsSurface"
    3 3 0 2 no 
    9 0 0 0 1 2 3 4 4 4
    13 -2 -1 0 1 2 3 4 5 6 7 8 9 10

    77
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    -3.5943266496573207e-017 -0.088216295764655561 -2.2332999188907222e-017
    0.017635918748742173 -0.088216295764655561 -0.01763591874874226
    0.024940955479381171 -0.088216295764655561 -5.4879609782365257e-018
    0.017635918748742194 -0.088216295764655561 0.017635918748742228
    -3.4249920494118131e-017 -0.088216295764655561 0.024940955479381209
    -0.017635918748742273 -0.088216295764655561 0.017635918748742239
    -0.024940955479381272 -0.088216295764655561 5.045241990938553e-018
    -0.017635918748742287 -0.088216295764655561 -0.017635918748742228
    -6.0736492392566665e-017 -0.088216295764655561 -0.024940955479381226
    0.017635918748742173 -0.088216295764655561 -0.01763591874874226
    0.024940955479381171 -0.088216295764655561 -5.4879609782365257e-018
    0.017635918748742194 -0.088216295764655561 0.017635918748742228
    0.054379169406585562 -0.069127314866026565 -0.054379169406585694
    0.076903758885377482 -0.069127314866026565 9.2681717704982957e-018
    0.05437916940658561 -0.069127314866026565 0.054379169406585652
    -2.6851335307337042e-017 -0.069127314866026565 0.076903758885377524
    -0.054379169406585694 -0.069127314866026565 0.054379169406585659
    -0.076903758885377566 -0.069127314866026565 1.4212576503632265e-017
    -0.054379169406585694 -0.069127314866026565 -0.054379169406585603
    -8.0986880233980439e-017 -0.069127314866026565 -0.076903758885377524
    0.054379169406585562 -0.069127314866026565 -0.054379169406585694
    0.076903758885377482 -0.069127314866026565 9.2681717704982957e-018
    0.05437916940658561 -0.069127314866026565 0.054379169406585652
    0.076501387595746942 5.7652798213080807e-018 -0.076501387595747095
    0.10818929987826627 1.0809208488349442e-018 2.5592473472170423e-017
    0.07650138759574697 -3.603438123638187e-018 0.076501387595747039
    -2.6307736542650753e-017 -5.5437631410606536e-018 0.10818929987826631
    -0.076501387595747053 -3.603438123638187e-018 0.076501387595747039
    -0.10818929987826638 1.0809208488349446e-018 1.9350179508710655e-017
    -0.076501387595747081 5.7652798213080746e-018 -0.076501387595746984
    -8.9268237018428043e-017 7.705604838730545e-018 -0.10818929987826631
    0.076501387595746942 5.7652798213080807e-018 -0.076501387595747095
    0.10818929987826627 1.0809208488349442e-018 2.5592473472170423e-017
    0.07650138759574697 -3.603438123638187e-018 0.076501387595747039
    0.05437916940658561 0.069127314866026593 -0.054379169406585694
    0.07690375888537751 0.069127314866026593 2.7115415356856617e-017
    0.05437916940658561 0.069127314866026593 0.054379169406585673
    -3.6232924405262285e-017 0.069127314866026593 0.076903758885377552
    -0.054379169406585694 0.069127314866026593 0.054379169406585673
    -0.076903758885377593 0.069127314866026593 1.3296641894140096e-017
    -0.054379169406585701 0.069127314866026593 -0.054379169406585652
    -7.1605291136055209e-017 0.069127314866026593 -0.076903758885377552
    0.05437916940658561 0.069127314866026593 -0.054379169406585694
    0.07690375888537751 0.069127314866026593 2.7115415356856617e-017
    0.05437916940658561 0.069127314866026593 0.054379169406585673
    0.017635918748742197 0.08821629576465552 -0.017635918748742246
    0.024940955479381181 0.08821629576465552 1.7287662837752351e-017
    0.017635918748742194 0.08821629576465552 0.017635918748742256
    -4.6222163886024846e-017 0.08821629576465552 0.02494095547938123
    -0.017635918748742291 0.08821629576465552 0.017635918748742246
    -0.024940955479381275 0.08821629576465552 3.876379023114005e-018
    -0.017635918748742284 0.08821629576465552 -0.017635918748742239
    -4.876424900065995e-017 0.08821629576465552 -0.024940955479381226
    0.017635918748742197 0.08821629576465552 -0.017635918748742246
    0.024940955479381181 0.08821629576465552 1.7287662837752351e-017
    0.017635918748742194 0.08821629576465552 0.017635918748742256
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018
    -2.9059573666051149e-017 0.088216295764655561 -1.4820026184809732e-018;""")
    return handleParent, handleShape

#def createRawHandleSegment(modHandleColour):
def createRawSegmentCurve(modHandleColour):
    segment = cmds.createNode('transform', name='segmentCurve')
    cmds.setAttr(segment+'.translateX', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.translateY', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.translateZ', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.rotateX', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.rotateY', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.rotateZ', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.scaleX', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.scaleY', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.scaleZ', channelBox=False, keyable=False)
    cmds.setAttr(segment+'.visibility', channelBox=False, keyable=False)

    segmentShape = cmds.createNode('nurbsCurve', name='segmentCurveShape', parent='segmentCurve')
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', modHandleColour)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 1 0 no 3
    2 0 1
    2
    -1 0 0
    1 0 0;""")
    startCluster = cmds.cluster(segment+'.cv[0]', relative=True, name='segmentCurve_startCluster')
    cmds.setAttr(startCluster[1]+'.visibility', 0)
    endCluster = cmds.cluster(segment+'.cv[1]', relative=True, name='segmentCurve_endCluster')
    cmds.setAttr(endCluster[1]+'.visibility', 0)

    startPosLocator = cmds.spaceLocator(name='segmentCurve_startLocator')[0]
    cmds.setAttr(startPosLocator + '.visibility', 0)
    tempConstraint = cmds.pointConstraint(startCluster[1], startPosLocator, maintainOffset=False)
    cmds.delete(tempConstraint)
    startClusterOnLocatorConstraint = cmds.pointConstraint(startPosLocator, startCluster[1], maintainOffset=False, name='startClusterOnLocator_pointConstraint')[0]
    endPosLocator = cmds.spaceLocator(name='segmentCurve_endLocator')[0]
    cmds.setAttr(endPosLocator + '.visibility', 0)
    tempConstraint = cmds.pointConstraint(endCluster[1], endPosLocator, maintainOffset=False)
    cmds.delete(tempConstraint)
    endClusterOnLocatorConstraint = cmds.pointConstraint(endPosLocator, endCluster[1], maintainOffset=False, name='endClusterOnLocator_pointConstraint')[0]
    # Collect nodes and remove unnecessary ones.
    nodes = cmds.listConnections(segmentShape, source=True, destination=True)[1:]
    i = 0
    for node in nodes:
        if cmds.nodeType(node) == 'tweak':
            cmds.delete(node)
            nodes.pop(i)
            break
        i += 1
    return segmentShape, segment, startCluster, endCluster, nodes, startPosLocator, endPosLocator, startClusterOnLocatorConstraint, endClusterOnLocatorConstraint

def createRawOrientationRepresentation(aimAxis):
    if aimAxis == 'X':
        representationTransformGroup = cmds.createNode('transform', name='orient_repr_transformGrp')
        representationTransform = cmds.createNode('transform', name='orient_repr_transform', parent='orient_repr_transformGrp')
        cmds.setAttr(representationTransform+'.translateX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.translateY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.translateZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.rotateY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.rotateZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.visibility', channelBox=False, keyable=False)
        cmds.setAttr('.rotatePivot', 0.090148619726501789, 0, 0, type='double3')
        cmds.setAttr('.scalePivot', 0.090148619726501789, 0, 0, type='double3')
        cmds.createNode('nurbsCurve', name='orient_repr_transform_Z_Shape', parent='orient_repr_transform')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 6)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 9 0 no 3
    10 0 1 1.1037066419999999 2 3 4 5 5.8686654909999998 6 7
    10
    0.090148619726501789 -9.4980217064741782e-017 0.046853382922080015
    1.0900000000000005 -1.0601068923886548e-016 0.046853382922080015
    1.0900000000000005 -9.0994236442105678e-017 0.38998523316589778
    0.090148619726500567 3.8786717245087916e-017 0.38998523316589778
    0.090148619726501789 -9.4980217064741782e-017 0.046853382922080015
    0.090148619726501955 -1.2726306795036011e-016 -0.046853382922077899
    0.090148619726502399 -2.2942823653755231e-016 -0.13193723316589548
    1.0900000000000005 -1.3109908967656421e-016 -0.13193723316589548
    1.0900000000000005 -1.1623259577623636e-016 -0.046853382922077899
    0.090148619726501955 -1.2726306795036011e-016 -0.046853382922077899;""")
        cmds.createNode('nurbsCurve', name='orient_repr_transform_Y_Shape', parent='orient_repr_transform')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 14)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 9 0 no 3
    10 0 1 1.160105749 2 3 4 5 5.8718532330000004 6 7
    10
    0.090148619726501789 -0.046853382922079072 1.0671197962702776e-015
    1.0900000000000005 -0.046853382922079072 3.8749495902726663e-015
    1.0900000000000005 -0.13193723316589662 1.0907069651407325e-015
    0.090148619726501789 -0.13193723316589662 1.0907069651407325e-015
    0.090148619726501789 -0.046853382922079072 1.0671197962702776e-015
    0.090148619726501789 0.04685338292207885 1.0556440271853279e-015
    0.090148619726501789 0.38998523316589651 1.0004550925922358e-015
    1.0900000000000005 0.38998523316589651 1.0004550925922358e-015
    1.0900000000000005 0.04685338292207885 3.8713159508693073e-015
    0.090148619726501789 0.04685338292207885 1.0556440271853279e-015;""")
    if aimAxis == 'Z':
        representationTransformGroup = cmds.createNode('transform', name='orient_repr_transformGrp')
        representationTransform = cmds.createNode('transform', name='orient_repr_transform', parent='orient_repr_transformGrp')
        cmds.setAttr(representationTransform+'.translateX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.translateY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.translateZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.rotateY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.rotateX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.visibility', channelBox=False, keyable=False)
        cmds.setAttr('.rotatePivot', 0, 0, 0.090148619726501789, type='double3')
        cmds.setAttr('.scalePivot', 0, 0, 0.090148619726501789, type='double3')
        cmds.createNode('nurbsCurve', name='orient_repr_transform_Y_Shape', parent='orient_repr_transform')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 14)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 9 0 no 3
    10 0 1 1.1037066419999999 2 3 4 5 5.8686654909999998 6 7
    10
    -5.7939669562224841e-017 0.04685338292208005 0.090148619726501789
    1.6977221747904518e-016 0.046853382922080286 1.0901486197265018
    1.8478867027580499e-016 0.38998523316589784 1.0901486197265018
    7.5827264747604857e-017 0.38998523316589778 0.090148619726500234
    -5.7939669562224841e-017 0.04685338292208005 0.090148619726501789
    -9.0222520447843095e-017 -0.046853382922077864 0.090148619726501955
    -1.9238768903503519e-016 -0.13193723316589548 0.090148619726502677
    1.4468381704134653e-016 -0.13193723316589528 1.0901486197265018
    1.595503109416743e-016 -0.046853382922077615 1.0901486197265018
    -9.0222520447843095e-017 -0.046853382922077864 0.090148619726501955;""")
        cmds.createNode('nurbsCurve', name='orient_repr_transform_X_Shape', parent='orient_repr_transform')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 13)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 9 0 no 3
    10 0 1 1.160105749 2 3 4 5 5.8718532330000004 6 7
    10
    -0.04685338292207903 1.1041603437727941e-015 0.090148619726501844
    -0.046853382922078801 4.1507324969905799e-015 1.0901486197265018
    -0.13193723316589637 1.3664898718586425e-015 1.0901486197265018
    -0.13193723316589662 1.1277475126432491e-015 0.090148619726502122
    -0.04685338292207903 1.1041603437727941e-015 0.090148619726501844
    0.046853382922078878 1.092684574687845e-015 0.090148619726501844
    0.38998523316589651 1.0374956400947524e-015 0.090148619726501511
    0.38998523316589673 1.2762379993101458e-015 1.0901486197265018
    0.04685338292207912 4.1470988575872177e-015 1.0901486197265018
    0.046853382922078878 1.092684574687845e-015 0.090148619726501844;""")
    if aimAxis == 'Y':
        representationTransformGroup = cmds.createNode('transform', name='orient_repr_transformGrp')
        representationTransform = cmds.createNode('transform', name='orient_repr_transform', parent='orient_repr_transformGrp')
        cmds.setAttr(representationTransform+'.translateX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.translateY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.translateZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.rotateX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.rotateZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleX', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleY', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.scaleZ', channelBox=False, keyable=False)
        cmds.setAttr(representationTransform+'.visibility', channelBox=False, keyable=False)
        cmds.setAttr('.rotatePivot', 0, 0.090148619726501789, 0, type='double3')
        cmds.setAttr('.scalePivot', 0, 0.090148619726501789, 0, type='double3')
        cmds.createNode('nurbsCurve', name='orient_repr_transform_Z_Shape', parent='orient_repr_transform')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 6)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 9 0 no 3
    10 0 1 1.1037066419999999 2 3 4 5 5.8686654909999998 6 7
    10
    -5.7939669562224841e-017 0.090148619726501789 0.046853382922080015
    1.6977221747904518e-016 1.0901486197265018 0.046853382922080015
    1.8478867027580499e-016 1.0901486197265018 0.38998523316589778
    7.5827264747604857e-017 0.090148619726500678 0.38998523316589778
    -5.7939669562224841e-017 0.090148619726501789 0.046853382922080015
    -9.0222520447843095e-017 0.090148619726501955 -0.046853382922077899
    -1.9238768903503519e-016 0.09014861972650251 -0.13193723316589548
    1.4468381704134653e-016 1.0901486197265018 -0.13193723316589548
    1.595503109416743e-016 1.0901486197265018 -0.046853382922077899
    -9.0222520447843095e-017 0.090148619726501955 -0.046853382922077899;""")
        cmds.createNode('nurbsCurve', name='orient_repr_transform_X_Shape', parent='orient_repr_transform')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 13)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 9 0 no 3
    10 0 1 1.160105749 2 3 4 5 5.8718532330000004 6 7
    10
    -0.04685338292207903 0.090148619726501844 1.0671197962702776e-015
    -0.046853382922078801 1.0901486197265018 3.8749495902726679e-015
    -0.13193723316589637 1.0901486197265018 1.0907069651407325e-015
    -0.13193723316589662 0.090148619726502122 1.0907069651407325e-015
    -0.04685338292207903 0.090148619726501844 1.0671197962702776e-015
    0.046853382922078878 0.090148619726501844 1.0556440271853279e-015
    0.38998523316589651 0.090148619726501511 1.0004550925922358e-015
    0.38998523316589673 1.0901486197265018 1.0004550925922358e-015
    0.04685338292207912 1.0901486197265018 3.8713159508693073e-015
    0.046853382922078878 0.090148619726501844 1.0556440271853279e-015;""")
    cmds.select(clear=True)

    return representationTransform, representationTransformGroup

def createRawSingleOrientationRepresentation():
    orientationTransform = cmds.createNode('transform', name='single_orient_repr_transform')
    cmds.setAttr(orientationTransform+'.translateX', keyable=False)
    cmds.setAttr(orientationTransform+'.translateY', keyable=False)
    cmds.setAttr(orientationTransform+'.translateZ', keyable=False)
    cmds.setAttr(orientationTransform+'.scaleX', keyable=False)
    cmds.setAttr(orientationTransform+'.scaleY', keyable=False)
    cmds.setAttr(orientationTransform+'.scaleZ', keyable=False)
    cmds.setAttr(orientationTransform+'.visibility', keyable=False)

    cmds.createNode('nurbsCurve', name='single_orient_repr_transform_Y_Shape', parent='single_orient_repr_transform')
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 14)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 9.5534973206283634e-018 0
    0 0.53492264104395215 0
    0 0.53492264104395215 0.047224379365857772
    0 0.69028345367286037 0
    0 0.53492264104395215 -0.047224379365857772
    0 0.53492264104395215 0
    0.047224379365857772 0.53492264104395215 0
    0 0.69028345367286037 0
    -0.047224379365857772 0.53492264104395215 0
    0 0.53492264104395215 0.047224379365857772
    0.047224379365857772 0.53492264104395215 0
    0 0.53492264104395215 -0.047224379365857772
    -0.047224379365857772 0.53492264104395215 0
    0 0.53492264104395215 0;""")
    cmds.createNode('nurbsCurve', name='single_orient_repr_transform_X_Shape', parent='single_orient_repr_transform')
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 13)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    9.5534973206283634e-018 2.1213025382112701e-033 0
    0.53492264104395215 1.9469912278619913e-016 0
    0.53492264104395215 1.9469912278619913e-016 0.047224379365857772
    0.69028345367286037 2.5355003523434651e-016 0
    0.53492264104395215 1.9469912278619913e-016 -0.047224379365857772
    0.53492264104395215 1.9469912278619913e-016 0
    0.53492264104395215 -0.04722437936585757 0
    0.69028345367286037 2.5355003523434651e-016 0
    0.53492264104395215 0.04722437936585798 0
    0.53492264104395215 1.9469912278619913e-016 0.047224379365857772
    0.53492264104395215 -0.04722437936585757 0
    0.53492264104395215 1.9469912278619913e-016 -0.047224379365857772
    0.53492264104395215 0.04722437936585798 0
    0.53492264104395215 1.9469912278619913e-016 0;""")
    cmds.createNode('nurbsCurve', name='single_orient_repr_transform_Z_Shape', parent='single_orient_repr_transform')
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 6)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    5.3032563455281761e-034 -2.1213025382112701e-033 9.5534973206283649e-018
    4.4336584227826986e-017 -1.9367910538232478e-016 0.53492264104395248
    -0.047224379365857744 -2.172724223653486e-016 0.53492264104395248
    6.3907925851379713e-017 -2.5146836706317446e-016 0.69028345367286092
    0.04722437936585782 -1.70085788399301e-016 0.53492264104395248
    4.4336584227826986e-017 -1.9367910538232478e-016 0.53492264104395248
    6.0065462216509521e-017 -0.047224379365857987 0.53492264104395248
    6.3907925851379713e-017 -2.5146836706317446e-016 0.69028345367286092
    2.8607706239144452e-017 0.047224379365857577 0.53492264104395248
    -0.047224379365857744 -2.172724223653486e-016 0.53492264104395248
    6.0065462216509521e-017 -0.047224379365857987 0.53492264104395248
    0.04722437936585782 -1.70085788399301e-016 0.53492264104395248
    2.8607706239144452e-017 0.047224379365857577 0.53492264104395248
    4.4336584227826986e-017 -1.9367910538232478e-016 0.53492264104395248;""")
    return orientationTransform

def createRawHierarchyRepresentation(aimAxis):
    if aimAxis == 'X':
        hierarchyRepresentation = cmds.createNode('transform', name='hierarchy_repr')
        cmds.createNode('nurbsCurve', name='hierarchy_reprShape', parent='hierarchy_repr')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 13)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 11 0 no 3
    12 12 13 14 15 16 17 18 19 20 21 22 23
    12
    0.11913113568119799 0 0
    -0.08799383886043731 0.039018907513668655 0.039018907513668655
    -0.08799383886043731 0.039018907513668655 -0.039018907513668655
    0.11913113568119799 0 0
    -0.08799383886043731 0.039018907513668655 -0.039018907513668655
    -0.08799383886043731 -0.039018907513668655 -0.039018907513668655
    0.11913113568119799 0 0
    -0.08799383886043731 -0.039018907513668655 -0.039018907513668655
    -0.08799383886043731 -0.039018907513668655 0.039018907513668655
    0.11913113568119799 0 0
    -0.08799383886043731 -0.039018907513668655 0.039018907513668655
    -0.08799383886043731 0.039018907513668655 0.039018907513668655;""")
    if aimAxis == 'Y':
        hierarchyRepresentation = cmds.createNode('transform', name='hierarchy_repr')
        cmds.createNode('nurbsCurve', name='hierarchy_reprShape', parent='hierarchy_repr')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 14)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 11 0 no 3
    12 12 13 14 15 16 17 18 19 20 21 22 23
    12
    4.0242110249429071e-017 0.11913121635934004 0
    -0.039018907513668655 -0.087993758182295295 0.039018907513668655
    -0.039018907513668655 -0.087993758182295295 -0.039018907513668655
    4.0242110249429071e-017 0.11913121635934004 0
    -0.039018907513668655 -0.087993758182295295 -0.039018907513668655
    0.039018907513668655 -0.087993758182295295 -0.039018907513668655
    4.0242110249429071e-017 0.11913121635934004 0
    0.039018907513668655 -0.087993758182295295 -0.039018907513668655
    0.039018907513668655 -0.087993758182295295 0.039018907513668655
    4.0242110249429071e-017 0.11913121635934004 0
    0.039018907513668655 -0.087993758182295295 0.039018907513668655
    -0.039018907513668655 -0.087993758182295295 0.039018907513668655;""")
    if aimAxis == 'Z':
        hierarchyRepresentation = cmds.createNode('transform', name='hierarchy_repr')
        cmds.createNode('nurbsCurve', name='hierarchy_reprShape', parent='hierarchy_repr')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 6)
        mel.eval("""setAttr ".cached" -type "nurbsCurve"
        1 11 0 no 3
    12 12 13 14 15 16 17 18 19 20 21 22 23
    12
    4.0242110249429071e-017 0 0.11913121635934004
    -0.039018907513668655 0.039018907513668655 -0.087993758182295295
    0.039018907513668655 0.039018907513668655 -0.087993758182295309
    4.0242110249429071e-017 0 0.11913121635934004
    0.039018907513668655 0.039018907513668655 -0.087993758182295309
    0.039018907513668655 -0.039018907513668655 -0.087993758182295295
    4.0242110249429071e-017 0 0.11913121635934004
    0.039018907513668655 -0.039018907513668655 -0.087993758182295295
    -0.039018907513668655 -0.039018907513668655 -0.087993758182295295
    4.0242110249429071e-017 0 0.11913121635934004
    -0.039018907513668655 -0.039018907513668655 -0.087993758182295295
    -0.039018907513668655 0.039018907513668655 -0.087993758182295295;""")

    cmds.setAttr(hierarchyRepresentation+'.translateX', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.translateY', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.translateZ', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.rotateX', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.rotateY', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.rotateZ', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.scaleX', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.scaleY', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.scaleZ', channelBox=False, keyable=False)
    cmds.setAttr(hierarchyRepresentation+'.visibility', channelBox=False, keyable=False)

    return hierarchyRepresentation

def createRawSplineAdjustCurveTransform(modHandleColour):
    splineAdjustCurvePreTransform = cmds.createNode('transform', name='spline_adjustCurve_preTransform')
    splineAdjustCurveTransform = cmds.createNode('transform', name='spline_adjustCurve_transform', parent='spline_adjustCurve_preTransform')
    cmds.setAttr('.rotateX', keyable=False)
    cmds.setAttr('.rotateY', keyable=False)
    cmds.setAttr('.rotateZ', keyable=False)
    cmds.setAttr('.scaleX', keyable=False)
    cmds.setAttr('.scaleY', keyable=False)
    cmds.setAttr('.scaleZ', keyable=False)
    cmds.setAttr('.visibility', keyable=False)
    cmds.createNode('nurbsCurve', name='spline_adjustCurve_transformShape', parent='spline_adjustCurve_transform')
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', modHandleColour)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 16 0 no 3
    17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    17
    -0.29294999999999999 0.29294999999999999 0.29294999999999999
    -0.29294999999999999 0.29294999999999999 -0.29294999999999999
    0.29294999999999999 0.29294999999999999 -0.29294999999999999
    0.29294999999999999 0.29294999999999999 0.29294999999999999
    -0.29294999999999999 0.29294999999999999 0.29294999999999999
    -0.29294999999999999 -0.29294999999999999 0.29294999999999999
    -0.29294999999999999 -0.29294999999999999 -0.29294999999999999
    -0.29294999999999999 0.29294999999999999 -0.29294999999999999
    -0.29294999999999999 0.29294999999999999 0.29294999999999999
    -0.29294999999999999 -0.29294999999999999 0.29294999999999999
    0.29294999999999999 -0.29294999999999999 0.29294999999999999
    0.29294999999999999 0.29294999999999999 0.29294999999999999
    0.29294999999999999 0.29294999999999999 -0.29294999999999999
    0.29294999999999999 -0.29294999999999999 -0.29294999999999999
    0.29294999999999999 -0.29294999999999999 0.29294999999999999
    0.29294999999999999 -0.29294999999999999 -0.29294999999999999
    -0.29294999999999999 -0.29294999999999999 -0.29294999999999999;""")
    return splineAdjustCurvePreTransform, splineAdjustCurveTransform

def createRawLocalAxesInfoRepresentation():
    axesInfoPreTransform = cmds.createNode('transform', name='localAxesInfoRepr_preTransform')
    axesInfoTransform = cmds.createNode('transform', name='localAxesInfoRepr', parent=axesInfoPreTransform)
    cmds.setAttr('.translateX', keyable=False)
    cmds.setAttr('.translateY', keyable=False)
    cmds.setAttr('.translateZ', keyable=False)
    cmds.setAttr('.rotateX', keyable=False)
    cmds.setAttr('.rotateY', keyable=False)
    cmds.setAttr('.rotateZ', keyable=False)
    cmds.setAttr('.scaleX', keyable=False)
    cmds.setAttr('.scaleY', keyable=False)
    cmds.setAttr('.scaleZ', keyable=False)
    cmds.setAttr('.visibility', keyable=False)
    cmds.createNode('nurbsCurve', name='localAxesInfoRepr_XShape', parent=axesInfoTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 13)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 1 0 no 3
    2 0 0.27750632000000003
    2
    -2.8101674601366001e-018 0 0
    0.83251896000000003 0 0;""")
    cmds.createNode('nurbsCurve', name='localAxesInfoRepr_ZShape', parent=axesInfoTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 6)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 1 0 no 3
    2 0 0.27750632000000003
    2
    0 0 -2.6450977786373555e-018
    0 0 0.83251896000000003;""")
    cmds.createNode('nurbsCurve', name='localAxesInfoRepr_YShape', parent=axesInfoTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 14)
    mel.eval("""setAttr ".cached" -type "nurbsCurve"
    1 1 0 no 3
    2 0 0.27750632000000003
    2
    0 -2.6450977786373555e-018 0
    0 0.83251896000000003 0;""")
    return axesInfoPreTransform, axesInfoTransform

def createRawIKPreferredRotationRepresentation(planeAxis):
    representationTransform = cmds.createNode('transform', name='IKPreferredRotationRepr')
    cmds.setAttr('.visibility', keyable=False)
    cmds.setAttr('.translateX', keyable=False)
    cmds.setAttr('.translateY', keyable=False)
    cmds.setAttr('.translateZ', keyable=False)
    cmds.setAttr('.rotateX', keyable=False)
    cmds.setAttr('.rotateY', keyable=False)
    cmds.setAttr('.rotateZ', keyable=False)
    cmds.setAttr('.scaleX', keyable=False)
    cmds.setAttr('.scaleY', keyable=False)
    cmds.setAttr('.scaleZ', keyable=False)
    shape = cmds.createNode('nurbsCurve', name='IKPreferredRotationReprShape', parent='IKPreferredRotationRepr')
    cmds.setAttr('.overrideEnabled', 1)
    mel.eval('''setAttr ".cached" -type "nurbsCurve"
    1 20 0 no 3
    21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    21
    -5.933301304234077e-017 -0.8196523338708297 -0.16995377878159712
    0.037052933986026118 -0.57727861871207187 -0.3753288626559228
    0.037052933986026104 -0.53629233322044922 -0.31358886685160847
    -5.933301304234077e-017 -0.8196523338708297 -0.16995377878159712
    0.037052933986026104 -0.53629233322044922 -0.31358886685160847
    -0.037052933986026125 -0.53629233322044922 -0.31358886685160847
    -5.933301304234077e-017 -0.8196523338708297 -0.16995377878159712
    -0.037052933986026125 -0.53629233322044922 -0.31358886685160847
    -0.037052933986026118 -0.57727861871207187 -0.3753288626559228
    -5.933301304234077e-017 -0.8196523338708297 -0.16995377878159712
    0.037052933986026118 -0.57727861871207187 -0.3753288626559228
    -0.037052933986026118 -0.57727861871207187 -0.3753288626559228
    -5.933301304234077e-017 -0.8196523338708297 -0.16995377878159712
    1.7072382561844779e-018 -0.46477959092505339 -0.40337892728023189
    3.2444088541761336e-017 -0.28656127878590931 -0.49477323356383185
    5.9528147047218323e-017 -0.092474160503183384 -0.544218858508281
    8.1601271192348766e-017 0.10774937215831795 -0.5492361639295601
    9.7556669387883563e-017 0.30406946737751767 -0.50957376854894876
    1.0659425397617707e-016 0.48664160211539348 -0.42722055366090267
    1.0826081917185999e-016 0.64631094377478027 -0.30630578763334904
    1.0247283011593438e-016 0.77507104434528862 -0.15289287258426201;''')
    if planeAxis == 'X':
        cmds.setAttr(shape+'.overrideColor', 13)
    if planeAxis == 'Y':
        cmds.setAttr(shape+'.overrideColor', 14)
    if planeAxis == 'Z':
        cmds.setAttr(shape+'.overrideColor', 6)
    return representationTransform

def createRawIKhingeAxisRepresenation(upFrontAxes):
    representationTransform = cmds.createNode('transform', name='IKhingeAxisRepresenation')
    cmds.setAttr('.visibility', keyable=False)
    cmds.setAttr('.translateX', keyable=False)
    cmds.setAttr('.translateY', keyable=False)
    cmds.setAttr('.translateZ', keyable=False)
    cmds.setAttr('.rotateX', keyable=False)
    cmds.setAttr('.rotateY', keyable=False)
    cmds.setAttr('.rotateZ', keyable=False)
    cmds.setAttr('.scaleX', keyable=False)
    cmds.setAttr('.scaleY', keyable=False)
    cmds.setAttr('.scaleZ', keyable=False)

    if upFrontAxes == 'XY':
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_upAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 13)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    3.1844991068761211e-018 -5.5153865993493004e-032 3.8998866381233926e-034
    0.1833075470146506 -4.9696062558958713e-015 3.4864043427905886e-017
    0.18330754701465093 0.022487799698022545 3.7103376835482072e-017
    0.24509448455762009 -6.558300335963865e-015 4.628119664684413e-017
    0.18330754701465021 -0.022487799698032485 3.2624710020329707e-017
    0.1833075470146506 -4.9696062558958713e-015 3.4864043427905886e-017
    0.1833075470146506 -4.9718455893034458e-015 0.022487799698027552
    0.24509448455762009 -6.558300335963865e-015 4.628119664684413e-017
    0.1833075470146506 -4.9673669224882936e-015 -0.022487799698027479
    0.18330754701465093 0.022487799698022545 3.7103376835482072e-017
    0.1833075470146506 -4.9718455893034458e-015 0.022487799698027552
    0.18330754701465021 -0.022487799698032485 3.2624710020329707e-017
    0.1833075470146506 -4.9673669224882936e-015 -0.022487799698027479
    0.1833075470146506 -4.9696062558958713e-015 3.4864043427905886e-017;''')
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_hingeAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 14)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 0 0
    4.9822732899003667e-015 0.18330754701465063 9.2048991537858521e-017
    -0.022487799698022535 0.18330754701465105 9.5536648595330133e-017
    6.577521309743155e-015 0.24509448455762031 1.2136438139527227e-016
    0.022487799698032499 0.18330754701465027 8.8561334480386921e-017
    4.9822732899003667e-015 0.18330754701465063 9.2048991537858521e-017
    4.982015976008152e-015 0.18330754701465063 0.022487799698027611
    6.577521309743155e-015 0.24509448455762031 1.2136438139527227e-016
    4.9825306037925821e-015 0.18330754701465063 -0.022487799698027427
    -0.022487799698022535 0.18330754701465105 9.5536648595330133e-017
    4.982015976008152e-015 0.18330754701465063 0.022487799698027611
    0.022487799698032499 0.18330754701465027 8.8561334480386921e-017
    4.9825306037925821e-015 0.18330754701465063 -0.022487799698027427
    4.9822732899003667e-015 0.18330754701465063 9.2048991537858521e-017;''')

    if upFrontAxes == 'XZ':
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_upAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 13)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    3.1844991068761211e-018 -3.8998866381235149e-034 -5.5153865993493004e-032
    0.2133075470146506 -3.4864043427906305e-017 -4.9696062558958713e-015
    0.21330754701465093 -3.2110082235900743e-017 0.022487799698022542
    0.27509448455762009 -4.6281196646845375e-017 -6.558300335963865e-015
    0.21330754701465021 -3.7618004619911899e-017 -0.022487799698032485
    0.2133075470146506 -3.4864043427906305e-017 -4.9696062558958713e-015
    0.2133075470146506 -0.022487799698027552 -4.9668522947038658e-015
    0.27509448455762009 -4.6281196646845375e-017 -6.558300335963865e-015
    0.2133075470146506 0.022487799698027482 -4.972360217087876e-015
    0.21330754701465093 -3.2110082235900743e-017 0.022487799698022542
    0.2133075470146506 -0.022487799698027552 -4.9668522947038658e-015
    0.21330754701465021 -3.7618004619911899e-017 -0.022487799698032485
    0.2133075470146506 0.022487799698027482 -4.972360217087876e-015
    0.2133075470146506 -3.4864043427906305e-017 -4.9696062558958713e-015;''')
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_hingeAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 6)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 0 0
    4.9822732899003675e-015 -3.0181480758971098e-017 0.21330754701465066
    -0.022487799698022535 -3.3669137816442624e-017 0.21330754701465104
    6.577521309743155e-015 -3.8235481764604839e-017 0.27509448455762031
    0.022487799698032499 -2.6693823701499569e-017 0.21330754701465029
    4.9822732899003675e-015 -3.0181480758971098e-017 0.21330754701465066
    4.982015976008152e-015 -0.022487799698027552 0.21330754701465066
    6.577521309743155e-015 -3.8235481764604839e-017 0.27509448455762031
    4.9825306037925813e-015 0.022487799698027486 0.21330754701465066
    -0.022487799698022535 -3.3669137816442624e-017 0.21330754701465104
    4.982015976008152e-015 -0.022487799698027552 0.21330754701465066
    0.022487799698032499 -2.6693823701499569e-017 0.21330754701465029
    4.9825306037925813e-015 0.022487799698027486 0.21330754701465066
    4.9822732899003675e-015 -3.0181480758971098e-017 0.21330754701465066;''')

    if upFrontAxes == 'YX':
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_upAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 14)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    -5.4446765147422574e-032 3.1844991068761211e-018 5.3775215342692907e-048
    -4.9036170421380627e-015 0.2133075470146506 1.8987071918683015e-031
    0.022487799698022611 0.21330754701465093 -2.2393334075759462e-018
    -6.4730897681620263e-015 0.27509448455762009 5.4248776910522902e-031
    -0.022487799698032416 0.21330754701465021 2.2393334075763267e-018
    -4.9036170421380627e-015 0.2133075470146506 1.8987071918683015e-031
    -4.9058563755456388e-015 0.2133075470146506 -0.02248779969802751
    -6.4730897681620263e-015 0.27509448455762009 5.4248776910522902e-031
    -4.9013777087304857e-015 0.2133075470146506 0.02248779969802751
    0.022487799698022611 0.21330754701465093 -2.2393334075759462e-018
    -4.9058563755456388e-015 0.2133075470146506 -0.02248779969802751
    -0.022487799698032416 0.21330754701465021 2.2393334075763267e-018
    -4.9013777087304857e-015 0.2133075470146506 0.02248779969802751
    -4.9036170421380627e-015 0.2133075470146506 1.8987071918683015e-031;''')
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_hingeAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 13)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 0 0
    0.21330754701465066 4.9208637461191366e-015 -9.2048991537858274e-017
    0.21330754701465104 -0.022487799698022594 -9.8290609787335529e-017
    0.27509448455762031 6.4943924101124858e-015 -1.2136438139527158e-016
    0.21330754701465029 0.022487799698032444 -8.5807373288381056e-017
    0.21330754701465066 4.9208637461191366e-015 -9.2048991537858274e-017
    0.21330754701465066 4.9233603934189282e-015 -0.022487799698027611
    0.27509448455762031 6.4943924101124858e-015 -1.2136438139527158e-016
    0.21330754701465066 4.9183670988193466e-015 0.022487799698027427
    0.21330754701465104 -0.022487799698022594 -9.8290609787335529e-017
    0.21330754701465066 4.9233603934189282e-015 -0.022487799698027611
    0.21330754701465029 0.022487799698032444 -8.5807373288381056e-017
    0.21330754701465066 4.9183670988193466e-015 0.022487799698027427
    0.21330754701465066 4.9208637461191366e-015 -9.2048991537858274e-017;''')

    if upFrontAxes == 'YZ':
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_upAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 14)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 3.1844991068761211e-018 0
    0 0.21330754701465066 0
    0 0.21330754701465066 0.02248779969802751
    0 0.27509448455762009 0
    0 0.21330754701465066 -0.02248779969802751
    0 0.21330754701465066 0
    0.02248779969802751 0.21330754701465066 0
    0 0.27509448455762009 0
    -0.02248779969802751 0.21330754701465066 0
    0 0.21330754701465066 0.02248779969802751
    0.02248779969802751 0.21330754701465066 0
    0 0.21330754701465066 -0.02248779969802751
    -0.02248779969802751 0.21330754701465066 0
    0 0.21330754701465066 0;''')
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_hingeAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 6)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 0 0
    6.3976934525675222e-017 1.5165035809901886e-017 0.21330754701465077
    7.0218552775152415e-017 -0.022487799698027503 0.21330754701465077
    8.3822789021058156e-017 2.1302641950459881e-017 0.27509448455762031
    5.7735316276198029e-017 0.022487799698027531 0.21330754701465077
    6.3976934525675222e-017 1.5165035809901886e-017 0.21330754701465077
    0.022487799698027586 1.7661683109692766e-017 0.21330754701465077
    8.3822789021058156e-017 2.1302641950459881e-017 0.27509448455762031
    -0.022487799698027451 1.2668388510111013e-017 0.21330754701465077
    7.0218552775152415e-017 -0.022487799698027503 0.21330754701465077
    0.022487799698027586 1.7661683109692766e-017 0.21330754701465077
    5.7735316276198029e-017 0.022487799698027531 0.21330754701465077
    -0.022487799698027451 1.2668388510111013e-017 0.21330754701465077
    6.3976934525675222e-017 1.5165035809901886e-017 0.21330754701465077;''')

    if upFrontAxes == 'ZX':
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_upAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 6)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    -5.4446765147422574e-032 3.8998866381234473e-034 3.1844991068761211e-018
    -4.9036170421380627e-015 3.4864043427906083e-017 0.2133075470146506
    0.022487799698022611 3.4864043427906133e-017 0.21330754701465093
    -6.4730897681620263e-015 4.6281196646844697e-017 0.27509448455762009
    -0.022487799698032416 3.4864043427906034e-017 0.21330754701465021
    -4.9036170421380627e-015 3.4864043427906083e-017 0.2133075470146506
    -4.9036170421380627e-015 0.022487799698027552 0.2133075470146506
    -6.4730897681620263e-015 4.6281196646844697e-017 0.27509448455762009
    -4.9036170421380627e-015 -0.022487799698027482 0.2133075470146506
    0.022487799698022611 3.4864043427906133e-017 0.21330754701465093
    -4.9036170421380627e-015 0.022487799698027552 0.2133075470146506
    -0.022487799698032416 3.4864043427906034e-017 0.21330754701465021
    -4.9036170421380627e-015 -0.022487799698027482 0.2133075470146506
    -4.9036170421380627e-015 3.4864043427906083e-017 0.2133075470146506;''')
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_hingeAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 13)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 0 0
    0.21330754701465066 6.3976934525675456e-017 4.9208637461191366e-015
    0.21330754701465104 6.7464591583147056e-017 -0.022487799698022594
    0.27509448455762031 8.382278902105881e-017 6.4943924101124858e-015
    0.21330754701465029 6.0489277468203881e-017 0.022487799698032444
    0.21330754701465066 6.3976934525675456e-017 4.9208637461191366e-015
    0.21330754701465066 0.022487799698027586 4.9206064322269235e-015
    0.27509448455762031 8.382278902105881e-017 6.4943924101124858e-015
    0.21330754701465066 -0.022487799698027451 4.9211210600113505e-015
    0.21330754701465104 6.7464591583147056e-017 -0.022487799698022594
    0.21330754701465066 0.022487799698027586 4.9206064322269235e-015
    0.21330754701465029 6.0489277468203881e-017 0.022487799698032444
    0.21330754701465066 -0.022487799698027451 4.9211210600113505e-015
    0.21330754701465066 6.3976934525675456e-017 4.9208637461191366e-015;''')

    if upFrontAxes == 'ZY':
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_upAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 6)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    -6.5550809943282608e-048 -5.3739664301352177e-032 3.1844991068761211e-018
    -2.3144824893577097e-031 -4.8396401076123877e-015 0.2133075470146506
    2.7539611920053893e-018 0.022487799698022677 0.21330754701465093
    -6.612807112450601e-031 -6.3892669791409687e-015 0.27509448455762009
    -2.7539611920058527e-018 -0.022487799698032346 0.21330754701465021
    -2.3144824893577097e-031 -4.8396401076123877e-015 0.2133075470146506
    -0.02248779969802751 -4.8368861464203814e-015 0.2133075470146506
    -6.612807112450601e-031 -6.3892669791409687e-015 0.27509448455762009
    0.02248779969802751 -4.8423940688043924e-015 0.2133075470146506
    2.7539611920053893e-018 0.022487799698022677 0.21330754701465093
    -0.02248779969802751 -4.8368861464203814e-015 0.2133075470146506
    -2.7539611920058527e-018 -0.022487799698032346 0.21330754701465021
    0.02248779969802751 -4.8423940688043924e-015 0.2133075470146506
    -2.3144824893577097e-031 -4.8396401076123877e-015 0.2133075470146506;''')
        cmds.createNode('nurbsCurve', name='IKhingeAxisRepresenation_hingeAxis_Shape', parent='IKhingeAxisRepresenation')
        cmds.setAttr('.overrideEnabled', 1)
        cmds.setAttr('.overrideColor', 14)
        mel.eval('''setAttr ".cached" -type "nurbsCurve"
        1 13 0 no 3
    14 142.9780762 162.38875300000001 166.38875300000001 175.33302499999999 184.277297
     188.277297 192.277297 201.22156899999999 210.165841 215.82269500000001 221.47954899999999
     227.136403 232.79325800000001 236.79325800000001
    14
    0 0 0
    -3.0181480758970857e-017 0.21330754701465066 4.8568868115934617e-015
    -3.6423099008447995e-017 0.21330754701465104 -0.022487799698022663
    -3.8235481764604161e-017 0.27509448455762031 6.4105696210914297e-015
    -2.3939862509493704e-017 0.21330754701465029 0.022487799698032378
    -3.0181480758970857e-017 0.21330754701465066 4.8568868115934617e-015
    -0.022487799698027552 0.21330754701465066 4.8593834588932533e-015
    -3.8235481764604161e-017 0.27509448455762031 6.4105696210914297e-015
    0.022487799698027486 0.21330754701465066 4.8543901642936701e-015
    -3.6423099008447995e-017 0.21330754701465104 -0.022487799698022663
    -0.022487799698027552 0.21330754701465066 4.8593834588932533e-015
    -2.3939862509493704e-017 0.21330754701465029 0.022487799698032378
    0.022487799698027486 0.21330754701465066 4.8543901642936701e-015
    -3.0181480758970857e-017 0.21330754701465066 4.8568868115934617e-015;''')

    return representationTransform

def createRawCharacterTransformControl():
    worldTransform = cmds.createNode('transform', name='__world_transform', skipSelect=True)
    rootTransform = cmds.createNode('transform', name='__root_transform', parent=worldTransform, skipSelect=True)
    cmds.createNode('nurbsCurve', name='__world_transformShape', parent=worldTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 3)
    cmds.setAttr(worldTransform+'.visibility', keyable=False)
    cmds.setAttr(rootTransform+'.visibility', keyable=False, lock=True)
    mel.eval('''setAttr ".cached" -type "nurbsCurve"
    1 24 0 no 3
    25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    25
    -0.0012198017766857383 0 0
    -0.00090588106601144293 0 -0.00048676009280348206
    -0.00090588106601144293 0 -0.00030196035533714766
    -0.0003592053246094439 0 -0.0003592053246094439
    -0.00030196035533714766 0 -0.00090588106601144293
    -0.00048676009280348206 0 -0.00090588106601144293
    0 0 -0.0012198017766857383
    0.00048676009280348206 0 -0.00090588106601144293
    0.00030196035533714766 0 -0.00090588106601144293
    0.0003592053246094439 0 -0.0003592053246094439
    0.00090588106601144293 0 -0.00030196035533714766
    0.00090588106601144293 0 -0.00048676009280348206
    0.0012900328852769516 0 0
    0.00090588106601144293 0 0.00048676009280348206
    0.00090588106601144293 0 0.00030196035533714766
    0.0003592053246094439 0 0.0003592053246094439
    0.00030196035533714766 0 0.00090588106601144293
    0.00048668914424207011 0 0.00090588106601144293
    0 0 0.0012198017766857383
    -0.00048668914424207011 0 0.00090588106601144293
    -0.00030196035533714766 0 0.00090588106601144293
    -0.0003592053246094439 0 0.0003592053246094439
    -0.00090588106601144293 0 0.00030196035533714766
    -0.00090588106601144293 0 0.00048676009280348206
    -0.0012198017766857383 0 0;''')
    cmds.createNode('nurbsCurve', name='__root_transform_zdShape', parent=rootTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 6)
    mel.eval('''setAttr ".cached" -type "nurbsCurve"
    1 3 0 no 3
    4 43.200000000000003 48 51.200000000000003 56
    4
    0.00026262551266839401 -5.8314578203687353e-17 -0.00026262551266839401
    0.00022077204231917425 -1.9608496366101335e-16 -0.00088308816927669702
    -0.00022077204231917425 -1.9608496366101335e-16 -0.00088308816927669702
    -0.00026262551266839401 -5.8314578203687353e-17 -0.00026262551266839401;''')
    cmds.createNode('nurbsCurve', name='__root_transform_zuShape', parent=rootTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 6)
    mel.eval('''setAttr ".cached" -type "nurbsCurve"
    1 3 0 no 3
    4 17.600000000000001 22.399999999999999 25.600000000000001 30.399999999999999
    4
    -0.00026262551266839401 5.8314578203687353e-17 0.00026262551266839401
    -0.00022077204231917425 1.9608496366101335e-16 0.00088308816927669702
    0.00022077204231917425 1.9608496366101335e-16 0.00088308816927669702
    0.00026262551266839401 5.8314578203687353e-17 0.00026262551266839401;''')
    cmds.createNode('nurbsCurve', name='__root_transform_xdShape', parent=rootTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 13)
    mel.eval('''setAttr ".cached" -type "nurbsCurve"
    1 3 0 no 3
    4 4.7999999999999998 9.5999999999999996 12.800000000000001 17.600000000000001
    4
    -0.00026262551266839401 -5.8314578203687353e-17 -0.00026262551266839401
    -0.00088308816927669702 -4.9021240915253338e-17 -0.00022077204231917425
    -0.00088308816927669702 4.9021240915253338e-17 0.00022077204231917425
    -0.00026262551266839401 5.8314578203687353e-17 0.00026262551266839401;''')
    cmds.createNode('nurbsCurve', name='__root_transform_xuShape', parent=rootTransform)
    cmds.setAttr('.overrideEnabled', 1)
    cmds.setAttr('.overrideColor', 13)
    mel.eval('''setAttr ".cached" -type "nurbsCurve"
    1 3 0 no 3
    4 30.399999999999999 35.200000000000003 38.399999999999999 43.200000000000003
    4
    0.00026262551266839401 5.8314578203687353e-17 0.00026262551266839401
    0.00088308816927669702 4.9021240915253338e-17 0.00022077204231917425
    0.00088308816927669702 -4.9021240915253338e-17 -0.00022077204231917425
    0.00026262551266839401 -5.8314578203687353e-17 -0.00026262551266839401;''')
    return [rootTransform, worldTransform]

def load_xhandleShape(transformName, modHandleColour, createWithTransform=False):
    if createWithTransform:
        xhandle_shape = cmds.createNode('xhandleShape', name=transformName+'Shape', skipSelect=True)
    else:
        xhandle_shape = cmds.createNode('xhandleShape', name=transformName+'Shape', parent=transformName, skipSelect=True)
    cmds.setAttr(xhandle_shape+'.overrideEnabled', 1)
    cmds.setAttr(xhandle_shape+'.overrideColor', modHandleColour)
    cmds.setAttr(xhandle_shape+'.localScaleX', keyable=False)
    cmds.setAttr(xhandle_shape+'.localScaleY', keyable=False)
    cmds.setAttr(xhandle_shape+'.localScaleZ', keyable=False)
    cmds.setAttr(xhandle_shape+'.localPositionX', keyable=False)
    cmds.setAttr(xhandle_shape+'.localPositionY', keyable=False)
    cmds.setAttr(xhandle_shape+'.localPositionZ', keyable=False)
    xhandle_parent = cmds.listRelatives(xhandle_shape, parent=True, type='transform')[0]
    return [xhandle_shape, xhandle_parent]
