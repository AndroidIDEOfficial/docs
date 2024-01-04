.. _tutorial-signing_apks:

Signing APKs
============

This tutorial shows how to create a signed release APK of your project with AndroidIDE.

Introduction
------------

This tutorial covers the following topics :


* Create a keystore file with AndroidIDE Terminal.
* Configure Gradle to use the signing key.
* Verify APK signature.

Creating the keystore
---------------------

For creating the keystore file, we'll use ``keytool`` that is provided by OpenJDK. You can execute the ``keytool -h``
command to check if the tool is available or not. If you do not see the help message, you might need
to `perform the basic setup </blogs/getting-started/2023/03/15/getting-started-with-androidide>`_ before you can proceed
with next steps.

Open the terminal and follow the instructions to create the keystore.

First of all, you need to ``cd`` into the directory where you want to store the keystore file. For this tutorial, we'll be
storing the keystore in the ``AndroidIDEProjects`` directory in the internal storage. Execute the following command
to ``cd`` into the projects' directory :

.. code-block:: bash

   cd $PROJECTS

Here, ``PROJECTS`` is an environment variable whose value is the absolute path of the projects' directory.

To create a new keystore file, execute the following command :

.. code-block:: bash

   keytool -genkey -v -keystore signing-key.jks -keyalg RSA -keysize 2048 -validity 9125 -alias myAlias

Explanation :


* ``-genkey`` : Command used to create new keystore with ``keytool``.
* ``-v`` : For verbose output.
* ``-keystore signing-key.jks`` : Specifies the filename of the output keystore file. In this example, the keystore file
  will be saved as ``signing-key.jks``.
* ``-keyalg RSA`` : Specifies the key algorithm to use for the keystore.
* ``-keysize 2048`` :  The number of bits in the key used by the key algorithm.
* ``-validity 9125`` : The validity of the key, in days. In this example, the value is ``9125 days`` which is equal
  to ``25 years``.
* ``-alias myAlias`` : The key alias.

`Learn more <https://docs.oracle.com/en/java/javase/17/docs/specs/man/keytool.html>`_ about ``keytool``.

After you execute the above command, you'll be asked to provide additional information about the keystore. After you
enter the required information, the keystore file will be created.

Configuring Gradle
------------------

We need to add ``signingConfig`` in the ``app/build.gradle`` file. The ``signingConfig`` specifies the keystore which will be
used to sign the build variants of your application. To do this, we need to copy the ``signing-config.jks`` file to
the ``app`` module's directory of our project. So go ahead and copy the file.

Then edit your ``app/build.gradle`` file like this :

.. code-block:: groovy

   android {
       ...
       signingConfigs {
           release {
               // Specify the name of your keystore file
               // The file must be located in your module directory
               storeFile file("signing-key.jks")

               // The keystore password
               storePassword "test1234"

               // The key alias, same as the one you specified with '-alias' argument while creating the keystore
               keyAlias "myAlias"

               // The key password
               keyPassword "test1234"
           }
       }

       // specify the signingConfig to use for release build type
       buildTypes {
           release {
               signingConfig signingConfigs.release
           }
       }
       ...
   }

That's it! You can now run ``:app:assembleRelease`` task to assemble the release build of your project. The resultant APK
will be signed with the ``signing-key.jks`` file.

Verify APK Signature
--------------------

You can use the ``apksigner`` tool provided by the Android SDK Build Tools to verify the signature of the APK. To do this,
just execute the following command :

.. code-block:: bash

   $HOME/android-sdk/build-tools/<build-tools-version>/apksigner verify --print-certs /path/to/your/app.apk

   # For example
   $HOME/android-sdk/build-tools/33.0.3/apksigner verify --print-certs $PROJECTS/MyApplication/app/build/outputs/apk/release/app-release.apk

This will print the information about the APK's signature. You can learn more about the ``apksigner``
tool `here <https://developer.android.com/tools/apksigner>`_.
