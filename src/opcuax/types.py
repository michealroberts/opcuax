# **************************************************************************************

# @package        upcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from typing import TypedDict

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
