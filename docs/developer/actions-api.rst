.. _dev-actions_api:

Actions API
===========

The Actions API (\ ``:actions`` module) is used to show various actions in the IDE.
It allows tools like LSP (and others) to add actions at various locations in the UI.
For example, the Java LSP adds code actions like 'Go to definition', 'Find references', etc.
in the code editor's text action window.

.. _dev-actions_api-action:

Action
------

An action is defined by implementing the the ``ActionItem`` interface and registering it to the ``ActionsRegistry``.

The ``ActionItem`` interface defines various properties and functions that can be overridden in order to achive a
specific behavior. Every ``ActionItem`` must have a unique string ID and a valid location. The locations for the
actions are defined in the ``ActionItem.Location`` enumeration.

For consistency, the IDs for the action item should have the following format :

.. code-block:: text

   ide.<subcomponent>[.<sub-subcomponents-or-category>...].<actionId>

For example, ``ide.editor.build.quickRun``.

.. _dev-actions_api-action_data:

Action data
^^^^^^^^^^^

``ActionData`` contains various parameters like ``Context``\ , ``CodeEditor``\ , etc that can be used by the action
implementation. The same ActionData is provided to all the functions of the ``ActionItem`` i.e. the ``prepare``\ ,
``execAction`` and ``postExec`` are called with the same ``ActionData`` instance.

The data provided in the ``ActionData`` differs for each ``ActionItem.Location``. However, a ``Context`` object is always
provided with an ``ActionData`` instance.

.. _dev-actions_api-prepare:

Prepare
^^^^^^^

The ``ActionItem.prepare(ActionData)`` method is called to prepare the action item. The action item can validate various
conditions and update the properties of the action. For example, an action can check if a build is in progress and decide
whether the action should be visible to the user or not. This method may or may not be called on the UI thread.

.. _dev-actions_api-execute:

Execute
^^^^^^^

The ``ActionItem.execAction(ActionData)`` method is called to execute the action. Based on the ``ActionItem.requiresUiThread`` property,
the action is executed either on the UI thread or a background thread. The action should make sure NOT to perform long running operations
when running on the UI thread.

This method could return a value which can later be accessed in the ``postExec`` function. If the action does not need to calculate and
process a result, this should simply return ``Unit`` or ``false``.

.. _dev-actions_api-process:

Process
^^^^^^^

The ``ActionItem.postExec(ActionData)`` method is called to let the action process the result from ``ActionItem.execAction()``. This method
is ALWAYS called on the UI thread and hence, the action should not perform any long running operations here.

Usually, this method is used to show the result of the action to the user.

.. _dev-actions_api-actions_menu:

Action menu
-----------

An action menu is a group of actions. Action menus are just queried and not executed. Hence, the ``execAction`` and
``postExec`` methods are never called for an action menu. Apart from this, they work very much similar to action items.

.. _dev-actions_api-querying_actions:

Querying actions
----------------

The ``ActionsRegistry`` provides various APIs to query the registered action.
See `ActionsRegistry <https://github.com/AndroidIDEOfficial/AndroidIDE/blob/dev/actions/src/main/java/com/itsaky/androidide/actions/ActionsRegistry.kt>`_
for more details.
