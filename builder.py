import xml.etree.ElementTree as ET

def update_texts(source_path, target_path, output_path):
    # Завантаження першого XML (джерело)
    source_tree = ET.parse(source_path)
    source_root = source_tree.getroot()

    # Створення словника: Tag -> Text
    tag_to_text = {}
    for row in source_root.findall(".//Row[@Tag]"):
        tag = row.get("Tag")
        text_element = row.find("Text")
        if tag and text_element is not None:
            tag_to_text[tag] = text_element.text or ""

    # Завантаження другого XML (ціль)
    target_tree = ET.parse(target_path)
    target_root = target_tree.getroot()

    # Оновлення Text елементів за Tag
    for replace in target_root.findall(".//Replace[@Tag]"):
        tag = replace.get("Tag")
        if tag in tag_to_text:
            text_element = replace.find("Text")
            if text_element is not None:
                text_element.text = tag_to_text[tag]

    # Запис зміненого XML у файл
    target_tree.write(output_path, encoding="utf-8", xml_declaration=True)

# Використання
SOURCE = "C:/Users/yul/Documents/Юлік/Програмування/CivVI_UA_localization/Base/Assets/Text/en_US/AdvisorText.xml"
TARGET = "D:/SteamLibrary/steamapps/common/Sid Meier's Civilization VI/Base/Assets/Text/Vanilla_uk_UA.xml"
update_texts(SOURCE, TARGET, "output_uk_UA.xml")
