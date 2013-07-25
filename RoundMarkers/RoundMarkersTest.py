#!/usr/bin/env python

import itertools
import matplotlib
import matplotlib.pyplot as plt
import RoundMarkers

# test

gl_style = [
        #color lw symbol mfc
        ('#dd181f', 2, 'rs', 'none'), # --- red
        ('#5e9c36', 2, 'r*', 'none'), # --- green
        ("#a00000", 2, 'r+', 'none'),
        ("#5060d0", 2, 'rx', 'none'),
        #        ("#f25900", 2, 
        ]
gl_styles = itertools.cycle(gl_style)


fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

foo.round_markers()

x = range(0, 100, 10)
y = x

for i in range(0, len(gl_style)):

    cl, lw, mk, mfc = gl_styles.next()

    y = [e+50 for e in y]
    
    ax.plot(x, y, 
            c=cl,
            marker=mk,
            mec=cl,
            mfc=mfc,
            mew=lw,
            markersize=7,
            lw=lw)

plt.show()
fig.savefig('test.pdf', bbox_inches='tight')
