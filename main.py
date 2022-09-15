import boto3
from boto3.dynamodb.conditions import Key


def get_item(key: str, table: str = "plotsV2"):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(table)
    response = table.get_item(
        Key={
            "key": key,
        }
    )
    return response["Item"]["value"]


x = get_item("jira")
