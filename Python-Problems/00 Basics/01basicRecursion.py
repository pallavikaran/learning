def add_recursion(tgt_num):
    if tgt_num > 0:
        result = tgt_num + add_recursion(tgt_num - 1)
        print(f"{tgt_num} + basic_recursion({tgt_num - 1}) => {result}")
    else:
        result = 0
    return result

print("\n\nRecursion Add Example Results")
add_recursion(6)


def sub_recursion(tgt_num):
    if tgt_num > 0:
        result = tgt_num - sub_recursion(tgt_num - 1)
        print(f"{tgt_num} - basic_recursion({tgt_num - 1}) => {result}")
    else:
        result = 0
    return result

print("\n\nRecursion Sub Example Results")
sub_recursion(10)
