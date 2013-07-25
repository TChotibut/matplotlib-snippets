"""
Provides rounded markers (square, ex, plus, asterisk) to matplotlib
"""

__author__='amiranda'
__date__='Thu Jul 25 09:30:57 CEST 2013'

import matplotlib.markers
from matplotlib.path import Path

def round_markers():
    """ 
    Turns on rounded markers. 
    """

    matplotlib.markers.MarkerStyle._set_rsquare = _set_rsquare
    matplotlib.markers.MarkerStyle.markers['rs'] = 'rsquare'

    matplotlib.markers.MarkerStyle._set_rx = _set_rx
    matplotlib.markers.MarkerStyle.markers['rx'] = 'rx'

    matplotlib.markers.MarkerStyle._set_rplus = _set_rplus
    matplotlib.markers.MarkerStyle.markers['r+'] = 'rplus'

    matplotlib.markers.MarkerStyle._set_rasterisk = _set_rasterisk
    matplotlib.markers.MarkerStyle.markers['r*'] = 'rasterisk'

    matplotlib.lines.Line2D.markers = matplotlib.markers.MarkerStyle.markers

# rounded square marker
def _set_rsquare(self):
    # call original function
    self._set_square()
    self._joinstyle = 'round'


# rounded 'x' marker
_rx_path = Path([[0.0, 0.0], [-1.0, -1.0], [+1.0, +1.0], [0.0, 0.0],
                 [0.0, 0.0], [+1.0, -1.0], [-1.0, +1.0], [0.0, 0.0],],
                [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
                 Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]) 

def _set_rx(self):
    self._set_x()
    self._path = _rx_path
    self._joinstyle = 'round'


# rounded '+' marker
_rplus_path = Path([[0.0,  0.0], [+1.0,  0.0], [-1.0, 0.0], [0.0, 0.0],
                    [0.0, +1.0], [ 0.0, -1.0], [ 0.0, 0.0]],
                    [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
                     Path.LINETO, Path.LINETO, Path.LINETO])

def _set_rplus(self):
    self._set_plus()
    self._path= _rplus_path
    self._joinstyle = 'round'


# rounded asterisk marker
_rasterisk_path = Path([[ 0.0,  0.0], [-1.0, -1.0], [+1.0, +1.0], [0.0, 0.0],
                        [+1.0, -1.0], [-1.0, +1.0], [ 0.0,  0.0],
                        [ 0.0, -1.0], [ 0.0, +1.0], [ 0.0,  0.0],
                        [-1.0,  0.0], [+1.0,  0.0], [ 0.0,  0.0],
                        
                        ],
                       [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO,
                        Path.LINETO, Path.LINETO, Path.LINETO,
                        Path.LINETO, Path.LINETO, Path.LINETO,
                        Path.LINETO, Path.LINETO, Path.LINETO]) 

def _set_rasterisk(self):
    self._transform = matplotlib.transforms.Affine2D().scale(0.5)
    self._snap_threshold = 1.0
    self.filled = False
    self._path = _rasterisk_path
    self._joinstyle = 'round'
