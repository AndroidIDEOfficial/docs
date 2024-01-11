.. _dev-get_started:

Getting started with building AndroidIDE
----------------------------------------

.. _dev-get_started_before_start:

Before you start
^^^^^^^^^^^^^^^^

The following are the requirements to build the project :


* Android Studio Flamingo or newer.
* JDK 17 (if building in terminal).
* ``git`` installed and available in ``PATH``.

Building in a Linux environment is recommended (tested on Pop!_OS 22.04 LTS).

.. _dev-get_started-windows&mac:

For Windows & Mac OS
^^^^^^^^^^^^^^^^^^^^

The build configurations have not been tested vastly on Windows and Mac. You might face errors while setting up the project. If you do, please let us know and we'll try to fix them as soon as possible.

.. _dev-get_started-get_source:

Get the source
^^^^^^^^^^^^^^

Make sure you have ``git`` installed and available on your ``PATH``. The ``git`` command is also used by the composite build (\ ``:build-logic:ide``\ ) to get information about the branch and commit information to generate the version name for AndroidIDE.

Once you have installed ``git``\ , clone the repository with :

.. code-block:: bash

   git clone https://github.com/AndroidIDEOfficial/AndroidIDE.git

Once the repository has been cloned, open the project in Android Studio and start exploring! No extra configuration is required.

.. _dev-get_started-branches:

Branches
^^^^^^^^

The default (mainline) branch is ``dev``. If you want to propose a change, the pull request must be made to the ``dev`` branch.

Whenever we want to release a new version, the changes are merged into the ``main``. When the workflow runs on the ``main`` branch, it creates and publishes a new AndroidIDE release.

.. _dev-get_started-signing_key:

Setting up the signing key
^^^^^^^^^^^^^^^^^^^^^^^^^^

For security reasons, the signing key for AndroidIDE is not shared publicly.
If you want to configure a custom signing key, copy the signing key to the root project directory and rename the file to ``signing-key.jks``. Then set up the following environment variables or project properties in ``local.properties`` :

.. list-table::
   :header-rows: 1

   * - Environment/property
     - Description
   * - ``IDE_SIGNING_ALIAS``
     - The keystore key alias.
   * - ``IDE_SIGNING_KEY_PASS``
     - The keystore key password.
   * - ``IDE_SIGNING_STORE_PASS``
     - The keystore password.


.. _dev-get_started-building_with_AndroidIDE:

Building with AndroidIDE
^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to build AndroidIDE in AndroidIDE itself. However, this is not recommended due to the size of the project.

If you do want to build the project in AndroidIDE, just open the project in AndroidIDE and it should "just work". Please note that the code completions and other language services may not work as expected.

You can build the project with the terminal as well. When doing so, the ``android.aapt2FromMavenOverride`` project property MUST be set in order to use AndroidIDE's ``aapt2`` binary (the build will fail if it isn't set). This can be done like the following :

.. code-block:: bash

   bash ./gradlew -Pandroid.aapt2FromMavenOverride=$HOME/.androidide/aapt2 <tasks>

To avoid writing this again and again, you can create a function in ``.bashrc`` file and export the function :

.. code-block:: bash

   # In $HOME/.bashrc file

   function gradlew {
       file="./gradlew"
       if test -f "$file" ; then
           bash $file -Pandroid.aapt2FromMavenOverride=$HOME/.androidide/aapt2 $@
       else
           echo "Invoke this command from a project's root directory."
       fi
   }

   export -f gradlew

Then, from the project's root directory, you can execute the script like this :

.. code-block:: bash

   gradlew <tasks>
