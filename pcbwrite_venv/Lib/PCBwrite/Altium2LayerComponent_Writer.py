import datetime

def altium_2_layer_component_writer(component_name, pcb):
    filename = component_name + 'Lib.LIA'
    fid = pcb_open(filename)
    pcb_head(fid, component_name)
    pcb_standard_lib(fid, pcb)
    pcb_custom_lib(fid, pcb, component_name)
    pcb_close(fid)


def pcb_open(fname):
    try:
        fid = open(fname, 'w')
    except Exception as e:
        if 'fid' in locals():
            fid.close()
        raise e
    return fid


def pcb_head(fid, lib_name):
    fid.write('ACCEL_ASCII "   " \n')
    fid.write('   \n')
    fid.write('(asciiHeader \n')
    fid.write('  (asciiVersion 3 0) \n')
    fid.write('  (timeStamp %s) \n' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    fid.write('  (program "Design Explorer 99 SE" "6.1.0") \n')
    fid.write('  (copyright "Copyright © 2002 Altium Ltd") \n')
    fid.write('  (headerString "") \n')
    fid.write('  (fileUnits Mil) \n')
    fid.write('  (guidString "{00000000-0000-0000-0000-000000000000}") \n')
    fid.write(') \n')
    fid.write('   \n')
    fid.write('(library "%s " \n' % lib_name)


def pcb_close(fid):
    try:
        fid.write(') \n')
        fid.write(' \n')
        fid.close()
    except Exception as e:
        if 'fid' in locals():
            fid.close()
        raise e


def pcb_standard_lib(fid, pcb):
    for slot_style in pcb['SlotStyle']:
        pad_size = slot_style['PadSize']
        shape = slot_style['Shape']
        fid.write('  (padStyleDef "%s" \n' % slot_style['Type'])
        fid.write('    (holeDiam %0.3fmm) \n' % slot_style['Holesize'][1])
        fid.write('    (startRange 1) \n')
        fid.write('    (endRange 2) \n')
        fid.write('    (padShape (layerNumRef 1) (padShapeType %s) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (shape, pad_size[0], pad_size[1]))
        fid.write('    (padShape (layerNumRef 2) (padShapeType %s) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (shape, pad_size[0], pad_size[1]))
        fid.write('    (padShape (layerType Signal) (padShapeType %s) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (shape, pad_size[0], pad_size[1]))
        fid.write('    (padShape (layerType Plane) (padShapeType NoConnect) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (padShape (layerType NonSignal) (padShapeType Oval) (shapeWidth 0mm) (shapeHeight 0mm) ) \n')
        fid.write('  ) \n')

    for pad_style in pcb['PadStyle']:
        pad_size = pad_style['PadSize']
        fid.write('  (padStyleDef "%s" \n' % pad_style['Type'])
        fid.write('    (holeDiam %0.3fmm) \n' % pad_style['holeDiam'])
        fid.write('    (startRange 1) \n')
        fid.write('    (endRange 2) \n')
        fid.write('    (padShape (layerNumRef 1) (padShapeType Oval) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (pad_size, pad_size))
        fid.write('    (padShape (layerNumRef 2) (padShapeType Oval) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (pad_size, pad_size))
        fid.write('    (padShape (layerType Signal) (padShapeType Oval) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (pad_size, pad_size))
        fid.write('    (padShape (layerType Plane) (padShapeType NoConnect) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (padShape (layerType NonSignal) (padShapeType Oval) (shapeWidth 0mm) (shapeHeight 0mm) ) \n')
        fid.write('  ) \n')

    for via_style in pcb['ViaStyle']:
        pad_size = via_style['PadSize']
        fid.write('  (viaStyleDef "%s" \n' % via_style['Type'])
        fid.write('    (holeDiam %0.3fmm) \n' % via_style['holeDiam'])
        fid.write('    (startRange 1) \n')
        fid.write('    (endRange 2) \n')    
        fid.write('    (viaShape (layerNumRef 1) (viaShapeType Ellipse) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (viaShape (layerNumRef 2) (viaShapeType Ellipse) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (viaShape (layerType Signal) (viaShapeType Ellipse) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (viaShape (layerType Plane) (viaShapeType NoConnect) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (viaShape (layerType NonSignal) (viaShapeType Ellipse) (shapeWidth 0mm) (shapeHeight 0mm) ) \n')
        fid.write('    (viaShape (layerNumRef 22) (viaShapeType Ellipse) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (pad_size, pad_size))
        fid.write('    (viaShape (layerNumRef 2) (viaShapeType Ellipse) (shapeWidth %0.3fmm)(shapeHeight %0.3fmm)) \n' % (pad_size, pad_size))
        fid.write('    (viaShape (layerNumRef 22) (viaShapeType NoConnect) (shapeWidth 0.0)(shapeHeight 0.0)) \n')
        fid.write('  ) \n')
    fid.write(' \n')


def pcb_custom_lib(fid, pcb, pattern_name):
    fid.write('  (patternDefExtended "%s_1" \n' % pattern_name)
    fid.write('    (patternGraphicsDef \n')
    fid.write('      (patternGraphicsNameDef "Primary") \n')

    # Vias
    vias = pcb['Vias']
    fid.write('      (multiLayer \n')
    for via in vias:
        fid.write('        (via (viaStyleRef "%s") (pt %0.3fmm %0.3fmm) ) \n' % (via['Type'], via['xc'], via['yc']))
    fid.write('      ) \n')
    fid.write('  \n')

    # TopE
    top_e = pcb['TopE']
    fid.write('      (layerContents (layerNumRef 1) \n')
    for item in top_e:
        pcb_polygon(fid, item['x'], item['y'])
    fid.write('      ) \n')
    fid.write('  \n')

    # BtmE
    btm_e = pcb['BtmE']
    fid.write('      (layerContents (layerNumRef 2) \n')
    for item in btm_e:
        pcb_polygon(fid, item['x'], item['y'])
    fid.write('      ) \n')
    fid.write('  \n')

    # TopMask
    top_mask = pcb['TopMask']
    fid.write('      (layerContents (layerNumRef 4) \n')
    for item in top_mask:
        pcb_polygon(fid, item['x'], item['y'])
    fid.write('      ) \n')
    fid.write('  \n')

    # BtmMask
    btm_mask = pcb['BtmMask']
    fid.write('      (layerContents (layerNumRef 5) \n')
    for item in btm_mask:
        pcb_polygon(fid, item['x'], item['y'])
    fid.write('      ) \n')
    fid.write('  \n')

    # TopSilk
    top_silk = pcb['TopSilk']
    fid.write('      (layerContents (layerNumRef 6) \n')
    for item in top_silk:
        pcb_polyline(fid, item['x'], item['y'], 0.1)
    fid.write('      ) \n')
    fid.write('  \n')

    fid.write('    )  \n')
    fid.write('  )  \n')
    fid.write('  \n')


def pcb_polygon(fid, xp, yp):
    fid.write('        (pcbPoly  \n')
    for i in range(len(xp)):
        fid.write('          (pt %0.3fmm %0.3fmm) \n' % (xp[i], yp[i]))
    fid.write('        ) \n')


def pcb_polyline(fid, xp, yp, linewidth):
    for i in range(len(xp) - 1):
        fid.write('          (line (pt %0.3fmm %0.3fmm) (pt %0.3fmm %0.3fmm) (width %0.3fmm) ) \n' % (xp[i], yp[i], xp[i+1], yp[i+1], linewidth))

'''
# Example usage:
if __name__ == "__main__":
    # Example PCB dictionary (replace with your actual data structure)
    pcb_data = {
        'SlotStyle': [...],  # List of slot styles
        'PadStyle': [...],   # List of pad styles
        'ViaStyle': [...],   # List of via styles
        'Vias': [...],       # List of vias
        'TopE': [...],       # List of top layer polygons
        'BtmE': [...],       # List of bottom layer polygons
        'TopMask': [...],    # List of top layer mask polygons
        'BtmMask': [...],    # List of bottom layer mask polygons
        'TopSilk': [...]     # List of top layer silk lines
    }

    # Call the function to generate the Altium library file
    altium_2_layer_component_writer("ComponentName", pcb_data)
'''