import matplotlib.pyplot as plt
import numpy as np


def pl_bresenham(x1, y1, x0=0, y0=0):  # todo translate matrix
    dx = x1 - x0
    dy = y1 - y0
    e = 2 * dy - dx
    y = 0
    xlm = np.zeros((dx, dy))
    yl = []
    xl = np.arange(0, dx)
    
    for x in xl:
        xlm[x, y] = 1
        yl.append(y)
        if e > 0:
            y += 1
            e -= 2 * dx
        e += 2 * dy
        print(f'x={x+x0},y={y+y0},er={e}')

    yl = np.array(yl)+y0
    xl = xl + x0

    fig, ax = plt.subplots(1)
    plt.imshow(xlm.transpose())

    xl0 = np.linspace(x0, x1)
    yl0 = xl0*dy/dx+y0

    plt.plot(xl, yl, xl0, yl0)
    plt.show()
    # centx = (x0+0.5*rad_lim, x0-0.5*rad_lim, 0.5*rad_lim+y0, y0-0.5*rad_lim)
    # print('centx',centx)
    # plt.imshow(xm, interpolation=None, extent=centx)
    # ax.set_xticks(centlim + x0, minor=True)
    # ax.set_yticks(centlim + y0, minor=True)
    # ax.grid(which='minor')
    # plt.show()


def cir_bresenham(r, x0=0, y0=0):  # todo origin imshow
    x = 0
    y = r

    rad_lim = 2 * r + 1
    e = 3-2*r

    xm = np.zeros((rad_lim, rad_lim))
    while y >= x:
        print(f'x={x}, y={y}')
        for i in [1, -1]:
            for j in [1, -1]:
                xv = x*i + r
                yv = y*j + r
                xm[xv, yv] = 1
                xm[yv, xv] = 1
        x += 1
        if e > 0:
            y -= 1
            e += 4 * (x-y) + 10
        else:
            e += 4 * x + 6

    fig, ax = plt.subplots(1)
    centlim = np.arange(-0.5*rad_lim, 0.5*rad_lim)
    centx = (x0+0.5*rad_lim, x0-0.5*rad_lim, 0.5*rad_lim+y0, y0-0.5*rad_lim)
    print('centx',centx)
    plt.imshow(xm, interpolation=None, extent=centx)
    ax.set_xticks(centlim + x0, minor=True)
    ax.set_yticks(centlim + y0, minor=True)
    ax.grid(which='minor')
    plt.show()


cir_bresenham(20)

#  pl_bresenham(60, 40)
#
