import darts
import numpy
import arcpy
import os
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')

tif_file_path="D:/desktop/data/0523CN/"
shp_file="D:/desktop/data/basic/China84.shp"
out_file_path="D:/desktop/data/mask/"
# projected_file_path = "D:/desktop/data-reprocessing/fenxi/projected/"
resample_file_path="D:/desktop/data/resample/"

arcpy.env.workspace=tif_file_path
arcpy.env.extent=shp_file

tif_file_name=arcpy.ListRasters("*","tif")
for tif_file in tif_file_name:
    mask_result=ExtractByMask(tif_file,shp_file)
    mask_result_path=out_file_path+"/"+tif_file.strip(".tif")+".tif"
    mask_result.save(mask_result_path)

arcpy.env.workspace=out_file_path
tif_file_name=arcpy.ListRasters("*","tif")
for tif_file in tif_file_name:
    resample_file_name=tif_file.strip(".tif")+"_Re.tif"
    arcpy.Resample_management(tif_file,resample_file_path+resample_file_name,
                              0.1,"BILINEAR")
import os
from arcpy.sa import *
arcpy.CheckOutExtension('Spatial')

tif_file_path="D:/desktop/data/0523CN/"
shp_file="D:/desktop/data/basic/China84.shp"
out_file_path="D:/desktop/data/mask/"
# projected_file_path = "D:/desktop/data-reprocessing/fenxi/projected/"
resample_file_path="D:/desktop/data/resample/"

arcpy.env.workspace=tif_file_path
arcpy.env.extent=shp_file

tif_file_name=arcpy.ListRasters("*","tif")
for tif_file in tif_file_name:
    mask_result=ExtractByMask(tif_file,shp_file)
    mask_result_path=out_file_path+"/"+tif_file.strip(".tif")+".tif"
    mask_result.save(mask_result_path)

arcpy.env.workspace=out_file_path
tif_file_name=arcpy.ListRasters("*","tif")
for tif_file in tif_file_name:
    resample_file_name=tif_file.strip(".tif")+"_Re.tif"
    arcpy.Resample_management(tif_file,resample_file_path+resample_file_name,
                              0.1,"BILINEAR")