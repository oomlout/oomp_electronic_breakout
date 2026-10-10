
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []


    #relay
    if True:
        option = {}
        option["type_1"] = "output"
        option["type_2"] = "relay"
        option["breakout_description"] = "49_mm_width_38_mm_height_black_pcb"
        option["manufacturer"] = "aliexpress"
        option["breakout_pcb_width"] = 49
        option["breakout_pcb_height"] = 38
        option["part_number_aliexpress"] = "1005002867727977"
        option["webpage_aliexpress"] = "https://www.aliexpress.com/item/1005002867727977.html"
        #breakout_hole_array
        mounting_hole_width = 44
        mounting_hole_height = 33
        mounting_holes = []
        if True:
            mounting_holes.append([mounting_hole_width/2, mounting_hole_height/2])
            mounting_holes.append([mounting_hole_width/2, -mounting_hole_height/2])
            mounting_holes.append([-mounting_hole_width/2, mounting_hole_height/2])
            mounting_holes.append([-mounting_hole_width/2, -mounting_hole_height/2])
        option["mounting_holes"] = mounting_holes
        options.append(option)
        #mounting_hole_radius_name
        option["mounting_hole_radius_name"] = "m3"
    
    

    return options



# Call main automatically
if __name__ == "__main__":
    main()
