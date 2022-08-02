import os
import streamlit.components.v1 as components

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "build")
_component_func = components.declare_component(
    "select", path=build_dir)


def select(options, label=None, key=None):
    component_value = _component_func(options=options, label=label, key=key)
    return component_value
