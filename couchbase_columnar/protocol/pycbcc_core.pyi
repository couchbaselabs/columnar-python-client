from typing import (Any,
                    Dict,
                    Optional,
                    Union)

from couchbase_columnar.common.core.query import QueryMetadataCore
from couchbase_columnar.protocol.core import PyCapsuleType

CXXCBC_METADATA: str

class exception:
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def err(self, *args: object, **kwargs: object) -> int: ...
    def err_category(self, *args: object, **kwargs: object) -> str: ...
    def error_context(self, *args: object, **kwargs: object) -> Optional[Dict[str, Any]]: ...
    def error_info(self, *args: object, **kwargs: object) -> Optional[Dict[str, Any]]: ...
    def strerror(self, *args: object, **kwargs: object) -> Optional[str]: ...

class pycbcc_logger:
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def configure_logging_sink(self, *args: object, **kwargs: object) -> None: ...
    def create_console_logger(self, *args: object, **kwargs: object) -> None: ...
    def enable_protocol_logger(self, *args: object, **kwargs: object) -> None: ...

class result:
    raw_result: Dict[str, Any]
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def err(self, *args: object, **kwargs: object) -> Optional[int]: ...
    def err_category(self, *args: object, **kwargs: object) -> Optional[str]: ...
    def get(self, *args: object, **kwargs: object) -> Any: ...
    def strerror(self, *args: object, **kwargs: object) -> Optional[str]: ...

class columnar_query_iterator:
    @classmethod
    def __init__(cls, *args: object, **kwargs: object) -> None: ...
    def cancel(self) -> None: ...
    def wait_for_core_query_result(self) -> Union[bool, exception]: ...
    def metadata(self) -> Optional[QueryMetadataCore]: ...
    # def is_cancelled(self, *args: object, **kwargs: object) -> bool: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...

def columnar_query(*args: object, **kwargs: object) -> Optional[columnar_query_iterator]: ...
def close_connection(*args: object, **kwargs: object) -> bool: ...
def cluster_info(*args: object, **kwargs: object) -> result: ...
def create_connection(*args: object, **kwargs: object) -> PyCapsuleType: ...
def get_connection_info(*args: object, **kwargs: object) -> result: ...
