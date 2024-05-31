#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> json util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> JsonUtil
from jsonpath import jsonpath
from yaml import safe_load, safe_dump
import ujson


class JsonUtil:
    """
    _json module_

    Returns:
        _type_: _nothing_
    """
    @classmethod
    def json_to_str(cls, src_json: any = None) -> str:
        """
        _convert json to string_

        Args:
            src_json (any, list/dict): _source json data_. Defaults to None.

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            if isinstance(src_json, (list, dict)) is True:
                return ujson.dumps(src_json, ensure_ascii=False)
            return ""
        except ujson.JSONDecodeError:
            return ""

    @classmethod
    def str_to_json(cls, src_data: any = None) -> list:
        """
        _convert string to json_

        Args:
            src_data (any, str/bytes): _source string data_. Defaults to None.

        Returns:
            any: _list/dict. Defaults to []_
        """
        try:
            if isinstance(src_data, (str, bytes)) is True:
                return ujson.loads(src_data)
            return []
        except ujson.JSONDecodeError:
            return []

    @classmethod
    def json_for_first(cls, src_json: any = None, syntax: str = "$.*") -> str:
        """
        _search json for first value_

        Args:
            src_json (any, list/dict): _source json data_. Defaults to None.
            syntax (str, optional): _path syntax_. Defaults to "$.".

        Returns:
            any: _any. Defaults to ""_
        """
        src_json = jsonpath(src_json, str(syntax))
        if src_json is not False:
            return src_json[0]
        else:
            return ""

    @classmethod
    def json_for_list(cls, src_json: any = None, syntax: str = "$.") -> list:
        """
        _search json for list_

        Args:
            src_json (any, optional): _list/dict_. Defaults to None.
            syntax (str, optional): _path syntax_. Defaults to "$.".

        Returns:
            list: _list. Defaults to []_
        """
        src_json = jsonpath(src_json, str(syntax))
        if src_json is not False:
            return src_json
        else:
            return []
        
    @classmethod
    def key_not_exist(cls, src_json: dict = None, key_list: list = None) -> str:
        """
        _check key if not in json_

        Args:
            src_json (dict, optional): _dict_. Defaults to None.
            src_keys (list, optional): _list of keys_. Defaults to None.

        Returns:
            str: _str. Defaults to ""_
        """
        if isinstance(src_json, dict) is True and isinstance(key_list, list) is True:
            for k in key_list:
                if k not in src_json.keys():
                    return k
        else:
            return ""

    @classmethod
    def read_from_file(cls, file_path: str = "") -> str:
        """
        _open json string_

        Args:
            file_path (str, optional): _path_. Defaults to "".

        Returns:
            any: _dict/list. Defaults to ""_
        """
        try:
            with open(str(file_path), encoding="utf-8") as f:
                 result_string = f.read()
            return result_string
        except FileNotFoundError:
            return ""
        
    @classmethod
    def write_to_file(cls, file_path: str = "", src_str: str = "") -> bool:
        """
        _write json string_

        Args:
            file_path (str, optional): _path_. Defaults to "".
            src_str (str, optional): _source string_. Defaults to "".

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            with open(str(file_path), "w", encoding="utf-8") as f:
                f.write(src_str)
            return True
        except FileNotFoundError:
            return False
        
    @classmethod
    def read_from_yaml(cls, file_path: str = "") -> list:
        """
        _open json string_

        Args:
            file_path (str, optional): _path_. Defaults to "".

        Returns:
            any: _dict/list. Defaults to []_
        """
        try:
            with open(str(file_path), encoding="utf-8") as f:
                 result_json = safe_load(f.read())
            return result_json
        except FileNotFoundError:
            return []

    @classmethod
    def write_to_yaml(cls, file_path: str = "", src_json: any = None) -> bool:
        """
        _write json string_

        Args:
            file_path (str, optional): _path_. Defaults to "".
            src_json (any, optional): _source json_. Defaults to None.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            with open(str(file_path), "w", encoding="utf-8") as f:
                safe_dump(src_json, f, allow_unicode=True)
            return True
        except FileNotFoundError:
            return False
        
    @classmethod
    def read_from_json(cls, file_path: str = "") -> any:
        """
        _open json string_

        Args:
            file_path (str, optional): _path_. Defaults to "".

        Returns:
            any: _dict/list. Defaults to []_
        """
        try:
            with open(str(file_path), encoding="utf-8") as f:
                 result_json = cls.str_to_json(f.read())
            return result_json
        except FileNotFoundError:
            return []

    @classmethod
    def write_to_json(cls, file_path: str = "", src_json: any = None) -> bool:
        """
        _write json string_

        Args:
            file_path (str, optional): _path_. Defaults to "".
            src_json (any, optional): _source json_. Defaults to None.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            with open(str(file_path), "w", encoding="utf-8") as f:
                result_data = cls.json_to_str(src_json)
                f.write(result_data)
            return True
        except FileNotFoundError:
            return False

