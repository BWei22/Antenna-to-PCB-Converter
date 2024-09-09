def add_pcblib_dev(dev, temp_dev):
    TopE = dev['TopE']
    BtmE = dev['BtmE']
    TopMask = dev['TopMask']
    BtmMask = dev['BtmMask']
    TopSilk = dev['TopSilk']
    BtmSilk = dev['BtmSilk']
    Vias = dev['Vias']
    Pads = dev['TopPads']

    # ++++++++++++++++++++++++++++++++++++++++++++++

    field_list = temp_dev.keys()
    for field in field_list:
        if field == 'TopE':
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
                    'Type': item['Type']
                })
        elif field == 'TopPads':
            mn = len(Pads)
            for item in temp_dev['TopPads']:
                mn += 1
                Pads.append({
                    'xc': item['xc'],
                    'yc': item['yc'],
                    'R': item['R'],
                    'Type': item['Type']
                })

    # ++++++++++++++++++++++++++++++++++++++++++++++

    dev['TopE'] = TopE
    dev['BtmE'] = BtmE
    dev['TopMask'] = TopMask
    dev['BtmMask'] = BtmMask
    dev['TopSilk'] = TopSilk
    dev['BtmSilk'] = BtmSilk
    dev['Vias'] = Vias
    dev['TopPads'] = Pads

    return dev
