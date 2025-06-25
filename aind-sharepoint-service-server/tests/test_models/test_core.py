"""Tests methods in core module"""

import unittest
from enum import Enum
from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
    WrapValidator,
)

from aind_sharepoint_service_server.models.core import (
    HealthCheck,
    optional_enum,
)


class TestHealthCheck(unittest.TestCase):
    """Tests for HealthCheck class"""

    def test_constructor(self):
        """Basic test for class constructor"""

        health_check = HealthCheck()
        self.assertEqual("OK", health_check.status)


class TestCoreMethods(unittest.TestCase):
    """Tests methods in core module"""

    def test_optional_enum_meta_case(self):
        """Tests optional enum wrapper returns None as expected."""

        class MyEnum(str, Enum):
            """Enum class for testing purposes"""

            ABC = "abc"
            DEF = "def"

        class MyModel(BaseModel):
            """Model for testing purposes"""

            name: str = Field(...)
            id: Annotated[MyEnum, WrapValidator(optional_enum)] = Field(
                default=None
            )

        model1 = MyModel.model_validate({"name": "name1"})
        model2 = MyModel.model_validate({"name": "name2", "id": "abc"})
        self.assertIsNone(model1.id)
        self.assertEqual(MyEnum.ABC, model2.id)


if __name__ == "__main__":
    unittest.main()
