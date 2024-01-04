.. _tutorials-using_room_db:

.. role:: raw-html-m2r(raw)
   :format: html

Using Room database
===================

This tutorial shows how to setup the Room persistence library so that it can work with AndroidIDE projects.

.. _tutorials-using_room_db-begin:

Before we begin
---------------

This tutorial is **not** meant for showing you how to **use** the Room persistence library. There are so many useful
posts/tutorials about that. In this post, we are focusing on how to fix the Gradle build error which is originated from
the `sqlite-jdbc library <https://github.com/xerial/sqlite-jdbc>`_.

I assume that you are already familiar with Room. If not, you might want to see the Android Developer Docs
for `saving data in a local database with Room <https://developer.android.com/training/data-storage/room>`_.

.. _tutorials-using_room_db-issue:

The issue
---------

When trying to build a project in AndroidIDE which uses the Room persistence library, the annotation processing phase of
the Java compilation process throws an ``UnsatisfiedLinkError`` which states that the ``sqlite-jdbc`` shared library cannot
be loaded. This happens because the ``sqlite-jdbc`` library does not recognize the Android Operating System as a valid
platform. As a result, the build process fails with the following error :

.. code-block::

   Task :app:compileDebugJavaWithJavac
   Failed to load native library:sqlite-3.39.3.0-d2db51cf-974c-4209-b766-2102751cbd0f-libsqlitejdbc.so. osinfo: Linux/aarch64
   java.lang.UnsatisfiedLinkError: /data/data/com.itsaky.androidide/files/usr/tmp/sqlite-3.39.3.0-d2db51cf-974c-4209-b766-2102751cbd0f-libsqlitejdbc.so: dlopen failed: library "libc.so.6" not found
    at java.base/jdk.internal.loader.NativeLibraries.load(Native Method)
    at java.base/jdk.internal.loader.NativeLibraries$NativeLibraryImpl.open(NativeLibraries.java:384)
    at java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:228)
    at java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:170)


.. _tutorials-using_room_db-issue_fix:

Fixing the issue
----------------

This issue was fixed in version ``3.40.1.0`` of the ``sqlite-jdbc`` library. But the ``androidx.room:room-compiler`` library
still uses an older version of ``sqlite-jdbc``. So, all we need to do is to configure Gradle such that it uses the newer
version of the library.

We're going to build the `android-room-with-a-view <https://github.com/googlecodelabs/android-room-with-a-view>`_ sample
project in AndroidIDE. To do so, we need to clone the repository first. Go ahead and clone the repository with
the ``Clone git repository`` button on the main screen or the AndroidIDE terminal.

Once you clone the repo, open the project and let the project synchronization to finish. This may take some time
depending on your device and network.

..

   If you try to build the same sample project directly in AndroidIDE, you'll get other errors as well, This is because
   AndroidIDE does not support Android Gradle Plugin older than ``v7.2.0`` and the project uses an older version of the
   same.
   To fix this, you'll have to update the sample project to use the newer versions of the Android Gradle Plugin.

   The changes you need to make in the project can be found
   in `this specific commit <https://github.com/itsaky/android-room-with-a-view/commit/a33fdd67dfb58487273b1adf67aca85c1f1b0893>`_.
   If you just want to build the sample project, without any modifications, you can
   clone `this repository <https://github.com/itsaky/android-room-with-a-view>`_ and build it directly in AndroidIDE.


After the project is initialized, we need to edit the ``app/build.gradle`` file in order to configure Gradle to use a
newer version of the library. There are two ways to achieve this.

.. _tutorials-using_room_db-issue_fix-first:

Method 1 - Exclude ``jdbc`` dependency from Room
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this method, we exclude the ``sqlite-jdbc`` module from the ``org.xerial`` group so that it will not be included when
resolving dependencies for the Room compiler. Another annotation processor dependency is then added explicitly for
the ``org.xerial:sqlite-jdbc:3.40.1.0`` module. This is a specific version of the ``sqlite-jdbc`` module that will be used
during the annotation processing phase.

.. code-block:: groovy

   dependencies {
       ...

       annotationProcessor("androidx.room:room-compiler:$rootProject.roomVersion") {
           // exclude the sqlite-jdbc dependency from the room-compiler
           exclude group: 'org.xerial', module: 'sqlite-jdbc'
       }

       // redefine the sqlite-jdbc dependency with the newest version
       annotationProcessor "org.xerial:sqlite-jdbc:3.40.1.0" // use latest version here

       ...
   }

.. _tutorials-using_room_db-issue_fix-second:

Method 2 - Force a specific ``jdbc`` version for all configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this method, the ``configurations.all`` block is used to modify the resolution strategy for all configurations (e.g.,
compile, runtime, test, annotationProcessor) defined in the project. The ``resolutionStrategy`` block inside it is then
used
to define custom resolution strategies for dependency conflicts.

In this case, the force method is used to force the resolution of the ``org.xerial:sqlite-jdbc:3.40.1.0`` module. This
means that Gradle will prioritize and use the version specified in this force statement.

.. code-block:: groovy

   configurations.all {
       resolutionStrategy {
           force 'org.xerial:sqlite-jdbc:3.40.1.0' // use latest version here
       }
   }

To summarize, the first method manages the dependencies specifically for the Room compiler during the annotation
processing phase, while the second method modifies the resolution strategy to forcefully use a specific version of
the ``sqlite-jdbc`` module for all configurations.

After you do the desired modification in the project, you just need to save the file and sync the project. After that,
you can build the project as usual. The screenshot below shows the sample application built with AndroidIDE.

:raw-html-m2r:`<!-- Room DB : Sample app -->`
:raw-html-m2r:`<img
src="/_static/images/screenshots/room-sample-app.png"
class="block mx-auto"
width="250px"
alt="Room DB Sample App"/>`
