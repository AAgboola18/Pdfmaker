def ft_inch_to_m(str_arg):
    str_arg = str_arg.split()
    metres = int(str_arg[0]) * 0.3048 + int(str_arg[1]) * 0.0254
    metres = round(metres, 2)
    return metres


print(ft_inch_to_m("6 3"))
.
