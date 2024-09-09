def definePCBfeatures(BoardData):
    PadData = BoardData['PadData']
    SlotData = BoardData['SlotData']
    ViaData = BoardData['ViaData']
    font = BoardData['font']

    PCB = {
        'TopText': [],
        'TopEpour': [],
        'BtmEpour': [],
        'TopE': [],
        'BtmE': [],
        'TopMask': [],
        'BtmMask': [],
        'TopPaste': [],
        'BtmPaste': [],
        'TopSilk': [],
        'BtmSilk': [],
        'TopPads': [],
        'BtmPads': [],
        'SlotPads': [],
        'Vias': [],
        'Outlines': [],
        'Cutouts': [],
        'fontHeight': font['Height'],
        'strokeWidth': font['strokeWidth'],
        'Boardinfo': {
            'Rpin': ViaData,
            'solderSwell': 0.1,
            'PadToPadClearance': 0.15,
            'PadToLineClearance': 0.15,
            'LineToLineClearance': 0.15,
            'ViaToPadClearance': 0.15,
            'ViaToLineClearance': 0.15,
            'ViaToViaClearance': 0.15,
            'pasteSwell': 0.0,
            'planeSwell': 0.5
        },
        'SlotStyle': [],
        'PadStyle': [],
        'ViaStyle': []
    }

    # Populate SlotStyle
    for m in range(len(SlotData)):
        PCB['SlotStyle'].append({
            'Type': SlotData[m][0],
            'Shape': SlotData[m][1],
            'HoleSize': SlotData[m][2],
            'PadSize': SlotData[m][3]
        })

    # Populate PadStyle
    for m in range(len(PadData)):
        PCB['PadStyle'].append({
            'Type': PadData[m][0],
            'Shape': PadData[m][1],
            'Layer': PadData[m][2],
            'HoleSize': PadData[m][3],
            'PadSize': PadData[m][4]
        })

    # Populate ViaStyle
    for m in range(len(ViaData)):
        PCB['ViaStyle'].append({
            'Type': ViaData[m][0],
            'holeDiam': ViaData[m][1] * 2,
            'PadSize': ViaData[m][2] * 2
        })

    return PCB

'''
# Example usage:
BoardData = {
    'PadData': [
        ('Pad1', 'Round', 'Top', 0.05, 0.1),
        ('Pad2', 'Square', 'Bottom', 0.06, 0.12)
    ],
    'SlotData': [
        ('Slot1', 'Rectangle', 0.1, 0.15),
        ('Slot2', 'Circle', 0.08, 0.12)
    ],
    'ViaData': [
        ('Via1', 0.07, 0.14),
        ('Via2', 0.08, 0.16)
    ],
    'font': {
        'Height': 0.2,
        'strokeWidth': 0.01
    }
}

PCB = definePCBfeatures(BoardData)
print(PCB)
'''