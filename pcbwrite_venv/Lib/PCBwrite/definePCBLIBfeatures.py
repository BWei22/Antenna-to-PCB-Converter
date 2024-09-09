def definePCBLIBfeatures(PadData, ViaData):
    PCB = {
        'TopText': [],
        'TopE': [],
        'BtmE': [],
        'TopMask': [],
        'BtmMask': [],
        'TopSilk': [],
        'BtmSilk': [],
        'TopPads': [],
        'BtmPads': [],
        'Vias': [],
        'PadStyle': [],
        'ViaStyle': []
    }

    # Populate PadStyle
    for m in range(len(PadData)):
        PCB['PadStyle'].append({
            'Type': f"NonPlated{ViaData[m][0]}",
            'holeDiam': 2 * PadData[m][1],
            'PadSize': 2 * PadData[m][2]
        })
        PCB['PadStyle'].append({
            'Type': f"Plated{ViaData[m][0]}",
            'holeDiam': 2 * PadData[m][1],
            'PadSize': 2 * PadData[m][2]
        })

    # Populate ViaStyle
    for m in range(len(ViaData)):
        PCB['ViaStyle'].append({
            'Type': ViaData[m][0],
            'holeDiam': 2 * ViaData[m][1],
            'PadSize': 2 * ViaData[m][2]
        })

    return PCB
'''
# Example usage:
PadData = [
    ('Pad1', 0.05, 0.1),
    ('Pad2', 0.06, 0.12)
]

ViaData = [
    ('Via1', 0.07, 0.14),
    ('Via2', 0.08, 0.16)
]

PCB = definePCBLIBfeatures(PadData, ViaData)
print(PCB)
'''