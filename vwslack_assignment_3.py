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
# Problem 1: 20 Points
#
# Given a csv file import it into the database passed as in the second parameter
# Each parameter is described below:

# csvFile: The absolute path of the file should be included (e.g., C:/users/ckoylu/test.csv)
# geodatabase: The workspace geodatabase
###################################################################### 

import arcpy
def importCSVIntoGeodatabase(csvFile, geodatabase):
    pass
    from arcpy import env
    arcpy.env.overwriteoutput = True
    env.workspace = env.workspace = "C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_3/hw3_data"
    feature_class = "yearly.csv"
    csv_file_path = "C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_3/hw3_data/yearly.csv"
    geodatabase_path = "C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_3/hw3_data/weather.gdb"
    arcpy.TableToTable_conversion(csv_file_path, geodatabase_path, yearly.csv)


##################################################################################################### 
# Problemii/ 2: 80 Points Total
#
# Given a csv table with point coordinates, this function should create an interpolated
# raster surface, clip it by a polygon shapefile boundary, and generate an isarithmic map

# You can organize your code using multiple functions. For example,
# you can first do the interpolation, then clip then equal interval classification
# to generate an isarithmic map

# Each parameter is described below:

# inTable: The name of the table that contain point observations for interpolation       
# valueField: The name of the field to be used in interpolation
# xField: The field that contains the longitude values
# yField: The field that contains the latitude values
# inClipFc: The input feature class for clipping the interpolated raster
# workspace: The geodatabase workspace

# Below are suggested steps for your program. More code may be needed for exception handling
#    and checking the accuracy of the input values.

# 1- Do not hardcode any parameters or filenames in your code.
#    Name your parameters and output files based on inputs. For example,
#    interpolated raster can be named after the field value field name 
# 2- You can assume the input table should have the coordinates in latitude and longitude (WGS84)
# 3- Generate an input feature later using inTable
# 4- Convert the projection of the input feature layer
#    to match the coordinate system of the clip feature class. Do not clip the features yet.
# 5- Check and enable the spatial analyst extension for kriging
# 6- Use KrigingModelOrdinary function and interpolate the projected feature class
#    that was created from the point feature layer.
# 7- Clip the interpolated kriging raster, and delete the original kriging result
#    after successful clipping. 
#################################################################################################################### 

import arcpy
from arcpy.sa import *

def krigingFromPointCSV(inTable, valueField, xField, yField, inClipFc, workspace = "assignment3.gdb"):
    pass

    workspace = "C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_3/hw3_data/weather.gdb"
    arcpy.env.workspace = workspace
    arcpy.envoverwriteOutput = True

    inTable = "/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_3/observations.csv"
    valueField = "ObservationValue"
    xField = "Longitude"
    yField = "Latitude"
    inClipFc = "C:/users/ckoylu/boundary.shp"

    inFeatureLayer = arcpy.MakeXYEventLayer_management(inTable, xField, yField, "inFeatureLayer", arcpy.SpatialReference(4326))

    arcpy.Project_management(inFeature, "projected_feature", inClipFc.spatialReference)

    if arcpy.CheckExtension("Spatial") == "Available":
        arcpy.CheckOutExtension("Spatial")
    else:
        raise Exception("Spatial Analyst extension is not available.")

    kriging_output = KrigingModelOrdinary(inProjectedFeatureLayer, valueField, "kriging_output")
    kriging_output.save("C:/Users/vivianslack/Downloads/Geospatial_Programming/Assignments/HW_3/kriging_output")
    clipped_raster = arcpy.Clip_management(kriging_output, "#", "clipped_raster", inClipFc)
    arcpy.Delete_management(kringing_output)

    output_raster = os.path.join(workspace, f"{valueField}_isarithmic_map.tif")
    clipped_raster.save(output_raster)

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
