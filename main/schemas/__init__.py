import numbers

from marshmallow import (
    INCLUDE,
    Schema,
    ValidationError,
    fields,
    post_load,
    pre_load,
    validate,
    validates_schema,
)


class BaseSchema(Schema):
    @pre_load
    def transform_data_pre_load(self, data, **__):
        """
        Convert fields from `$...` to `_...`
        """
        new_data = {}

        for k, v in data.items():
            if k.startswith("$"):
                # Replace the first _ with $
                new_k = "_" + k[1:]
            elif k.startswith("_"):
                raise ValidationError(
                    message="Field name cannot start with an underscore (_).",
                    field_name=k,
                )
            else:
                new_k = k

            new_data[new_k] = v

        return new_data

    @post_load
    def transform_data_post_load(self, data, **__):
        """
        Convert fields from `_...` to `$...`
        """
        new_data = {}

        for k, v in data.items():
            if k.startswith("_"):
                # Replace the first _ with $
                new_k = "$" + k[1:]
            else:
                new_k = k

            new_data[new_k] = v

        return new_data
