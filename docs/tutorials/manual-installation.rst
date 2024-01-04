.. tutorials-manual_installation:

Manually installing AndroidIDE
==============================

This tutorial walks through the process of **manually** installing the build tools like
JDK, Android SDK, etc. in AndroidIDE.

.. note::

   This guide assumes a basic understanding of AndroidIDE and its terminal usage. If you encounter any issues during
   the installation process, refer to the AndroidIDE documentation or seek assistance from the Android development
   community.

Introduction
------------

AndroidIDE is a powerful, integrated development environment used for Android app development. While the installation
process typically involves using the ``idesetup`` script, there may be instances where users encounter network issues or
other reasons that require manual installation of the build tools. In this blog post, I will walk you through the
step-by-step process of manually installing the build tools in AndroidIDE.

Step 1: Determine CPU Architecture
----------------------------------

Before proceeding with the manual installation, you need to determine the CPU architecture of your Android device.
AndroidIDE supports two CPU architectures:


* ``arm64-v8a``
* ``armeabi-v7a``
* ``x86_64``

Knowing your device's CPU architecture is crucial for downloading the appropriate build tools.

Step 2: Downloading the Build Tools
-----------------------------------

The build tools can be downloaded from the AndroidIDE Tools GitHub repository. Follow these steps to download the
necessary files:


#. Visit the `androidide-tools repository <https://github.com/AndroidIDEOfficial/androidide-tools>`_ on GitHub.

#. Navigate to the releases page.

#. Download the following files:


   * 
     Android SDK base files and the command line tools
     from `this specific release <https://github.com/AndroidIDEOfficial/androidide-tools/releases/tag/sdk>`_.


     * ``android-sdk.tar.xz``
     * ``cmdline-tools.tar.xz``

   * 
     Architecture-specific build and platform tools from one of the other releases. Download the following files:


     * ``build-tools-<tools_version>-<cpu_arch>.tar.xz``
     * ``platform-tools-<tools_version>-<cpu_arch>.tar.xz``

The ``<tools_version>`` is the desired version number of the build and platform tools, and ``<cpu_arch>`` is the
CPU architecture of your device. For ``arm64-v8a`` architecture, look for files mentioning ``aarch64`` and
for ``armeabi-v7a``\ , choose files mentioning ``arm``. At the time of writing this post, the available build and platform
tools versions are ``33.0.3`` and ``33.0.1``. If you're unsure, it's recommended to choose the latest version.

For example, if your device has a ``arm64-v8a`` CPU, you need to download the following files:


* ``android-sdk.tar.xz``
* ``cmdline-tools.tar.xz``
* ``build-tools-33.0.3-aarch64.tar.xz``
* ``platform-tools-33.0.3-aarch64.tar.xz``

Step 3: Installing the Build Tools
----------------------------------

Once you have downloaded the necessary files, follow these steps to install the build tools:


#. Open AndroidIDE and access the terminal.

#. If the current working directory is not ``HOME`` or if you're unsure about the current working directory, execute the
   following command to navigate to the ``HOME`` directory:

   .. code-block:: bash

      cd

#. 
   Extract the ``android-sdk.tar.xz`` file using the following command:

   .. code-block:: bash

      tar xvJf /path/to/android-sdk.tar.xz

Replace ``/path/to/android-sdk.tar.xz`` with the path to the downloaded ``android-sdk.tar.xz`` file. After extraction,
navigate to the ``android-sdk`` directory with the following command :

.. code-block:: bash

   cd android-sdk


#. Install the build tools, platform tools, and command line tools using the following commands:

.. code-block:: bash

   tar xvJf /path/to/build-tools-tar.xz
   tar xvJf /path/to/platform-tools-.tar.xz
   tar xvJf /path/to/cmdline-tools-.tar.xz

Replace the path to each respective archive file.

Step 4: Installing OpenJDK 17 Package
-------------------------------------

To complete the installation, you need to install the ``openjdk-17`` package. Execute the following command in the
AndroidIDE terminal:

.. code-block:: bash

   pkg upgrade && pkg install openjdk-17

Conclusion
----------

In situations where network issues or other factors prevent the automatic installation of build tools in AndroidIDE,
manual installation becomes necessary. By following the steps outlined in this blog post, you can successfully install
the build tools, platform tools, and command line tools, ensuring a seamless development experience in AndroidIDE.
Remember to choose the appropriate files based on your device's CPU architecture and stay updated with the latest tool
versions for optimal performance and compatibility. Happy coding!

