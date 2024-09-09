import matplotlib.pyplot as plt
import numpy as np

def Draw4LayerPCBDev(Dev, Nfig):
    TopE = Dev['TopE']
    In1E = Dev['In1E']
    In2E = Dev['In2E']
    BtmE = Dev['BtmE']
    # TopMask = Dev['TopMask']
    # BtmMask = Dev['BtmMask']
    TopSilk = Dev['TopSilk']
    BtmSilk = Dev['BtmSilk']
    # TopPads = Dev['TopPads']
    # BtmPads = Dev['BtmPads']
    TopOutlines = Dev['TopOutlines']
    BtmOutlines = Dev['BtmOutlines']
    Vias = Dev['Vias']

    plt.figure(Nfig)
    plt.clf()

    # Plot BtmE, In1E, In2E
    for m in range(len(BtmE)):
        plt.fill(BtmE[m]['x'], BtmE[m]['y'], facecolor='g')
    for m in range(len(In1E)):
        plt.fill(In1E[m]['x'], In1E[m]['y'], facecolor='g')
    for m in range(len(In2E)):
        plt.fill(In2E[m]['x'], In2E[m]['y'], facecolor='g')

    # Plot TopE
    for m in range(len(TopE)):
        plt.fill(TopE[m]['x'], TopE[m]['y'], facecolor='y')

    # Plot TopSilk and BtmSilk
    for m in range(len(TopSilk)):
        plt.plot(TopSilk[m]['x'], TopSilk[m]['y'], color='c', linewidth=2)
    for m in range(len(BtmSilk)):
        plt.plot(BtmSilk[m]['x'], BtmSilk[m]['y'], color='c')

    # Plot TopOutlines and BtmOutlines
    if TopOutlines:
        plt.plot(TopOutlines[0]['x'], TopOutlines[0]['y'], color='m', linewidth=2)
    for m in range(1, len(BtmOutlines)):
        plt.plot(BtmOutlines[m]['x'], BtmOutlines[m]['y'], color='m', linewidth=2)

    # Plot Vias
    phi = np.linspace(0, 2*np.pi, 50)
    dw = 0.02
    for via in Vias:
        Rvia = via['R']
        xx = via['xc'] + np.concatenate((Rvia * np.cos(phi), (Rvia + dw) * np.cos(phi[::-1]), [Rvia]))
        yy = via['yc'] + np.concatenate((Rvia * np.sin(phi), (Rvia + dw) * np.sin(phi[::-1]), [0]))
        plt.fill(xx, yy, facecolor='w')

    # Additional settings (optional)
    # plt.xlabel('x (mm)')
    # plt.ylabel('y (mm)')
    # plt.axis([-15, 30, -8, 8])
    # plt.grid(False)
    plt.axis('equal')  # Ensure equal scaling
    plt.draw()
    plt.show()

'''
# Example usage:
Dev = {
    'TopE': [{'x': [], 'y': []}],  # Replace with actual data
    'In1E': [{'x': [], 'y': []}],  # Replace with actual data
    'In2E': [{'x': [], 'y': []}],  # Replace with actual data
    'BtmE': [{'x': [], 'y': []}],  # Replace with actual data
    'TopSilk': [{'x': [], 'y': []}],  # Replace with actual data
    'BtmSilk': [{'x': [], 'y': []}],  # Replace with actual data
    'TopOutlines': [{'x': [], 'y': []}],  # Replace with actual data
    'BtmOutlines': [{'x': [], 'y': []}],  # Replace with actual data
    'Vias': [{'xc': 0, 'yc': 0, 'R': 0.1}],  # Replace with actual data
}

Nfig = 1
Draw4LayerPCBDev(Dev, Nfig)
'''