# petaverse django restapi

### Swagger generate script (yaml -> json)
python -c 'import sys, yaml, json; json.dump(yaml.safe_load(sys.stdin), sys.stdout, indent=4)' < shared/openapi-schema.yml > breed_app/static/swagger.json

