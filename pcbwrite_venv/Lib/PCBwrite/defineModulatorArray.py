import numpy as np
import matplotlib.pyplot as plt

def defineModulatorArray(BoardData, Offset, L_LNB):
    PadData = BoardData['PadData']
    ViaData = BoardData['ViaData']
    font = BoardData['font']
    Narray = BoardData['Narray'] // 2

    # Initialize Mod structure
    Mod = {}
    Mod['XLcut'] = 6.5
    Mod['XRcut'] = L_LNB + 6.5
    Mod['Ycut'] = 8
    Mod['Xq'] = 0.5
    Mod['Dxy'] = 0.2
    Mod['Rlnb'] = 0.3
    Mod['Yspacing'] = 0.25
    Mod['Xlnb'] = 0.45
    Mod['Ylnb'] = 0.24
    Mod['Wlnb'] = 0.01
    Mod['Glnb'] = 0.015
    Mod['Wflnb'] = 0.03
    Mod['Gflnb'] = 0.035
    Mod['Llnb'] = L_LNB
    Mod['Slnb'] = 0.5
    Mod['Tlnb'] = 1.0
    Mod['Wstrip'] = 0.006

    Nr = 61
    phi1 = np.linspace(np.pi, 1.5 * np.pi, Nr)
    phi2 = np.linspace(1.5 * np.pi, np.pi, Nr)
    phi3 = np.linspace(np.pi / 2, 0, Nr)
    phi4 = np.linspace(0, np.pi / 2, Nr)

    # Initialize MS and OptWG lists
    MS = []
    OptWG = []

    # Loop over Narray
    for m in range(1, Narray + 2):
        xa = -(Narray / 2 + 0.5 - m) * Mod['Xq']
        xb = xa + Mod['Llnb']
        y0 = 0.5 * (Mod['Ycut'] - (Narray - 1) * Mod['Yspacing']) + (m - 1) * Mod['Yspacing']
        y1 = y0 - Mod['Slnb'] - Mod['Tlnb']
        y2 = y0 - Mod['Slnb']
        y3 = y0 + Mod['Slnb']
        y4 = y0 + Mod['Slnb'] + Mod['Tlnb']
        y5 = Mod['Ycut'] - 0.05

        if m == 1:
            XA = [xb - Mod['Gflnb'], xb - Mod['Gflnb'], xb - Mod['Glnb'], xb - Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi4), xa + Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi2), xa - Mod['Glnb'], xa - Mod['Gflnb'], xa - Mod['Gflnb'], -Mod['XLcut'], -Mod['XLcut'], xb - Mod['Gflnb']]
            YA = [0, y1, y2, y0 - Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi4), y0 + Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi2), y3, y4, y5, y5, 0, 0]
        else:
            XA = [xb - Mod['Gflnb'], xb - Mod['Gflnb'], xb - Mod['Glnb'], xb - Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi4), xa + Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi2), xa - Mod['Glnb'], xa - Mod['Gflnb'], xa - Mod['Gflnb'], xa - Mod['Xlnb'], xa - Mod['Xlnb'] + Mod['Dxy'], xa - Mod['Xlnb'] + Mod['Dxy'] + Mod['Dxy'], xb - Mod['Xlnb'], xb - Mod['Gflnb']]
            YA = [0, y1, y2, y0 - Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi4), y0 + Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi2), y3, y4, y5, y5, y0 - Mod['Ylnb'] + Mod['Dxy'], y0 - Mod['Ylnb'], y0 - Mod['Ylnb'] - Mod['Dxy'], y0 - Mod['Ylnb'] - Mod['Dxy'] - Mod['Dxy'], 0, 0]

        MS.append({'x': XA, 'y': YA})

        XB = [xb + Mod['Wflnb'], xb + Mod['Wflnb'], xb + Mod['Wlnb'], xb - Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi4), xa + Mod['Rlnb'] + Mod['Glnb'] * np.cos(phi2), xa + Mod['Wlnb'], xa + Mod['Wflnb'], xa + Mod['Wflnb']]
        YB = [0, y1, y2, y0 - Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi4), y0 + Mod['Rlnb'] + Mod['Glnb'] * np.sin(phi2), y3, y4, y5]
        XB.extend([xa - Mod['Wflnb'], xa - Mod['Wflnb'], xa - Mod['Wlnb'], xa + Mod['Rlnb'] + Mod['Wlnb'] * np.cos(phi1), xb - Mod['Rlnb'] + Mod['Glnb'] * np.cos(phi3), xb - Mod['Wlnb'], xb - Mod['Wflnb'], xb - Mod['Wflnb'], xb + Mod['Wflnb']])
        YB.extend([y5, y4, y3, y0 + Mod['Rlnb'] + Mod['Wlnb'] * np.sin(phi1), y0 - Mod['Rlnb'] + Mod['Glnb'] * np.sin(phi3), y2, y1, 0, 0])

        MS.append({'x': XB, 'y': YB})

        if m == Narray + 1:
            XC = [xa + Mod['Gflnb'], xa + Mod['Gflnb'], xa + Mod['Glnb'], xa + Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi1), xb - Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi3), xb + Mod['Glnb'], xb + Mod['Gflnb'], xb + Mod['Gflnb'], Mod['XRcut'], Mod['XRcut'], xa + Mod['Gflnb']]
            YC = [y5, y4, y3, y0 + Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi1), y0 - Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi3), y2, y1, 0, 0, y5, y5]
        else:
            XC = [xa + Mod['Gflnb'], xa + Mod['Gflnb'], xa + Mod['Glnb'], xa + Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi1), xb - Mod['Rlnb'] + Mod['Rlnb'] * np.cos(phi3), xb + Mod['Glnb'], xb + Mod['Gflnb'], xb + Mod['Gflnb'], xb + Mod['Xlnb'], xb + Mod['Xlnb'] - Mod['Dxy'], xb + Mod['Xlnb'] - Mod['Dxy'] - Mod['Dxy'], xa + Mod['Xlnb'], xa + Mod['Gflnb']]
            YC = [y5, y4, y3, y0 + Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi1), y0 - Mod['Rlnb'] + Mod['Rlnb'] * np.sin(phi3), y2, y1, 0, 0, y0 + Mod['Ylnb'] - Mod['Dxy'], y0 + Mod['Ylnb'], y0 + Mod['Ylnb'] + Mod['Dxy'], y0 + Mod['Ylnb'] + Mod['Dxy'] + Mod['Dxy'], y5, y5]

        MS.append({'x': XC, 'y': YC})

        # Append OptWG for plotting
        OptWG.append({'x': [-Mod['XLcut'], Mod['XRcut'], Mod['XRcut'], -Mod['XLcut'], -Mod['XLcut']], 'y': [-1, -1, 1, 1, -1] * Mod['Wstrip'] / 2 + y0})

    # Define ModBNDx and ModBNDy
    ModBNDx = [-Mod['XLcut'], Mod['XRcut'], Mod['XRcut'], -Mod['XLcut'], -Mod['XLcut']]
    ModBNDy = [0, 0, Mod['Ycut'], Mod['Ycut'], 0]

    # Create TempDev dictionary
    TempDev = {
        'TopSilk': [{'x': OptWG[m]['x'], 'y': OptWG[m]['y']} for m in range(len(OptWG))],
        'TopE': [{'x': MS[m]['x'], 'y': MS[m]['y']} for m in range(len(MS))],
        'Outlines': [{'x': ModBNDx, 'y': ModBNDy}]
    }

    # Example function definitions not provided, placeholder for equivalent Python functions
    # Dev0 = definePCBfeatures(PadData, ViaData, font)
    # Dev0 = AddPCBDevice(Dev0, TempDev)
    # Dev0 = MoveDev(Dev0, Offset)

    Ldev = max(TempDev['Outlines'][0]['x']) - min(TempDev['Outlines'][0]['x'])
    Wdev = max(TempDev['Outlines'][0]['y']) - min(TempDev['Outlines'][0]['y'])
    print(f"Ldev3={Ldev}     Wdev3={Wdev}")

    # Plotting code (matplotlib example)
    plt.figure(123)
    for m in range(len(TempDev['TopE'])):
        plt.fill(TempDev['TopE'][m]['x'], TempDev['TopE'][m]['y'], facecolor='c')
    for m in range(len(TempDev['TopSilk'])):
        plt.plot(TempDev['TopSilk'][m]['x'], TempDev['TopSilk'][m]['y'], color='y')
    for m in range(len(OptWG)):
        plt.plot(OptWG[m]['x'], OptWG[m]['y'], color='g')
    plt.plot(TempDev['Outlines'][0]['x'], TempDev['Outlines'][0]['y'], color='k', linewidth=1)
    plt.axis('equal')
    plt.show()

'''
# Example usage:
BoardData = {
    'PadData': [
        ('Pad1', 0.05, 0.1),
        ('Pad2', 0.06, 0.12)
    ],
    'ViaData': [
        ('TBVia1', 0.07, 0.14),
        ('BBVia2', 0.08, 0.16)
    ],
    'font': {
        'Height': 0.2,
        'strokeWidth': 0.01
    },
    'Narray': 4
}

Offset = 10
L_LNB = 20

defineModulatorArray(BoardData, Offset, L_LNB)
'''