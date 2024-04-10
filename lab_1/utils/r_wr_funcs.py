import json

from typing import Dict, Optional


def read_txt(path_to_txt: str) -> Optional[str]:
    """
    Read the text in a user path.

    Args:
        path_to_text: path .txt file

    Returns:
        text: text from .txt or None
    """
    try:
        with open(path_to_txt, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        text = None
    finally:
        return text
    

def save_txt(path_to_save: str, text: str) -> bool:
    """
    Save the text in a user path.

    Args:
        path_to_save: path .txt file to write
        text: text to write to a .txt file

    Returns:
        saved: bool
    """
    saved = True
    try:
        with open(path_to_save, 'w', encoding='utf-8') as f:
            f.write(text)
    except FileNotFoundError:
        saved = False
    finally:
        return saved


def read_json(path_to_data: str) -> Optional[Dict[str, str]]:
    """
    Read data in json format at a user path.

    Args:
        path_to_data: path .json file

    Returns:
        data: text from .json or None
    """
    try:
        with open(path_to_data, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = None
    finally:
        return data


def save_json(path_to_save: str, data: Dict[str, str]) -> bool:
    """
    Save data in json format at a user path.

    Args:
        path_to_save: path .json file
        data: text to write to a .json file

    Returns:
        saved: flag, text has been saved or not
    """
    saved = True
    try:
        with open(path_to_save, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
    except FileNotFoundError:
        saved = False
    finally:
        return saved