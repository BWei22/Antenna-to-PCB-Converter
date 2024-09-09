def define4LayerPCBfeatures(PadData, ViaData, font):
    PCB = {
        "TopText": [],
        "TopE": [],
        "In1E": [],
        "In2E": [],
        "BtmE": [],
        "Vias": [],
        "Pads": [],
        "TopOutlines": [],
        "BtmOutlines": [],
        "TopSilk": [],
        "BtmSilk": [],
        "fontHeight": font["Height"],
        "strokeWidth": font["strokeWidth"],
        "Boardinfo": {
            "Rpin": ViaData,
            "solderSwell": 0.1,
            "PadToPadClearance": 0.15,
            "PadToLineClearance": 0.15,
            "LineToLineClearance": 0.15,
            "ViaToPadClearance": 0.15,
            "ViaToLineClearance": 0.15,
            "ViaToViaClearance": 0.15,
            "pasteSwell": 0.0,
            "planeSwell": 0.5,
        },
    }

    # Processing PadData
    for m in range(len(PadData)):
        PCB["Pads"].append({
            "Type": f"NonPlated{PadData[m][0]}",
            "holeDiam": PadData[m][1] * 2,
            "PadSize": PadData[m][2] * 2,
        })
        PCB["Pads"].append({
            "Type": f"Plated{PadData[m][0]}",
            "holeDiam": PadData[m][1] * 2,
            "PadSize": PadData[m][2] * 2,
        })

    # Processing ViaData
    for m in range(len(ViaData)):
        ViaType = ViaData[m][0]
        if ViaType[:2] == 'TB':
            startRange = 1
            endRange = 21
        elif ViaType[:2] == 'BB':
            startRange = 21
            endRange = 2
        else:
            startRange = 1
            endRange = 2

        PCB["Vias"].append({
            "Type": ViaType,
            "startRange": startRange,
            "endRange": endRange,
            "holeDiam": ViaData[m][1] * 2,
            "PadSize": ViaData[m][2] * 2,
        })

    return PCB

'''
# Example usage:
PadData = [
    ("Pad1", 0.05, 0.1),
    ("Pad2", 0.06, 0.12),
]

ViaData = [
    ("TBVia1", 0.07, 0.14),
    ("BBVia2", 0.08, 0.16),
]

font = {
    "Height": 0.2,
    "strokeWidth": 0.01,
}

PCB = define4LayerPCBfeatures(PadData, ViaData, font)
print(PCB)
'''