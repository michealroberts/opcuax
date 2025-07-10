# **************************************************************************************

# @package        upcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from typing import Generic, List, NotRequired, TypedDict, TypeVar

# **************************************************************************************

T = TypeVar("T", bound=object)

# **************************************************************************************


class NodeId(TypedDict):
    """
    Uniquely identifies a node in the OPC UA address space.
    """

    # The namespace index for scoping the identifier:
    namespace: int
    # The identifier (numeric, string, or GUID) as a string:
    identifier: str


# **************************************************************************************


class QualifiedName(TypedDict):
    """
    A name qualified by namespace for use in browses and references.
    """

    # The namespace index for scoping the name:
    namespace: int
    # The name itself:
    name: str


# **************************************************************************************


class StatusCode(TypedDict):
    """
    Status code returned by service calls or value operations as defined in the
    OPC UA specification.
    """

    # The numeric value of the status code:
    value: int


# **************************************************************************************


class Variant(TypedDict, Generic[T]):
    """
    Represents a typed value with optional array dimensions, parameterized by T.
    """

    # The underlying value, which can be a scalar or a list:
    value: T
    # The built-in DataType ID:
    datatype: int
    # Optional dimensions if the value is an array:
    array_dimensions: NotRequired[List[int]]


# **************************************************************************************


class DataValue(TypedDict, Generic[T]):
    """
    A DataValue represents a value with its quality and timestamps as defined in the
    OPC UA specification.
    """

    # The actual data value, which is a Variant[T]:
    value: Variant[T]
    # The status code indicating the quality of the value:
    status_code: StatusCode
    # Optional source timestamp (in seconds since epoch):
    source_timestamp: NotRequired[float]
    # Optional server timestamp (in seconds since epoch):
    server_timestamp: NotRequired[float]


# **************************************************************************************
