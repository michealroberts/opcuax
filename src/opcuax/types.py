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
