import matplotlib.pyplot as plt
import numpy as np

    #Edit these Rpin numbers depending on requirements 
Rpin = {
    'S': .015,
    'M': .3,
    'L': .5
}

def DrawPCBDevice(Dev):
    TopE = Dev['TopE']
    BtmE = Dev['BtmE']
    TopMask = Dev['TopMask']
    BtmMask = Dev['BtmMask']
    Outlines = Dev['Outlines']
    Vias = Dev['Vias']
    Pads = Dev['TopPads']

    # Initialize figure
    plt.figure(999)
    plt.clf()

    # Plot BtmE
    for m in range(len(BtmE)):
        plt.fill(BtmE[m]['x'], BtmE[m]['y'], color=[1, 1, 0])

    # Plot TopE
    for m in range(len(TopE)):
        plt.fill(TopE[m]['x'], TopE[m]['y'], color='y')

    # Plot Outlines
    for m in range(len(Outlines)):
        plt.plot(Outlines[m]['x'], Outlines[m]['y'], color='b')

    # Plot TopMask
    for m in range(len(TopMask)):
        plt.plot(TopMask[m]['x'], TopMask[m]['y'], color='r')

    # Plot BtmMask
    for m in range(len(BtmMask)):
        plt.plot(BtmMask[m]['x'], BtmMask[m]['y'], color='k')

    phi = np.linspace(0, 2*np.pi, 25)
    dw = 0.1

    # Plot Vias
    for m in range(len(Vias)):
        if Vias[m]['Type'] == 'ViaS':
            Rvia = Rpin['S']
        elif Vias[m]['Type'] == 'ViaM':
            Rvia = Rpin['M']
        elif Vias[m]['Type'] == 'ViaL':
            Rvia = Rpin['L']
        else:
            Rvia = 0.15

        xx = Vias[m]['xc'] + np.concatenate([Rvia * np.cos(phi), (Rvia + dw) * np.cos(phi[::-1]), [Rvia]])
        yy = Vias[m]['yc'] + np.concatenate([Rvia * np.sin(phi), (Rvia + dw) * np.sin(phi[::-1]), [0]])
        plt.fill(xx, yy, 'w')

    # Plot Pads
    for m in range(len(Pads)):
        if Pads[m]['Type'] in ['PlatedPadS', 'NonPlatedPadS']:
            Rpad = Rpin['S']
        elif Pads[m]['Type'] in ['PlatedPadM', 'NonPlatedPadM']:
            Rpad = Rpin['M']
        elif Pads[m]['Type'] in ['PlatedPadL', 'NonPlatedPadL']:
            Rpad = Rpin['L']
        else:
            Rpad = 0.15

        xx = Pads[m]['xc'] + np.concatenate([Rpad * np.cos(phi), (Rpad + dw) * np.cos(phi[::-1]), [Rpad]])
        yy = Pads[m]['yc'] + np.concatenate([Rpad * np.sin(phi), (Rpad + dw) * np.sin(phi[::-1]), [0]])
        plt.fill(xx, yy, 'w')

    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.axis('equal')
    plt.axis('tight')
    plt.draw()
    plt.show()
