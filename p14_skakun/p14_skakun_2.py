import json

with open('image_info_test-dev2017.json') as file:
    for line in file:
        dict = json.loads(line)
        print("Number of images:", len(dict['images']))
        print("Number of categories:", len(dict['categories']))
        file_id = 0
        for i in dict['images']:
            if i["file_name"] == "000000000001.jpg":
                print('Link to photo 000000000001.jpg:', i["coco_url"], '\nPhoto height 000000000001.jpg:', i["height"], 
                '\nPhoto width 000000000001.jpg:', i["width"],
                '\nPhoto ID 000000000001.jpg:', i["id"])
            if i["id"]>file_id:
                file_id=i["id"]
        for i in dict['images']:
            if i["id"] == file_id:
                print("The largest number has a photo:", i["file_name"])