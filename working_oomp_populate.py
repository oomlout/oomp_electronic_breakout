
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []

    import working_oomp_populate_input_sensor
    #options.extend(working_oomp_populate_input_sensor.main(**kwargs))
    import working_oomp_populate_mcu
    #options.extend(working_oomp_populate_mcu.main(**kwargs))
    import working_oomp_populate_output
    options.extend(working_oomp_populate_output.main(**kwargs))
    
###### populate taxonomy details and oobb details
    if True:
        for option in options:       
            option["taxonomy_1"] = f"electronic"  
            option["taxonomy_2"] = f"breakout"             
            count = 3
            value_name = "type_1"
            value = option.get(value_name, None)
            option[f"taxonomy_{count}"] = f"{value}"
            count += 1
            if "type_2" in option:
                value_name = "type_2"
                value = option.get(value_name, None)
                option[f"taxonomy_{count}"] = f"{value}"
                count += 1
            if "type_3" in option:
                value_name = "type_3"
                value = option.get(value_name, None)
                option[f"taxonomy_{count}"] = f"{value}"
                count += 1
            value_name = "breakout_description"
            value = option.get(value_name, None)
            option[f"taxonomy_{count}"] = f"{value}"
            count += 1
            if "manufacturer" in option:
                value_name = "manufacturer"
                value = option.get(value_name, None)
                option[f"taxonomy_14"] = f"{value}"            
            if "part_number" in option:
                value_name = "part_number"
                value = option.get(value_name, None)
                option[f"taxonomy_15"] = f"{value}"
            #oobb details
            if True:
                pass
                oobb_details = {}
                #taxonomy_4 hole_cover
                oobb_details["oobb_name"] = "mounting_plate_default"
                oobb_details.update(option)
                option["oobb_details"] = oobb_details
            #svg details
            if False:
                pass
                svg_details = {}
                svg_details["svg_name"] = option_type
                svg_details["svg_width"] = option.get("width", None)            
                svg_details["svg_height"] = option.get("height", None)
                option["svg_details"] = svg_details
    
    #load the options into full list
    extras = []
    for option in options:
        extra = {}
        extra.update(option)
        extras.append(extra)

    
    ######### add notes from an id string
    import working_oomp_populate_extra_detail
    working_oomp_populate_extra_detail.main(extras=extras)


    write_extras(extras)



# Call main automatically
if __name__ == "__main__":
    main()
