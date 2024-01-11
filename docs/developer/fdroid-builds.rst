.. _dev-fdroid_builds:

F-Droid builds
==============

F-Droid builds (most) applications from source, signs them using their signing key and then those applications are published on their
applications repository. Publishing on F-Droid also requires us to make sure that the project is Free, Libre and Open Source Software (FLOSS)
and does not use or depend on proprietary software, trackers or ad libraries.

AndroidIDE already complies with
`F-Droid's Inclusion Policy <https://f-droid.org/en/docs/Inclusion_Policy/#:~:text=All%20applications%20in%20the%20repository,a%20GPL%20or%20Apache%20license.>`_.
However, there are a few things that must be taken into account when working on the AndroidIDE project.

.. note::
    The following instructions MUST be followed if you are working on the AndroidIDE project and plan to propose a change.
    The instructions can be ignored if you're building AndroidIDE for personal use or if you do not intend to propose your changes to the
    upstream AndroidIDE repository.

* **Trusted maven repositories** - Only trusted Maven repositories must be used in the project. Check the list of maven repositories that
  are allowed by F-Droid in their inclusion policy.

* **No pre-packaged libraries** - Prebuilt libraries must not be included in the project's codebase. For example, you cannot directly
  include a ``.jar`` or ``.aar`` file in the libs directory. Instead, try to build the library from source by adding it as a module. If this
  is not possible, please open an issue so it can be discussed with the maintainers.

* **No prebuilt executables/shared-libraries** - Prebuilt executable files must not be included in the project's codebase. For example, you cannot simply
  include a JNI library into the codebase. Shared libraries must be built from source, always.


Build configuration
-------------------

When building AndroidIDE for F-Droid, certain properties are provided to the Gradle build via the ``fdroid.properties`` file.
As of this writing, the following properties are defined in this file :


* ``ide.build.fdroid=<boolean>`` - Whether we are building AndroidIDE in F-Droid's build server. This is always set to ``true`` when building for F-Droid.
* ``ide.build.fdroid.version=<string>`` and ``ide.build.fdroid.vercode=<integer>``- Version name and version code for AndroidIDE. When building for F-Droid,
  a fixed version name and version code is provided. Learn more about this in :doc:`versioning </developer/versioning>`.
* ``ide.build.fdroid.arch=<string>`` - An APK for each supported CPU architecture is built separately for F-Droid builds. This property specifies the CPU
  architecture that we are building for. Its value must be one of the following :

  * ``arm64-v8a``
  * ``armeabi-v7a``
  * ``x86_64``

* ``ide.build.fdroid.aapt2File.<arch>=<path-to-aapt2>`` - Path to the prebuilt ``aapt2`` file for the given CPU architecture. The value of ``<arch>`` here
  must be the same as the value of ``ide.build.fdroid.arch`` property. The F-Droid build server builds ``aapt2`` from source before building AndroidIDE, then
  it provides the path to this built ``aapt2`` binary via this property.