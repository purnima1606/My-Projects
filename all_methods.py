import cv2
from pyzbar.pyzbar import decode
import pytesseract
from PIL import Image
import re
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def aadhar_card(aadhar_file):
    img = cv2.imread(aadhar_file)
    for item in decode(img):
        my_data = item.data.decode("utf-8")
        # print(my_data)
        if len(my_data) > 50:
            full_name = re.findall(r'name="(.*?)"', my_data)[0]
            father_name = re.findall(r'co="(.*?)"', my_data)[0]
            rel, rel_name = father_name.split(": ")
            gender = re.findall(r'gender="(.*?)"', my_data)[0]
            uid = re.findall(r"\d{12}", my_data)[0]
            DOB = re.findall(r"\d{2}/\d{2}/\d{4}", my_data)[0]
            details = {"Name": full_name, "Guardian": rel_name,
                       "DOB": DOB, "Gender": gender, "Aadhar no": uid}
        else:
            details = {"Name": None, "Guardian": None, "DOB": None,
                       "Gender": None, "Aadhar no": None}
    return details


def passport(passport_file):
    img = cv2.imread(passport_file)
    pass_data = {"Passport No": None}
    for item in decode(img):
        my_data = item.data.decode("utf-8")
        if len(my_data) == 8:
            pass_data["Passport No"] = my_data
            # print(pass_data)
    return pass_data


def pancard(pancard_file):
    pancard_img = Image.open(pancard_file)
    text = pytesseract.image_to_string(pancard_img)
    if text:
        my_data = re.findall("[A-Z]{5}[0-9]{4}[A-Z]{1}", text)
        if my_data:
            if len(my_data[0]) == 10:
                pan_data = {"Pancard no":  my_data[0]}
            # return pan_data
            else:
                pan_data = {"Pancard no":  None}
        else:
            pan_data = {"Pancard no":  None}
            # return pan_data
    else:
        pan_data = {"Pancard No": None}
        # return pan_data
    return pan_data
