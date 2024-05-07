  def hawkid():
    return(["Vivian Slack", vwslack"])

import arcpy

# Set environment
arcpy.env.workspace = r"C:/Users/vivianslack/Downloads/Geospatial_Programming/Quizzes/Quiz_5/airports"
arcpy.env.overwriteOutput = True

# Input feature class
input_fc = "/Users/vivianslack/Downloads/Geospatial_Programming/Quizzes/Quiz_5/airports/airports.shp"

# Output feature class for buffers
major_airport_output_fc = "/Users/vivianslack/Downloads/Geospatial_Programming/Quizzes/Quiz_5/airports/MajorAirports_buffer.shp"
minor_airport_output_fc = "/Users/vivianslack/Downloads/Geospatial_Programming/Quizzes/Quiz_5/airports/MinorAirports_buffer.shp"
seaplane_base_output_fc = "/Users/vivianslack/Downloads/Geospatial_Programming/Quizzes/Quiz_5/airports/SeaplaneBase_buffer.shp"

# Field names
feature_field = "FEATURE"
emplanements_field = "TOT_ENP"

# Create a feature layer
arcpy.MakeFeatureLayer_management(input_fc, "temp_layer")

# Create selection queries for different types of facilities
airport_query = "{} = 'airport'".format(feature_field, emplanements_field)
small_airport_query = "{} = 'airport'".format(feature_field, emplanements_field)
seaplane_base_query = "{} = 'seaplane base'".format(feature_field, emplanements_field)

# Apply selection queries
arcpy.SelectLayerByAttribute_management("temp_layer", "NEW_SELECTION", airport_query)

# Create buffers for airports with emplanements exceeding 10000
arcpy.SelectLayerByAttribute_management("temp_layer", "SUBSET_SELECTION", "{} >= 10000".format(enplanements_field))
arcpy.Buffer_analysis("temp_layer", major_airport_output_fc, "15000 Meters")

# Create buffers for airports with emplanements below 10000
arcpy.SelectLayerByAttribute_management("temp_layer", "REMOVE_FROM_SELECTION", "{} >= 10000".format(enplanements_field))
arcpy.Buffer_analysis("temp_layer", minor_airport_output_fc, "10000 Meters")

# Clear selection
arcpy.SelectLayerByAttribute_management("temp_layer", "CLEAR_SELECTION")

# Apply selection query for seaplane bases
arcpy.SelectLayerByAttribute_management("temp_layer", "NEW_SELECTION", seaplane_base_query)

# Create buffers for seaplane bases with emplanements surpassing 1,000
arcpy.SelectLayerByAttribute_management("temp_layer", "SUBSET_SELECTION", "{} > 1000".format(enplanements_field))
arcpy.Buffer_analysis("temp_layer", seaplane_base_output_fc, "7500 Meters")

# Clear selection
arcpy.SelectLayerByAttribute_management("temp_layer", "CLEAR_SELECTION")
