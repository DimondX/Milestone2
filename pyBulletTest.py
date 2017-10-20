# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:42:04 2017

@author: Chris
"""
import sys
import pybullet as p
import pybullet_data
physicsClient = p.connect(p.DIRECT)#or p.DIRECT for non-graphical version
p.setPhysicsEngineParameter(enableFileCaching=0) #dont cache urdf files
p.setGravity(0,0,-10)
#cubeStartPos = [0,0,10]
#cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
try:
    #boxId = p.loadURDF("chris.urdf",cubeStartPos, cubeStartOrientation)
    boxId = p.loadURDF("chris.urdf")
    print('boxID=',boxId)
    vData = p.getVisualShapeData(boxId)
    #vData = p.getVisualShapeData(boxId)
    for o in vData:
        print('index',o[1],'kind',o[2],'size',o[3])
        #print(o)
    for i in range(3):
        p.stepSimulation()
        cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
        print(cubePos)
    #print(cubePos,cubeOrn)
except pybullet.error as e:
    if e.__str__()=="Cannot load URDF file.":
        print('caught bad URDF')
    else:
        print('pybullet error: bad urdf?')
        print(e)
except:
    #what err did we get?
    e = sys.exc_info()[0]
    print( "<p>Error: %s</p>" % e )
    

p.disconnect()
