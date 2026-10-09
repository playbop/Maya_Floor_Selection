import maya.cmds as cmds


def floor_selection():
    # Get current active selection
    selection = cmds.ls(selection=True)

    if not selection:
        cmds.warning("Please select at least one object or group.")
        return

    for obj in selection:
        # Query the exact minimum Y bounding box coordinate in world space
        # [xmin, ymin, zmin, xmax, ymax, zmax]
        bbox = cmds.xform(obj, query=True, boundingBox=True, worldSpace=True)
        min_y = bbox[1]

        # Calculate offset needed to place the lowest point on Y = 0
        y_offset = -min_y

        # Move object/group relative to its current position along world Y
        cmds.xform(obj, translation=[0, y_offset, 0], relative=True, worldSpace=True)

    cmds.inViewMessage(
        amg=f"<col=00FF00>Floored {len(selection)} item(s) to Y = 0</col>",
        pos="topCenter",
        fade=True,
    )


# Execute the function
floor_selection()