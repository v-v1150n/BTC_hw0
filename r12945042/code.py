import json
with open('/Users/v_v1150n/Desktop/Py_tool/project-5-at-2024-02-28-05-11-5144d2d4.json', 'r') as f:
    original_data = json.load(f)

new_data = {}


for index, entry in enumerate(original_data):
    if index == 0:
        filename = "amazon.mp4"
    elif index == 1:
        filename = "reddit.mp4"
    else:
        filename = f"{index + 1}.mp4"
    new_data[filename] = []
    for action in entry['annotations'][0]['result']:
        new_action = {
            "start_frame": None,
            "end_frame": None,
            "action_type": None,
            "down_coordinate": None,
            "up_coordinate": None,
            "type_word": None
        }
        if action['value']['labels'] == ['click']:
            new_action['action_type'] = 'click'
            new_action['type_word'] = None
        elif action['value']['labels'] == ['swipe']:
            new_action['action_type'] = 'swipe'
            new_action['type_word'] = None
        elif action['value']['labels'] == ['type']:
            new_action['action_type'] = 'type'
            new_action['type_word'] = 'macbook' 
        if action['value']['sequence']:
            new_action['start_frame'] = action['value']['sequence'][0]['frame']
            new_action['end_frame'] = action['value']['sequence'][1]['frame']

            down_x = action['value']['sequence'][0]['x']
            down_y = action['value']['sequence'][0]['y']
            down_width = action['value']['sequence'][0]['width']
            down_height = action['value']['sequence'][0]['height']
            new_action['down_coordinate'] = [down_x + down_width / 2, down_y - down_height / 2]
            
            up_x = action['value']['sequence'][1]['x']
            up_y = action['value']['sequence'][1]['y']
            up_width = action['value']['sequence'][1]['width']
            up_height = action['value']['sequence'][1]['height']
            new_action['up_coordinate'] = [up_x + up_width / 2, up_y - up_height / 2]
        new_data[filename].append(new_action)
with open('hw01.json', 'w') as f:
    json.dump(new_data, f, indent=4)
