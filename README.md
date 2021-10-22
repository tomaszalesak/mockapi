# Mockapi

Dynamic API mock which returns what you set up.

You can fire it up with:

```
docker run -d -p <desiredport>:5000 tomaszalesak/mockapi
```

```json
{
    "companyId":
    {
        "endpoint":
        {
            "headers": {},
            "body": "body",
            "status": 200
        }
    },
    ...
}
```

```json
{
    "1": {
        "bob/api/v2/service/instance/list": {
            "headers": {
                "companyId": "1"
            },
            "body": {
                "Services": [
                    {
                        "Id": "1",
                        "CompanyId": "101001",
                        "Name": "DummyName",
                        "Definition": {
                            "Id": 1,
                            "Type": "PRODAAS",
                            "Name": "DummyName",
                            "Version": "1",
                            "Description": "BlahBlah"
                        },
                        "CurrentState": "Running",
                        "DesiredState": "Running",
                        "User": "Dummy",
                        "Details": {
                            "Endpoints": []
                        }
                    }
                ],
                "LatestDefinitionVersion": "21.10"
            },
            "status": 200
        }
    }
}
```