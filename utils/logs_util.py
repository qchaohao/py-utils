#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> logs util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> LogsUtil
from dataclasses import dataclass, field
import logging


@dataclass
class LogsUtil:
    """
    _logs instance_

    Returns:
        _type_: _nothing_
    """
    logger: object = field(default_factory=bool)
    handler: object = field(default_factory=bool)
    formatter: object = field(default_factory=bool)
    
    def set_level(self, log_name: str = "root", log_level: str = "debug") -> None:
        """
        _set level_

        Args:
            log_name (str, optional): _description_. Defaults to "root".
            log_level (str, optional): _description_. Defaults to "debug".
        """
        self.logger = logging.getLogger(log_name)
        if log_level == "debug":
            self.logger.setLevel(level=logging.DEBUG)
        elif log_level == "info":
            self.logger.setLevel(level=logging.INFO)
        elif log_level == "warning":
            self.logger.setLevel(level=logging.WARNING)
        elif log_level == "error":
            self.logger.setLevel(level=logging.ERROR)
        elif log_level == "critical":
            self.logger.setLevel(level=logging.CRITICAL)
        else:
            self.logger.setLevel(level=logging.DEBUG)
        self.formatter = logging.Formatter(
            fmt="[%(asctime)s.%(msecs)d] [%(levelname)s] [%(process)d] %(message)s", 
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    def stream_mode(self, log_name: str = "root", log_level: str = "debug") -> None:
        """
        _print logs_

        Args:
            log_name (str, optional): _description_. Defaults to "root".
            log_level (str, optional): _description_. Defaults to "debug".
        """
        self.set_level(log_name, log_level)
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        
    def unsafe_mode(
        self, log_name: str = "root", log_level: str = "debug", log_path: str = "root.log") -> None:
        """
        _process unsafe_

        Args:
            log_name (str, optional): _description_. Defaults to "root".
            log_level (str, optional): _description_. Defaults to "debug".
            log_path (str, optional): _description_. Defaults to "root.log".
        """
        self.set_level(log_name, log_level)
        self.handler = logging.FileHandler(log_path, encoding="utf-8")
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def remove_handler(self) -> None:
        """
        _remove hanler_
        """
        if isinstance(self.handler, (logging.StreamHandler, logging.FileHandler)) is True:
            if isinstance(self.logger, logging.Logger) is True:
                self.logger.removeHandler(self.handler)

