# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:34:36 2022

@author: Shashank
"""
import sys
sys.path.append('D:\KSP 3.0\Galaxy-Evolution-through-N-body-simulations\Solar_System_using_Barnes_Hut')
import barnes_hut as bh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import time

init_pos = np.loadtxt("galaxy_coords.txt")
init_vel = np.loadtxt("galaxy_vels.txt")
init_m = np.loadtxt("galaxy_masses.txt")

t_0 = 0
t = t_0
div = 1
dt = 86400/div
t_end = 86400 * 365 * 10
t_array = np.arange(t_0, t_end, dt)



