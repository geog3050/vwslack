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
    try: 
        import arcpy # this imports arcpy
        arcpy.env.workspace = workspace # defines workspace
        fcs = arcpy.ListFeatureClasses() # establishes feature class list as the feature classes in the workspace
        for i in fcs:
            desc = arcpy.Describe(i) # this creates a describe object
            if desc.shapeType == "Polygon":
                print(fc + " is a polygon feature class")
            elif desc.shapeType == "Polyline": # every feature class that has this shape type polygon will be printed
                print(fc + " is a polyline feature class")
            elif desc.shapeType == "Point": # every feature class that has the shape type point will be printed
                print(fc + " is a point feature class")
            else: # all other feature classes are printed
                print("Type unknown")
    except arcpy.ExecuteError:  
        msgs = arcpy.GetMessages(2) 
        arcpy.AddError(msgs) 
        print("Tool Error:", msgs)

###################################################################### 
# Problem 2 (20 Points)
#
# This function reads all the attribute names in a feature class or shape file and
# prints the name of each attribute name and its type (e.g., integer, float, double)
# only if it is a numerical type

###################################################################### 
def printNumericalFieldNames(inputFc, workspace):      # inputFc is the filepath for a feature class and workspace is the filepath for the geodatabase.
    try:
        import arcpy
            #this imports arcpy
        arcpy.env.workspace = workspace                # defines the workspace in arcpy as the inputted "workplace" file path
        desc=arcpy.Describe(inputFc)                   # creates a Describe object which pulls the properties of the input feature class (inputFc)
        fields=desc.fields                             # establishes the fields object as the description of all the fields in the inputFc
        for field in fields:
            if field.type in ["Integer", "Float","OID","Double"]:    # all numeric field types
                print(f"{field.name} has a type of {field.type}")
    except arcpy.ExecuteError:
       print(arcpy.GetMessages(2)) 
###################################################################### 
# Problem 3 (30 Points)
#
# Given a geodatabase with feature classes, and shape type (point, line or polygon) and an output geodatabase:
# this function creates a new geodatabase and copying only the feature classes with the given shape type into the new geodatabase

###################################################################### 
def exportFeatureClassesByShapeType(input_geodatabase, shapeType, output_geodatabase):
    try:
        import arcpy     # imports arcpy
        import os        # import operating system module
        arcpy.env.workspace = input_geodatabase # defines workspace in arcpy
        out_folder_path = os.path.dirname(os.path.abspath(output_geodatabase)) # this creates new folder path
        arcpy.CreateFileGDB_management(out_folder_path, output_geodatabase)    # this create new geodatabase in output_geodatabase
        featureclasses = arcpy.ListFeatureClasses()    #establish feature class lit
        for fc in featureclasses:
            describe_fc = arcpy.Describe(fc)     # creates a describe object
            if describe_fc.shapeType == shapeType:  shape type matches the input shape type
                arcpy.Copy_management(fc, output_geodatabase + "/" + fc) # copies the feature class to the new geodatabase
    except arcpy.ExecuteError: 
        msgs = arcpy.GetMessages(2) 
        arcpy.AddError(msgs) 
        print("Tool Error:", msgs)
###################################################################### 
# Problem 4 (40 Points)
#
# Given an input feature class or a shape file and a table in a geodatabase or a folder workspace,
# join the table to the feature class using one-to-one and export to a new feature class.
# Print the results of the joined output to show how many records matched and unmatched in the join operation. 

###################################################################### 
def exportAttributeJoin(inputFc, idFieldInputFc, inputTable, idFieldTable, workspace):
    try:
        import arcpy    # imports arcpy
        arcpy.env.workspace = workspace     # defines the workspace in arcpy as the inputted "workplace" file path
        desc= arcpy.Describe(inputFc)    # creates a Describe object
        new_fc = arcpy.AddJoin_management(inputFc, idFieldInputFc, inputTable, idFieldTable)    # joins the input feature class and input table as a new feature class
        arcpy.conversion.ExportFeatures(new_fc, f"{desc.name}_joined")    # exports and saves the new feature class with the name of the input feature class plus _joined
        arcpy.management.ValidateJoin(inputFc, idFieldInputFc, inputTable, idFieldTable)    # validate the join
        print(arcpy.GetMessages())    # prints the join messages
        
    except arcpy.ExecuteError:
       print(arcpy.GetMessages(2))
######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__' and hawkid()[1] == "hawkid":
    print('### Error: YOU MUST provide your hawkid in the hawkid() function.')
