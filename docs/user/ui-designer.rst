.. _user-ui_designer:

UI Designer
===========

The UI Designer in AndroidIDE facilitates the visual design of XML layouts through intuitive drag-and-drop functionality. This document provides an overview of the UI Designer workspace and its key elements.

.. _user-ui_designer-workspace:

The Workspace
-------------

Your XML code is parsed and inflated by AndroidIDE's `LayoutInflater API`, then displayed in the workspace. Drag and drop inflated views and widgets to rearrange, modify attributes, add new views, or delete existing ones.

.. _user-ui_designer-workspace-add_new_views:

**Adding New Views:**

To add new views:

1. Open the left drawer displaying supported views and layouts.
2. Long-click on list items to start the drag.
3. Drop items into the workspace to add to the layout.

.. _user-ui_designer-workspace-move_views:

Moving Views
~~~~~~~~~~~~

To move a view in the workspace, long-press the view to initiate the drag and drop it at the desired position.

.. _user-ui_designer-workspace-edit_view_attrs:

Editing View Attributes
~~~~~~~~~~~~~~~~~~~~~~~

1. Click on an inflated view to open the view info sheet.
2. The sheet contains:
   - `Add`: Shows attributes that can be added to the selected view (excluding applied attributes).
   - `Delete`: Deletes the selected view.
   - List of applied attributes.
3. Click on any attribute to open the value editor and modify its value.
4. Click on 'Delete' to remove an attribute (excluding necessary attributes).

.. _user-ui_designer-workspace-layout_hierarchy:

Layout Hierarchy
----------------

The layout hierarchy view displays the structure of views in a tree-like format. Open it by:
- Opening the right drawer.
- Clicking on the 'hierarchy' view in the options menu.

Clicking on nodes in the hierarchy tree is equivalent to clicking on views in the workspace, opening the view info sheet.