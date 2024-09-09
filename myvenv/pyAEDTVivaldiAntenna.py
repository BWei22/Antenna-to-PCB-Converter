#== Imports =========================================================================================
import pyaedt
import numpy as np
from pyaedt.hfss import Hfss
import math
# import matplotlib.pyplot as plt
# from pyaedt import Maxwell3d
# import time

#== Setup Data (mm) ======================================================================================
save_path = "C:\\Users\\rdumnich\\Documents\\PSI\\AEDT_vivaldi_antenna\\Vivaldi_Antenna.aedt"
export_path = "C:\\Users\\rdumnich\\Documents\\PSI\\AEDT_vivaldi_antenna"

wavelength = 12 # mm (AKA 25GHz)
clones = 3      # antenna array count

# Dielectric-----------------------
SubTrim = 2.55             # Trim off/shorten back antenna (subtracts from the overall length)
SubL = 15 + SubTrim     # 1st number is desired length, adds trip to keep accurate length
SubH = 0.254
SubW = 5.8

# Dielectric Extension------------------
Sub_EXL = 2                  # Section for connectors and VIAs
Sub_EXW = SubW
Sub_EXH = SubH

# GND------------------------------------
GNDH = 0.017            # GND metal height
GNDW = SubW
GNDL = SubL

# Side GND Extension-----------------------------------
GND_EXH = GNDH        # Ground extension parameters - connection area with VIAs
GND_EXW = SubW
GND_EXL = Sub_EXL
GND_cutW = 2.5        # Shaping parameters of EX GND
GND_cutL = 0.5
GNDEX_angle = 45

FeedGND_EXL = 0.35

Center_GND_cut_L = GND_EXL
Center_GND_cut_H = GND_EXH

# VIAs----------------------------------------
VRadius = 0.11
VIA_spacing_modifier = 0.015
VHeight = GND_EXH + SubH + GNDH
n_vias = 4              # number of vias in a section
VIA_xshift = -0.15      # Adjust location of top row VIAs
VIA_yshift = -0.15
VIA_x2shift = -0.45      # for the bottom row VIAs
VIA_y2shift = 1.05

VIAC_xshift = 0      # Adjust location of Center VIAs
VIAC_yshift = 0
n_vias_c = 3


# Vivaldi Shape-----------------------
VAmp = 0.36                 # Amplitude (finely adjusts curve)
EXPRate =  0.26             # Exponential rate (coarsely adjusts curve)
y_start = 0.05              # starting gap
y_end = SubW/2              # ending width
num_points = 150            # number of points
x_offset = 0

# Cave/Termination GND---------------------
Cave_rotate_deg = 0         # rotate termination if desired
CaveSideL = 0.85            # Side length
Cave_side_deg = 48          # angle of sides
CaveRadius = 0.25           # radius of curve

# Rectangular Slot/Gap------------------
GapL = 0.4              # Gap length
GapH = GNDH             # Same height as GND metal

# Feed-----------------------------------
num_points_feedA = 100      # Points built into each arc
FeedMetalH = GNDH

    # 1st taper
FStartW = 0.49                     # Width starting from base of feed
FTaper_y1 = FStartW/2 - 0.07     # Taper from feed base (keep subtract number > FstartW/2)
FTaperL1 = 2.25                    # Length of tapered edges (1st one from base)

    # 1st arc/curve segment & other side
FeedRadius_A1 = 1.4              # Curve radius
start_angle_A1 = 180           # Angle at which the curve stars/stops in degrees
end_angle_A1 = 133
start_angle_AO1 = start_angle_A1
end_angle_AO1 = end_angle_A1

    # 2nd arc/curve & other side
FeedRadius_A2 = 1.4
start_angle_A2 = end_angle_A1 - 180
end_angle_A2 = 0
start_angle_AO2 = start_angle_A2
end_angle_AO2 = end_angle_A2

    # 2nd Taper
FTaper_cut = -0.08
FTaper_W = 2*FTaper_y1 + 2*FTaper_cut
FTaperL2 = 1
    # 3rd arc/curve
FeedRadius_A3 = 0.7
start_angle_A3 = 0
end_angle_A3 = 90
start_angle_AO3 = start_angle_A3
end_angle_AO3 = end_angle_A3

    # neck
FNeckW = FTaper_W                   # Neck Width
FNeckL = 0.26

    # Feed head/termination
FHead_deg = 50       
FHead_rotate_deg = -90
FHeadSideL = 1
FeedRadius_H = 0.33

# Raditaion --------------------------------------
RadiationW = 4*wavelength
RadiationH = 4*wavelength
RadiationL = 4*wavelength

# Port -------------------------------------------
PortB = 5           # Port base and height
PortH = 3
    
#== HFSS Design =====================================================================================
# Names & graphical mode-----------------------------
project_name = pyaedt.generate_unique_project_name(project_name="Vivaldi_Antenna")
hfss = Hfss(non_graphical=False, project=project_name, design="HFSS_Design", new_desktop=False,
            close_on_exit=True, student_version=False)
hfss.modeler.model_units = "mm"

# Base Dielectric Substrate---------------------------
Substrate = hfss.modeler.create_box(origin=[-SubL/2 + SubTrim, -SubW/2, -SubH],     # Creates a box to serve as substrate with specified parameters
                            sizes=[SubL, SubW, SubH],
                            name="Substrate",
                            material="Rogers RO4350 (tm)")
Substrate.color = "Green"
Substrate.transparency = 0

hfss.modeler.fit_all()

# GND/Top metal------------------------------
GND = hfss.modeler.create_box(origin=[-GNDL/2 + SubTrim, -GNDW/2, 0],
                            sizes=[GNDL, GNDW, GNDH],
                            name="GND",
                            material="Copper")
GND.transparency = 0

# Vivaldi Curve----------------------------------------
points = []

def create_vivaldi_curve(hfss, name, VAmp, EXPRate, y_start, y_end, num_points, x_offset):      # Calculates points to create desired curve
    """ Calculates the points to be used for an equation based polyline curve

    Args:
        hfss (): software library
        name (string): name of the curve
        VAmp (int): Amplitude of curve
        EXPRate (int): exponential rate of curve
        y_start (int): desired y starting point
        y_end (int): desired y end, will be width of antenna
        num_points (int): number of points to generate the curve with
        x_offset (int): x offset if needed
    """
    
    # Calculate the initial x value based on y_start to ensure it starts from the origin.
    x_start = math.log(y_start / VAmp + 1) / EXPRate

    for i in range(0, num_points):
        y = y_start + (y_end - y_start) * i / (num_points - 1)
        x = (math.log(y / VAmp + 1)) / EXPRate - x_start + x_offset
        points.append([x, y, 0])
        if i < 10:  # Print the first few points for debugging
            print(f"Point {i}: x = {x}, y = {y}")

    hfss.modeler.create_polyline(points, name=name)
    print(f"Number of points: {len(points)}")

create_vivaldi_curve(hfss, "VivaldiCurve", VAmp, EXPRate, y_start, y_end, num_points, x_offset)

    # Mirror Curve
hfss.modeler.mirror(assignment="VivaldiCurve",          # mirrors curve - to make a cut in antenna later
                    origin=[0, 0, SubH],
                    vector=[0, 1, 0],
                    duplicate=True)

hfss.modeler.fit_all()
# Rectangular Slot--------------------------
Rect_slot = hfss.modeler.create_box(origin=[0, -points[0][1], 0],
                            sizes=[-GapL, points[0][1] + y_start, GNDH],
                            name="Gap")
Rect_slot.transparency = 0.5
# Cave/Termination--------------------------
    # Allows for the angling of the cave sides and adjust of length
C_x1 = -CaveSideL*math.sin(math.radians(Cave_side_deg))
C_y1 = CaveSideL*math.cos(math.radians(Cave_side_deg))

    # Calculations for dynamic cave polylines
Cave_points = [[0, points[0][1], 0],
               [C_x1, C_y1 + points[0][1], 0],
               [C_x1 - CaveRadius, 0, 0],
               [C_x1, -C_y1 - points[0][1], 0],
               [0, -points[0][1], 0]]
    
    # Vector to move it from the origin to desired position at end of rect slot
Cave_move_vector = [-GapL, 0, 0]
    # Creates the outline of the Cave
Cpoly = hfss.modeler.create_polyline(
        points=Cave_points,
        segment_type=["Line", "Arc", "Line"],
        close_surface=True,
        cover_surface=True,
        name="Cave")
    # Rotates about z axis and places in accordance to end of rectangle slot
hfss.modeler.rotate(Cpoly, "Z", Cave_rotate_deg, "deg")
hfss.modeler.move(Cpoly, Cave_move_vector)

    # Unite curve, slot, and cave for thicken then to cut/subtract from GND
hfss.modeler.connect(["VivaldiCurve", "VivaldiCurve_1"])
hfss.modeler.thicken_sheet(assignment="Cave", thickness=GNDH)
hfss.modeler.thicken_sheet(assignment="VivaldiCurve", thickness=-GNDH)
hfss.modeler.unite(["VivaldiCurve", "Gap", "Cave"])

    # Subtract from GND
hfss.modeler.subtract("GND", "VivaldiCurve", keep_originals=False)

# Front excess trim------------------------
        # Gets ride of excess substrate to make end of antenna flush with base
Front_trim = hfss.modeler.create_box(origin=[points[num_points - 1][0], points[num_points - 1][1], -SubH - GNDH],
                            sizes=[SubL/2 + SubTrim - points[num_points - 1][0], -SubW, SubH + 2*GNDH],
                            name="FrontTrim")
Front_trim.transparency = 0.5

hfss.modeler.subtract("GND, Substrate", "FrontTrim", keep_originals=False)

# Feed------------------------------------
Fstart_x = -SubL/2 + SubTrim       # Starting point botom right base

Feed_points_T1 = [[Fstart_x, FStartW/2, -SubH],                  # Base of feed, 1st taper
               [Fstart_x + FTaperL1, FTaper_y1, -SubH],
               [Fstart_x + FTaperL1, -FTaper_y1, -SubH],
               [Fstart_x, -FStartW/2, -SubH]]

Feed_points_A1 = []      # 1st Arc bottom up
Feed_points_AO1 = [Feed_points_T1[1]]     # 1st Arc Other side
Feed_points_A2 = []      # 2nd Arc
Feed_points_AO2 = []
Feed_points_AO3 = []

FstartA_x1 = Fstart_x + FTaperL1                    # Center point for curve_1 x & y
FstartA_y1 = FTaper_y1 + FeedRadius_A1              # Add radius so starting poing is right on last point
FstartA_xO1 = FstartA_x1
FstartA_yO1 = FstartA_y1
def get_feed_curve_points(curve_points_list, FstartA_x, FstartA_y, start_angle_A, end_angle_A, FeedRadius_A, num_points_feed):
    """ Gets the points needed to generate desired curves for the feed of the antenna

    Args:
        curve_points_list (list): Desired list to be altered/appended to - made outsde of the function because used elsewhere
        FstartA_x (int): starting x coordinate of the arc
        FstartA_y (int): starting y coordinate of the arc
        start_angle_A (int): starting angle of the arc
        end_angle_A (int): ending angle of the arc
        FeedRadius_A (int): radius of the arc - designed to adjust curvature of arc while keeping it in place
        num_points_feed (int): number of points to make the curve out of
    """
    
    angle_step = (end_angle_A - start_angle_A) / (num_points_feed - 1)       # Where to calculate each point
        
    for i in range(num_points_feed):
        angle = math.radians(start_angle_A + i * angle_step)
        x = FstartA_x + FeedRadius_A * math.sin(angle)
        y = FstartA_y + FeedRadius_A * math.cos(angle)
        curve_points_list.append([x, y, -SubH])

get_feed_curve_points(Feed_points_A1, FstartA_x1, FstartA_y1, start_angle_A1, end_angle_A1, FeedRadius_A1, num_points_feedA)

FeedRadius_AO1 = FstartA_y1 + FTaper_y1
get_feed_curve_points(Feed_points_AO1, FstartA_xO1, FstartA_yO1, start_angle_AO1, end_angle_AO1, FeedRadius_AO1, num_points_feedA)

FstartA_x2 = Feed_points_A1[num_points_feedA - 1][0] + FeedRadius_A2*math.cos(math.radians(90 + start_angle_A2))     # Moves center fo circle so arc starts on desired spot
FstartA_y2 = Feed_points_A1[num_points_feedA - 1][1] - FeedRadius_A2*math.sin(math.radians(90 + start_angle_A2))
get_feed_curve_points(Feed_points_A2, FstartA_x2, FstartA_y2, start_angle_A2, end_angle_A2, FeedRadius_A2, num_points_feedA)

Feed_points_A2.append([Feed_points_A2[num_points_feedA - 1][0], Feed_points_A2[num_points_feedA - 1][1] - 2*FTaper_y1, -SubH])        # Connects the end of the arcs to the other side of the arcs in this section

FstartA_xO2 = FstartA_x2                        # Same start of A2, altered radius to match other side
FstartA_yO2 = FstartA_y2
FeedRadius_AO2 = FeedRadius_A2 - 2*FTaper_y1
get_feed_curve_points(Feed_points_AO2, FstartA_xO2, FstartA_yO2, start_angle_AO2, end_angle_AO2, FeedRadius_AO2, num_points_feedA)


Feed_points_T2 = [Feed_points_A2[num_points_feedA - 1],         # 2nd Taper
                  [Feed_points_A2[num_points_feedA - 1][0] + FTaperL2, Feed_points_A2[num_points_feedA - 1][1] + FTaper_cut, -SubH],
                  [Feed_points_A2[num_points_feedA - 1][0] + FTaperL2, Feed_points_A2[num_points_feedA - 1][1] + FTaper_cut - FTaper_W, -SubH],
                  Feed_points_A2[num_points_feedA]]

Feed_points_A3 = [[Feed_points_A2[num_points_feedA - 1][0] + FTaperL2, Feed_points_A2[num_points_feedA - 1][1] + FTaper_cut - FTaper_W, -SubH]]
FstartA_x3 = Feed_points_A2[num_points_feedA - 1][0] + FTaperL2                     # 3rd Arc
FstartA_y3 = Feed_points_A2[num_points_feedA - 1][1] + FTaper_cut - FeedRadius_A3
get_feed_curve_points(Feed_points_A3, FstartA_x3, FstartA_y3, start_angle_A3, end_angle_A3, FeedRadius_A3, num_points_feedA)
Feed_points_A3.append([Feed_points_A3[num_points_feedA][0] - FTaper_W, Feed_points_A3[num_points_feedA][1], -SubH])

FstartA_xO3 = FstartA_x3                # 3rd curve other side
FstartA_yO3 = FstartA_y3
FeedRadius_AO3 = FeedRadius_A3 - FTaper_W
get_feed_curve_points(Feed_points_AO3, FstartA_xO3, FstartA_yO3, start_angle_AO3, end_angle_AO3, FeedRadius_AO3, num_points_feedA)


Feed_points_N = [Feed_points_A3[num_points_feedA],                      # Neck
                 (np.array(Feed_points_A3[num_points_feedA]) - np.array([0, FNeckL, 0])).tolist(),
                 (np.array(Feed_points_A3[num_points_feedA]) - np.array([FTaper_W, FNeckL, 0])).tolist(),
                 Feed_points_A3[num_points_feedA + 1]]

FHead_x = FHeadSideL*math.sin(math.radians(FHead_deg))                   # Head/Termination
Fhead_y = FHeadSideL*math.cos(math.radians(FHead_deg))
Feed_points_H = [[0, FTaper_W/2, -SubH],
                 [FHead_x, FTaper_W/2 + Fhead_y, -SubH],
                 [FHead_x + FeedRadius_H, 0, -SubH],
                 [FHead_x, -(FTaper_W/2 + Fhead_y), -SubH],
                 [0, -FTaper_W/2, -SubH]]
FeedH_move_vector = [((np.array(Feed_points_A3[num_points_feedA]) - np.array([0, FNeckL, 0])).tolist())[0] - FTaper_W/2,
                     ((np.array(Feed_points_A3[num_points_feedA]) - np.array([0, FNeckL, 0])).tolist())[1], 0]

Feedpoly_1 = hfss.modeler.create_polyline(
        points=Feed_points_T1,
        close_surface=True,
        cover_surface=True,
        segment_type=[],
        material="Copper",
        name="Feed")

Feedpoly_2 = hfss.modeler.create_polyline(
        points=Feed_points_A1,
        material="Copper",
        name="FeedA1")

Feedpoly_3 = hfss.modeler.create_polyline(
        points=Feed_points_AO1,
        material="Copper",
        name="FeedAO1")

Feedpoly_4 = hfss.modeler.create_polyline(
        points=Feed_points_A2,
        material="Copper",
        name="FeedA2")

Feedpoly_5 = hfss.modeler.create_polyline(
        points=Feed_points_AO2,
        material="Copper",
        name="FeedAO2")

Feedpoly_6 = hfss.modeler.create_polyline(
        points=Feed_points_T2,
        close_surface=True,
        cover_surface=True,
        material="Copper",
        name="FeedT2")

Feedpoly_7 = hfss.modeler.create_polyline(
        points=Feed_points_A3,
        material="Copper",
        name="FeedA3")

Feedpoly_8 = hfss.modeler.create_polyline(
        points=Feed_points_AO3,
        material="Copper",
        name="FeedAO3")

Feedpoly_9 = hfss.modeler.create_polyline(
        points=Feed_points_N,
        close_surface=True,
        cover_surface=True,
        material="Copper",
        name="FeedN")

Feedpoly_10 = hfss.modeler.create_polyline(
        points=Feed_points_H,
        close_surface=True,
        cover_surface=True,
        segment_type=["Line", "Arc", "Line"],
        material="Copper",
        name="FeedH")

    # Union, cover, finalize feed
hfss.modeler.rotate("FeedH", "Z", FHead_rotate_deg, "deg")
hfss.modeler.move("FeedH", FeedH_move_vector)
    
Feed_poly_list = [Feedpoly_2, Feedpoly_3, Feedpoly_4, Feedpoly_5]       # makes 1st Arc section whole
hfss.modeler.unite(Feed_poly_list)
hfss.modeler.cover_lines(Feedpoly_2)

Feed_poly_list_2 = [Feedpoly_7, Feedpoly_8]
hfss.modeler.unite(Feed_poly_list_2)          # Makes 2nd arc section whole 
hfss.modeler.cover_lines(Feedpoly_7)

Feed_poly_list_total = [Feedpoly_1, Feedpoly_2, Feedpoly_6, Feedpoly_7, Feedpoly_9, Feedpoly_10]
hfss.modeler.unite(Feed_poly_list_total)        # Unites all of the feed 

hfss.modeler.thicken_sheet(assignment="Feed", thickness=FeedMetalH)

# GND & VIA connections---------------------------------------
    # Substrate extension
SubEX = hfss.modeler.create_box(origin=[-SubL/2 + SubTrim, -Sub_EXW/2, 0],
                            sizes=[-Sub_EXL, Sub_EXW, -Sub_EXH],
                            name="SubEX",
                            material="Rogers RO4350 (tm)")
SubEX.color = "Green"
SubEX.transparency = 0

hfss.modeler.fit_all()

    # GND Extension
GNDEX = hfss.modeler.create_box(origin=[-SubL/2 + SubTrim, -GND_EXW/2, -SubH - FeedMetalH],
                            sizes=[-GND_EXL, GND_EXW, GND_EXH],
                            name="GNDEX",
                            material="Copper")
GNDEX.transparency = 0

    # GND cut
GND_y_corner_change = (GND_cutL / math.sin(math.radians(GNDEX_angle)))*math.cos(math.radians(GNDEX_angle))
GND_cut_points = [[-SubL/2 + SubTrim, GND_cutW/2, -SubH - FeedMetalH],
                  [-SubL/2 + SubTrim, -GND_cutW/2, -SubH - FeedMetalH],
                  [-SubL/2 + SubTrim -GND_cutL, -GND_cutW/2 + GND_y_corner_change, -SubH - FeedMetalH],
                  [-SubL/2 + SubTrim -GND_cutL, GND_cutW/2 - GND_y_corner_change, -SubH - FeedMetalH]]

GND_EXpoly = hfss.modeler.create_polyline(
    points=GND_cut_points,
    close_surface=True,
    cover_surface=True,
    name="S_GNDEX_cut")

hfss.modeler.thicken_sheet(assignment="S_GNDEX_cut", thickness=-GND_EXH)

hfss.modeler.subtract("GNDEX", "S_GNDEX_cut", keep_originals=False)


    # Feed GND extension
FeedGND_EXW = FStartW
Feed_GNDEX = hfss.modeler.create_box(origin=[-SubL/2 + SubTrim -GND_cutL, FStartW/2, -SubH - FeedMetalH],
                            sizes=[FeedGND_EXL, -FeedGND_EXW, GND_EXH],
                            name="FeedGNDEX",
                            material="Copper")

    # VIAs creation and mirroring
    # Spacing equation found: x = (L - 2Lnr) / (n + 1) ===> L-length; n-# of vias; r-radius of vias
VIA_spacing = (((-SubW/2) - (-GND_cutW/2 + GND_y_corner_change)) + 2*VRadius*n_vias) / (n_vias - 1) - VIA_spacing_modifier
VIA = hfss.modeler.create_cylinder(orientation="Z",         # Creates a cylinder for VIA cut
                                   origin=[-SubL/2 + SubTrim -GND_cutL/2 + VIA_xshift, VIA_spacing + (-GND_cutW/2 + GND_y_corner_change) + VIA_yshift, GNDH],
                                   radius=VRadius,
                                   height=-VHeight,
                                   name="VIA")

hfss.modeler[VIA].duplicate_along_line(vector=[0, VIA_spacing, 0],           # Vector to duplicate along starts from target
                                  clones=n_vias,                             # Final number of copies
                                  attach=True)                               # Attach to make 1 solid

VIA_1 = hfss.modeler[VIA].duplicate_along_line(vector=[VIA_x2shift, VIA_y2shift, 0],
                                  clones=2,
                                  attach=False)

hfss.modeler.mirror(assignment=[VIA, "VIA_1"],          # mirrors VIAs
                    origin=[0, 0, GNDH],
                    vector=[0, 1, 0],
                    duplicate=True)

# Raditation-------------------------------------
Radiation = hfss.modeler.create_box(origin=[-SubL/2 + SubTrim, -RadiationW/2, -RadiationH/4],
                            sizes=[RadiationL, RadiationW, RadiationH],
                            name="Radiation",
                            material="air")
Radiation.transparency = 1

# Duplicate for array---------------------------------
VIA_list = ["VIA", "VIA_1", "VIA_2", "VIA_1_1"]
TSA_parts_attached = ["Radiation", "Feed", "Substrate"]
TSA_parts_separate = ["GND", "SubEX", "GNDEX", "FeedGNDEX"] + VIA_list

for i in TSA_parts_attached:     # Attatched Duplicates
    hfss.modeler[i].duplicate_along_line(vector=[0, SubW, 0],           # Vector to duplicate along, number of copies
                                  clones=clones,
                                  attach=True)

for i in TSA_parts_separate:     # Separate Duplicates
    hfss.modeler[i].duplicate_along_line(vector=[0, SubW, 0],           # Vector to duplicate along, number of copies
                                  clones=clones,
                                  attach=False)
    
hfss.modeler.subtract(["GNDEX", "GNDEX_2", "SubEX", "SubEX_2"], VIA_list + ["VIA_4", "VIA_2_2", "VIA_1_3", "VIA_1_1_2"], keep_originals=False)

    # Altering/fixing of center antenna connector
hfss.modeler.delete(["VIA_1_2", "VIA_1_1_1", "FeedGNDEX_1"])

    # Center cut
Center_GND_cut_W = GND_cutW - 2*GND_y_corner_change
Cent_ant_GND_cut = hfss.modeler.create_box(origin=[Fstart_x, SubW - Center_GND_cut_W/2, -SubH - FeedMetalH],
                            sizes=[-Center_GND_cut_L, Center_GND_cut_W, Center_GND_cut_H],
                            name="centGNDcut")

hfss.modeler.subtract("GNDEX_1", "centGNDcut", keep_originals=False)

    # Center extension
Cent_ant_extension = hfss.modeler.create_box(origin=[Fstart_x, SubW - (FStartW - 0.09)/2, -SubH - FeedMetalH],
                            sizes=[-Sub_EXL, FStartW - 0.09, Center_GND_cut_H],
                            name="CentAntExt",
                            material="Copper")

    # Center VIAs
VIA_C_Spacing = ((Sub_EXL) + 2*VRadius*n_vias_c) / (n_vias_c - 1) - VIA_spacing_modifier
VIA_C = hfss.modeler.create_cylinder(orientation="Z",         # Creates a cylinder for VIA cut
                                   origin=[0, 0, GNDH],
                                   radius=VRadius,
                                   height=-VHeight,
                                   name="VIA_C")

# hfss.modeler[VIA].duplicate_along_line(vector=[VIA_C_Spacing, 0, 0],           # Vector to duplicate along starts from target
#                                   clones=n_vias,                             # Final number of copies
#                                   attach=True)                               # Attach to make 1 solid

# hfss.modeler.mirror(assignment=VIA_C,          # mirrors VIAs
#                     origin=[0, 0, GNDH],
#                     vector=[0, 1, 0],
#                     duplicate=True)

# Port-------------------------------------------
Port = hfss.modeler.create_rectangle(origin=[-SubL/2 + SubTrim, (clones-2)*SubW + PortB/2, GNDH],
                            sizes=[-PortB, -PortH],
                            name="WavePort",
                            orientation="YZ")
#== Sim Setup & Run ===============================================================================
# Solution type---------------------------------
hfss.solution_type = "DrivenModal"

# Assign wave port excitation-------------------
hfss.wave_port(Port, modes=1, name="WavePort1", renormalize=False)

# Assign Radiation (air box)-------------------
hfss.assign_radiation_boundary_to_objects("Radiation", name="AirRad")

# Set up frequency sweep simulation parameters---------------
setup1 = hfss.create_setup("Setup1")
setup1.props["Frequency"] = "35GHz"
# print(setup1.props)   # Help Debug
setup1.create_frequency_sweep(unit="GHz",
                              start_frequency=10, 
                              stop_frequency=50, 
                              num_of_freq_points= 80,
                              sweep_type= "Fast",
                              name="Sweep1")

# Far Field Infinite Sphere Setup------------------
Sphere1 = hfss.insert_infinite_sphere(x_start=0, x_stop=270, x_step=5, 
                                      y_start=0, y_stop=270, y_step=5,
                                      name="InfiniteSphere1")

# Start simulation---------------------------------
# hfss.analyze()

# # Simulation Data Reports--------------------------
# hfss.post.create_report("dB(S(1,1))",plot_type="Rectangular Plot",plot_name="S-Parameters")
# hfss.post.create_report("dB(GainTotal)", report_category="Far Fields", plot_type="3D Polar Plot",
#                         variations={"Freq": ["25GHz"]},
#                         plot_name="FarFieldGain")

#== Save & Export =====================================================================================
hfss.save_project(save_path)
print(f"\n===> Project saved at {save_path}")
    
hfss.modeler.export_3d_model(file_name='3x1_Vivaldi_Antenna_Array',
                             file_path=export_path,
                             file_format='.dxf',
                             assignment_to_export=None,
                             assignment_to_remove=None)
print(f"===> Project exported as .dxf at {export_path}\n")

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