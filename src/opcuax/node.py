# **************************************************************************************

# @package        opcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from typing import TypedDict

from .enums import ReferenceTypeId
from .types import NodeId

# **************************************************************************************


class Reference(TypedDict):
    # Type of the reference:
    type_id: ReferenceTypeId
    # Identifier of the target node:
    target_node_id: NodeId
    # Whether the reference direction is inverse:
    is_inverse: bool


# **************************************************************************************
