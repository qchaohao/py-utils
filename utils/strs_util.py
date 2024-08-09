#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> regexp util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> StrsUtil
import re


class StrsUtil:
    """
    _string module_

    Returns:
        _type_: _nothing_
    """
    @classmethod
    def regex_for_first(cls, src_str: str = "", syntax: str = "") -> str:
        """
        _regex match the first value_

        Args:
            src_str (str, optional): _source string_. Defaults to "".
            syntax (str, optional): _regex syntax_. Defaults to "".

        Returns:
            str: _new string. Defaults to ""_
        """
        comp_regex = re.compile(str(syntax), re.S)
        new_str = comp_regex.findall(str(src_str))
        if new_str:
            return new_str[0]
        else:
            return ""

    @classmethod
    def regex_for_list(cls, src_str: str = "", syntax: str = "") -> list:
        """
        _regex match the list_

        Args:
            src_str (str, optional): _source string_. Defaults to "".
            syntax (str, optional): _regex syntax_. Defaults to "".

        Returns:
            str: _string list_
        """
        comp_regex = re.compile(str(syntax), re.S)
        return comp_regex.findall(str(src_str))

    @classmethod
    def regex_to_split(cls, src_str: str = "", syntax: str = "") -> list:
        """
        _regex split a string to list_

        Args:
            src_str (str, optional): _source string_. Defaults to "".
            syntax (str, optional): _regex syntax_. Defaults to "".

        Returns:
            list: _new list_
        """
        comp_regex = re.compile(str(syntax), re.S)
        return comp_regex.split(str(src_str))
 
    @classmethod       
    def regex_to_replace(cls, src_str: str = "", syntax: str = "", replace: str = "") -> str:
        """
        _regex replace a sub string_

        Args:
            src_str (str, optional): _source string_. Defaults to "".
            syntax (str, optional): _regex syntax_. Defaults to "".
            replace (str, optional): _replace string_. Defaults to "".

        Returns:
            str: _new string. Defaults to ""_
        """
        comp_regex = re.compile(str(syntax), re.S)
        return comp_regex.sub(str(replace), str(src_str))

    @classmethod
    def regex_to_int(cls, src_str: str = "") -> int:
        """
        _convert string to int_

        Args:
            src_str (str, optional): _source string_. Defaults to "".

        Returns:
            int: _int. Defaults to 0_
        """
        new_data = cls.regex_to_replace(src_str, ",", "")
        new_str = cls.regex_for_first(new_data, "-{0,1}\\d+")
        if new_str:
            return int(new_str)
        else:
            return 0

    @classmethod
    def regex_to_float(cls, src_str: str = "", deci_num: int = 2) -> float:
        """
        _convert string to float_

        Args:
            src_str (str, optional): _source string_. Defaults to "".
            deci_num (int, optional): _bits of num_. Defaults to 2.

        Returns:
            float: _float. Defaults to 0.0_
        """
        if isinstance(deci_num, int) is False:
            deci_num = 2
        
        new_data = cls.regex_to_replace(src_str, ",", "")
        new_str = ""
        if "." in new_data:
            new_str = cls.regex_for_first(new_data, "-{0,1}\\d+.\\d+")
        else:
            new_str = cls.regex_for_first(new_data, "-{0,1}\\d+")
        if new_str:
            return round(float(new_str), deci_num)
        else:
            return 0.0
        
    @classmethod
    def clear_all_spaces(cls, src_str: str = "") -> str:
        """
        _clear all spaces_

        Args:
            src_str (str, optional): _source string_. Defaults to "".

        Returns:
            str: _new string. Defaults to ""_
        """
        return cls.regex_to_replace(src_str, r"\r|\n|\t|\s+", "")

    @classmethod
    def clear_html_tags(cls, src_str: str = "") -> str:
        """
        _clear the html tags_

        Args:
            src_str (str, optional): _html tag string_. Defaults to "".

        Returns:
            str: _new string_
        """
        return cls.regex_to_replace(src_str, r"<[^>]+>", " ")
    
    @classmethod
    def one_space_separate(cls, src_str: str = "") -> str:
        """
        _the string is separated by a space_

        Args:
            src_str (str, optional): _source string_. Defaults to "".

        Returns:
            str: _new string_
        """
        new_str = cls.regex_to_replace(src_str, r"\r|\n|\t", "")
        new_str = cls.regex_to_replace(new_str, r"\s+", " ")
        new_str = new_str.strip()
        return new_str

    @classmethod
    def one_space_less(cls, src_str: str = "", src_len: int = 30) -> str:
        """
        _the string is separated by a space and less than a length_

        Args:
            src_str (str, optional): _source string_. Defaults to "".
            src_str (str, optional): _source length_. Defaults to 30.

        Returns:
            str: _new string_
        """
        if isinstance(src_len, int) is False:
            src_len = 30

        new_str = ""
        src_str = cls.one_space_separate(src_str)
        if len(src_str) <= src_len:
            new_str = src_str
        else:
            new_len = 0
            src_list = src_str.split(" ")
            for n in range(len(src_list)):
                single_word = f"{src_list[n]} "
                single_lenth = len(single_word)
                new_len += single_lenth
                if new_len < src_len:
                    new_str += single_word

        return new_str.strip()

    @classmethod
    def millions_to_units(cls, src_int: int = 0) -> str:
        """
        _convert numbers to unit string_

        Args:
            src_int (int, optional): _source int_. Defaults to 0.

        Returns:
            str: _str. Defaults to ""_
        """
        if isinstance(src_int, int) is False:
            return ""
        
        def str_size(nums, levels):
            if levels >= 2:
                return nums, levels
            elif nums >= 10000:
                nums /= 10000
                levels += 1
                return str_size(nums, levels)
            else:
                return nums, levels
    
        units = ["", "万", "亿"]
        num, level = str_size(src_int, 0)
        if level > len(units):
            level -= 1
        return f"{round(num, 2)}{units[level]}"
    
    @classmethod
    def units_to_millions(cls, src_str: str = "") -> any:
        """
        _convert unit string to numbers_

        Args:
            src_str (str, optional): _source string_. Defaults to "".

        Returns:
            any: _int/float. Defaults to 0_
        """
        src_str = str(src_str)
        units = ["w", "W", "万", "亿"]
        result = 0
        
        if any(u in src_str for u in units) is True:              
            if "." in src_str:
                result = cls.regex_to_float(src_str)
            else:
                result = cls.regex_to_int(src_str)

            if "亿" in src_str:
                result *= 100000000
            else:
                result *= 10000
        else:
            if "." in src_str:
                result = cls.regex_to_float(src_str)
            else:
                result = cls.regex_to_int(src_str)

        return result

