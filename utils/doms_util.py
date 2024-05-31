#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> html util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> DomsUtil
from typing import Generator
from urllib.parse import quote, unquote, quote_plus, unquote_plus
from urllib.parse import urlencode, parse_qs, urlparse
from lxml import etree
from cssselect.parser import SelectorSyntaxError
import html


class DomsUtil:
    """
    _lxml/urllib module_

    Returns:
        _type_: _nothing_
    """
    @classmethod
    def break_up_url(cls, src_url: str = "") -> tuple:
        """
        _pull url out params_

        Args:
            src_url (str, optional): _url address_. Defaults to "".

        Returns:
            tuple: _head, domain, path, dict. Defaults to tuple_
        """
        url_head = urlparse(str(src_url)).scheme
        url_domain = urlparse(str(src_url)).netloc
        url_path = urlparse(str(src_url)).path
        url_query = urlparse(str(src_url)).query
        url_dict = parse_qs(url_query)
        return url_head, url_domain, url_path, url_dict
    
    @classmethod
    def joint_to_url(cls, src_dict: dict = None) -> str:
        """
        _push params in url_

        Args:
            src_dict (dict, optional): _source dict_. Defaults to None.

        Returns:
            str: _str. Defaults to ""_
        """
        if isinstance(src_dict, dict) is True:
            return urlencode(src_dict, encoding="utf-8")
        else:
            return ""

    @classmethod
    def str_to_quote(cls, src_data: any = "", safe_str = "") -> str:
        """
        _convert string to quote_

        Args:
            src_str (str, optional): _url string_. Defaults to "".
            safe_str (str, "/,?,=,&"): _not convert string_. Defaults to "".

        Returns:
            str: _quote string. Defaults to ""_
        """
        if isinstance(src_data, (str, bytes)) is True:
            return quote(src_data, safe=safe_str)
        else:
            return ""

    @classmethod
    def quote_to_str(cls, src_quo: any = "") -> str:
        """
        _convert quote to string_

        Args:
            src_quo (str, optional): _quote string_. Defaults to "".

        Returns:
            str: _url string. Defaults to ""_
        """
        if isinstance(src_quo, (str, bytes)) is True:
            return unquote(src_quo)
        else:
            return ""
    
    @classmethod
    def str_to_plus(cls, src_data: any = "", safe_str = "") -> str:
        """
        _convert string to quote plus_

        Args:
            src_str (str, optional): _url string_. Defaults to "".
            safe_str (str, "/,?,=,&"): _not convert string_. Defaults to "".

        Returns:
            str: _quote string. Defaults to ""_
        """
        if isinstance(src_data, (str, bytes)) is True:
            return quote_plus(src_data, safe=safe_str)
        else:
            return ""

    @classmethod
    def plus_to_str(cls, src_quo: any = "") -> str:
        """
        _convert quote plus to string_

        Args:
            src_quo (str, optional): _quote string_. Defaults to "".

        Returns:
            str: _url string. Defaults to ""_
        """
        if isinstance(src_quo, (str, bytes)) is True:
            return unquote_plus(src_quo)
        else:
            return ""
        
    @classmethod
    def html_to_escape(cls, src_str: str = "") -> str:
        """
        _convert html string to escape_

        Args:
            src_str (str, optional): _html string_. Defaults to "".

        Returns:
            str: _escape string_
        """
        return html.escape(str(src_str))

    @classmethod
    def escape_to_html(cls, src_esc: str = "") -> str:
        """
        _convert escape to html string_

        Args:
            src_esc (str, optional): _escape string_. Defaults to "".

        Returns:
            str: _html string_
        """
        return html.unescape(str(src_esc))
    
    @classmethod
    def html_to_dom(cls, src_str: str = "") -> etree._Element:
        """
        _convert html string to dom object_

        Args:
            src_str (str, optional): _html string_. Defaults to "".

        Returns:
            etree._Element: _dom object_
        """
        if str(src_str) == "":
            src_str = "<html></html>"
        return etree.HTML(str(src_str), parser=etree.HTMLPullParser(encoding="utf-8"))

    @classmethod
    def css_first_tags(cls, dom: etree._Element = None, syntax: str = "") -> str:
        """
        _css selector first tags_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            elements = dom.cssselect(str(syntax))
        except SelectorSyntaxError:
            return False
        else:
            # keep first tags
            if elements:
                for i in elements:
                    return etree.tostring(i, encoding="utf-8", method="html").decode("utf-8")
            else:
                return ""

    @classmethod
    def css_first_text(cls, dom: etree._Element = None, syntax: str = "") -> str:
        """
        _css selector first text_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            elements = dom.cssselect(str(syntax))
        except SelectorSyntaxError:
            return False
        else:
            if elements:
                for i in elements:
                    if i.text is not None:
                        return i.text
                    else:
                        return ""
            else:
                return ""

    @classmethod
    def css_first_attr(cls, dom: etree._Element = None, syntax: str = "", attr: str = "class") -> str:
        """
        _css selector first attr_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".
            attr (str, optional): _css attribute_. Defaults to "class".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            elements = dom.cssselect(str(syntax))
        except SelectorSyntaxError:
            return False
        else:
            if elements:
                for i in elements:
                    return str(i.attrib.get(str(attr), ""))
            else:
                return ""
    
    @classmethod
    def css_generate_tags(cls, dom: etree._Element = None, syntax: str = "") -> Generator:
        """
        _css selector generator_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            _type_: _nothing_

        Yields:
            Generator: _generator. Defaults to generator_
        """
        try:
            elements = dom.cssselect(str(syntax))
        except SelectorSyntaxError:
            return (x for x in range(0))
        else:
            # keep tags
            for i in elements:
                yield etree.tostring(i, encoding="utf-8", method="html").decode("utf-8")

    @classmethod
    def css_generate_text(cls, dom: etree._Element = None, syntax: str = "") -> Generator:
        """
        _css selector generator_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            _type_: _nothing_

        Yields:
            Generator: _generator. Defaults to generator_
        """
        try:
            elements = dom.cssselect(str(syntax))
        except SelectorSyntaxError:
            return (x for x in range(0))
        else:
            for i in elements:
                if i.text is not None:
                    yield i.text
                else:
                    yield ""

    @classmethod
    def css_generate_attr(
        cls, dom: etree._Element = None, syntax: str = "", attr: str = "class") -> Generator:
        """
        _css selector generator_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            _type_: _nothing_

        Yields:
            Generator: _generator. Defaults to generator_
        """
        try:
            elements = dom.cssselect(str(syntax))
        except SelectorSyntaxError:
            return (x for x in range(0))
        else:
            for i in elements:
                yield str(i.attrib.get(str(attr), ""))

    @classmethod
    def xpath_first_tags(cls, dom: etree._Element = None, syntax: str = "") -> str:
        """
        _xpath first tags_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            elements = dom.xpath(str(syntax))
        except etree.XPathEvalError:
            return False
        else:
            # keep first tags
            if elements:
                for i in elements:
                    return etree.tostring(i, encoding="utf-8", method="html").decode("utf-8")
            else:
                return ""

    @classmethod
    def xpath_first_value(cls, dom: etree._Element = None, syntax: str = "") -> str:
        """
        _xpath first value_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            elements = dom.xpath(str(syntax))
        except etree.XPathEvalError:
            return False
        else:
            if elements:
                for i in elements:
                    return str(i)
            else:
                return ""
            
    @classmethod
    def xpath_generate_tags(cls, dom: etree._Element = None, syntax: str = "") -> Generator:
        """
        _xpath generator_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            elements = dom.xpath(str(syntax))
        except etree.XPathEvalError:
            return (x for x in range(0))
        else:
            # keep tags
            for i in elements:
                yield etree.tostring(i, encoding="utf-8", method="html").decode("utf-8")

    @classmethod
    def xpath_generate_value(cls, dom: etree._Element = None, syntax: str = "") -> Generator:
        """
        _xpath generator_

        Args:
            dom (etree._Element, optional): _dom object_. Defaults to None.
            syntax (str, optional): _css syntax_. Defaults to "".

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            elements = dom.xpath(str(syntax))
        except etree.XPathEvalError:
            return (x for x in range(0))
        else:
            for i in elements:
                yield str(i)

