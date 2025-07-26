import os
import xml.etree.ElementTree as ET

def collect_tags_from_sources(source_folder):
    tag_to_text = {}

    for filename in os.listdir(source_folder):
        if filename.endswith(".xml"):
            full_path = os.path.join(source_folder, filename)
            try:
                tree = ET.parse(full_path)
                root = tree.getroot()

                for row in root.findall(".//Row[@Tag]"):
                    tag = row.get("Tag")
                    text_element = row.find("Text")
                    if tag and text_element is not None:
                        tag_to_text[tag] = text_element.text or ""
            except ET.ParseError as e:
                print(f"Warning: Failed to parse {filename}: {e}")
    
    return tag_to_text

def update_target_with_tags(tag_to_text, target_path, output_path):
    # Завантаження цільового файлу
    target_tree = ET.parse(target_path)
    target_root = target_tree.getroot()

    updated_count = 0

    for replace in target_root.findall(".//Replace[@Tag]"):
        tag = replace.get("Tag")
        if tag in tag_to_text:
            text_element = replace.find("Text")
            if text_element is not None:
                text_element.text = tag_to_text[tag]
                updated_count += 1

    print(f"Updated {updated_count} entries.")
    target_tree.write(output_path, encoding="utf-8", xml_declaration=True)

# --- Використання ---
SOURCE_FOLDER = "C:/Users/yul/Documents/Юлік/Програмування/CivVI_UA_localization/Base/Assets/Text/en_US"
TARGET = "D:/SteamLibrary/steamapps/common/Sid Meier's Civilization VI/Base/Assets/Text/Vanilla_uk_UA.xml"
OUTPUT = "output_uk_UA.xml"

all_tags = collect_tags_from_sources(SOURCE_FOLDER)
update_target_with_tags(all_tags, TARGET, OUTPUT)
