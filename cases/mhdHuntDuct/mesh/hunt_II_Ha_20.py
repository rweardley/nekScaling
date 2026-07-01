#!python

import cubit
import sys
import numpy as np

sys.path.append(r"../../../../python")
import gll_quadrature as gll

# set parameters

polynomialOrder = 5
length = 2
height = 2
width = 2
hart_wall_thickness = 0.01
hart_N = 40 / polynomialOrder
side_N = 20 / polynomialOrder
delta_x = length/3
meshname = "Ha_20_hunt_II"
meshname_solid = meshname + "_solid"
meshname_fluid = meshname + "_fluid"
meshname_combined = meshname + "_fluid+solid"
hartmann_layers = True
side_layers = False
solid_layers = False

solid_height = height + 2*hart_wall_thickness

N = polynomialOrder
nPoints = N+1
print("GLL quadrature points for N=" + str(N))
x, w = gll.gLLNodesAndWeights(nPoints)
print(x)

# calculate desired first layer thickness y1 (e.g. ~1/Ha); will correspond to difference between x[0] and x[1] rescaled by element size
# first_gridpoint_fraction = abs(x[0]-x[1])/2
# y1 = first_gridpoint_fraction*first_layer_element_size
# so first_layer_element_size = y1 / first_gridpoint_fraction
# then calculate other parameters based on desired number of elements
# r is unknown
# L = delta_1*(r^N - 1)/(r - 1)
# so r*(delta_1*r^(N-1) - L) - delta_1 + L = 0
# tried solving, but too complicated
# instead, just give a guess, check if calculated L matches half-width closely enough, then continue or not
# L = delta_1*(r^N - 1)/(r - 1)

Ha = 20
y1_hart = 1/Ha
y1_side = 1/np.sqrt(Ha)

n_gll_points_in_boundary_hart = 2
n_gll_points_in_boundary_side = 3

y1_fraction_hart = abs(x[0]-x[n_gll_points_in_boundary_hart])/2
print(y1_fraction_hart)
y1_fraction_side = abs(x[0]-x[n_gll_points_in_boundary_side])/2
print(y1_fraction_side)
delta_1_hart = y1_hart / y1_fraction_hart
delta_1_side = y1_side / y1_fraction_side

r_hart = 1.405 # human guess
hart_tol = 1e-3
r_side = 1.875 # human guess
side_tol = 1e-3

def L_calc(delta_1, r, N_points):
  L = delta_1*(r**N_points - 1)/(r - 1)
  return L

L_calculated_hart = L_calc(delta_1_hart, r_hart, hart_N/2)
L_calculated_side = L_calc(delta_1_side, r_side, side_N/2)

hart_diff = L_calculated_hart - height/2
side_diff = L_calculated_side - width/2

print("Hartmann layer:\tTarget L = %f\tCalculated L = %f\tDifference = %f" % (height/2, L_calculated_hart, hart_diff))
print("Side layer:\tTarget L = %f\tCalculated L = %f\tDifference = %f" % (width/2, L_calculated_side, side_diff))

if L_calculated_hart is np.nan or L_calculated_side is np.nan:
  raise Exception("Calculated L cannot be NaN")

if (hart_diff < 0):
  raise Exception("Hartmann layer total length is smaller than target  - abort")
elif (abs(hart_diff) > hart_tol):
  raise Exception("Hartmann layers don't match target - abort")
if (side_diff < 0):
  raise Exception("Side layer total length is smaller than target  - abort")
elif (abs(side_diff) > side_tol):
  raise Exception("Side layers don't match target - abort")

# print("Solution (Hartmann layer):")
# initial_guess = np.linspace(1, 2, num=N)
# print(solve_for_r(delta_1_hart, hart_N/2, height, initial_guess.tolist()))
# print("Solution (side layer):")
# print(solve_for_r(delta_1_side, side_N/2, width, initial_guess.tolist()))

#####

# calculate boundary layers
# hart_num_layers = hart_N / 2
# hart_growth_factor = hart_total_expansion ** (1 / (hart_num_layers - 1))
# hart_first_row = (height / 2) * (hart_growth_factor - 1) / (hart_total_expansion * hart_growth_factor - 1)
hart_num_layers = hart_N/2 - 1 # -1: to prevent it being overly constrained, allow it to fill the central portion in
hart_growth_factor = r_hart
hart_first_row = delta_1_hart

hart_final_size = hart_first_row * hart_growth_factor ** (hart_num_layers)

side_num_layers = side_N/2 - 1 # -1: to prevent it being overly constrained, allow it to fill the central portion in
side_growth_factor = r_side
side_first_row = delta_1_side

side_final_size = side_first_row * side_growth_factor ** (side_num_layers)

approx_core_size = (hart_final_size + side_final_size) / 2

# side_num_layers = side_N / 2
# side_growth_factor = side_total_expansion ** (1 / (side_num_layers - 1))
# side_first_row = (width / 2) * (side_growth_factor - 1) / (side_total_expansion * side_growth_factor - 1)

# create geometry

cubit.cmd(f'brick x {length} y {height} z {width}') # fluid region
cubit.cmd(f'brick x {length} y {solid_height} z {width}') # solid+fluid region
cubit.cmd('subtract volume 1 from volume 2 keep_tool') # create solid-only region (body 2)
cubit.cmd('imprint volume all') # imprint
cubit.cmd('merge volume all') # merge

# create named sidesets

cubit.cmd('sideset 1 add surface 4')
cubit.cmd('sideset 1 name "inlet"')
cubit.cmd('sideset 2 add surface 6')
cubit.cmd('sideset 2 name "outlet"')
cubit.cmd('sideset 3 add surface 5 3')
cubit.cmd('sideset 3 name "hartmann_fs_interface"')
cubit.cmd('sideset 4 add surface 1 2')
cubit.cmd('sideset 4 name "side_walls"')
cubit.cmd('sideset 5 add surface 15 18')
cubit.cmd('sideset 5 name "solid_inlet"')
cubit.cmd('sideset 6 add surface 17 20')
cubit.cmd('sideset 6 name "solid_outlet"')
cubit.cmd('sideset 7 add surface 14 16 19 21')
cubit.cmd('sideset 7 name "solid_side_walls"')
cubit.cmd('sideset 8 add surface 9 11')
cubit.cmd('sideset 8 name "solid_exterior_walls"')

# create fluid boundary layers

if hartmann_layers:
  cubit.cmd('create boundary_layer 1')
  cubit.cmd(f'modify boundary_layer 1 uniform height {hart_first_row} growth {hart_growth_factor} layers {hart_num_layers}')
  cubit.cmd('modify boundary_layer 1 add surface 3 volume 1 surface 5 volume 1')
  cubit.cmd('modify boundary_layer 1 continuity off')
if side_layers:
  cubit.cmd('create boundary_layer 2')
  cubit.cmd(f'modify boundary_layer 2 uniform height {side_first_row} growth {side_growth_factor} layers {side_num_layers}')
  cubit.cmd('modify boundary_layer 2 add surface 1 volume 1 surface 2 volume 1')
  cubit.cmd('modify boundary_layer 2 add surface 14 volume 3 surface 16 volume 3') # add solid parts
  cubit.cmd('modify boundary_layer 2 add surface 19 volume 4 surface 21 volume 4') # add solid parts
  cubit.cmd('modify boundary_layer 2 continuity off')

# create solid boundary layers


if solid_layers:
    hart_growth_factor_solid = 1.1
    hart_num_layers_solid = 1
    cubit.cmd('create boundary_layer 3')
    cubit.cmd(f'modify boundary_layer 3 uniform height {hart_first_row} growth {hart_growth_factor_solid} layers {hart_num_layers_solid}')
    cubit.cmd('modify boundary_layer 3 add surface 3 volume 3 surface 5 volume 4')
    cubit.cmd('modify boundary_layer 3 continuity off')

# set mesh size for axial resolution

cubit.cmd(f'volume 1 size {delta_x}')

# set approximate mesh size for core

cubit.cmd(f'surface 4 size {approx_core_size}')

# mesh inlet

cubit.cmd('surface 4 submap smooth off')
cubit.cmd('surface 4 scheme submap')
cubit.cmd('mesh surface 4')

# mesh volume by sweeping from inlet to outlet

cubit.cmd('volume 1 3 4 redistribute nodes off')
cubit.cmd('volume 1 scheme Sweep source surface 4 target surface 6 sweep transform least squares')
cubit.cmd('volume 3 scheme Sweep source surface 3 target surface 9 sweep transform least squares')
cubit.cmd('volume 4 scheme Sweep source surface 5 target surface 11 sweep transform least squares')
cubit.cmd('volume 1 3 4 autosmooth target on fixed imprints off smart smooth off')
cubit.cmd('mesh volume 1')
cubit.cmd('mesh volume 3')
cubit.cmd('mesh volume 4')

# create element blocks
cubit.cmd('block 1 add volume 1')
cubit.cmd('block 2 add volume 3 4')

# set element type
cubit.cmd('block 1 element type hex20')
cubit.cmd('block 2 element type hex20')

# save mesh (exodus)

cubit.cmd('set exodus netcdf4 off')
cubit.cmd('set large exodus file on')
cubit.cmd(f'export mesh "{meshname_fluid}.exo" block 1 overwrite')
cubit.cmd(f'export mesh "{meshname_solid}.exo" block 2 overwrite')
cubit.cmd(f'export mesh "{meshname_combined}.exo" block 1 2 overwrite')
