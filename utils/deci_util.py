#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> decimal util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> DeciUtil
from ctypes import c_uint32


class DeciUtil:
    """
    _decimal module_

    Returns:
        _type_: _nothing_
    """
    @classmethod
    def count_page_numbers(cls, sum_num: int = 1, per_num: int = 1) -> int:
        """
        _count pages_

        Args:
            sum_num (int, optional): _total num_. Defaults to 1.
            per_num (int, optional): _num per page_. Defaults to 1.

        Returns:
            int: _int_
        """
        if isinstance(sum_num, int) is False:
            sum_num = 1
        if isinstance(per_num, int) is False or per_num == 0:
            per_num = 1
        
        pages = 1
        mod = sum_num % per_num
        if mod == 0:
            pages = int(sum_num / per_num)
        else:
            pages = int(sum_num / per_num) + 1
            
        return pages

    @classmethod
    def average_seqs_numbers(cls, src_seqs: any = None, end_index: int = 2, deci_num: int = 2) -> float:
        """
        _average sequence numbers_

        Args:
            src_seqs (any, list/tuple etc.): _seqs data_. Defaults to None.
            end_index (int, optional): _end index_. Defaults to 2.
            deci_num (int, optional): _bits of decimal_. Defaults to 2.

        Returns:
            float: _float. Defaults to 0.0_
        """
        if isinstance(src_seqs, (list, tuple)) is True and src_seqs:
            src_seqs = src_seqs[:end_index]
            if all(isinstance(x, (int, float)) is True for x in src_seqs) is True:
                result_num = sum(src_seqs) / len(src_seqs)
                return round(float(result_num), deci_num)
            
        return 0.0

    @classmethod
    def overflow_to_32bits(cls, src_num: any = 0) -> int:
        """
        _java 32 bits integer type overflow_

        Args:
            src_num (any, optional): _int/float_. Defaults to 0.

        Returns:
            int: _new int. Defaults to 0_
        """
        if isinstance(src_num, (int, float)) is True:
            # @@..> maximum java int
            max_int = 2147483647
            if not -max_int - 1 <= int(src_num) <= max_int:
                src_num = (src_num + (max_int + 1)) % (2 * (max_int + 1)) - max_int - 1
                return src_num
        
        return 0
        
    @classmethod
    def unsigned_right_shift(cls, src_num: int = 0, shift_num: int = 0) -> int:
        """
        _unsigned right shift_

        Args:
            src_num (int, optional): _source int_. Defaults to 0.
            shift_num (int, optional): _bits of right shift_. Defaults to 0.

        Returns:
            int: _new int. Defaults to 0_
        """
        if isinstance(src_num, int) is False:
            src_num = 0
        if isinstance(shift_num, int) is False:
            shift_num = 0

        # @@..! if number is less than 0 then convert to 32-bit unsigned uint.
        if src_num < 0:
            src_num = c_uint32(src_num).value
        # @@..! in order to be compatible with js and things like that,
        # @@..! the negative number shifts to the left.
        if shift_num < 0:
            return -cls.overflow_to_32bits(src_num << abs(shift_num))
        else:
            return cls.overflow_to_32bits(src_num >> shift_num)

