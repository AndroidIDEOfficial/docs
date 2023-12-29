---
title: Installation
desc: This guide shows how to install AndroidIDE, setting up the terminal and the Android build tools installation. 
---

# Installation

This guide shows how to install AndroidIDE, setting up the terminal and the Android build tools installation.

Before getting started, please make sure that your Android device meets the minimum requirements.

## Minimum requirements

Before installing and using AndroidIDE, it is essential to ensure that your device meets the minimum requirements to run the application.

- ARM based CPU - You must ensure that your device has an arm based CPU i.e. `arm64-v8a (aarch64)` or `armeabi-v7a`.
  Please note that AndroidIDE cannot be used on most emulators as they often do not meet the CPU architecture
  requirement.
- Enough **available** RAM - You will be working with the Gradle build system. Depending on the size of your project,
  you'll need enough **free RAM** so that the Gradle Daemon is not killed by the system. A minimum of **1.5GB - 2GB free
  RAM** is recommended.
- Enough storage space - A minimum of 4GB free storage space is required. You'll need enough space for various Gradle
  distributions and dependencies, according to your project configuration. After the basic setup, around 1GB of space is
  used by AndroidIDE (without any dependencies or distributions installed).

> Internet connection is required for the initial setup. A **WiFi connection** is recommended.

## Download AndroidIDE

- Latest Release Version (2.5.0-beta)
  - [arm64-v8a (aarch64)](https://github.com/AndroidIDEOfficial/AndroidIDE/releases/download/v2.5.0-beta/androidide-v2.5.0-beta-arm64-v8a.apk)
  - [armeabi-v7a](https://github.com/AndroidIDEOfficial/AndroidIDE/releases/download/v2.5.0-beta/androidide-v2.5.0-beta-armeabi-v7a.apk)
- [Download from Github Release](https://github.com/AndroidIDEOfficial/AndroidIDE/releases)
- [Debug Version (for tester)](https://github.com/AndroidIDEOfficial/AndroidIDE/actions)
  <p>to download this version, you have to choose `Build and test` workflow, then download the artifact.</p>

> Make sure you have logged in to github in your browser.

> Debug version is for tester.

## Setup the terminal [^cheat]

- Open AndroidIDE [terminal](./user_interface#terminal). It will install the bootstrap packages.
- Then run `pkg upgrade` to update packages to latest version.

## Build Tools Installation [^cheat]

Install the JDK, SDK and commandline tools for sdk.

- Open terminal and run `idesetup -c`.
- After you execute the above command, it'll show a summary of the configuration. Type `y` to confirm the configuration and start the installation process.
- After successful installation, `Downloads completed. You are ready to go!` will be printed.

You can execute `idesetup -h` to see configuration options.

[^cheat]: Cheatsheet :

    - One command to setup the terminal and to install build tools.
      ```bash
      cd && pkg upg && idesetup -c
      ```
