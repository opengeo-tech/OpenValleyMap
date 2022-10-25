flw = pyflwdir.from_dem(
        data=elevtn,
        nodata=nodata,
        transform=transform,
        latlon=crs.is_geographic,
    )
basins = flw.basins()