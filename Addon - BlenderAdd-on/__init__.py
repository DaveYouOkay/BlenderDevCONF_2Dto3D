import bpy

bl_info = {
    "name": "BlenderAdd-on",
    "author": "David, Michael, Sacha, Dorian",
    "description": "Addon Blender for DevCONF",
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "",
    "category": "Generic"
}

classes = (
)

register, unregister = bpy.utils.register_classes_factory(classes)
