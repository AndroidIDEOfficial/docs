.. _dev-versioning:

Versioning
==========

The AndroidIDE version numbers are incremented automatically based on the commit messages and the previous releases.
This is achieved using the `Nyx <https://github.com/mooltiverse/nyx>`_ project. Nyx is a powerful, flexible and
extremely configurable semantic release tool.

.. note:: 
   Nyx plugin is not used for F-Droid builds. This is because the F-Droid builds provide a fixed version name
   and version code and hence, they need not to be calculated dynamically.

.. _dev-versioning-basics:

Basics
------

AndroidIDE uses `semantic versioning <https://semver.org/>`_. The version numbers are automatically incremented by Nyx
based on the type of `conventional commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ and previous release. Specifically :


* ``fix`` commits increment the PATCH version number.
* ``feat`` commits increment the MINOR version number.
* ANY type of commit with a ``BREAKING CHANGE`` update the MAJOR version number.

For example, if the previous release's version name was ``v2.5.3-beta`` and then the new version will be:


* ``v3.0.0-beta`` - if at least one commit has a ``BREAKING CHANGE``.
* ``v2.6.0-beta`` - if there are no breaking changes and least one commit has type ``feat``.
* ``v2.5.4-beta`` - if there are no breaking changes, no ``feat`` commits and at least one commit has type ``fix``.

.. _dev-versioning-version_format:

Version name format
-------------------

The release version names specified in the following format :

.. code-block::

   v[MAJOR].[MINOR].[PATCH]-[PRE-RELEASE]

For example : ``v2.5.3-beta``.

The CI builds contain additional information in their version names. This makes it easier for us to know the exact version for debug builds
and fix issues faster :

.. code-block::

   v[MAJOR].[MINOR].[PATCH]-[PRE-RELEASE].[RELEASE-TYPE].[REVISION]+branch.[BRANCH-NAME].commit.[SHORT-COMMIT-HASH].timestamp.[TIMESTAMP]

For example : ``v2.5.3-beta.internal.1+branch.dev.commit.41779f3.timespamp.[...]``

.. _dev-versioning-configuration:

Configuration
-------------

Nyx is configured using the ``.nyx.yml`` file located in AndroidIDE project's root directory.
A `detailed documentation <https://mooltiverse.github.io/nyx/guide/user/>`_ about using Nyx is available on the project's site.

The Nyx Gradle plugin is applied to the ``settings.gradle.kts`` file and the configuration file is set by configuring the ``NyxExtension``.
Read the Nyx documentation for more details.
