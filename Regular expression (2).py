import csv
import re

with open('phonebook_raw.csv', encoding='utf8') as f:
    rows = csv.reader(f, delimiter=',')
    contacts_list = list(rows)
all_data = []
repeated_dict = {}
repeated_data = []
v_sorted_list_1 = []
v_sorted_list_2 = []
i_v_list_1 = []
i_v_list_2 = []
index_list_1 = []
index_list_2 = []
value_dict = {}
i_v_dict_1 = {}
i_v_dict_2 = {}
i_v_dict_3 = {}
i_v_dict_4 = {}
data_list = []
pattern_l_f_s_name = r'([А-Я]\w+)\s*\W*([А-Я]\w+)\s*\W?([А-Я]\w+)*\W?'
pattern_organization = r'\,([А-Я]+\w+)'
pattern_numbers = r'(\+7|8)\W*\s*(\d{2,3})\W*\s*\-*(\d{2,3})\-*(\d{2})*\-*(\d{2})'
pattern_numbers_optional = r'(\s*\W*доб.*\s*\W*(\d{4})\s*\W*)'
substitution_l_f_s_name = r'\1, \2, \3, '
substitution_organization = r' \1'
substitution_numbers = r' +7(\2)\3-\4-\5'
substitution_numbers_optional = r' доб.\2, '
for rows in contacts_list:
    join_list = ",".join(rows)
    l_f_s_name = re.sub(pattern_l_f_s_name, substitution_l_f_s_name, join_list, re.A)
    organization = re.sub(pattern_organization, substitution_organization, l_f_s_name, re.A)
    numbers = re.sub(pattern_numbers, substitution_numbers, organization, re.A)
    numbers_optional = re.sub(pattern_numbers_optional, substitution_numbers_optional, numbers, re.A)
    split_list = numbers_optional.split(',')
    all_data.append(split_list)
for record in all_data:
    repeated_dict[record[0]] = repeated_dict.setdefault(record[0], 0) + 1
    if repeated_dict.setdefault(record[0]) != 1:
        repeated_data.append(record[0])
for record in all_data:
    data_dct = {record[0]: record[1:]}
    for keys, values in data_dct.items():
        if keys in repeated_data[0]:
            for index, value in enumerate(values):
                if value != '' and value != ' ':
                    i_v_1 = index, value
                    if i_v_1 not in i_v_list_1:
                        i_v_list_1.append(i_v_1)
        if keys in repeated_data[1]:
            for index, value in enumerate(values):
                if value != '' and value != ' ':
                    i_v_2 = index, value
                    if i_v_2 not in i_v_list_2:
                        i_v_list_2.append(i_v_2)
    value_dict.update(data_dct)
for i, v in i_v_list_1:
    index_list_1.append(i)
    index_list_1.sort()
    i_v_dict = {i: v}
    i_v_dict_1.update(i_v_dict)
for n in index_list_1:
    i_v_dict_2[n] = i_v_dict_1.setdefault(n)
for key, value in i_v_dict_2.items():
    if value not in v_sorted_list_1:
        v_sorted_list_1.append(value)
for key, value in value_dict.items():
    if key in repeated_data[0]:
        value_dict[key] = v_sorted_list_1
for i, v in i_v_list_2:
    index_list_2.append(i)
    index_list_2.sort()
    i_v_dict = {i: v}
    i_v_dict_3.update(i_v_dict)
for n in index_list_2:
    i_v_dict_4[n] = i_v_dict_3.setdefault(n)
for key, value in i_v_dict_4.items():
    if value not in v_sorted_list_2:
        v_sorted_list_2.append(value)
for key, value in value_dict.items():
    if key in repeated_data[1]:
        value_dict[key] = v_sorted_list_2
for key, value in value_dict.items():
    if key not in data_list:
        value.insert(0, key)
        data_list.append(value)
for rows in data_list:
    for i, v in enumerate(rows):
        if v == '' or v == ' ':
            rows.pop(i)
    for i, v in enumerate(rows):
        if '+7' in v:
            if i == 5:
                continue
            rows[i] = ''
            rows.insert(5, v)
            break
with open("phonebook.csv", 'w', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=",")
    for rows in data_list:
        datawriter.writerow(rows)

