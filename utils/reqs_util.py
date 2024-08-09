#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> requsets util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> ReqsUtil
from dataclasses import dataclass, field
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import SSLError, ProxyError, ReadTimeout, ConnectionError
import time
import random
# @@..! eliminate ssl alarm
disable_warnings(InsecureRequestWarning)


@dataclass
class ReqsUtil:
    """
    _requests instance_

    Returns:
        _type_: _nothing_
    """
    # @@..> request args
    request_session: any = field(default_factory=object) 
    request_url: str = field(default_factory=str)
    request_head: dict = field(default_factory=dict)
    request_data: any = field(default_factory=bool)
    request_proxy: dict = field(default_factory=dict)
    request_cookie: list = field(default_factory=list)
    request_time: int = field(default_factory=int)
    # @@..> response args
    response_url: str = field(default_factory=str)
    response_head: dict = field(default_factory=dict)
    response_code: int = field(default_factory=int)
    response_page: str = field(default_factory=str)
    response_cookie: list = field(default_factory=list)
    response_time: float = field(default_factory=float)
    response_total: float = field(default_factory=float)
    # @@..> error args
    error_resp: bool = field(default_factory=bool)
    error_code: int = field(default_factory=int)
    error_desc: str = field(default_factory=str)
    # @@..> user-agent args
    ua_name: str = field(default_factory=str)
    ua_version: str = field(default_factory=str)
    ua_header: dict = field(default_factory=dict) 
        
    def start_session(
        self, identifier: str = "chrome_117", random_extension: bool = True, 
        is_http1: bool = False) -> None:
        """
        _start session_

        Args:
            identifier (str, optional): _identifier version_. Defaults to "chrome_117".
            random_extension (bool, optional): _random extension_. Defaults to True.
            is_http1 (bool, optional): _if http1 or not_. Defaults to False.

        """
        self.request_session = Session()
        adapter = HTTPAdapter(max_retries=0)
        self.request_session.mount("http://", adapter)
        self.request_session.mount("https://", adapter)

    def close_session(self) -> None:
        # @@..> close session
        del self.request_session

    def clear_cookies(self) -> None:
        # @@..> clear cookies
        self.request_session.cookies.clear()

    def set_cookies(self) -> None:
        # @@..> set cookies
        for c in self.request_cookie:
            if c.get("domain"):
                self.request_session.cookies.set(
                    name=c.get("name"), value=c.get("value"), 
                    domain=c.get("domain"), path=c.get("path"))
            else:
                self.request_session.cookies.set(name=c.get("name"), value=c.get("value"))

    def update_cookies(self) -> None:
        # @@..> update cookies
        for c in self.request_cookie:
            self.request_session.cookies.update({c.get("name"): c.get("value")})
            
    def get_cookies(self) -> None:
        # @@..> get cookies
        self.response_cookie = []
        for s in self.request_session.cookies:
            self.response_cookie.append(
                {"name": s.name, "value": s.value, "domain": s.domain, "path": s.path})

    def method_to_request(
        self, method_string: str = "GET", data_type: str = "None", is_redirect: bool = False, 
        redirect_times: int = 1, skip_verify: bool = False, is_content: bool = False) -> bool:
        """
        _request method_

        Args:
            method_string (str, optional): _method of request_. Defaults to "GET".
            data_type (str, optional): _type of request data_. Defaults to "None".
            is_redirect (bool, optional): _if jump or not_. Defaults to False.
            redirect_times (int, optional): _jump numbers_. Defaults to 1.
            skip_verify (bool, optional): _if skip verify or not_. Defaults to False.
            is_content (bool, optional): _if content or not_. Defaults to False.

        Returns:
            bool: _bool. Defaults to False_
        """
        # @@..> start time
        start_time = time.time()
        if method_string not in ["GET", "HEAD", "OPTIONS", "DELETE", "POST", "PUT", "PATCH"]:
            # @@..> count time  
            self.response_time = round(time.time() - start_time, 3)
            self.response_total = round(self.response_total + self.response_time, 3)
            self.error_resp = False
            self.error_code = 520
            self.error_desc = f"Invalid Args**{method_string}"
            return False
        # @@..> make args
        is_verify = True
        if skip_verify is True:
            is_verify = False
        request_params = {
            "url": self.request_url, "headers": self.request_head, "proxies": self.request_proxy, 
            "timeout": self.request_time, "allow_redirects": bool(is_redirect), "verify": is_verify,
            "stream": False, 
        }
        if data_type == "data":
            request_params.update({"data": self.request_data})
        elif data_type == "json": 
            request_params.update({"json": self.request_data})
        elif data_type == "files": 
            request_params.update({"files": self.request_data})
        else:
            request_params.update({"data": self.request_data})

        try:
            # @@..> set args
            self.request_session.keep_alive = False
            self.request_session.max_redirects = redirect_times 
            if method_string == "GET":
                resp = self.request_session.get(**request_params)
            elif method_string == "HEAD":
                resp = self.request_session.head(**request_params)
            elif method_string == "OPTIONS":
                resp = self.request_session.options(**request_params)
            elif method_string == "DELETE":
                resp = self.request_session.delete(**request_params)
            elif method_string == "POST":
                resp = self.request_session.post(**request_params)
            elif method_string == "PUT":
                resp = self.request_session.put(**request_params)
            elif method_string == "PATCH":
                resp = self.request_session.patch(**request_params)
            else:
                resp = self.request_session.get(**request_params)

            resp.encoding = "utf-8"
            self.response_url = resp.url
            self.response_head = resp.headers
            self.response_code = resp.status_code
            if is_content is True:
                self.response_page = resp.content
            else:
                self.response_page = resp.content.decode("utf-8")
            
            resp.close()
        except SSLError as ex:
            self.error_resp = True
            self.error_code = 521
            self.error_desc = ex
        except ProxyError as ex:
            self.error_resp = True
            self.error_code = 522
            self.error_desc = ex
        except ConnectionError as ex:
            self.error_resp = True
            self.error_code = 523
            self.error_desc = ex
        except ReadTimeout as ex:
            self.error_resp = True
            self.error_code = 524
            self.error_desc = ex
        except Exception as ex:
            self.error_resp = True
            self.error_code = 525
            self.error_desc = ex
        else:
            self.error_resp = False
            self.error_code = 0
            self.error_desc = f"Success**{method_string}**{data_type}"
        # @@..> count time
        self.response_time = round(time.time() - start_time, 3)
        self.response_total = round(self.response_total + self.response_time, 3)
        if self.error_resp is True:
            return False
        else:
            return True

    def make_user_agent(self, ua_name: str = "chrome_win") -> None:
        """
        _build base header_

        Args:
            ua_name (str, optional): _user agent version name_. Defaults to "chrome_win".

        """
        # @@..> version dict
        defaults = {
            "chrome_win": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                          "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
            },
            "chrome_mac": {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                          "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
                "Sec-Ch-Ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"macOS"',
            },
            "chrome_chase": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                          "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
            },
            "chrome": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                          "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
            },
            "edge": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                              "(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,"
                          "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "keep-alive",
            },
            "firefox": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) "
                              "Gecko/20100101 Firefox/109.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                          "*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
            },
            "nexus": {
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                              " (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                          "*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
            },
            "iphone": {
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
                              "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 "
                              "Safari/604.1",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,"
                          "*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Connection": "keep-alive",
            },
        }
        # @@..> get header
        if ua_name == "random":
            ua_list = list(defaults.keys())
            ua_name = random.choice(ua_list)
        
        version_dict = defaults.get(str(ua_name), "")
        self.ua_name = str(ua_name)
        self.ua_header = version_dict
        if not version_dict:
            version_dict = defaults.get("chrome_win")
            self.ua_name = "chrome_win"
            self.ua_header = version_dict
        
        self.ua_version = self.ua_header.get("User-Agent", "")
    
        