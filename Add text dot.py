import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import Rhino
import scriptcontext
import System.Guid
import scriptcontext as sc
import os
#############################################
#Select a file to open
filename = rs.OpenFileName("Open CSV file","*.csv|", None, None, None)
 
#open the file for reading
file = open(filename, 'r')
lines = file.readlines() 
file.close()
del lines[0]

#Read the lines in excel sheet and define the values needed
for line in lines:
    line = line.rstrip()
    ptInfo = line.split(',')
    print(type(line))
    print(type(ptInfo))
    #Create a layer for each shipment
    #shipment = ptInfo[1]
    #print ("shipment info read",shipment)
    #rs.AddLayer(shipment)
    
    ##Insert cargos in this shipment
    #Read the translation of the cargo
    #x = 1000*float(ptInfo[4])
    #y = 1000*float(ptInfo[5])
    #z = 1000*float(ptInfo[6])
    #if the unit is in meter
    x = float(ptInfo[4])
    y = float(ptInfo[5])
    z = float(ptInfo[6])
    arrPoint = x,y,z
    print(arrPoint)
    
    #Read the path and filename of the cargo
    #file = ptInfo[6]
    #print('filecargo:' ,file)
    #rs.Command('_-Import ' + file + ' _Enter')

    #unhide all objects
    #objs = rs.LastCreatedObjects()
    #if objs: rs.HideObjects(objs)
    #Do something here...
    #rs.ShowObjects( objs )

#    #Explode blocks
#    strObjects = rs.BlockNames(True)
#    if strObjects:
#        for strObject in strObjects:
#            if rs.IsBlock(strObject):
#                object_explode = rs.BlockObjects(strObject)
#            #if rs.IsBlockInstance(strObject):
#                rs.ExplodeBlockInstance(object_explode)
#            else:
#                continue
#    else:
#        continue
#    #Delete irrelevant layers
#    layers = rs.LayerNames()
#    for layer in layers: 
#        if rs.LayerVisible(layer)== False:
#            rs.LayerVisible(layer,True)
#        if layer == shipment:
#            continue 
#        else:
#            if layer:
#                rs.PurgeLayer(layer)
#            else:
#                continue
    #delete curves in the objects
    #objs= rs.LastCreatedObjects()
    #print("objs:",objs)
    #for obj in objs:
    #    if rs.IsCurve(obj):
    #        rs.DeleteObject(obj)
    #    else:
    #        #If successful, move the objects to the base point
    #        rs.MoveObject(obj, arrPoint)
            
    #        #match the objectcargo to its own shipment layer
    #        rs.ObjectLayer(obj, shipment)
            
            #Add text dot to the object
    cargoname = ptInfo[2]
    text_insert_point = arrPoint
    text = cargoname
    text_id = rs.AddTextDot( text, text_insert_point )

    #        #match the text to its own shipment layer
    #        rs.ObjectLayer(text_id, shipment)
    #        
    #        #Group Text dot with Cargo
    #        name = rs.AddGroup(cargoname)
    #        object_ids = text_id, obj
    #        if object_ids: rs.AddObjectsToGroup(object_ids, cargoname)