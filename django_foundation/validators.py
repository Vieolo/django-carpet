# Python
from datetime import datetime, date
import decimal
import json
from typing import overload
from typing import Optional, Union, Callable, Tuple

# This App
from .exceptions import InputError


@overload
def string_validation(text: Optional[str], max_length: int, obj: str, empty: bool) -> Optional[str]:
    ...

@overload
def string_validation(text: Optional[str], max_length: int, obj: str) -> str:
    ...

def string_validation(text: Optional[str], max_length: int, obj: str, empty: bool | None=False) :
    try:
        if empty is False and (text is None or len(text) == 0):
            raise InputError(obj=obj, message=' cannot be empty!')
        elif empty is True and (text is None or len(text) == 0):
            return None
        elif text is not None and len(text) > max_length:
            raise InputError(obj=obj, message=' cannot be more than ' + str(max_length) + ' characters!')
        else:
            return text
    except TypeError:
        raise InputError(obj=obj, message=' is either missing or not a string')  # noqa: B904


@overload
def choice_validation(text: Optional[str], choices: Union[Tuple, list], obj: str, null: bool) -> Optional[str]:
    ...

@overload
def choice_validation(text: Optional[str], choices: Union[Tuple, list], obj: str) -> str:
    ...

def choice_validation(text: Optional[str], choices: Union[Tuple, list], obj: str, null: bool | None = False):
    try:
        if null is True and (text is None or len(text) == 0):
            return None
        elif null is False and (text is None or len(text) == 0):
            raise InputError(obj=obj, message=' has to be selected!')
        elif ((type(choices) is list or type(choices) is tuple) and text in choices) or text in dict(choices):
            return text
        else:
            raise InputError(obj=obj, message=' cannot have this value!')
    except ValueError:
        raise InputError(obj=obj, message=' cannot have this value!') from None




@overload
def integer_validation(number: Optional[str], low: int, high: int, obj: str, empty: bool) -> Optional[int]:
    ...

@overload
def integer_validation(number: Optional[str], low: int, high: int, obj: str) -> int:
    ...

def integer_validation(number: Optional[str], low: int, high: int, obj: str, empty: bool | None = False):
    if empty and (number is None or (type(number) == str and len(number) == 0)):
        return None
    elif empty is False and (number is None):
        raise InputError(obj=obj, message=' has to be an integer!')
    else:
        try:
            n = int(number) # type: ignore
            if low <= n <= high:
                return n
            else:
                if n < low:
                    message = ' has to be equal or bigger than ' + str(low)
                else:
                    message = ' has to be equal or smaller than ' + str(high)
                raise InputError(obj=obj, message=message)
        except ValueError:
            raise InputError(obj=obj, message=' has to be an integer!')  # noqa: B904


def boolean_validation(boo: Optional[str], obj: str) -> bool:
    if boo == 'true':
        return True
    elif boo == 'false':
        return False
    else:
        raise InputError(obj=obj, message=' has to be either true or false!')



@overload
def date_validation(target_date: str | None, obj: str, empty: bool, min_date: str | date | None=None) -> Optional[date]:
    ...


@overload
def date_validation(target_date: str | None, obj: str, empty: None=None, min_date: str | date | None=None) -> date:
    ...
    

def date_validation(target_date: str | None, obj: str, empty: bool | None = False, min_date : str | date | None =None):
    if empty and (target_date is None or (type(target_date) == str and len(target_date) == 0)):
        return None
    elif empty is False and (target_date is None or len(target_date) == 0):
        raise InputError(obj=obj, message=' cannot be empty!')
    else:
        try:
            formatted_date = datetime.strptime(target_date, "%Y-%m-%d").date() # type: ignore
            if min_date is None:
                return formatted_date
            else:
                formatted_min_date = datetime.strptime(min_date, "%Y-%m-%d").date() if type(min_date) == str else min_date
                if formatted_date >= formatted_min_date: # type: ignore
                    return formatted_date
                else:
                    raise InputError(obj=obj, message=' cannot be earlier than ' + str(min_date))
        except ValueError:
            raise InputError(obj=obj, message=' is not a valid date!')  # noqa: B904




def decimal_validation(number, low, high, decimal_count, obj, round_decimal=True, empty=False, more_message=None):
    try:
        dec = decimal.Decimal(number)
        dec_places = dec.as_tuple().exponent
        if low <= dec <= high:
            if dec_places <= decimal_count:
                return dec
            else:
                if round_decimal:
                    return dec.quantize(decimal.Decimal(10) ** (decimal_count * -1))
                else:
                    raise InputError(obj=obj, message=' cannot have more than ' + decimal_count + ' places!')
        else:
            if dec < low:
                message = ' cannot be smaller than ' + str(low)
            else:
                if more_message is None:
                    message = ' cannot be larger than ' + str(high)
                else:
                    message = more_message
            raise InputError(obj=obj, message=message)
    except decimal.InvalidOperation:
        if empty and len(number) == 0:
            return decimal.Decimal(0)
        else:
            raise InputError(obj=obj, message=' is not a valid number!')  # noqa: B904
    except TypeError:
        raise InputError(obj=obj, message=' is not a valid number!')  # noqa: B904


def json_validation(j, obj, empty=False) -> dict:
    try:
        if len(j) == 0 and empty:
            return j
        elif len(j) == 0 and not empty:
            raise InputError(obj=obj, message=' cannot be empty!')

        return json.loads(j)

    except json.decoder.JSONDecodeError:
        raise InputError(obj=obj, message=' is not valid!')  # noqa: B904


def list_validation(raw_list: Union[list, str], obj: str, nature: Callable, empty: bool = False) -> list:
    converted_list = list(raw_list)
    if empty and len(converted_list) == 0:
        return []
    elif empty is False and len(converted_list) == 0:
        raise InputError(obj=obj, message=' cannot be empty!')
    else:
        temp_list = []
        for c in converted_list:
            if nature.__name__ != 'all' and nature.__name__ != 'any':
                temp_list.append(nature(c))
            else:
                temp_list.append(c)
        return temp_list