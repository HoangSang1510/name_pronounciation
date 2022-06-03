import pickle
path = "/Users/sangdh/code/training-0522/project"
vocab_dir = path + "/name_pronunciation/rhyme.pkl"

vocab = pickle.load(open(vocab_dir, 'rb'))

# data cho trước
list_name = ['Hương', 'Hưng', 'Thiên', 'Trường', 'Trúc', 'Hiền', 'Nhực',
             'Nhựt', 'Nhật', 'Hào', 'Tạo', 'Tài', 'Mai', 'Hân', 'Nguyên',
             'Tiền', 'Thương', 'Hiệp', 'Duyên']
list_subname = [['N', 'T', 'T', 89], ['H', 'N', 'H', 91], ['P', 'N', 90],
                ['N', 'C', 'T', 95], ['M', 'T', 'T', 92], ['T', 'T', 'T', 88],
                ['H', 'T', 'M', 87], ['H', 'N', 83], ['H', 'K', 83],
                ['T', 'V', 84], ['H', 'N', 85], ['H', 'N', 83], ['Đ', 'T', 85],
                ['H', 'N', 90], ['T', 'N', 83], ['V', 'N', 93], ['T', 'H', 94],
                ['L', 'N', 96], ['L', 'T', 98]]


# print(len(vocab))
# print(vocab[0])
# print(len(vocab[0]))
# if('hoa' in vocab[0]):
#     print("yes")

name_dic = {}
subname_dic = {}

List_name_lenght = len(list_name)
vocab_lenght = len(vocab)

# tạo 2 từ điển dict name và sub name, với key là thứ tự nhóm mà tên thuộc về
for i in range(List_name_lenght):
    for j in range(vocab_lenght):
        if(list_name[i].lower() in vocab[j]):
            if(j in name_dic.keys()):
                name_dic[j].append(list_name[i])
                subname_dic[j].append(list_subname[i])
            else:
                name_dic[j] = []
                subname_dic[j] = []
                name_dic[j].append(list_name[i])
                subname_dic[j].append(list_subname[i])
# print(name_dic)
# print(subname_dic)


def remove_dup(list_of_list):
    ban_list = []
    for i in range(len(list_of_list)):
        list_of_list[i] = list(map(str, list_of_list[i]))
        for j in range(len(list_of_list[i])):
            if(list_of_list[i][j] in ban_list):
                list_of_list[i][j] = '?'
            else:
                ban_list.append(list_of_list[i][j])
    result = [[ele for ele in sub if ele != '?'] for sub in list_of_list]
    return result


# chuẩn hóa dict của sub name, loại bỏ trùng
for i in subname_dic:
    subname_dic[i] = remove_dup(subname_dic[i])
# print(subname_dic)


# tạo ra tên mới từ 2 dict
none_dup_name = []
for i in name_dic:
    for j in range(len(name_dic[i])):
        for k in subname_dic[i][j]:
            none_dup_name.append(name_dic[i][j] + " " + k)


print(none_dup_name)
