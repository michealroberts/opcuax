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


class AttributeId(IntEnum):
    # Unique identifier used to locate the node in the address space:
    NodeId = 1
    # Classification of the node such as object, variable, or method:
    NodeClass = 2
    # Name used during browsing that is qualified by namespace to avoid ambiguity:
    BrowseName = 3
    # Human-readable name intended to be shown in user interfaces:
    DisplayName = 4
    # Text explaining the purpose or semantics of the node:
    Description = 5
    # Mask indicating which attributes clients are permitted to modify:
    WriteMask = 6
    # Mask indicating which attributes the current user context is permitted to modify:
    UserWriteMask = 7
    # Flag that indicates the node is abstract and cannot be instantiated directly:
    IsAbstract = 8
    # Flag that specifies whether a reference is symmetric in nature:
    Symmetric = 9
    # Localized name used for the inverse side of symmetric references:
    InverseName = 10
    # Flag ensuring that the reference hierarchy contains no cycles:
    ContainsNoLoops = 11
    # Bitmask specifying whether the node is allowed to emit events:
    EventNotifier = 12
    # Current data value held by the node when applicable:
    Value = 13
    # Identifier of the data type associated with the node's value:
    DataType = 14
    # Indicator of whether the value is scalar or has array dimensions:
    ValueRank = 15
    # Dimensions of the array when the value is an array:
    ArrayDimensions = 16
    # Default rights for reading or writing the node's value:
    AccessLevel = 17
    # Effective rights for the current user to read or write the value:
    UserAccessLevel = 18
    # Suggested minimum interval between sampling operations for the value:
    MinimumSamplingInterval = 19
    # Indicator of whether historical data collection is enabled for the node:
    Historizing = 20


# **************************************************************************************
