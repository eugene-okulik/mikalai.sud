my_tuple = ("t1", "t2", "t3", "t4", "t5")

my_list = ["l1", "l2", "l3", "l4", "l5"]

my_dict1 = {"d1": "d1", "d2": "d2", "d3": "d3", "d4": "d4", "d5": "d5"}

my_set = {"s1", "s2", "s3", "s4", "s5"}

my_dict = {"tuple": my_tuple, "list": my_list, "dict": my_dict1, "set": my_set}
# default
print(my_dict)

# Для того, что хранится под ключом ‘tuple’: выведите на экран последний элемент
print(my_dict["tuple"][-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_list.append("l6")
my_list.pop(2)
print(my_list)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict1["i am a tuple"] = "new"
my_dict1.pop("d3")
print(my_dict1)

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества
my_set.add("s6")
my_set.remove("s3")
print(my_set)

# итог
print(my_dict)
