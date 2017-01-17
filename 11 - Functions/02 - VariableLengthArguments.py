##!/usr/bin/python3

# def functionname([formal_args,] *var_args_tuple ):
#     "function_docstring"
#     function_suite
#     return [expression]

def printinfo( arg1, *vartuple):
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(10)
print(8,23,46)