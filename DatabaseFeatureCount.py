import arcpy
import os
from arcpy import env

workspace = "Database Connections/SDE.sde"
env.workspace =workspace

feature_classes = []
feature_tables = []
countList = []

#*******************************************************************************************************************************
# Count features in all layers
#*********************Count Points, Lines and Polygons***********************

for dirpath, dirnames, filenames in arcpy.da.Walk(workspace, datatype='FeatureClass', type=['Polygon', 'Polyline', 'Point']):
    for filename in filenames:
        feature_classes.append(os.path.join(dirpath, filename))
        layer = filename
        fcNameProp = arcpy.Describe(layer)
        featureResult = int(arcpy.GetCount_management(layer).getOutput(0))
        countList.append(featureResult)

#**********************Count table rows****************************************

for dirpath, dirnames, filenames in arcpy.da.Walk(workspace, datatype='Table'):
    for filename in filenames:
        feature_tables.append(os.path.join(dirpath, filename))
        table = filename
        tableNameProp = arcpy.Describe(table)
        tableResult = int(arcpy.GetCount_management(table).getOutput(0))
        countList.append(tableResult)

#************************Sum all records**************************************
sumFeatures = 0
for i in countList:
  sumFeatures += i

print (sumFeatures)