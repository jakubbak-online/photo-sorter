import config


def flatten(s):
    return [item for sublist in s for item in sublist]


def get_keys_from_value(value_to_search):
    ext_dict = config.extensions_and_folders
    key = list()

    for values_dict in (ext_dict.values()):
        if value_to_search in values_dict:

            key += [key for key, value in ext_dict.items() if value == values_dict]

            # print(f"{values_dict} {value}")
            # print(key)

    return key
