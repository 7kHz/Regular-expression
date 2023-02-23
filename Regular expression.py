import csv
import re

with open('phonebook_raw.csv', encoding='utf8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
split_list_ = []
pattern_l_f_s_name = r'([А-Я]\w+)\s*\W*([А-Я]\w+)\s*\W*([А-Я]\w+)*(\W+)'
pattern_organization = r'\,([А-Я]+\w+)\,(\W?)'
pattern_numbers = r'(\+7|8)\W*\s*(\d{2,3})\W*\s*\-*(\d{2,3})\-*(\d{2})*\-*(\d{2})'
pattern_numbers_optional = r'(\s*\W*доб.*\s*\W*)(\d{4})\s*\W*'
substitution_l_f_s_name = r'\1 \2 \3,'
substitution_organization = r', \1, '
substitution_numbers = r'+7(\2)\3-\4-\5'
substitution_numbers_optional = r' доб.\2, '
for rows in contacts_list[1:]:
    join_list = ",".join(rows)
    l_f_s_name = re.sub(pattern_l_f_s_name, substitution_l_f_s_name, join_list, re.A)
    organization = re.sub(pattern_organization, substitution_organization, l_f_s_name, re.A)
    numbers = re.sub(pattern_numbers, substitution_numbers, organization, re.A)
    numbers_optional = re.sub(pattern_numbers_optional, substitution_numbers_optional, numbers, re.A)
    split_list = numbers_optional.split(',')
    split_list_.append(split_list)
with open("phonebook.csv", 'w') as f:
    datawriter = csv.writer(f, delimiter=",")
    for row in split_list_:
        datawriter.writerow(row)