import os
import cv2

import scripts.mask.gay as gay
import scripts.mask.trans as trans

import scripts.filter.pinker as pinker
import scripts.filter.threshold_pinker as threshold_pinker
import scripts.filter.blurrer as blurrer


import scripts.filter.mask_pinker as mask_pinker
import scripts.filter.threshold_mask_pinker as mask_threshold_pinker

# configs
input_image = "input.jpg"
output_type = "png"

filters = [
    {
        "name": "pinker",
        "scripts": [pinker]
    },
    {
        "name": "threshold_pinker",
        "scripts": [threshold_pinker]
    },
    {
        "name": "blurrer",
        "scripts": [blurrer]
    },
    {
        "name": "pink_blurrer",
        "scripts": [pinker, blurrer]
    },
    {
        "name": "threshold_blurrer",
        "scripts": [threshold_pinker, blurrer]
    },
    {
        "name": "gay",
        "scripts": [gay, mask_pinker]
    },
    {
        "name": "gay_threshold",
        "scripts": [gay, mask_threshold_pinker]
    },
    {
        "name": "gay_blurrer",
        "scripts": [gay, mask_pinker, blurrer]
    },
    {
        "name": "gay_threshold_blurrer",
        "scripts": [gay, mask_threshold_pinker, blurrer]
    },
    {
        "name": "gay_threshold_pinked_blurrer",
        "scripts": [gay, mask_threshold_pinker, threshold_pinker, blurrer]
    },
    {
        "name": "trans",
        "scripts": [trans, mask_pinker]
    },
    {
        "name": "trans_threshold",
        "scripts": [trans, mask_threshold_pinker]
    },
    {
        "name": "trans_blurrer",
        "scripts": [trans, mask_pinker, blurrer]
    },
    {
        "name": "trans_threshold_blurrer",
        "scripts": [trans, mask_threshold_pinker, blurrer]
    },
    {
        "name": "trans_threshold_pinked_blurrer",
        "scripts": [trans, mask_threshold_pinker, threshold_pinker, blurrer]
    }
]

# begin script
edit_times = {}

for filter in filters:
    for script in filter["scripts"]:
        script_file = os.path.abspath(script.__file__)
        if script_file in edit_times:
            continue
        edit_time = os.path.getmtime(script_file)
        edit_times[script_file] = edit_time

def should_run_filter(filter):
    name = filter["name"]

    output_file = os.path.join("outputs", f"{name}.{output_type}")

    if not os.path.exists(output_file):
        return True

    last_edit_script = None
    for script in filter["scripts"]:
        script_file = os.path.abspath(script.__file__)
        last_edit = edit_times[script_file]
        if last_edit_script == None or last_edit > last_edit_script:
            last_edit_script = last_edit
    last_edit_output = os.path.getmtime(output_file)

    edited_script_after_output = last_edit_script > last_edit_output
    edited_input_after_output = last_edit_input > last_edit_output

    return edited_input_after_output or edited_script_after_output

if not os.path.exists(input_image):
    print(f"input image {input_image} doesnt exist")
    exit(1)

img = cv2.imread(input_image)
last_edit_input = os.path.getmtime(input_image)

for filter in filters:
    name = filter["name"]
    output_file = os.path.join("outputs", f"{name}.{output_type}")

    if not should_run_filter(filter):
        continue

    print(f"running {name}")
    result = img.copy()
    for script in filter["scripts"]:
        result = script.run_filter(result)
    cv2.imwrite(output_file, result)
