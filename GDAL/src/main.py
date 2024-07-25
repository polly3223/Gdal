from osgeo import gdal
from pathlib import Path


def open_geotiff(file_name):
    src = gdal.Open(file_name)
    band = src.GetRasterBand(1)
    arr = band.ReadAsArray()
    gt = src.GetGeoTransform()
    print(gt)
    print(arr)



def main():
    print("Hello World!")
    print("Try to open a geotif file to test that GDAL is working")
    open_geotiff("sample.tif")



if __name__ == "__main__":
    main()
