def lenient_construct(cls, data: dict):
    values = {}
    present = set()
    for name, field in cls.__fields__.items():
        if name in data:
            present.add(name)
            raw = data[name]
        elif field.alias in data:
            present.add(name)
            raw = data[field.alias]
        else:
            values[name] = field.get_default()
            continue

        coerced, error = field.validate(raw, {}, loc=name)
        values[name] = raw if error else coerced

    obj = cls.construct(**values)
    object.__setattr__(obj, '__fields_set__', present)
    return obj


def lenient_nested(nested_cls, raw):
    if isinstance(raw, dict):
        return nested_cls.from_dict(raw)
    return raw


def lenient_nested_list(nested_cls, raw):
    if isinstance(raw, list):
        return [lenient_nested(nested_cls, item) for item in raw]
    return raw
