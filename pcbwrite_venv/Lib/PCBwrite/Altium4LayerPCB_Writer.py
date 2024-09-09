def Altium4LayerPCB_Writer(filename, PCB):
    with open(filename, 'w') as FID:
        pcb_HEAD(FID)
        pcb_LIB(FID, PCB)
        pcb_NETLIST(FID)
        pcb_DESIGN(FID, PCB)


def pcb_HEAD(FID):
    FID.write('(head (cache "C:\\Users\\jj\\")) \n')
    FID.write(' \n')


def pcb_LIB(FID, PCB):
    FID.write('(libDef \n')
    FID.write('  (lib "C:\\Users\\jj\\Desktop\\Duo-1-SingleChannel.PcbLib") \n')
    FID.write('  (lib "C:\\Users\\jj\\Desktop\\Duo-1-MotherBoard.PcbLib") \n')
    FID.write('  (lib "C:\\Users\\jj\\Desktop\\Ritn\\SMD.passive.PcbLib") \n')
    FID.write('  (lib "C:\\Users\\jj\\Desktop\\Ritn\\Connectors.PcbLib") \n')
    FID.write('  (lib "C:\\Users\\jj\\Desktop\\Ritn\\Inductor.PcbLib") \n')
    FID.write('  (lib "C:\\Users\\jj\\Desktop\\Ritn\\Capacitors.PcbLib") \n')
    FID.write('  (lib "C:\\Users\\jj\\Desktop\\Ritn\\IC-LED.PcbLib") \n')
    FID.write(') \n')
    FID.write(' \n')


def pcb_NETLIST(FID):
    FID.write('(netlist \n')
    FID.write('  (cache "C:\\Users\\jj\\") \n')
    FID.write(') \n')
    FID.write(' \n')


def pcb_DESIGN(FID, PCB):
    import datetime
    date = datetime.date.today().strftime("%Y-%m-%d")

    FID.write('(pcbDesign "PcbDesign_1" \n')
    FID.write('  (pcbDesignHeader \n')
    FID.write('    (workspaceSize 812.8mm 812.8mm) \n')
    FID.write('    (gridDfns \n')
    FID.write('      (grid "0.1mm") \n')
    FID.write('    ) \n')
    FID.write('    (designInfo \n')
    FID.write(f'      (fieldSet "(Default)" \n')
    FID.write(f'        (fieldDef "Date" "{date}") \n')
    FID.write('        (fieldDef "Time" "2:46:30 PM") \n')
    FID.write('        (fieldDef "Author" "") \n')
    FID.write('        (fieldDef "Revision" "") \n')
    FID.write('        (fieldDef "Title" "") \n')
    FID.write('        (fieldDef "Approved By" "") \n')
    FID.write('        (fieldDef "Checked By" "") \n')
    FID.write('        (fieldDef "Company Name" "") \n')
    FID.write('        (fieldDef "Drawing Number" "") \n')
    FID.write('        (fieldDef "Drawn By" "") \n')
    FID.write('        (fieldDef "Engineer" "") \n')
    FID.write('      ) \n')
    FID.write('    ) \n')
    FID.write(f'    (solderSwell {PCB["Boardinfo"]["solderSwell"]:.3f}mm) \n')
    FID.write(f'    (pasteSwell {PCB["Boardinfo"]["pasteSwell"]:.3f}mm) \n')
    FID.write(f'    (planeSwell {PCB["Boardinfo"]["planeSwell"]:.3f}mm) \n')
    FID.write('  ) \n')
    FID.write('  \n')

    layer_definitions = [
        {"name": "Top Assy", "number": 10, "type": "NonSignal"},
        {"name": "Top Mask", "number": 4, "type": "NonSignal"},
        {"name": "TOP", "number": 1, "type": "Signal"},
        {"name": "PLANE1", "number": 21, "type": "Signal"},
        {"name": "PLANE2", "number": 22, "type": "Signal"},
        {"name": "Bottom", "number": 2, "type": "Signal"},
        {"name": "Bot Mask", "number": 5, "type": "NonSignal"},
        {"name": "Bot Assy", "number": 11, "type": "NonSignal"},
        {"name": "Board", "number": 3, "type": "NonSignal"},
    ]

    for layer_def in layer_definitions:
        FID.write(f'  (layerDef "{layer_def["name"]}" \n')
        FID.write(f'    (layerNum {layer_def["number"]}) \n')
        FID.write(f'    (layerType {layer_def["type"]}) \n')
        FID.write('    (fieldSetRef "(Default)") \n')
        FID.write('  ) \n')
        FID.write('  \n')

    FID.write(f'  (layerDef "TOP" \n')
    FID.write(f'    (layerNum 1) \n')
    FID.write(f'    (layerType Signal) \n')
    FID.write(f'    (attr "PadToPadClearance" "{PCB["Boardinfo"]["PadToPadClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "PadToLineClearance" "{PCB["Boardinfo"]["PadToLineClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "LineToLineClearance" "{PCB["Boardinfo"]["LineToLineClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "ViaToPadClearance" "{PCB["Boardinfo"]["ViaToPadClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "ViaToLineClearance" "{PCB["Boardinfo"]["ViaToLineClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "ViaToViaClearance" "{PCB["Boardinfo"]["ViaToViaClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write('    (fieldSetRef "(Default)") \n')
    FID.write('  ) \n')
    FID.write('  \n')

    FID.write(f'  (layerDef "BOTTOM" \n')
    FID.write(f'    (layerNum 2) \n')
    FID.write(f'    (layerType Signal) \n')
    FID.write(f'    (attr "PadToPadClearance" "{PCB["Boardinfo"]["PadToPadClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "PadToLineClearance" "{PCB["Boardinfo"]["PadToLineClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "LineToLineClearance" "{PCB["Boardinfo"]["LineToLineClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "ViaToPadClearance" "{PCB["Boardinfo"]["ViaToPadClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "ViaToLineClearance" "{PCB["Boardinfo"]["ViaToLineClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write(f'    (attr "ViaToViaClearance" "{PCB["Boardinfo"]["ViaToViaClearance"]:.3f}mm" (textStyleRef "(Default)") (constraintUnits mil) ) \n')
    FID.write('    (fieldSetRef "(Default)") \n')
    FID.write('  ) \n')
    FID.write('  \n')

    FID.write('  (multiLayer \n')
    for via in PCB["Vias"]:
        FID.write(f'    (via (viaStyleRef "{via["Type"]}") (pt {via["xc"]:.3f}mm {via["yc"]:.3f}mm) ) \n')
    FID.write('  ) \n')
    FID.write('  \n')

    for pad in PCB["TopPads"]:
        FID.write(f'  (pad (padStyleRef "{pad["Type"]}") (pt {pad["xc"]:.3f}mm {pad["yc"]:.3f}mm) ) \n')
    FID.write('  \n')

    for e in PCB["TopE"]:
        pcb_Polyline(FID, e["x"], e["y"], 0.0)

    for e in PCB["BtmE"]:
        pcb_Polyline(FID, e["x"], e["y"], 0.0)

    for outline in PCB["TopOutlines"]:
        pcb_Polyline(FID, outline["x"], outline["y"], 0.0)

    for outline in PCB["BtmOutlines"]:
        pcb_Polyline(FID, outline["x"], outline["y"], 0.0)

    FID.write(')  \n')
    FID.write('  \n')


def pcb_Polyline(FID, xp, yp, w):
    FID.write('(pcbLine \n')
    FID.write(f'  (pt {xp[0]:.3f}mm {yp[0]:.3f}mm) \n')
    FID.write(f'  (pt {xp[1]:.3f}mm {yp[1]:.3f}mm) \n')
    FID.write(f'  (width {w:.3f}mm) \n')
    FID.write(')  \n')
    FID.write('  \n')

'''
# Example usage:
PCB = {
    "Boardinfo": {
        "solderSwell": 0.100,
        "pasteSwell": 0.050,
        "planeSwell": 0.050,
        "PadToPadClearance": 0.200,
        "PadToLineClearance": 0.150,
        "LineToLineClearance": 0.150,
        "ViaToPadClearance": 0.150,
        "ViaToLineClearance": 0.150,
        "ViaToViaClearance": 0.150,
    },
    "Vias": [{"Type": "via1", "xc": 1.0, "yc": 2.0}],
    "TopPads": [{"Type": "pad1", "xc": 3.0, "yc": 4.0}],
    "TopE": [{"x": [1, 2, 3], "y": [4, 5, 6]}],
    "BtmE": [{"x": [7, 8, 9], "y": [10, 11, 12]}],
    "TopOutlines": [{"x": [13, 14, 15], "y": [16, 17, 18]}],
    "BtmOutlines": [{"x": [19, 20, 21], "y": [22, 23, 24]}],
}

Altium4LayerPCB_Writer("output.txt", PCB)
'''