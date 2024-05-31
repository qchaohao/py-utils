#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@@..> datetime util
@@..> package category.utils
@@..> author pyleo
"""
############################################################################################################
# @@..> TimeUtil
from datetime import datetime, timedelta
from calendar import monthrange
import time
import random


class TimeUtil:
    """
    _datetime module_

    Returns:
        _type_: _nothing_
    """
    @classmethod
    def sleep_time(cls, is_random: bool = True, secs: int = 5) -> None:
        """
        _sleep n seconds_

        Args:
            is_random (bool, optional): _bool_. Defaults to True.
            sec (any, optional): _int/float_. Defaults to 5.
        """
        if isinstance(secs, (int, float)) is True:
            if is_random is True:
                secs = random.randint(0, secs)
            time.sleep(secs)
        else:
            time.sleep(5)
        
    @classmethod
    def time_now(cls) -> float:
        """
        _return time now_

        Returns:
            float: _float_
        """
        return time.time()
        
    @classmethod
    def timestamp_now(cls, bit_num: int = 0) -> int:
        """
        _return how many bits of timestamp_

        Args:
            bit_num (int, optional): _bits of num_. Defaults to 0.

        Returns:
            int: _bits of timestamp. Defaults to timestamp_
        """
        if isinstance(bit_num, int) is True:
            return int(time.time() * (10 ** bit_num))
        else:
            return int(time.time() * (10 ** 0))
    
    @classmethod
    def datetime_now(cls) -> datetime:
        """
        _return date now_

        Returns:
            datetime: _datetime. Defaults to datetime_
        """
        return datetime.now()

    @classmethod
    def calculate_datetime(
        cls, src_date: datetime = None, days: any = 0, 
        hours: any = 0, mins: any = 0, secs: any = 0) -> datetime:
        """
        _convert date to custom date_

        Args:
            src_date (datetime, optional): _datetime_. Defaults to None.
            days (any, optional): _int/float_. Defaults to 0.
            hours (any, optional): _int/float_. Defaults to 0.
            mins (any, optional): _int/float_. Defaults to 0.
            secs (any, optional): _int/float_. Defaults to 0.

        Returns:
            datetime: _datetime. Defaults to datetime_
        """
        try:
            return src_date + timedelta(days=days, hours=hours, minutes=mins, seconds=secs)
        except Exception:
            return datetime.now()

    @classmethod
    def datetime_to_timestamp(cls, src_date: datetime = None) -> int:
        """
        _convert date to 10 bits timestamp_

        Args:
            src_date (datetime, optional): _datetime_. Defaults to None.

        Returns:
            int: _int. Defaults to timestamp_
        """
        if isinstance(src_date, datetime) is True:
            return int(time.mktime(src_date.timetuple()))
        else:
            return int(time.time() * (10 ** 0))

    @classmethod
    def timestamp_to_unixdate(cls, src_time: int = 0) -> datetime:
        """
        _convert 10 bits timestamp to date_

        Args:
            src_time (int, optional): _timestamp_. Defaults to 0.

        Returns:
            datetime: _datetime. Defaults to datetime_
        """
        if isinstance(src_time, int) is True:
            src_time = int(str(src_time)[:10])
            return datetime(1970, 1, 1) + timedelta(seconds=src_time)
        else:
            return datetime(1970, 1, 1) + timedelta(seconds=0)
           
    @classmethod 
    def str_to_datetime(cls, src_str: str = "", formatter: str = "") -> datetime:
        """
        _convert date string to date_

        Args:
            src_str (str, optional): _date string_. Defaults to "".
            formatter (str, optional): _formatter_. Defaults to "".

        Returns:
            datetime: _datetime. Defaults to datetime_
        """
        try:
            return datetime.strptime(src_str, formatter)
        except Exception:
            return datetime.now()
          
    @classmethod 
    def int_to_datetime(cls, src_year: int = 0, src_month: int = 0, src_day: int = 0) -> datetime:
        """
        _convert int to date_

        Args:
            src_year (int, optional): _source year_. Defaults to 0.
            src_month (int, optional): _source month_. Defaults to 0.
            src_day (int, optional): _source day_. Defaults to 0.

        Returns:
            datetime: _datetime. Defaults to datetime_
        """
        try:
            return datetime(src_year, src_month, src_day)
        except Exception:
            return datetime.now()

    @classmethod
    def make_last_day(cls, src_year: int = 0, src_month: int = 0) -> int:
        """
        _the last day of the month_

        Args:
            src_year (int, optional): _source year_. Defaults to 0.
            src_month (int, optional): _source month_. Defaults to 0.

        Returns:
            int: _int. Defaults to 31_
        """
        try:
            return monthrange(src_year, src_month)[1]
        except Exception:
            return 31
        
    @classmethod
    def make_day_list(
            cls, start_date: datetime = None, end_date: datetime = None,
            steps: int = 1, formatter: str = "%Y-%m-%d") -> list:
        """
        _days list_

        Args:
            start_date (datetime, optional): _date_. Defaults to None.
            end_date (datetime, optional): _date_. Defaults to None.
            steps (int, optional): _date step_. Defaults to 1.
            formatter (str, optional): _formatter_. Defaults to "%Y-%m-%d".

        Returns:
            list: _list. Defaults to []_
        """
        try:
            return_days = []
            days = (end_date - start_date).days + 1
            for i in range(0, days, steps):
                steps_date = start_date + timedelta(i)
                return_days.append(datetime.strftime(steps_date, formatter))
            return return_days
        except Exception:
            return []
           
