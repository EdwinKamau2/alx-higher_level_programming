#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nw_list = []
    for i in range(list_length):
        try:
            nw_list.append(my_list_1[i] / my_list_2[i])
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            nw_list.append(0) if len(nw_list) == i else None
    return nw_list
