#== Imports =========================================================================================
import pyaedt
# import numpy as np
# import matplotlib.pyplot as plt
from pyaedt.hfss import Hfss
# from pyaedt import Maxwell3d
# import time

#== Setup Data (mm) ======================================================================================
save_path = "C:\\Users\\rdumn\\OneDrive\\Desktop\\PSI\\AEDT_patch_antenna\\Patch_Antenna.aedt"

wavelength = 12 #mm

FeedSubL = 25
FeedSubW = 30
FeedSubH = 1
PatchL = 6
PatchW = 10
PatchH = 0.05
PatchCutL = 3
PatchCutW = 2
PatchCutH = PatchH
FeedL = FeedSubL/2
FeedW = 1.6
FeedH = PatchH
GNDL = FeedSubL
GNDW = FeedSubW
GNDH = 0.05
RadiationL = 4*wavelength
RadiationW = 4*wavelength
RadiationH = 4*wavelength
PortB = FeedSubW/4
PortH = 3*(FeedSubH + FeedH + GNDH)

#== HFSS Design =====================================================================================
# Names & graphical mode
project_name = pyaedt.generate_unique_project_name(project_name="Patch_Antenna")
hfss =  Hfss(non_graphical=False, project=project_name, design="HFSS_Design", new_desktop=False,
            close_on_exit=True, student_version=True)
hfss.modeler.model_units = "mm"

# Base Dielectric Substrate
Feed_sub = hfss.modeler.create_box(origin=[-FeedSubL/2, -FeedSubW/2, -FeedSubH/2],
                            sizes=[FeedSubL, FeedSubW, FeedSubH],
                            name="FeedSubstrate",
                            material="Rogers RT/duroid 5880 (tm)")
print(Feed_sub.faces)
Feed_sub.color = "Green"
Feed_sub.transparency = 0.2
hfss.modeler.fit_all()

# Patch & Feed & Patch Subtract & Unite
Patch = hfss.modeler.create_box(origin=[-PatchL/2, -PatchW/2, FeedSubH/2],
                            sizes=[PatchL, PatchW, PatchH],
                            name="Patch",
                            material="Copper")
print(Patch.faces)
Patch.color = (255, 128, 64)
Patch.transparency = 0

# Feed
Feed = hfss.modeler.create_box(origin=[0, -FeedW/2, FeedSubH/2],
                            sizes=[FeedL, FeedW, FeedH],
                            name="Feed",
                            material="Copper")
print(Feed.faces)
Feed.color = (255, 128, 64)
Feed.transparency = 0

# Cut Rectangle
Patch_cut = hfss.modeler.create_box(origin=[PatchL/2, -PatchCutW/2, FeedSubH/2],
                            sizes=[-PatchCutL, PatchCutW, PatchCutH],
                            name="Cut")
print(Patch_cut.faces)
Patch_cut.color = (255, 0, 0)
Patch_cut.transparency = 0

# Subtract cut from patch
hfss.modeler.subtract("Patch", "Cut", keep_originals=False)

# Unite
hfss.modeler.unite(["Patch", "Feed"])

# GND
GND = hfss.modeler.create_box(origin=[-FeedSubL/2, -FeedSubW/2, -FeedSubH/2],
                            sizes=[GNDL, GNDW, -GNDH],
                            name="GND",
                            material="Copper")
print(GND.faces)
GND.color = (255, 128, 64)
GND.transparency = 0

# Raditation

Radiation = hfss.modeler.create_box(origin=[FeedSubL/2, -RadiationW/2, -RadiationH/4],
                            sizes=[-RadiationL, RadiationW, RadiationH],
                            name="Radiation",
                            material="air")
print(Radiation.faces)
Radiation.transparency = 1
# hfss.modeler.fit_all()

# Port box
Port_box = hfss.modeler.create_rectangle(origin=[FeedL, -PortB/2, -FeedSubH/2 - GNDH],
                            sizes=[PortB, PortH],
                            name="PortBox",
                            orientation="YZ")

#== Sim Setup & Run ===============================================================================
# Solution type
hfss.solution_type = "DrivenModal"

# Assign wave port excitation
hfss.wave_port("PortBox", modes=1, impedance=50, name="WavePort1")

# Assign Radiation (air box)
hfss.assign_radiation_boundary_to_objects("Radiation", name="AirRad")

# Set up frequency sweep simulation parameters 
setup1 = hfss.create_setup(name="setup1")
setup1.props["Frequency"] = "25GHz"
# print(setup1.props)   # Help Debug
setup1.create_frequency_sweep(unit="GHz",
                              start_frequency=20, 
                              stop_frequency=32.5, 
                              num_of_freq_points= 155,
                              sweep_type= "Fast",
                              name="Sweep1")

# Far Field Infinite Sphere Setup
Sphere1 = hfss.insert_infinite_sphere(x_start=0, x_stop=180, x_step=5, 
                                      y_start=0, y_stop=180, y_step=5,
                                      name="InfiniteSphere1")

# Start simulation
hfss.analyze()

#Simulation Data Reports
hfss.post.create_report("dB(S(1,1))",plot_type="Rectangular Plot",plot_name="S-Parameters")
hfss.post.create_report("dB(GainTotal)", report_category="Far Fields", plot_type="3D Polar Plot",
                        variations={"Freq": ["25GHz"]},
                        plot_name="FarFieldGain")

#== Save Path =====================================================================================
hfss.save_project(save_path)
print(f"Project saved at {save_path}")
    
#== Exit ==========================================================================================
# # Won't close until input
# input("Press Enter to exit")
# # Gnarly ah Goofy ah countdown
# for i in range(3, 0, -1):
#     print(i)
#     time.sleep(0.3)

# # Release desktop (aka close project)
# hfss.release_desktop()
# print("Desktop released")