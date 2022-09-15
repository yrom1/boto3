import boto3

TABLE = "plotsV2"


def put_item(key: str, value) -> None:
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE)
    # NOTE if you want to support floats add this probably, untested
    # x = json.loads(json.dumps(cartBefore), parse_float=Decimal)
    response = table.put_item(
        Item={
            "key": key,
            "value": value,
        }
    )
    assert response["ResponseMetadata"]["HTTPStatusCode"] == 200


def get_item(key: str):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(TABLE)
    response = table.get_item(
        Key={
            "key": key,
        }
    )
    return response["Item"]["value"]


put_item("test5", 42)
x = get_item("test5")
print(x)
