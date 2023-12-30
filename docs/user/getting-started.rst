.. _user-getting_started:

Getting Started
===============

This guide helps you get started with AndroidIDE and build your first Android application.
Ensure you have installed the build tools by following :doc:`the installation guide </user/installation>` before proceeding.

.. _user-getting_started-creating_project:

Creating a New Project
----------------------


#. Open AndroidIDE.
#. Click on the ``Create project`` button.
#. Choose a project template to set up basic configurations.
#. Enter application details, including name, package name, directory, and SDK versions.
#. Click 'Create project' to initiate project creation.

.. _user-getting_started-working_with_project:

Working with an Existing Project
--------------------------------


#. Click ``Open existing project`` in the main activity.
#. Use the SAF file picker to choose the project directory.
#. Ensure your project uses Android Gradle Plugin ``v7.2.0`` or newer for compatibility.
#. Update build scripts if opening projects from older IDEs.

.. note::
    When building projects with AndroidIDE, your project must use Android Gradle Plugin ``v7.2.0`` or newer.
    If you project uses an older version of the Android Gradle Plugin, you may need to update your project
    in order to build it in AndroidIDE. However, building the project in the terminal does not require any
    changes.

.. _user-getting_started-syncing_and_building:

Syncing and Building
--------------------


* After project creation or opening, the IDE opens the :doc:`editor </user/editor/index>`.
* The IDE starts syncing the project, which may take time based on your internet connection.
* To check the build progress, :ref:`swipe up the build status bar <user-editor-bottom_sheet>` at the bottom of your screen.
* Once sync is successful, you can start working on your project or press :ref:`Run <user-editor-options_menu>`
  in the :ref:`toolbar <user-editor-options_menu>` to build and install your application.

Refer to the documentation for detailed information on each step and advanced usage tips.
