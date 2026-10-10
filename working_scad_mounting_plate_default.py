import copy
import oobb
import yaml
import os
import scad_help

def get_plate_dimensions(**kwargs):
    """Size the plate in OOBB units, adding optional per-axis extras in mm."""
    dimensions = []
    for key, default in (("breakout_pcb_width", 49), ("breakout_pcb_height", 38)):
        minimum = kwargs.get(key, default) + kwargs.get(f"{key}_extra", 0) + 12
        dimensions.append(int((minimum + 14) // 15) + 1)
    return tuple(dimensions)

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("depth", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    breakout_pcb_width = kwargs.get("breakout_pcb_width", 49)
    breakout_pcb_height = kwargs.get("breakout_pcb_height", 38)
    mounting_holes = kwargs.get("mounting_holes", [])
    mounting_hole_radius_name = kwargs.get("mounting_hole_radius_name", "m3")

    width, height = get_plate_dimensions(**kwargs)
    kwargs["width"] = width
    kwargs["height"] = height
    #add plate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_plate"    
        p3["depth"] = depth
        #p3["holes"] = True         uncomment to include default holes
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb.append_full(thing,**p3)
    
    #add holes seperate
    if True:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = "perimeter"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb.append_full(thing,**p3)

    # Add PCB standoffs; the default lift is 3 mm.
    mounting_holes = kwargs.get("mounting_holes", [])
    for hole in mounting_holes:
        add_mounting_hole(thing, hole, **kwargs)


    #add a test screw_countersunk
    if False:
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"screw_countersunk"
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        pos1 = copy.deepcopy(pos)         
        pos1[2] += depth
        p3["pos"] = pos1
        p3["m"] = "#"
        oobb.append_full(thing,**p3)

    if prepare_print:
        scad_help.prepare_base_for_print(thing, pos, **kwargs)

def add_mounting_hole(thing, hole, **kwargs):
    pos = kwargs.get("pos", [0, 0, 0])
    depth = kwargs.get("depth", 3)
    lift = kwargs.get("mounting_lift", 3)
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "negative"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["depth"] = depth + lift
    mounting_hole_radius_name = kwargs.get("mounting_hole_radius_name", "m3")
    p3["radius_name"] = mounting_hole_radius_name
    pos1 = copy.deepcopy(pos)
    pos1[0] += hole[0]
    pos1[1] += hole[1]
    p3["pos"] = pos1
    rot1 = copy.deepcopy(kwargs.get("rot", [0, 0, 0]))
    rot1[1] += 180
    p3["rot"] = rot1
    oobb.append_full(thing, **p3)
    #add_cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_cylinder"
    dep = lift
    p3["depth"] = dep
    radius = float(mounting_hole_radius_name.replace("m", "").replace("_",".")) + 1.5/2
    p3["radius"] = radius
    pos1 = copy.deepcopy(pos)
    pos1[0] += hole[0]
    pos1[1] += hole[1]
    pos1[2] += dep/2 + depth
    p3["pos"] = pos1
    oobb.append_full(thing, **p3)
