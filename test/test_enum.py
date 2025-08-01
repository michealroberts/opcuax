# **************************************************************************************

# @package        upcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest

from opcuax.enums import NodeClass

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
