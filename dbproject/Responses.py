import random
import os

def responses(input_text):
    user_message = str(input_text).lower()
    if len(user_message) <= 4:
        return "Please enter a valid question"
    elif user_message[-1] == "?":
        rint = random.randint(1,6)
        if rint == 1:
            return "100 %"
        elif rint == 2:
            return "More likely yes than no"
        elif rint == 3:
            return "Perhaps🤔"
        elif rint == 4:
            return "Never"
        elif rint == 5:
            return "More likely no than yes"
        elif rint == 6:
            return "50/50"
    return "Please input a valid question"

imgExtension = ["png", "jpeg", "jpg"] #Image Extensions to be chosen from
allImages = list()

def chooseRandomImage(directory="D:/pymemes/dummybot/files/favouritememes"):
    for img in os.listdir(directory): #Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice] #Do Whatever you want with the image file
    return directory + "/" + chosenImage


def responseByProcent(input_text):
    user_message = str(input_text).lower()
    if len(user_message) <= 4:
        return "Please enter a valid question"
    rint = random.randint(1, 100)
    if user_message[-1] == "?":
        return "Шанс " + str(rint) + "%"
    return "Pls enter a valid question"