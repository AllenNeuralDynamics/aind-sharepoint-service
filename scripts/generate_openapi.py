"""Module to create openapi.json file"""

import json
import os
from pathlib import Path
from typing import Any, Dict
import importlib
import inspect
from enum import Enum

import toml
from fastapi.openapi.utils import get_openapi


def load_env_from_toml(toml_path):
    """Load pytest env from pyproject.toml file"""
    config = toml.load(toml_path)
    env_vars = dict(
        [
            (row.split("=")[0], row.split("=")[1])
            for row in config.get("tool", dict())
            .get("pytest")
            .get("ini_options")
            .get("env")
        ]
    )
    for key, value in env_vars.items():
        os.environ[key] = str(value)


def get_enum_class_by_name(enum_name: str):
    """Dynamically find and import enum class by name"""
    model_modules = [
        "aind_sharepoint_service_server.models.las_2020",
        "aind_sharepoint_service_server.models.nsb_2019",
        "aind_sharepoint_service_server.models.nsb_2023",
    ]
    
    for module_name in model_modules:
        try:
            module = importlib.import_module(module_name)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (inspect.isclass(attr) and 
                    issubclass(attr, Enum) and 
                    attr.__name__ == enum_name):
                    return attr
        except ImportError:
            continue
    
    return None


def fix_enum_schemas(openapi_schema: Dict[str, Any]) -> Dict[str, Any]:
    """Fix all enum schemas by adding x-enum-varnames using actual enum member names"""
    
    if "components" not in openapi_schema or "schemas" not in openapi_schema["components"]:
        return openapi_schema
    
    for schema_name, schema in openapi_schema["components"]["schemas"].items():
        if schema.get("type") == "string" and "enum" in schema:
            enum_class = get_enum_class_by_name(schema_name)
            
            if enum_class:
                enum_values = schema["enum"]
                value_to_name = {member.value: member.name for member in enum_class}
                x_enum_varnames = []
                for value in enum_values:
                    member_name = value_to_name.get(value)
                    if member_name:
                        x_enum_varnames.append(member_name)
                    else:
                        safe_name = (value.replace(" ", "_")
                                   .replace("-", "_")
                                   .replace("–", "_")
                                   .replace("(", "")
                                   .replace(")", "")
                                   .replace(".", "")
                                   .upper())
                        x_enum_varnames.append(safe_name)
                
                schema["x-enum-varnames"] = x_enum_varnames
    
    return openapi_schema


if __name__ == "__main__":
    env_toml_path = os.getenv(
        "TOML_PATH",
        Path("aind-sharepoint-service-server") / "pyproject.toml",
    )
    load_env_from_toml(env_toml_path)
    from aind_sharepoint_service_server.main import app

    specs = get_openapi(
        title=app.title if app.title else None,
        version=app.version if app.version else None,
        openapi_version=app.openapi_version if app.openapi_version else None,
        description=app.description if app.description else None,
        routes=app.routes if app.routes else None,
    )
    
    # Fix all enum schemas
    specs = fix_enum_schemas(specs)
    
    with open("openapi.json", "w", encoding="utf-8") as f:
        json.dump(specs, f, ensure_ascii=False, indent=2)
