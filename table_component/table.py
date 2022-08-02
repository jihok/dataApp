import os
import streamlit.components.v1 as components

# _component_func = components.declare_component(
#     "table",
#     url="http://localhost:3001",
# )

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "build")
_component_func = components.declare_component(
    "table", path=build_dir)


def table(df, options=None, key=None):
    component_value = _component_func(df=df, options=options, key=key)
    return component_value
