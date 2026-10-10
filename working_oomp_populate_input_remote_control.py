
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []


    #relay
    if True:
        option = {}
        option["type_1"] = "input"
        option["type_2"] = "remote_control"
        option["type_3"] = "servo_tester"
        option["breakout_description"] = "18_mm_width_14_mm_height_purple_pcb"
        option["manufacturer"] = "aliexpress"
        option["breakout_pcb_width"] = 18
        option["breakout_pcb_height"] = 14
        option["part_number_aliexpress"] = "1005009566745868"
        option["webpage_aliexpress"] = "https://www.aliexpress.com/item/1005009566745868.html"
        #breakout_hole_array
        mounting_hole_width = 15
        mounting_hole_height = 11
        mounting_holes = []
        if True:
            mounting_holes.append([mounting_hole_width/2, mounting_hole_height/2])
            mounting_holes.append([mounting_hole_width/2, -mounting_hole_height/2])
            #mounting_holes.append([-mounting_hole_width/2, mounting_hole_height/2])
            #mounting_holes.append([-mounting_hole_width/2, -mounting_hole_height/2])
        option["mounting_holes"] = mounting_holes
        options.append(option)
        #mounting_hole_radius_name
        option["mounting_hole_radius_name"] = "m2"
    
    

    return options



# Call main automatically
if __name__ == "__main__":
    main()
