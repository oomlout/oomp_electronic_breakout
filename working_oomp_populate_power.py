
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []


    #relay
    if True:
        option = {}
        option["type_1"] = "power"
        option["type_2"] = "dc_to_dc"
        option["type_3"] = "step_down"
        option["type_4"] = "lm2596"
                
        option["breakout_description"] = "48_mm_width_25_mm_height_blue_pcb"
        option["manufacturer"] = "aliexpress"
        option["breakout_pcb_width"] = 48
        option["breakout_pcb_width_extra"] = 10
        option["breakout_pcb_height"] = 25
        #shift_wire_hole_y -5  and x 5
        option["shift_wire_hole_y"] = -5
        option["shift_wire_hole_x"] = -5
        option["part_number_aliexpress"] = "1005010001439374"
        option["webpage_aliexpress"] = "https://www.aliexpress.com/item/1005010001439374.html"
        #breakout_hole_array
        mounting_hole_width = 36
        mounting_hole_height = 20
        mounting_holes = []
        if True:
            #mounting_holes.append([mounting_hole_width/2, mounting_hole_height/2])
            mounting_holes.append([mounting_hole_width/2, -mounting_hole_height/2])
            mounting_holes.append([-mounting_hole_width/2, mounting_hole_height/2])
            #mounting_holes.append([-mounting_hole_width/2, -mounting_hole_height/2])
        option["mounting_holes"] = mounting_holes
        options.append(option)
        #mounting_hole_radius_name
        option["mounting_hole_radius_name"] = "m3"
    
    

    return options



# Call main automatically
if __name__ == "__main__":
    main()
