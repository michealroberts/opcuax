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


class ReferenceTypeId(IntEnum):
    # General references supertype:
    References = 31
    # Non-hierarchical references supertype:
    NonHierarchicalReferences = 32
    # Hierarchical references supertype:
    HierarchicalReferences = 33
    # Indicates that the target is a child in a generic hierarchy:
    HasChild = 34
    # Indicates organizational grouping of the target under the source:
    Organizes = 35
    # Indicates that the target is an event source:
    HasEventSource = 36
    # Indicates modelling rule association:
    HasModellingRule = 37
    # Indicates encoding relationship (e.g., data type to its encoding):
    HasEncoding = 38
    # Indicates a type definition relationship:
    HasTypeDefinition = 40
    # Indicates subtype relationship of types:
    HasSubtype = 45
    # Indicates that the target is a property of the source:
    HasProperty = 46
    # Indicates that the target is a component of the source:
    HasComponent = 47
    # Indicates that the target is a notifier for events:
    HasNotifier = 48
    # Indicates an ordered component relationship:
    HasOrderedComponent = 49
    # Indicates a cause-effect relationship where source causes target:
    HasCause = 57
    # Indicates a cause-effect relationship where source is the effect:
    HasEffect = 58


# **************************************************************************************
