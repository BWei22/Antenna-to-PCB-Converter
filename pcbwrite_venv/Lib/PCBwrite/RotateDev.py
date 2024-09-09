import math

def RotateDev(Dev, RotationAngle):

    ARot = RotationAngle * math.pi / 180

    if Dev.get('TopEpour'):
        xtmp = Dev['TopEpour']['x']
        ytmp = Dev['TopEpour']['y']
        Dev['TopEpour']['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['TopEpour']['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    if Dev.get('BtmEpour'):
        xtmp = Dev['BtmEpour']['x']
        ytmp = Dev['BtmEpour']['y']
        Dev['BtmEpour']['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['BtmEpour']['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['Outlines'])):
        xtmp = Dev['Outlines'][m]['x']
        ytmp = Dev['Outlines'][m]['y']
        Dev['Outlines'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['Outlines'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['TopE'])):
        xtmp = Dev['TopE'][m]['x']
        ytmp = Dev['TopE'][m]['y']
        Dev['TopE'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['TopE'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['BtmE'])):
        xtmp = Dev['BtmE'][m]['x']
        ytmp = Dev['BtmE'][m]['y']
        Dev['BtmE'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['BtmE'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['TopMask'])):
        xtmp = Dev['TopMask'][m]['x']
        ytmp = Dev['TopMask'][m]['y']
        Dev['TopMask'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['TopMask'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['BtmMask'])):
        xtmp = Dev['BtmMask'][m]['x']
        ytmp = Dev['BtmMask'][m]['y']
        Dev['BtmMask'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['BtmMask'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['TopSilk'])):
        xtmp = Dev['TopSilk'][m]['x']
        ytmp = Dev['TopSilk'][m]['y']
        Dev['TopSilk'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['TopSilk'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['BtmSilk'])):
        xtmp = Dev['BtmSilk'][m]['x']
        ytmp = Dev['BtmSilk'][m]['y']
        Dev['BtmSilk'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['BtmSilk'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['Cutouts'])):
        xtmp = Dev['Cutouts'][m]['x']
        ytmp = Dev['Cutouts'][m]['y']
        Dev['Cutouts'][m]['x'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['Cutouts'][m]['y'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['Vias'])):
        xtmp = Dev['Vias'][m]['xc']
        ytmp = Dev['Vias'][m]['yc']
        Dev['Vias'][m]['xc'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['Vias'][m]['yc'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['TopPads'])):
        xtmp = Dev['TopPads'][m]['xc']
        ytmp = Dev['TopPads'][m]['yc']
        Dev['TopPads'][m]['xc'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['TopPads'][m]['yc'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    for m in range(len(Dev['BtmPads'])):
        xtmp = Dev['BtmPads'][m]['xc']
        ytmp = Dev['BtmPads'][m]['yc']
        Dev['BtmPads'][m]['xc'] = xtmp * math.cos(ARot) - ytmp * math.sin(ARot)
        Dev['BtmPads'][m]['yc'] = xtmp * math.sin(ARot) + ytmp * math.cos(ARot)

    return Dev
