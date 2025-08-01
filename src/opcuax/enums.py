# **************************************************************************************

# @package        upcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from enum import IntEnum

# **************************************************************************************


class NodeClass(IntEnum):
    Unspecified = 0
    Object = 1
    Variable = 2
    Method = 4
    ObjectType = 8
    VariableType = 16
    ReferenceType = 32
    DataType = 64
    View = 128


# **************************************************************************************
