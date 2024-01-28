"""
корреляция Пирсона
r'xy = (sum((x'i-M'x)(y'i-M'y)))/(sum((x'i-M'x)**2)(y'i-M'y)**2)**0.5
"""

def Pirsons_correlation(list_x, list_y):
    def mean(value):
        return sum(value) / len(value)

    numerator = sum(map(lambda xi, yi: (xi - mean(list_x)) * (yi - mean(list_y)), list_x, list_y))
    denominator_1 = (sum(map(lambda xi: (xi - mean(list_x)) ** 2, list_x))) ** 0.5
    denominator_2 = (sum(map(lambda yi: (yi - mean(list_y)) ** 2, list_y))) ** 0.5

    if denominator_1 == 0 or denominator_2 == 0:
        return 0

    corr = numerator / (denominator_1 * denominator_2)
    return corr


list_x = [1, 2, 3, 4, 5]
list_y = [2, 3, 600, 8, 10]
correlation = Pirsons_correlation(list_x, list_y)
print(correlation)