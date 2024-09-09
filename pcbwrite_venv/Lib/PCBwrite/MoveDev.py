def MoveDev(Dev, Offset):
    
    FieldList = Dev.keys()
    for m in FieldList:
        if m == 'TopEpour':
            if Dev['TopEpour'] is not None:
                Dev['TopEpour']['x'] += Offset[0]
                Dev['TopEpour']['y'] += Offset[1]

        elif m == 'BtmEpour':
            if Dev['BtmEpour'] is not None:
                Dev['BtmEpour']['x'] += Offset[0]
                Dev['BtmEpour']['y'] += Offset[1]

        elif m == 'TopE':
            if Dev['TopE'] is not None:
                for item in Dev['TopE']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'BtmE':
            if Dev['BtmE'] is not None:
                for item in Dev['BtmE']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'TopMask':
            if Dev['TopMask'] is not None:
                for item in Dev['TopMask']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'BtmMask':
            if Dev['BtmMask'] is not None:
                for item in Dev['BtmMask']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'TopPaste':
            if Dev['TopPaste'] is not None:
                for item in Dev['TopPaste']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'BtmPaste':
            if Dev['BtmPaste'] is not None:
                for item in Dev['BtmPaste']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'TopSilk':
            if Dev['TopSilk'] is not None:
                for item in Dev['TopSilk']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'BtmSilk':
            if Dev['BtmSilk'] is not None:
                for item in Dev['BtmSilk']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'Vias':
            if Dev['Vias'] is not None:
                for item in Dev['Vias']:
                    item['xc'] += Offset[0]
                    item['yc'] += Offset[1]

        elif m == 'SlotPads':
            if Dev['SlotPads'] is not None:
                for item in Dev['SlotPads']:
                    item['xc'] += Offset[0]
                    item['yc'] += Offset[1]

        elif m == 'TopPads':
            if Dev['TopPads'] is not None:
                for item in Dev['TopPads']:
                    item['xc'] += Offset[0]
                    item['yc'] += Offset[1]

        elif m == 'BtmPads':
            if Dev['BtmPads'] is not None:
                for item in Dev['BtmPads']:
                    item['xc'] += Offset[0]
                    item['yc'] += Offset[1]

        elif m == 'Outlines':
            if Dev['Outlines'] is not None:
                for item in Dev['Outlines']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

        elif m == 'Cutouts':
            if Dev['Cutouts'] is not None:
                for item in Dev['Cutouts']:
                    item['x'] += Offset[0]
                    item['y'] += Offset[1]

    return Dev
