def add_4_layer_pcb_device(dev, temp_dev):
    TopE = dev['TopE']
    In1E = dev['In1E']
    In2E = dev['In2E']
    BtmE = dev['BtmE']
    TopSilk = dev['TopSilk']
    BtmSilk = dev['BtmSilk']
    TopOutlines = dev['TopOutlines']
    BtmOutlines = dev['BtmOutlines']
    Vias = dev['Vias']

    # ++++++++++++++++++++++++++++++++++++++++++++++

    field_list = temp_dev.keys()
    for field in field_list:
        if field == 'TopE':
            mn = len(TopE)
            for item in temp_dev['TopE']:
                mn += 1
                TopE.append({'x': item['x'], 'y': item['y']})
        elif field == 'In1E':
            mn = len(In1E)
            for item in temp_dev['In1E']:
                mn += 1
                In1E.append({'x': item['x'], 'y': item['y']})
        elif field == 'In2E':
            mn = len(In2E)
            for item in temp_dev['In2E']:
                mn += 1
                In2E.append({'x': item['x'], 'y': item['y']})
        elif field == 'BtmE':
            mn = len(BtmE)
            for item in temp_dev['BtmE']:
                mn += 1
                BtmE.append({'x': item['x'], 'y': item['y']})
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
        elif field == 'TopOutlines':
            mn = len(TopOutlines)
            for item in temp_dev['TopOutlines']:
                mn += 1
                TopOutlines.append({'x': item['x'], 'y': item['y']})
        elif field == 'BtmOutlines':
            mn = len(BtmOutlines)
            for item in temp_dev['BtmOutlines']:
                mn += 1
                BtmOutlines.append({'x': item['x'], 'y': item['y']})
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
    
    # ++++++++++++++++++++++++++++++++++++++++++++++

    dev['TopE'] = TopE
    dev['In1E'] = In1E
    dev['In2E'] = In2E
    dev['BtmE'] = BtmE
    dev['Vias'] = Vias
    dev['TopSilk'] = TopSilk
    dev['TopOutlines'] = TopOutlines
    dev['BtmOutlines'] = BtmOutlines

    return dev
