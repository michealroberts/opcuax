# **************************************************************************************

# @package        upcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from opcuax.enums import AttributeId, NodeClass, ReferenceTypeId

# **************************************************************************************


class TestNodeClassEnum(unittest.TestCase):
    def test_node_class_enum(self):
        self.assertEqual(NodeClass.Unspecified, 0)
        self.assertEqual(NodeClass.Object, 1)
        self.assertEqual(NodeClass.Variable, 2)
        self.assertEqual(NodeClass.Method, 4)
        self.assertEqual(NodeClass.ObjectType, 8)
        self.assertEqual(NodeClass.VariableType, 16)
        self.assertEqual(NodeClass.ReferenceType, 32)
        self.assertEqual(NodeClass.DataType, 64)
        self.assertEqual(NodeClass.View, 128)


# **************************************************************************************


class TestReferenceTypeIdEnum(unittest.TestCase):
    def test_reference_type_id_enum(self):
        self.assertEqual(ReferenceTypeId.References, 31)
        self.assertEqual(ReferenceTypeId.NonHierarchicalReferences, 32)
        self.assertEqual(ReferenceTypeId.HierarchicalReferences, 33)
        self.assertEqual(ReferenceTypeId.HasChild, 34)
        self.assertEqual(ReferenceTypeId.Organizes, 35)
        self.assertEqual(ReferenceTypeId.HasEventSource, 36)
        self.assertEqual(ReferenceTypeId.HasModellingRule, 37)
        self.assertEqual(ReferenceTypeId.HasEncoding, 38)
        self.assertEqual(ReferenceTypeId.HasTypeDefinition, 40)
        self.assertEqual(ReferenceTypeId.HasSubtype, 45)
        self.assertEqual(ReferenceTypeId.HasProperty, 46)
        self.assertEqual(ReferenceTypeId.HasComponent, 47)
        self.assertEqual(ReferenceTypeId.HasNotifier, 48)
        self.assertEqual(ReferenceTypeId.HasOrderedComponent, 49)
        self.assertEqual(ReferenceTypeId.HasCause, 57)
        self.assertEqual(ReferenceTypeId.HasEffect, 58)


# **************************************************************************************


class TestAttributeIdEnum(unittest.TestCase):
    def test_attribute_id_enum(self):
        self.assertEqual(AttributeId.NodeId, 1)
        self.assertEqual(AttributeId.NodeClass, 2)
        self.assertEqual(AttributeId.BrowseName, 3)
        self.assertEqual(AttributeId.DisplayName, 4)
        self.assertEqual(AttributeId.Description, 5)
        self.assertEqual(AttributeId.WriteMask, 6)
        self.assertEqual(AttributeId.UserWriteMask, 7)
        self.assertEqual(AttributeId.IsAbstract, 8)
        self.assertEqual(AttributeId.Symmetric, 9)
        self.assertEqual(AttributeId.InverseName, 10)
        self.assertEqual(AttributeId.ContainsNoLoops, 11)
        self.assertEqual(AttributeId.EventNotifier, 12)
        self.assertEqual(AttributeId.Value, 13)
        self.assertEqual(AttributeId.DataType, 14)
        self.assertEqual(AttributeId.ValueRank, 15)
        self.assertEqual(AttributeId.ArrayDimensions, 16)
        self.assertEqual(AttributeId.AccessLevel, 17)
        self.assertEqual(AttributeId.UserAccessLevel, 18)
        self.assertEqual(AttributeId.MinimumSamplingInterval, 19)
        self.assertEqual(AttributeId.Historizing, 20)


# **************************************************************************************
