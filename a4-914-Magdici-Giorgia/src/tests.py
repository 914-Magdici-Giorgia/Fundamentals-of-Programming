from functions import get_coefficients, add_number, insert, \
    remove_pos, remove_interval, replace_nrs, get_real_interval, modulo, get_list_mod_comp, \
    sum_complex, prod_complex, sum_interval, product_interval


def test_get_coefficients():
    assert get_coefficients("+3+7i") == [3, 7]
    assert get_coefficients("3-i") == [3, -1]
    assert get_coefficients("+3") == [3, 0]
    assert get_coefficients("+7i") == [0, 7]
    assert get_coefficients("+i") == [0, 1]
    assert get_coefficients("+3-7i") == [3, -7]
    assert get_coefficients("-3+7i") == [-3, 7]
    assert get_coefficients("3") == [3, 0]
    assert get_coefficients("7i") == [0, 7]
    assert get_coefficients("i") == [0, 1]
    assert get_coefficients("3-7i") == [3, -7]
    assert get_coefficients("-3") == [-3, 0]
    assert get_coefficients("-7i") == [0, -7]
    assert get_coefficients("-i") == [0, -1]
    assert get_coefficients("-3-7i") == [-3, -7]


def test_add_number():
    assert add_number([], "6+9i") == ["6+9i"]
    assert add_number(["3", "8i", "2+4i"], "i") == ["3", "8i", "2+4i", "i"]


def test_insert():
    assert insert([], "3", 0) == ["3"]
    assert insert(["2+8i", "2+4i", "6+9i"], "5+87i", 2) == ["2+8i", "2+4i", "5+87i", "6+9i"]


def test_remove_pos():
    assert remove_pos(["2+8i", "2+4i", "5+87i", "6+9i"], 2) == ["2+8i", "2+4i", "6+9i"]
    assert remove_pos(["1+3i", "6+i", "87i", "12+5i"], 0) == ["6+i", "87i", "12+5i"]


def test_remove_interval():
    assert remove_interval(["2+8i", "2+4i", "5+87i", "6+9i"], 0, 2) == ["6+9i"]
    assert remove_interval(["2+8i", "2+4i", "5+87i", "6+9i"], 0, 3) == []
    assert remove_interval(["2+8i", "2+4i", "5+87i", "6+9i"], 2, 3) == ["2+8i", "2+4i"]


def test_replace_nrs():
    assert replace_nrs(["2+8i", "2i", "2+4i", "2i", "5+87i", "6+9i"], "2i", "5i") == ["2+8i", "5i", "2+4i", "5i",
                                                                                      "5+87i", "6+9i"]
    assert replace_nrs(["2+8i", "4i", "2+4i", "6i", "5+87i", "2+4i"], "2+4i", "5+7i") == ["2+8i", "4i", "5+7i", "6i",
                                                                                          "5+87i", "5+7i"]


def test_get_real_interval():
    assert get_real_interval(["2+8i", "4", "2", "6i", "5", "2+4i", "2+4i", "5+7i"], 0, 4) == ["4", "2", "5"]
    assert get_real_interval(["2+8i", "4i", "2+4i", "6", "5+87i", "2+4i", "2+4i", "5"], 3, 7) == ["6", "5"]


def test_modulo():
    assert modulo("3+4i") == 5
    assert modulo("6") == 6
    assert modulo("9i") == 9
    assert modulo("i") == 1
    assert modulo("0") == 0


def test_get_list_mod_comp():
    assert get_list_mod_comp(["2+8i", "4i", "2+4i", "6", "5+87i", "2+4i", "2+4i", "5"], ">", "5") == ["2+8i", "6",
                                                                                                      "5+87i"]
    assert get_list_mod_comp(["2+8i", "5i", "3+4i", "6", "5+87i", "3+4i", "2+4i", "5"], "=", "5") == ["5i", "3+4i",
                                                                                                      "3+4i", "5"]
    assert get_list_mod_comp(["2+8i", "4i", "1+4i", "6", "2i", "8+4i", "2+4i", "3"], "<", "5") == ["4i", "1+4i", "2i",
                                                                                                   "2+4i", "3"]


def test_sum_complex():
    assert sum_complex('2+6i', '9+7i') == '11+13i'
    assert sum_complex('2', '9+7i') == '11+7i'
    assert sum_complex('6i', '7i') == '13i'
    assert sum_complex('0', '9+7i') == '9+7i'


def test_prod_complex():
    assert prod_complex('8-5i', '3-2i') == '14-31i'
    assert prod_complex('7i', '-2+i') == '-7-14i'
    assert prod_complex('-9+7i', '-2') == '18-14i'


def test_sum_interval():
    assert sum_interval(['1+3i', '2', '5i', '2-i', '-8-2i'], 1, 4) == '-4+2i'
    assert sum_interval(['1+3i', '2', '5i', '2-i', '-8-2i'], 0, 3) == '5+7i'
    assert sum_interval(['1+3i', '2', '5i', '2-i', '-8-2i'], 4, 4) == '-8-2i'


def test_product_interval():
    assert product_interval(['1+3i', '2', '5i', '2-i', '-8-2i'], 1, 4) == '-40-180i'
    assert product_interval(['1+3i', '2', '5i', '2-i', '-8-2i'], 0, 4) == '500-300i'
    assert product_interval(['1+3i', '2', '5i', '2-i', '-8-2i'], 4, 4) == '-8-2i'


def test_functions():
    test_prod_complex()
    test_sum_complex()
    test_get_list_mod_comp()
    test_modulo()
    test_get_real_interval()
    test_replace_nrs()
    test_remove_interval()
    test_remove_pos()
    test_insert()
    test_add_number()
    test_get_coefficients()
    test_sum_interval()
    test_product_interval()


