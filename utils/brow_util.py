#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> browser util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> BrowUtil
from dataclasses import dataclass, field


@dataclass
class BrowUtil:
    """
    _playwright instance_

    Returns:
        _type_: _nothing_
    """
    # @@..> request args
    page: object = field(default_factory=bool)
    frame: object = field(default_factory=bool)
    # @@..> error args
    error_code: int = field(default_factory=int)
    error_desc: str = field(default_factory=str)

    def reload_page(self) -> bool:
        """
        _refresh page_

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            self.page.reload()
            return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def close_page(self) -> bool:
        """
        _close the tab_

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            self.page.close()
            return True
        except Exception as ex:
            self.error_desc = ex
            return False

    def execute_js(self, js_str: str = "") -> bool:
        """
        _javascript execute_

        Args:
            js_str (str, optional): _javascript string_. Defaults to "".

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            self.page.evaluate(js_str)
            return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def open_url(self, src_url: str = "", timeout: int = 30) -> bool:
        """
        _open url_

        Args:
            src_url (str, optional): _source url_. Defaults to "".
            timeout (int, optional): _timeout_. Defaults to 30.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            self.page.goto(str(src_url), wait_until="load", timeout=timeout * 1000)
            return True
        except Exception as ex:
            self.error_desc = ex
            return False

    def get_url(self) -> str:
        """
        _get the url_

        Returns:
            str: _str. Defaults to str_
        """
        try:
            return self.page.url
        except Exception as ex:
            self.error_desc = ex
            return ""

    def get_page(self, is_frame: bool = False) -> str:
        """
        _get the page_

        Returns:
            any: _any. Defaults to str_
        """
        try:
            if is_frame is True:
                return self.frame.content()
            else:
                return self.page.content()
        except Exception as ex:
            self.error_desc = ex
            return ""

    def change_frame(self, syntax: str = "") -> bool:
        """
        _select frame_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            self.frame = self.page.query_selector(syntax).content_frame()
            return True
        except Exception as ex:
            self.error_desc = ex
            self.frame = False
            return False
            
    def wait_element(self, syntax: str = "", timeout: int = 30, is_frame: bool = False) -> bool:
        """
        _wait for element_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            timeout (int, optional): _timeout_. Defaults to 30.
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                self.frame.wait_for_selector(str(syntax), timeout=timeout * 1000, state="visible")
            else:
                self.page.wait_for_selector(str(syntax), timeout=timeout * 1000, state="visible")
            return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def get_text(self, syntax: str = "", is_frame: bool = False) -> str:
        """
        _get element text value_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            if is_frame is True:
                element = self.frame.query_selector(syntax)
                value = element.inner_text()
                return value
            else:
                element = self.page.query_selector(syntax)
                value = element.inner_text()
                return value
        except Exception as ex:
            self.error_desc = ex
            return ""
        
    def get_attribute(self, syntax: str = "", attr: str = "", is_frame: bool = False) -> str:
        """
        _get element attr value_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            attr (str, optional): _element attr_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            str: _str. Defaults to ""_
        """
        try:
            if is_frame is True:
                element = self.frame.query_selector(syntax)
                value = element.get_attribute(attr)
                return value
            else:
                element = self.page.query_selector(syntax)
                value = element.get_attribute(attr)
                return value
        except Exception as ex:
            self.error_desc = ex
            return ""
        
    def get_attribute_list(self, syntax: str = "", attr: str = "", is_frame: bool = False) -> list:
        """
        _get element attr values_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            attr (str, optional): _element attr_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            list: _list. Defaults to []_
        """
        value_list = []
        try:
            if is_frame is True:
                elements = self.frame.query_selector_all(syntax)
                for i in elements:
                    value = i.get_attribute(attr)
                    value_list.append(value)
                return value_list
            else:
                elements = self.page.query_selector_all(syntax)
                for i in elements:
                    value = i.get_attribute(attr)
                    value_list.append(value)
                return value_list
        except Exception as ex:
            self.error_desc = ex
            return []
        
    def keyboard_text(self, syntax: str = "", src_str: str = "", is_frame: bool = False) -> bool:
        """
        _set text_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            src_str (str, optional): _source string_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                self.frame.focus(syntax)
                self.frame.type(syntax, src_str, delay=0.2 * 1000)
                return True
            else:
                self.page.focus(syntax)
                self.page.type(syntax, src_str, delay=0.2 * 1000)
                return True          
        except Exception as ex:
            self.error_desc = ex
            return False

    def fill_text(self, syntax: str = "", src_str: str = "", is_frame: bool = False) -> bool:
        """
        _set text_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            src_str (str, optional): _source string_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                self.frame.focus(syntax)
                self.frame.fill(syntax, src_str)
                return True
            else:
                self.page.focus(syntax)
                self.page.fill(syntax, src_str)
                return True          
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def click_element(self, syntax: str = "", is_frame: bool = False) -> bool:
        """
        _element click_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.query_selector(syntax)
                button.click()
                return True
            else:
                button = self.page.query_selector(syntax)
                button.click()
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def check_element(self, syntax: str = "", is_frame: bool = False) -> bool:
        """
        _element check_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.query_selector(syntax)
                button.check()
                return True
            else:
                button = self.page.query_selector(syntax)
                button.check()
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def uncheck_element(self, syntax: str = "", is_frame: bool = False) -> bool:
        """
        _element uncheck_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.query_selector(syntax)
                button.uncheck()
                return True
            else:
                button = self.page.query_selector(syntax)
                button.uncheck()
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def select_element(self, syntax: str = "", src_str: str = "", is_frame: bool = False) -> bool:
        """
        _element select_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            src_str (str, optional): _source string_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.query_selector(syntax)
                button.select_option(src_str)
                return True
            else:
                button = self.page.query_selector(syntax)
                button.select_option(src_str)
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def bound_element(self, syntax: str = "", is_frame: bool = False) -> bool:
        """
        _element bound_

        Args:
            syntax (str, optional): _css/xpath/text_. Defaults to "".
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.query_selector(syntax)
                return button.bounding_box()
            else:
                button = self.page.query_selector(syntax)
                return button.bounding_box()
        except Exception as ex:
            self.error_desc = ex
            return {}

    def mouse_click(self, x_args: float = 0, y_args: float = 0, is_frame: bool = False) -> bool:
        """
        _mouse click_

        Args:
            x_args (float, optional): _x bound_. Defaults to 0.
            y_args (float, optional): _y bound_. Defaults to 0.
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.mouse.click(x_args, y_args)
                return True
            else:
                button = self.page.mouse.click(x_args, y_args)
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def mouse_move(self, x_args: float = 0, y_args: float = 0, is_frame: bool = False) -> bool:
        """
        _mouse move_

        Args:
            x_args (float, optional): _x bound_. Defaults to 0.
            y_args (float, optional): _y bound_. Defaults to 0.
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.mouse.move(x_args, y_args)
                return True
            else:
                button = self.page.mouse.move(x_args, y_args)
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def mouse_wheel(self, x_args: float = 0, y_args: float = 0, is_frame: bool = False) -> bool:
        """
        _mouse wheel_

        Args:
            x_args (float, optional): _x bound_. Defaults to 0.
            y_args (float, optional): _y bound_. Defaults to 0.
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.mouse.wheel(x_args, y_args)
                return True
            else:
                button = self.page.mouse.wheel(x_args, y_args)
                return True
        except Exception as ex:
            self.error_desc = ex
            return False

    def mouse_down(self, is_frame: bool = False) -> bool:
        """
        _mouse down_

        Args:
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.mouse.down()
                return True
            else:
                button = self.page.mouse.down()
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def mouse_up(self, is_frame: bool = False) -> bool:
        """
        _mouse up_

        Args:
            is_frame (str, optional): _if frame_. Defaults to False.

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            if is_frame is True:
                button = self.frame.mouse.up()
                return True
            else:
                button = self.page.mouse.up()
                return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def keyboard_action(self, key_string: str = "Enter") -> bool:
        """
        _element enter_

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            self.page.keyboard.press(key_string, delay=0.2 * 1000)
            return True
        except Exception as ex:
            self.error_desc = ex
            return False
        
    def screen_shot(self, path: str = "init.png") -> bool:
        """
        _screen shot_

        Args:
            path (str, optional): _path_. Defaults to "init.png".

        Returns:
            bool: _bool. Defaults to True_
        """
        try:
            self.page.screenshot(path=str(path), full_page=True)
            return True
        except Exception as ex:
            self.error_desc = ex
            return True

