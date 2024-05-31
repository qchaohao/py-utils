#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> base util
@@..> package category.utils
@@..> author pyleo

@@..> descriptive
@@..! important
@@..? unfinished
@@..x discarded

@@..> load on/load off  加载/卸载
@@..> push in/pull out  装入/提取
@@..> convert to/search for  转换/查找 
@@..> if is/value or gener  是否/生成值 或 生成器  
"""
############################################################################################################
# @@..> BaseUtil
from typing import Iterable
from itertools import tee, zip_longest
from pprint import pprint
from copy import deepcopy
import uuid
import random
import string


############################################################################################################
class BaseUtil:
    """
    _base funcitons_

    Returns:
        _type_: _nothing_
    """
    @classmethod
    def get_uuid(cls) -> str:
        """
        _return uuid1_

        Returns:
            str: _nothing_
        """
        return str(uuid.uuid4())
    
    @classmethod
    def get_ranten(cls) -> str:
        """
        _return random ten numbers_

        Returns:
            str: _nothing_
        """
        return str(random.random())[2:12]
    
    @classmethod
    def get_ranstr(cls, bit_num: int = 16) -> str:
        """
        _return random string_

        Args:
            bit_num (int, optional): _bits of num_. Defaults to 16.

        Returns:
            str: _nothing_
        """
        if isinstance(bit_num, int) is False:
            bit_num = 16
        
        str_set = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + "!@#$%^&*()_+"
        return "".join([random.choice(str_set) for _ in range(bit_num)])
    
    @classmethod
    def get_groupstr(cls, src_str: str = "", group_num: int = 4, 
                     filter_str: str = "", split_str: str = "-") -> str:
        """
        _return regroup string_

        Args:
            src_str (str, optional): _source string_. Defaults to "".
            group_num (int, optional): _number of group_. Defaults to 4.
            filter_str (str, optional): _filter string_. Defaults to "".
            split_str (str, optional): _split string_. Defaults to "-".

        Returns:
            str: _nothing_
        """
        src_list = [iter(str(src_str))] * group_num
        src_gen = zip_longest(*src_list, fillvalue=str(filter_str))
        new_list = ["".join(s) for s in src_gen]
        return f"{str(split_str)}".join(new_list)

    @classmethod
    def print_data(cls, src_data: any = None) -> None:
        """
        _print object_

        Args:
            src_data (any, str/list/dict etc.): _source data_. Defaults to None.
        """
        pprint(src_data)

    @classmethod
    def copy_data(cls, src_data: any = None) -> any:
        """
        _deep copy object_

        Args:
            src_data (any, str/list/dict etc.): _source data_. Defaults to None.

        Returns:
            any: _nothing_
        """
        return deepcopy(src_data)

    @classmethod
    def copy_generator(cls, src_gen: Iterable = None) -> tuple:
        """
        _copy generator_

        Args:
            src_gen (Iterable, optional): _source generator_. Defaults to None.

        Returns:
            tuple: _(generator, generator)_
        """
        if isinstance(src_gen, Iterable) is True:
            return tee(src_gen)
        else:
            return (x for x in range(0)), (x for x in range(0))

