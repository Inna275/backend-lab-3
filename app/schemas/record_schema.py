from marshmallow import Schema, fields

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    currency_id = fields.Int(required=False)
    amount = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)
