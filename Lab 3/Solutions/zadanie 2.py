import os

def dir_list_rec(act_dir):
    result_list = []
    i = 0
    max_i = len(os.listdir(act_dir)) - 1
    for f in os.listdir(act_dir):
        if i != max_i:
            result_list.append("├───" + f)
        else:
            result_list.append("└───" + f)
        if os.path.isdir(os.path.join(act_dir, f)):
            for sub_element in dir_list_rec(os.path.join(act_dir, f)):
                if i != max_i:
                    result_list.append("│   " + sub_element)
                else:
                    result_list.append("    " + sub_element)
        i += 1
    return result_list

path = input("Podaj sciezke: ")
print(path)
print(*dir_list_rec(path), sep = "\n")


