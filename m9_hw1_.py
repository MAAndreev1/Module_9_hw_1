def apply_all_func(int_list, *functions):
    __result = {}
    for i in functions:
        __result.update({i.__name__: i(int_list)})
    return __result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
