import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(0, 2*np.pi, 25)

def DrawPCBDev(Dev, Nfig, DisplayFlag):
    TopE = Dev['TopE']
    TopEpour = Dev['TopEpour']
    BtmE = Dev['BtmE']
    TopMask = Dev['TopMask']
    BtmMask = Dev['BtmMask']
    TopSilk = Dev['TopSilk']
    BtmSilk = Dev['BtmSilk']
    TopPaste = Dev['TopPaste']
    BtmPaste = Dev['BtmPaste']
    SlotPads = Dev['SlotPads']
    TopPads = Dev['TopPads']
    BtmPads = Dev['BtmPads']
    Outlines = Dev['Outlines']
    Cutouts = Dev['Cutouts']
    Vias = Dev['Vias']

    # Initialize figure
    plt.figure(Nfig)
    if DisplayFlag == 0:
        plt.clf()
    plt.axis('equal')

    # Plot BtmMask
    for m in range(len(BtmMask)):
        plt.fill(BtmMask[m]['x'], BtmMask[m]['y'], 'c')
    plt.title('BtmMask')

    # Plot BtmE
    for m in range(len(BtmE)):
        plt.fill(BtmE[m]['x'], BtmE[m]['y'], 'g')
    plt.title('BtmE')

    # Plot TopE
    for m in range(len(TopE)):
        plt.fill(TopE[m]['x'], TopE[m]['y'], 'y', alpha=0.3)
    plt.title('TopE')

    # Plot TopEpour
    for m in range(len(TopEpour)):
        plt.fill(TopEpour[m]['x'], TopEpour[m]['y'], 'c', alpha=0.2)
    plt.title('TopEpour')

    # Plot TopMask
    for m in range(len(TopMask)):
        plt.fill(TopMask[m]['x'], TopMask[m]['y'], 'm', alpha=0.3)
    plt.title('TopMask')

    # Plot TopSilk
    for m in range(len(TopSilk)):
        plt.plot(TopSilk[m]['x'], TopSilk[m]['y'], color='c', linewidth=2)

    # Plot SlotPads
    phi1 = np.linspace(-0.5 * np.pi, 0.5 * np.pi, 15)
    phi2 = np.linspace(0.5 * np.pi, 1.5 * np.pi, 15)
    for m in range(len(SlotPads)):
        HS = SlotPads[m]['HoleSize'] / 2
        PS = SlotPads[m]['PadSize'] / 2
        xc = PS[0] - PS[1]
        if SlotPads[m]['Shape'] == 'Oval':
            xi = SlotPads[m]['xc'] + [0, xc + PS[1] * np.cos(phi1), -xc + PS[1] * np.cos(phi2), 0]
            yi = SlotPads[m]['yc'] + [-PS[1], PS[1] * np.sin(phi1), PS[1] * np.sin(phi2), -PS[1]]
            xo = SlotPads[m]['xc'] + [0, xc + HS[1] * np.cos(phi1), -xc + HS[1] * np.cos(phi2), 0]
            yo = SlotPads[m]['yc'] + [-HS[1], HS[1] * np.sin(phi1), HS[1] * np.sin(phi2), -HS[1]]
        elif SlotPads[m]['Shape'] == 'Rect':
            xi = SlotPads[m]['xc'] + np.array([-1, 1, 1, -1, -1]) * PS[0]
            yi = SlotPads[m]['yc'] + np.array([-1, -1, 1, 1, -1]) * PS[1]
            xo = SlotPads[m]['xc'] + np.array([-1, 1, 1, -1, -1]) * HS[0]
            yo = SlotPads[m]['yc'] + np.array([-1, -1, 1, 1, -1]) * HS[1]
        plt.fill(xi, yi, 'y')
        plt.fill(xo, yo, 'w')

    # Plot TopPads
    for m in range(len(TopPads)):
        HoleSize = TopPads[m]['HoleSize'] / 2
        PadSize = TopPads[m]['PadSize'] / 2
        if TopPads[m]['Layer'] == 'THRU':
            xx = TopPads[m]['xc'] + np.concatenate([HoleSize[0] * np.cos(phi), PadSize[0] * np.cos(phi[::-1]), [HoleSize[0]]])
            yy = TopPads[m]['yc'] + np.concatenate([HoleSize[0] * np.sin(phi), PadSize[0] * np.sin(phi[::-1]), [0]])
        elif TopPads[m]['Layer'] == 'SMT':
            if TopPads[m]['Shape'] == 'Oval':
                xx = TopPads[m]['xc'] + np.concatenate([HoleSize[0] * np.cos(phi), PadSize[0] * np.cos(phi[::-1]), [HoleSize[0]]])
                yy = TopPads[m]['yc'] + np.concatenate([HoleSize[0] * np.sin(phi), PadSize[0] * np.sin(phi[::-1]), [0]])
            elif TopPads[m]['Shape'] == 'Rect':
                xx = TopPads[m]['xc'] + np.array([-1, 1, 1, -1, -1]) * PadSize[0]
                yy = TopPads[m]['yc'] + np.array([-1, -1, 1, 1, -1]) * PadSize[1]
        plt.fill(xx, yy, 'w')

    # Plot Outlines
    if Outlines:
        plt.plot(Outlines[0]['x'], Outlines[0]['y'], color='m', linewidth=2)
        for m in range(1, len(Outlines)):
            plt.plot(Outlines[m]['x'], Outlines[m]['y'], color='m', linewidth=2)

    # Plot Cutouts
    if Cutouts:
        plt.plot(Cutouts[0]['x'], Cutouts[0]['y'], color='k', linewidth=2)
        for m in range(1, len(Cutouts)):
            plt.plot(Cutouts[m]['x'], Cutouts[m]['y'], color='k', linewidth=2)

    # Plot Vias
    for m in range(len(Vias)):
        Rvia = Vias[m]['R']
        Rvia0 = Vias[m]['R0']
        xx = Vias[m]['xc'] + np.concatenate([Rvia * np.cos(phi), Rvia0 * np.cos(phi[::-1]), [Rvia]])
        yy = Vias[m]['yc'] + np.concatenate([Rvia * np.sin(phi), Rvia0 * np.sin(phi[::-1]), [0]])
        plt.fill(xx, yy, 'w')

    # Plot TopText
    TopText = Dev['TopText']
    for m in range(len(TopText)):
        plt.text(TopText[m]['x'], TopText[m]['y'], TopText[m]['String'], fontsize=5)

    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.grid(False)
    plt.draw()
    plt.show()
