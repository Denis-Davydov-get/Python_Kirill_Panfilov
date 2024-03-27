print('\n\n'.join(
    ['\n'.join(['\t\t'.join([f'{y:<2}* {x:<2} = {x * y:>2}' for y in range(2 + n, 6 + n)]) for x in range(2, 11)]) for n
     in (0, 4)]))
