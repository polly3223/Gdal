# Gdal

A python container with all that is required to run gdal.

Gdal is now shipped with eccodes https://confluence.ecmwf.int/display/ECC

If you have docker installed just run:

```
docker compose run gdal bash
```

This will build the image, run it as a container and give you a command line interface to it.

Once it lauches you can run:

```
python3 main.py
```

This will test the eccodes installation by opening a geotiff with GDAL.

The geotiff sample comes from:
https://github.com/mommermi/geotiff_sample
