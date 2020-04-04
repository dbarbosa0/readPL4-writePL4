#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  readPL4.py
#  https://github.com/ldemattos/readPL4
#  
#  Copyright 2019 Leonardo M. N. de Mattos <l@mattos.eng.br>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.0.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
from lib_readPL4 import readPL4
from lib_readPL4 import getVarData
import numpy as np

def main(args):
	
	# Call the library
	dfHEAD,data,miscData = readPL4(sys.argv[1])
	
	# Give some information to the user
	print "PL4 Header info:"
	print miscData
	
	print "Data shape:"
	print np.shape(data)
	
	# EXAMPLES
	###############################################################
	# Get time
	time = data[:,0]
	
	# Get some variable, remember ATP's variable has a maximum of 6 characters
	# Check dfHEAD for var 'TYPE' and 'COMPLEX'
    # Further information is available at project's github wiki pages
    #
    # For time domain simulations:
	# ~ sel_data = getVarData(dfHEAD,data,'TYPE','FROM','TO')
    #
    # For frequency domain simulations:
	# ~ sel_data = getVarData(dfHEAD,data,'TYPE','FROM','TO','COMPLEX')
	
	# Launch ipython session
	import IPython as ipy
	ipy.embed()
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
