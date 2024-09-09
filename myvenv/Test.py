#== Imports =========================================================================================
import pyaedt
import numpy as np
from pyaedt.hfss import Hfss
from pyaedt import Maxwell3d
import time

#== Setup Data ======================================================================================
FeedSubL = 10
FeedSubW = 10
FeedSubH = 1

save_path = "C:\\Users\\rdumn\\OneDrive\\Desktop\\PSI\\TestAEDT\\TestHFSS.aedt"

#== HFSS Design =====================================================================================
# Names & graphical mode
project_name = pyaedt.generate_unique_project_name(project_name="TestHFSS")
hfss =  Hfss(non_graphical=False,project=project_name, design="HFSS_Design")

box = hfss.modeler.create_box(origin=[0, 0, 0],
                            sizes=[FeedSubL, FeedSubW, FeedSubH],
                            name="FeedSubstrate",
                            material="Rogers RT/duroid 5880 (tm)")
print(box.faces)
box.color = "Green"
box.transparency = 0.4

#== Sim Setup & Run ===============================================================================


#== Save Path =====================================================================================
hfss.save_project(save_path)
print(f"Project saved at {save_path}")
    
#== Exit ==========================================================================================
# Won't close until input
input("Press Enter to exit")
# Cool countdown
for i in range(3, 0, -1):
    print(i)
    time.sleep(0.5)

# Release desktop (aka close)
hfss.release_desktop()
print("Desktop released")