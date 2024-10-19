import os, shutil

extensions_dict = {
    "image_extensions": (".jpg", ".webp"),
    "video_extensions": (".mp4", ".mkv", ".MKV", ".flv"),
}


folder_path = input("Enter folder path : ")


def file_finder(folder_path, file_extensions=""):
    return [
        file
        for file in os.listdir(folder_path)
        for extensions in file_extensions
        if file.endswith(extensions)
    ]


for extension_type, extension_tuple in extensions_dict.items():
    folderName = extension_type.split("_")[0] + "Files"
    folderPath = os.path.join(folder_path, folderName)
    os.mkdir(folderPath)
    for item in file_finder(folder_path, extension_tuple):
        item_path = os.path.join(folder_path, item)
        item_new_path = os.path.join(folderName, item)
        shutil.move(item_path, item_new_path)
