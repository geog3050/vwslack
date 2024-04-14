###################################################################### 
# Edit the following function definition, replacing the words
# 'name' with your name and 'hawkid' with your hawkid.
# 
# Note: Your hawkid is the login name you use to access ICON, and not
# your firsname-lastname@uiowa.edu email address.
# 
# def hawkid():
#     return(["Caglar Koylu", "ckoylu"])
###################################################################### 
def hawkid():
    return(["Vivian Slack", "vwslack"])

###################################################################### 
# Problem 1 (10 Points)
#
# This function reads all the feature classes in a workspace (folder or geodatabase) and
# prints the name of each feature class and the geometry type of that feature class in the following format:
# 'states is a point feature class'

###################################################################### 
def printFeatureClassNames(workspace):
    pass

import arcpy
arcpy.env.workspace = ("C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_2/hw2.gdb")
print(arcpy.env.workspace)

fcList = arcpy.ListFeatureClasses()
print(fcList)
for fc in fcList:
    desc = acrpy.Describe(fc)
    geometry_type = desc.shapeType
    print(f"{fc} is a {geometry_type} feature class")   

###################################################################### 
# Problem 2 (20 Points)
#
# This function reads all the attribute names in a feature class or shape file and
# prints the name of each attribute name and its type (e.g., integer, float, double)
# only if it is a numerical type

###################################################################### 
def printNumericalFieldNames(inputFc, workspace):
    pass

import arcpy
arcpy.env.workspace = "C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_2/hw2.gdb"

fields = arcpy.ListFields("C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_2/hw2.gdb")

for field in fields:
    if field.type in ['Integer', 'SmallInteger', 'Single', 'Double']:
        print(f"{field.name}: {field.type}")


###################################################################### 
# Problem 3 (30 Points)
#
# Given a geodatabase with feature classes, and shape type (point, line or polygon) and an output geodatabase:
# this function creates a new geodatabase and copying only the feature classes with the given shape type into the new geodatabase

###################################################################### 
def exportFeatureClassesByShapeType(input_geodatabase, shapeType, output_geodatabase):
    pass

import arcpy
import os

input_geodatabase = ("C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_2/hw2.gdb")
arcpy.env.workspace = input_geodatabase

output_geodatabase = ("C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_2/hw2.gdb/hw2_output.gdb")

if not arcpy.Exists(output_geodatabase):
    arcpy.CreatleFileGDB_management(os.path.dirname(output_geodata), os.path.basename(out_geodatabase))

arcpy.env.workspace = input_geodatabase
feature_classes = arcpy.ListFeaturesClasses()

for fc in feature_classes:
    desc = arcpy.Describe(fc)
    if desc.shapeType.lower() == shapeType.lower():
        output_fc = os.path.join(output_geodatabase, desc.name)
        arcpy.CopyFeatures_management(fc, output_fc)
        print(output_fc)
 
for gdb, datasets, features in arcpy.da.Walk(env.workspace):
    for dataset in datasets:
        for feature in arcpy.ListFeatureClasses("Polyline_*", "POLYLINE", dataset):
            arcpy.CopyFeatures_management(feature,os.path.join(outputGDB, "Polyline_"+dataset))


###################################################################### 
# Problem 4 (40 Points)
#
# Given an input feature class or a shape file and a table in a geodatabase or a folder workspace,
# join the table to the feature class using one-to-one and export to a new feature class.
# Print the results of the joined output to show how many records matched and unmatched in the join operation. 

###################################################################### 
def exportAttributeJoin(inputFc, idFieldInputFc, inputTable, idFieldTable, workspace):
    pass

import arcpy
import os

inputFc = ''
outlocation = '/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_2/hw2.gdb/hw2_prob4_output.gdb'
outFeature = ''
delimtedField = arcpy.AddFieldDelimeters(arcpy.env.workspace, '')
expression = delimtedField + " + '' "
joined_output = arcpy.conversion.FeatureClasstoFeatureClass(inputFc, outlocation, outfeatureClass, expression)
print(joined_output)


######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
