.. _user-installation:

Installation
============

This guide walks you through the installation process for AndroidIDE,
including setting up the terminal and installing Android build tools.

.. _user-installation-minreq:

**Minimum Requirements:**

Before proceeding, ensure that your Android device meets these minimum requirements:


* 
  **Supported CPU Architectures:**


  * ``arm64-v8a``
  * ``armeabi-v7a``
  * ``x86_64`` (requires AndroidIDE v2.7.0-beta or newer)

* 
  **RAM:**


  * Minimum of **1.5GB - 2GB free RAM** is recommended.

* 
  **Storage Space:**


  * Minimum of 4GB free storage space.

* 
  **Internet Connection:**


  * WiFi connection is recommended for the initial setup.

**Download AndroidIDE:**


* `Download from Github Releases <https://github.com/AndroidIDEOfficial/AndroidIDE/releases>`_
* `Debug Version (for testers) <https://github.com/AndroidIDEOfficial/AndroidIDE/actions?query=branch%3Adev+event%3Apush>`_

  * Make sure to be logged in to GitHub in your browser when downloading artifacts.
* `F-Droid <https://f-droid.org/packages/com.itsaky.androidide/>`_

.. warning::
  F-Droid and GitHub builds are incompatible with each other! You can't use them interchangeably.
.. note::
  Debug version is for testing purposes. It can be **unstable**.

.. _user-installation-process:

**Setup the Terminal:**


#. Open AndroidIDE terminal.
#. It will install bootstrap packages if required.
#. Run ``pkg upgrade`` to update packages to the latest version.

**Build Tools Installation:**

Install JDK, SDK, and commandline tools for SDK.


#. Open the terminal and run ``idesetup -c``.
#. Confirm the configuration and start the installation process by typing ``y``.
#. After successful installation, ``Downloads completed. You are ready to go!`` will be printed.

**Cheatsheet:**


* One command to setup the terminal and install build tools:

  .. code-block:: bash

     cd && pkg upg && idesetup -c
