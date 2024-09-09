import datetime

def altium_2_layer_component_writer(component_name, pcb):
    filename = component_name + '.PCB'
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
    fid.write('  (timeStamp %s) \n' % datetime.datetime.now().strftime('%d-%b-%Y'))
    fid.write('  (program "Design Explorer 99 SE" "6.1.0") \n')
    fid.write('  (copyright "Copyright ® 2002 Altium Ltd") \n')
    fid.write('  (headerString "") \n')
    fid.write('  (fileUnits Mil) \n')
    fid.write('  (guidString "{00000000-0000-0000-0000-000000000000}") \n')
    fid.write(') \n')
    fid.write('   \n')
    fid.write('(library "%s" \n' % lib_name)

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
        pad_size = via_style['PadSize'][0]
        fid.write('  (viaStyleDef "%s" \n' % via_style['Type'])
        fid.write('    (holeDiam %0.3fmm) \n' % via_style['holeDiam'])
        fid.write('    startRange 1 endRange 2 (viaShape (layerNumRef 1) (viaShapeType Ellipse) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (pad_size, pad_size))
        fid.write('    (viaShape (layerNumRef 2) (viaShapeType Ellipse) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (pad_size, pad_size))
        fid.write('    (viaShape (layerType Signal) (viaShapeType Ellipse) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (viaShape (layerType Plane) (viaShapeType NoConnect) (shapeWidth 0.0) (shapeHeight 0.0) ) \n')
        fid.write('    (viaShape (layerType NonSignal) (viaShapeType Ellipse) (shapeWidth 0mm) (shapeHeight 0mm) ) \n')
        fid.write('    (viaShape (layerNumRef 22) (viaShapeType Ellipse) (shapeWidth %0.3fmm) (shapeHeight %0.3fmm) ) \n' % (pad_size, pad_size))
        fid.write('    (viaShape (layerNumRef 2) (viaShapeType Ellipse) (shapeWidth %0.3fmm)(shapeHeight %0.3fmm)) \n' % (pad_size, pad_size))
        fid.write('    (viaShape (layerNumRef 22) (viaShapeType NoConnect) (shapeWidth 0.0)(shapeHeight 0.0)) \n')
        fid.write('  ) \n')
    fid.write(') \n')

def pcb_custom_lib(fid, pcb, pattern_name):
    fid.write('(netlist "Netlist_1" \n')
    fid.write('  (net "net1") \n')
    fid.write(') \n')
    fid.write('   \n')
    fid.write('(pcbDesign "%s" \n' % pattern_name)
    fid.write('  (pcbDesignHeader \n')
    fid.write('    (workspaceSize 812.8mm 812.8mm) \n')
    fid.write('    (gridDfns \n')
    fid.write('      (grid "0.1mm") \n')
    fid.write('    ) \n')
    fid.write('    (designInfo \n')
    fid.write('      (fieldSet "(Default)" \n')
    fid.write('        (fieldDef "Date" "%s") \n' % datetime.datetime.now().strftime('%d-%b-%Y'))
    fid.write('        (fieldDef "Time" "%s") \n' % datetime.datetime.now().strftime('%I:%M:%S %p'))
    fid.write('        (fieldDef "Author" "") \n')
    fid.write('        (fieldDef "Revision" "") \n')
    fid.write('        (fieldDef "Title" "") \n')
    fid.write('        (fieldDef "Approved By" "") \n')
    fid.write('        (fieldDef "Checked By" "") \n')
    fid.write('        (fieldDef "Company Name" "") \n')
    fid.write('        (fieldDef "Drawing Number" "") \n')
    fid.write('        (fieldDef "Drawn By" "") \n')
    fid.write('        (fieldDef "Engineer" "") \n')
    fid.write('      ) \n')
    fid.write('    ) \n')
    fid.write('    (solderSwell 0.100mm) \n')
    fid.write('    (pasteSwell 0.000mm) \n')
    fid.write('    (planeSwell 0.500mm) \n')
    fid.write('  ) \n')
  
    for layer in pcb['LayerDefs']:
        fid.write('  (layerDef "%s" \n' % layer['name'])
        fid.write('    (layerNum %d) \n' % layer['num'])
        fid.write('    (layerType %s) \n' % layer['type'])
        fid.write('    (fieldSetRef "(Default)") \n')
        fid.write('  ) \n')
  
    fid.write('  (multiLayer \n')
    for via in pcb['Vias']:
        fid.write('    (via (viaStyleRef "%s") (pt %0.3fmm %0.3fmm) ) \n' % (via['Type'], via['xc'], via['yc']))
    fid.write('  ) \n')
    fid.write('   \n')

    for layer in pcb['LayerContents']:
        fid.write('  (layerContents (layerNumRef %d) \n' % layer['layerNum'])
        for item in layer['items']:
            if item['type'] == 'polygon':
                pcb_polygon(fid, item['x'], item['y'])
            elif item['type'] == 'line':
                pcb_polyline(fid, item['x'], item['y'], item['width'])
        fid.write('  ) \n')
    fid.write(') \n')

def pcb_close(fid):
    try:
        fid.close()
    except Exception as e:
        if 'fid' in locals():
            fid.close()
        raise e

def pcb_polygon(fid, xp, yp):
    fid.write('    (pcbPoly  \n')
    for i in range(len(xp)):
        fid.write('      (pt %0.3fmm %0.3fmm) \n' % (xp[i], yp[i]))
    fid.write('    ) \n')

def pcb_polyline(fid, xp, yp, linewidth):
    for i in range(len(xp) - 1):
        fid.write('      (line (pt %0.3fmm %0.3fmm) (pt %0.3fmm %0.3fmm) (width %0.3fmm) ) \n' % (xp[i], yp[i], xp[i+1], yp[i+1], linewidth))

'''
# Example usage:
if __name__ == "__main__":
    # Example PCB dictionary (replace with your actual data structure)
    pcb_data = {
        'SlotStyle': [
            {'Type': 'RndSlot1', 'Holesize': [0.8, 0.8], 'PadSize': [1.95, 0.8], 'Shape': 'Oval'},
            {'Type': 'RectSlot1', 'Holesize': [1.0, 1.0], 'PadSize': [2.56, 1.0], 'Shape': 'Rect'}
        ],
        'PadStyle': [
            {'Type': 'Pad1', 'holeDiam': 0.825, 'PadSize': 1.0},
            {'Type': 'Pad2', 'holeDiam': 0.825, 'PadSize': 1.2},
            {'Type': 'Pad3', 'holeDiam': 1.5, 'PadSize': 2.0}
        ],
        'ViaStyle': [
            {'Type': 'ViaS', 'holeDiam': 0.2, 'PadSize': [0.3]},
            {'Type': 'ViaS1', 'holeDiam': 0.4, 'PadSize': [1.0]},
            {'Type': 'ViaM', 'holeDiam': 0.7, 'PadSize': [1.2]},
            {'Type': 'ViaL', 'holeDiam': 1.6, 'PadSize': [2.0]}
        ],
        'Vias': [
            {'Type': 'ViaS', 'xc': 0.75, 'yc': -9.6},
            {'Type': 'ViaS', 'xc': 0.75, 'yc': -9.2},
            # Add more vias as required...
        ],
        'LayerDefs': [
            {'name': 'Top Assy', 'num': 10, 'type': 'NonSignal'},
            {'name': 'Top Silk', 'num': 6, 'type': 'NonSignal'},
            {'name': 'Top Mask', 'num': 4, 'type': 'NonSignal'},
            {'name': 'Top Paste', 'num': 8, 'type': 'NonSignal'},
            {'name': 'TOP', 'num': 1, 'type': 'Signal'},
            {'name': 'Bottom', 'num': 2, 'type': 'Signal'},
            {'name': 'Bot Mask', 'num': 5, 'type': 'NonSignal'},
            {'name': 'Bot Paste', 'num': 9, 'type': 'NonSignal'},
            {'name': 'Bot Silk', 'num': 7, 'type': 'NonSignal'},
            {'name': 'Bot Assy', 'num': 11, 'type': 'NonSignal'},
            {'name': 'Board', 'num': 3, 'type': 'NonSignal'}
        ],
        'LayerContents': [
            {'layerNum': 1, 'items': [
                {'type': 'polygon', 'x': [0.205, 0.205, 0.6, 0.6], 'y': [-10.0, 3.62, 3.72, 6.4]},
                {'type': 'line', 'x': [0.205, 0.455], 'y': [-10.0, -10.0], 'width': 0.1}
                # Add more layer contents as required...
            ]}
            # Add more layers as required...
        ]
    }

    # Call the function to generate the Altium PCB file
    altium_2_layer_component_writer("Library_1", pcb_data)
'''
