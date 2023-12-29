---
title: Bottom Sheet
desc: A brief explanation about the components of the bottom sheet in the editor activity.
---

# Editor Bottom Sheet

The bottom sheet can be expanded either by sliding or by a simple click. It shows the output from various builds. It
also shows the application logs, logs from the IDE itself, search results and file diagnostics.

## Build Output

This tab shows the build output as emitted by the Gradle build process. This is where your project's build related
issues will be shown.

<details>
  <summary>See screenshot</summary>
  <img src="/images/build_output.png" width="250"/>
</details>

## App Logs

When you build apps in AndroidIDE, it automatically adds the `LogSender` API for `debug` builds of your application.
The `LogSender` automatically starts
when your application is started and continuously send logs from your application to AndroidIDE. This tab shows these
logs received from your application.

<details>
  <summary>See screenshot</summary>
  <img src="/images/app_logs.png" width="250"/>
</details>

## IDE Logs

This tab shows the logs from the IDE. With these logs, you can understand what is going on in the IDE. If any errors
occur in the IDE itself, this is where it will be shown. When reporting IDE related issues, you are expected to provide
these logs.

<details>
  <summary>See screenshot</summary>
  <img src="/images/ide_logs.png" width="250"/>
</details>

## Diagnostics

This tab helps you to locate and identify syntax problems with the code. See errors and warnings from your code here.

<details>
  <summary>See screenshot</summary>
  <img src="/images/diagnostics.png" width="250"/>
</details>

## Search Results

The results of `Find in project` and `Find references` action are shown in this tab.

<details>
  <summary>See screenshot</summary>
  <img src="/images/search_results.png" width="250"/>
</details>