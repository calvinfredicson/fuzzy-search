from fuzzywuzzy import fuzz
from sys import argv, exit, stdout
import json


stdout.reconfigure(encoding='utf-8')


def fuzzy_ratio(search_string: str, template: str) -> int:
    ratio = fuzz.ratio(search_string, template)
    return ratio


def read_json_to_dict(file_path: str) -> list:
    with open(file_path, 'r', encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


def fuzzy_search_from_all_result(query_string, json_data) -> list:
    all_result = json.loads(json_data)
    match_result_list = []
    for recognized_rectangle in all_result:
        ocr_text = recognized_rectangle["text"]
        search_result = {
            "ratio": fuzzy_ratio(ocr_text, query_string),
            "data": recognized_rectangle
        }
        match_result_list.append(search_result)
    result = max(match_result_list, key=lambda x: x["ratio"])
    return result


def main(json_data, query_string) -> None:
    find_string = fuzzy_search_from_all_result(query_string, json_data)
    print(json.dumps(find_string))


if __name__ == "__main__":
    # json_file_path = r"C:\Users\Calvin Fredicson\Documents\Personal\Python\FuzzySearch\google_vision_words.json"
    # query_string = "Component Name"
    if len(argv) != 3:
        exit(1)
    query_string = argv[1]
    json_data = argv[2]
    main(json_data, query_string)
