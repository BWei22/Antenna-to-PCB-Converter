def add_pcb_device(dev, temp_dev):
    TopText = dev['TopText']
    TopE = dev['TopE']
    BtmE = dev['BtmE']
    TopEpour = dev['TopEpour']
    BtmEpour = dev['BtmEpour']
    TopPaste = dev['TopPaste']
    TopMask = dev['TopMask']
    BtmMask = dev['BtmMask']
    BtmPaste = dev['BtmPaste']
    TopSilk = dev['TopSilk']
    BtmSilk = dev['BtmSilk']
    Vias = dev['Vias']
    SlotPads = dev['SlotPads']
    TopPads = dev['TopPads']
    BtmPads = dev['BtmPads']
    Outlines = dev['Outlines']
    Cutouts = dev['Cutouts']

    # ++++++++++++++++++++++++++++++++++++++++++++++

    field_list = temp_dev.keys()
    for field in field_list:
        if field == 'TopEpour':
            TopEpour = temp_dev['TopEpour']
        elif field == 'BtmEpour':
            BtmEpour = temp_dev['BtmEpour']
        elif field == 'TopE':
            mn = len(TopE)
            for item in temp_dev['TopE']:
                mn += 1
                TopE.append({'x': item['x'], 'y': item['y']})
        elif field == 'BtmE':
            mn = len(BtmE)
            for item in temp_dev['BtmE']:
                mn += 1
                BtmE.append({'x': item['x'], 'y': item['y']})
        elif field == 'TopMask':
            mn = len(TopMask)
            for item in temp_dev['TopMask']:
                mn += 1
                TopMask.append({'x': item['x'], 'y': item['y']})
        elif field == 'TopPaste':
            mn = len(TopPaste)
            for item in temp_dev['TopPaste']:
                mn += 1
                TopPaste.append({'x': item['x'], 'y': item['y']})
        elif field == 'BtmPaste':
            mn = len(BtmPaste)
            for item in temp_dev['BtmPaste']:
                mn += 1
                BtmPaste.append({'x': item['x'], 'y': item['y']})
        elif field == 'BtmMask':
            mn = len(BtmMask)
            for item in temp_dev['BtmMask']:
                mn += 1
                BtmMask.append({'x': item['x'], 'y': item['y']})
        elif field == 'TopSilk':
            mn = len(TopSilk)
            for item in temp_dev['TopSilk']:
                mn += 1
                TopSilk.append({'x': item['x'], 'y': item['y']})
        elif field == 'BtmSilk':
            mn = len(BtmSilk)
            for item in temp_dev['BtmSilk']:
                mn += 1
                BtmSilk.append({'x': item['x'], 'y': item['y']})
        elif field == 'Vias':
            mn = len(Vias)
            for item in temp_dev['Vias']:
                mn += 1
                Vias.append({
                    'xc': item['xc'],
                    'yc': item['yc'],
                    'R': item['R'],
                    'R0': item['R0'],
                    'Type': item['Type']
                })
        elif field == 'SlotPads':
            mn = len(SlotPads)
            for item in temp_dev['SlotPads']:
                mn += 1
                SlotPads.append({
                    'xc': item['xc'],
                    'yc': item['yc'],
                    'HoleSize': item['HoleSize'],
                    'PadSize': item['PadSize'],
                    'Type': item['Type'],
                    'Shape': item['Shape']
                })
        elif field == 'TopPads':
            mn = len(TopPads)
            for item in temp_dev['TopPads']:
                mn += 1
                TopPads.append({
                    'xc': item['xc'],
                    'yc': item['yc'],
                    'Type': item['Type'],
                    'Shape': item['Shape'],
                    'Layer': item['Layer'],
                    'HoleSize': item['HoleSize'],
                    'PadSize': item['PadSize']
                })
        elif field == 'BtmPads':
            mn = len(BtmPads)
            for item in temp_dev['BtmPads']:
                mn += 1
                BtmPads.append({
                    'xc': item['xc'],
                    'yc': item['yc'],
                    'Type': item['Type'],
                    'Shape': item['Shape'],
                    'Layer': item['Layer'],
                    'HoleSize': item['HoleSize'],
                    'PadSize': item['PadSize']
                })
        elif field == 'Outlines':
            mn = len(Outlines)
            for item in temp_dev['Outlines']:
                mn += 1
                Outlines.append({'x': item['x'], 'y': item['y']})
        elif field == 'Cutouts':
            mn = len(Cutouts)
            for item in temp_dev['Cutouts']:
                mn += 1
                Cutouts.append({'x': item['x'], 'y': item['y']})
                # Cutouts[mn]['z'] = item['z']  # Uncomment if 'z' field exists in Cutouts

    # ++++++++++++++++++++++++++++++++++++++++++++++

    dev['TopText'] = TopText
    dev['TopE'] = TopE
    dev['BtmE'] = BtmE
    dev['TopEpour'] = TopEpour
    dev['BtmEpour'] = BtmEpour
    dev['TopPaste'] = TopPaste
    dev['TopMask'] = TopMask
    dev['BtmMask'] = BtmMask
    dev['BtmPaste'] = BtmPaste
    dev['TopSilk'] = TopSilk
    dev['BtmSilk'] = BtmSilk
    dev['Vias'] = Vias
    dev['SlotPads'] = SlotPads
    dev['TopPads'] = TopPads
    dev['BtmPads'] = BtmPads
    dev['Outlines'] = Outlines
    dev['Cutouts'] = Cutouts

    return dev
