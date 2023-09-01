from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

phone_pattern = r'(\+7|8)\s*(\s?\()*(\d{3})[\s\)-]*(\d{3})[\)\s-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\3)\4-\5-\6 \7\8'

def main(contact_list: list):
    """Приведения справочника к формату (ФИО к Ф+И+О и номера к +7(999)999-99-99 доб.9999)"""
    new_list = list()
    for item in contact_list:
        name = ' '.join(item[:3]).split(' ')
        result = [name[0], name[1], name[2], item[3], item[4],
                  re.sub(phone_pattern, phone_sub, item[5]),
                  item[6]]
        new_list.append(result)
    return list_processing(new_list)


def list_processing(contacts: list):
    """Функция обработки списка от дублей ФИО и пустых записях"""
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]

    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)

    return result_list

if __name__ == '__main__':
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(main(contacts_list))