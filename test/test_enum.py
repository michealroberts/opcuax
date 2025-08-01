# **************************************************************************************

# @package        upcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from opcuax.enums import NodeClass, ReferenceTypeId

# **************************************************************************************


class TestNodeClassEnum(unittest.TestCase):
    def test_node_class_enum(self):
        # Test that the NodeClass enum has the expected values
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
        # Test that the ReferenceTypeId enum has the expected values
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
