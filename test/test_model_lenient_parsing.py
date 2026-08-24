from __future__ import absolute_import

import inspect
import unittest
from datetime import datetime

import authress.models as models_pkg
from authress.models.client_access_key import ClientAccessKey

try:
    from pydantic.v1 import BaseModel
    from pydantic.v1.fields import SHAPE_LIST, SHAPE_DICT
except ImportError:
    from pydantic import BaseModel
    from pydantic.fields import SHAPE_LIST, SHAPE_DICT


def _scalar_value(tp):
    if isinstance(tp, type) and issubclass(tp, BaseModel):
        return {}
    if isinstance(tp, type) and issubclass(tp, bool):
        return True
    if isinstance(tp, type) and issubclass(tp, int):
        return 1
    if isinstance(tp, type) and issubclass(tp, float):
        return 1.0
    if isinstance(tp, type) and issubclass(tp, datetime):
        return "2024-01-01T00:00:00Z"
    return "example"


def _baseline_value(field):
    if field.shape == SHAPE_LIST:
        return [_scalar_value(field.type_)]
    if field.shape == SHAPE_DICT:
        return {"key": _scalar_value(field.type_)}
    return _scalar_value(field.type_)


def _baseline_payload(cls):
    return {field.alias: _baseline_value(field) for field in cls.__fields__.values()}


def _mutations_for(value):
    mutations = [None]
    if isinstance(value, dict):
        mutations += [[1, 2, 3], "not-an-object", 42]
    elif isinstance(value, list):
        mutations += [{"a": 1}, "not-a-list", 42]
    elif isinstance(value, bool):
        mutations += ["not-a-bool", 42]
    elif isinstance(value, (int, float)):
        mutations += ["not-a-number", [1, 2], {"a": 1}]
    else:
        mutations += [42, [1, 2], {"a": 1}, "!!!invalid-format$$$"]
    return mutations


def _model_classes():
    classes = {}
    for name in dir(models_pkg):
        obj = getattr(models_pkg, name)
        if inspect.isclass(obj) and issubclass(obj, BaseModel) and hasattr(obj, "from_dict"):
            classes[obj.__name__] = obj
    return list(classes.values())


class ModelLenientParsingTest(unittest.TestCase):
    def _assert_all_fields_readable(self, cls, obj):
        self.assertIsNotNone(obj)
        for name in cls.__fields__:
            getattr(obj, name)

    def test_missing_null_extra_and_type_confused_fields_never_raise(self):
        for cls in _model_classes():
            baseline = _baseline_payload(cls)

            with self.subTest(model=cls.__name__, case="extra_property"):
                payload = dict(baseline)
                payload["unexpectedZzzField"] = "unexpected-value"
                self._assert_all_fields_readable(cls, cls.from_dict(payload))

            for field in cls.__fields__.values():
                with self.subTest(model=cls.__name__, field=field.alias, case="missing"):
                    payload = dict(baseline)
                    payload.pop(field.alias, None)
                    self._assert_all_fields_readable(cls, cls.from_dict(payload))

                for mutated_value in _mutations_for(baseline[field.alias]):
                    with self.subTest(model=cls.__name__, field=field.alias, mutated_value=mutated_value):
                        payload = dict(baseline)
                        payload[field.alias] = mutated_value
                        self._assert_all_fields_readable(cls, cls.from_dict(payload))

    def test_top_level_shape_mismatch_never_raises(self):
        for cls in _model_classes():
            for bad_top_level in [[1, 2, 3], "not-a-dict", 42]:
                with self.subTest(model=cls.__name__, bad_top_level=bad_top_level):
                    self._assert_all_fields_readable(cls, cls.from_dict(bad_top_level))

            with self.subTest(model=cls.__name__, bad_top_level=None):
                self.assertIsNone(cls.from_dict(None))


class ClientAccessKeyRegressionTest(unittest.TestCase):
    def test_base64url_public_key_from_original_bug_report_does_not_raise(self):
        obj = ClientAccessKey.from_dict({
            "keyId": "abc123",
            "publicKey": "JxtSC5tZZJuaW7Aeu5Kh_3tgCpPZRkHaaFyTj5sQ3KU",
        })
        self.assertEqual(obj.public_key, "JxtSC5tZZJuaW7Aeu5Kh_3tgCpPZRkHaaFyTj5sQ3KU")

    def test_standard_base64_public_key_is_accepted_and_coerced_fields_stay_typed(self):
        obj = ClientAccessKey.from_dict({
            "keyId": "abc123",
            "publicKey": "abc+DEF/012=",
            "generationDate": "2024-01-01T00:00:00Z",
        })
        self.assertEqual(obj.public_key, "abc+DEF/012=")
        self.assertIsInstance(obj.generation_date, datetime)


if __name__ == "__main__":
    unittest.main()
