import json

att_headWear_list = ["Pink Cap", "Blue Wizard Hat", "Red Beanie", "Curly Hair",
    "No Hat", "Devil's Horns", "Green Antennae", "Square Academic Cap",
    "Octopus Hat", "Towel Lamb's Head"]

att_eyebrows_list = ["Angry Dark Eyebrows", "Frowning Eyebrows", "Dotted Eyebrows",
    "Bushman Eyebrows", "Short Eyebrows", "Straight Eyebrows", "Wiggling Eyebrows",
    "Scratch Eyebrows", "Light Gray Eyebrows", "Mona Lisa's Eyebrows"]

att_eyes_list = ["Flat Blue Eyes", "Bright Eyes", "Sick Eyes", "Closed Eyes",
    "Tears", "Angry Eyes", "Money Eyes", "Dizzy Eyes",
    "Smiling Eyes", "Heart Eyes"]    

att_mouth_list = ["Growling Mouth", "Shy Smile", "Upset", "Drool",
    "Biting Bones", "Biting Bitcoin", "Dracula's Mouth",
    "Muzzle Mouth", "Smoking Mouth", "Mask"]

att_item_list = ["Pink Leash", "Cat Bell Leash", "Spike Leash", "Red String Ribbon",
    "Chain Leash", "Green Bow Tie", "Lucky Wooden Sign",
    "Purple Scarf", "Headset", "Angel Wings"]

att_att_skin_list = ["Baduk", "Dalmatian", "Injeolmi", "Pink Cheetah",
    "Dark Gray", "Rainbow Dress", "Mermaid", "Zebra",
    "Monkey", "Blue Ice"]

att_background_list = ["In The Warm Sea", "Purple City", "The Clouds Reflected In The Sea",
    "Green Forest", "Volcanic Zone", "Pink Princess Room", "In Front Of The Asis",
    "Covered In White", "Outside The Earth", "Lavender Field"]

level5 = [0, 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]

for i in range(10):
    # 레벨 측정
    if i in level5:
        level_value = 5
    elif i >= 100 and i % 100 == 0:
        level_value = 4
    elif i < 1000:
        level_value = 3
    elif i > 1000 and i < 4000:
        level_value = 2
    else:
        level_value = 1

    # json파일로 해당하는 애들값 저장
    file_data = []

    headWear = {"trait_type":"Headwear", "value":att_headWear_list[i]}
    eyebrows = {"trait_type":"Eyebrows", "value":att_eyebrows_list[i]}
    eyes = {"trait_type":"Eyes", "value":att_eyes_list[i]}
    mouth = {"trait_type":"Mouth", "value":att_mouth_list[i]}
    item = {"trait_type":"Item", "value":att_item_list[i]}
    skin = {"trait_type":"Skin", "value":att_att_skin_list[i]}
    background = {"trait_type":"Background", "value":att_background_list[i]}
    level = {"trait_type":"Level", "value": level_value}

    file_data.append(headWear)
    file_data.append(eyebrows)
    file_data.append(eyes)
    file_data.append(mouth)
    file_data.append(item)
    file_data.append(skin)
    file_data.append(background)
    file_data.append(level)
    
    with open(f'./att/attribute{i}.json', 'w') as mk_f:
        json.dump(file_data, mk_f, indent=5)
        

    with open(f'./att/attribute{i}.json', 'r') as f:
        json_data = json.load(f)

    print(json.dumps(json_data, indent=5))