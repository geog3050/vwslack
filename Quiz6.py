import arcpy
import os

def calculatePercentAreaOfPolygonAInPolygonB(input_geodatabase, fcPolygonA, fcPolygonB, idFieldPolygonB):
    arcpy.env.workspace = input_geodatabase

# Set path
    input_geodatabase = r"C:/Users/vivianslack/Downloads/week6.gdb"

# Calculate total area of parks
    arcpy.AddField_management(fcPolygonA, "park_areas", "areasqm", "DOUBLE")
    fcPolygonA = "park_areas"
    arcpy.CalculateGeometeryAttributes_management("park_areas", [["areasqm", "AREA"]], "MILES_US", "SQUARE_MILES_US")

# Calculate total area of block groups
    arcpy.AddField_management(fcPolygonB, "block_groups", "areasqm", "DOUBLE")
    fcPolygonB = "block_groups"
    arcpy.CalculateGeometryAttributes_management("block_groups", [["areasqm", "AREA"]], "MILES_US", "SQUARE_MILES_US")

    idFieldPolygonB = "block_group_id"

    # Create a dictionary to store park area by ObjectID
    park_area_dict = {row[0]: row[1] for row in arcpy.da.SearchCursor(fcPolygonA, ["OBJECTID", "park_areas"])}

    # Iterate through features in fcPolygonB
    with arcpy.da.UpdateCursor(fcPolygonB, ["SHAPE@", "block_groups", "areasqm"]) as cursor:
        for row in cursor:
            fcPolygonB = row[0]
            block_groups = row[1]

            # Calculate total area of parks within the current block group
            park_area_within_block_group = sum(park.geometry.area for park in arcpy.da.SearchCursor(fcPolygonA, ["SHAPE@"]) if park.geometry.within(fcPolygonB))
            # Calculate the percentage and update the field
            percentage = (park_area_within_block_group / block_group_area) * 100 if block_group_area != 0 else 0
            row[2] = percentage
            cursor.updateRow(row)
            print(percentage)
