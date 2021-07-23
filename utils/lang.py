import json
import os


def load(mode):
    with open(f"lang/{mode}.json", "r", encoding='utf-8') as f:
        language = json.load(f)
        return language


def list_lang():
    translations = []
    for lang in os.listdir('lang'):
        if lang.endswith(".json"):
            lang = lang[:-5]
            translations.append(lang)

    return translations


def get(mode):
    lang = load(mode)
    dictionary = {
        'errors': lang['errors'],
        'lang_currently_using': lang["lang_currently_using"],
        'list_of_lang': lang["list_of_lang"],
        'invalid_lang': lang["invalid_lang"],
        'changed_lang': lang["changed_lang"],
        'set_vault_to': lang['set_vault_to'],
        'add_vault': lang['add_vault'],
        'sub_vault': lang['sub_vault'],
        'balance': lang['balance'],
        'deposit': lang['deposit'],
        'withdraw': lang['withdraw'],
        'load': lang['load'],
        'unload': lang['unload'],
        'reload': lang['reload'],
        '8ball': lang['8ball'],
        'cmd_usage': lang['cmd_usage'],
        'lotto': lang['lotto'],
        'toggle': lang['toggle']
    }
    return dictionary
