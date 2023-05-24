import trusspy as tp

M = tp.Model()

# create nodes
with M.Nodes as MN:
    MN.add_node(1, (0, 0, 0))
    MN.add_node(2, (1, 0, 0))

# create element
with M.Elements as ME:
    ME.add_element(1, [1, 2])
    ME.assign_material("all", [1])
    ME.assign_geometry("all", [1])

# create displacement (U) boundary conditions
with M.Boundaries as MB:
    MB.add_bound_U(1, (0, 0, 0))
    MB.add_bound_U(2, (1, 0, 0))

# create external forces
with M.ExtForces as MF:
    MF.add_force(2, (1, 0, 0))

# build model, run, show results
M.build()
M.run()

# plot results of last increment
M.plot_model(inc=-1, contour="force")