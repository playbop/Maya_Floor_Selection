# Maya Floor Selection Tool

A simple Maya Python script that snaps selected objects or groups to world Y = 0 based on the lowest point of their bounding box. Built for prepping assets for Unity.

## How to use

1. Open the Script Editor in Maya (`Windows > General Editors > Script Editor`).
2. Paste `floor_selection.py` into a Python tab.
3. Highlight the code and drag it to your Shelf using the Middle Mouse Button.
4. (Optional) Set the button icon to `icons/icon_floor.png`.

Select your mesh or parent group and click the shelf button to drop it to the floor grid.

## Compatibility
Tested on Maya 2022+ (Python 3) on macOS and Windows.
