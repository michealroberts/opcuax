# **************************************************************************************

# @package        opcuax
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import unittest
from typing import cast

from opcuax import NodeId, Reference, ReferenceTypeId

# **************************************************************************************


class TestNode(unittest.TestCase):
    def test_reference_with_valid_fields(self) -> None:
        reference_with_component: Reference = {
            "target_node_id": NodeId(namespace=1, identifier="Sensor1"),
            "type_id": ReferenceTypeId.HasComponent,
            "is_inverse": False,
        }
        self.assertIsInstance(reference_with_component, dict)
        self.assertIn("target_node_id", reference_with_component)
        self.assertIn("type_id", reference_with_component)
        self.assertIn("is_inverse", reference_with_component)

        target_node_id = reference_with_component["target_node_id"]
        self.assertIsInstance(target_node_id, dict)
        self.assertIsInstance(target_node_id.get("namespace"), int)
        self.assertIsInstance(target_node_id.get("identifier"), str)

        self.assertIs(reference_with_component["type_id"], ReferenceTypeId.HasComponent)
        self.assertIsInstance(reference_with_component["is_inverse"], bool)
        self.assertFalse(reference_with_component["is_inverse"])

    def test_reference_missing_is_inverse_raises(self) -> None:
        reference_missing_is_inverse: dict = {
            "target_node_id": NodeId(namespace=2, identifier="VarA"),
            "type_id": ReferenceTypeId.Organizes,
        }
        with self.assertRaises(KeyError):
            _ = cast(Reference, reference_missing_is_inverse)["is_inverse"]

    def test_reference_with_wrong_namespace_type(self) -> None:
        reference_with_wrong_namespace: dict = {
            "target_node_id": {"namespace": "not-an-int", "identifier": "NodeX"},
            "type_id": ReferenceTypeId.HasProperty,
            "is_inverse": True,
        }
        target_node_id = reference_with_wrong_namespace["target_node_id"]
        self.assertIsInstance(target_node_id, dict)
        self.assertNotIsInstance(target_node_id.get("namespace"), int)
        self.assertIsInstance(target_node_id.get("identifier"), str)
        self.assertIs(
            reference_with_wrong_namespace["type_id"],
            ReferenceTypeId.HasProperty,
        )
        self.assertIsInstance(reference_with_wrong_namespace["is_inverse"], bool)

    def test_reference_with_wrong_identifier_type(self) -> None:
        reference_with_wrong_identifier: dict = {
            "target_node_id": {"namespace": 0, "identifier": 123},
            "type_id": ReferenceTypeId.HasProperty,
            "is_inverse": True,
        }
        target_node_id = reference_with_wrong_identifier["target_node_id"]
        self.assertIsInstance(target_node_id, dict)
        self.assertIsInstance(target_node_id.get("namespace"), int)
        self.assertNotIsInstance(target_node_id.get("identifier"), str)

    def test_reference_with_invalid_reference_type(self) -> None:
        reference_with_invalid_reference_type: dict = {
            "target_node_id": NodeId(namespace=0, identifier="NodeY"),
            "type_id": "not-an-enum",
            "is_inverse": False,
        }
        self.assertNotIsInstance(
            reference_with_invalid_reference_type["type_id"], ReferenceTypeId
        )

    def test_reference_with_invalid_is_inverse_type(self) -> None:
        reference_with_invalid_is_inverse: dict = {
            "target_node_id": NodeId(namespace=0, identifier="NodeY"),
            "type_id": ReferenceTypeId.HasNotifier,
            "is_inverse": "false",
        }
        self.assertNotIsInstance(reference_with_invalid_is_inverse["is_inverse"], bool)

    def test_reference_with_extra_fields(self) -> None:
        reference_with_extra: dict = {
            "target_node_id": NodeId(namespace=3, identifier="DeviceX"),
            "type_id": ReferenceTypeId.HasProperty,
            "is_inverse": True,
            "additional_info": "extra",
        }
        self.assertIn("additional_info", reference_with_extra)
        self.assertEqual(reference_with_extra["additional_info"], "extra")
        target_node_id = reference_with_extra["target_node_id"]
        self.assertIsInstance(target_node_id.get("namespace"), int)
        self.assertIsInstance(target_node_id.get("identifier"), str)
        self.assertIs(reference_with_extra["type_id"], ReferenceTypeId.HasProperty)
        self.assertTrue(reference_with_extra["is_inverse"])

    def test_casting_valid_dict_to_reference(self) -> None:
        raw_reference: dict = {
            "target_node_id": NodeId(namespace=4, identifier="Thing"),
            "type_id": ReferenceTypeId.Organizes,
            "is_inverse": False,
        }
        self.assertIsInstance(raw_reference["target_node_id"]["namespace"], int)
        self.assertIsInstance(raw_reference["target_node_id"]["identifier"], str)
        self.assertIsInstance(raw_reference["type_id"], ReferenceTypeId)
        self.assertIsInstance(raw_reference["is_inverse"], bool)

        typed_reference = cast(Reference, raw_reference)
        self.assertEqual(typed_reference["target_node_id"]["identifier"], "Thing")
        self.assertIs(typed_reference["type_id"], ReferenceTypeId.Organizes)
        self.assertFalse(typed_reference["is_inverse"])


# **************************************************************************************


if __name__ == "__main__":
    unittest.main()

# **************************************************************************************
