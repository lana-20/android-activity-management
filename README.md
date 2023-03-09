# Android Activity Management

*Android apps come with a sort of subdivision that iOS apps don't, called Activities. Using Appium you can interact directly with Activities and not only apps.*

Android Activities is an important topic, unique to Android.

### What are Android Activities?

1. Well, the first thing we need to talk about is the fact that Android apps are not really just one monolithic thing. On iOS, an app is more or less an app. Sure, it is composed of multiple views, but from the perspective of the operating system, it's all just one app. On Android, the situation is different. Android apps are actually collections of smaller divisions known as Activities. An app might consist of only one Activity, but more commonly there will be more than one. Take a look at the various screens of the Android settings app here. Each of these different views is actually a separate Activity which has its own unique name. As you move through the app, the system is actually switching between the various activities under the hood. At any given point in the lifetime of the operating system, Android knows exactly which app is running, and it knows exactly which activity within that app is running. An app is never running without one of its activities running. Of course, there is a default sort of activity, known as the Launch Activity, which is the activity that is loaded whenever your app is launched.

2. What's the point of Activities, then? Why did Android decide to allow apps to be split into these activities? One reason is that users often want to go directly to specific places within an app. Imagine wanting to check for available wifi networks without wanting to open up the settings app, and navigate through a number of different views to get there. By making the wifi settings view a separate activity, the system is able to open that activity directly if it is directed to do so, bypassing all the other app views. In essence, each Activity is a portion of your app which could be triggered directly, even from outside the app.

3. The other main design consideration for Activities is that each Activity can be registered with Android as handling one or more generic action requests, called "Intents". Examples of intents would be the intent of a user to capture an image, or to share something with a contact. When users take actions on the device, these Intents can be triggered, and Android will look for any activity on the device which has registered support for that intent. For example, if I want to set the wallpaper on my device, that triggers an intent action called <code>android.intent.action.SET_WALLPAPER</code>. What happens now is that Android looks for any app which has registered an activity that supports this particular intent action. If it finds more than one, it will present a list of options like you see in the image here, asking the user to pick which app it should use to fulfill the action. When the user selects the app, then the particular activity which supports that intent is launched. When the activity is launched, it is also told what intent triggered it, so that it can take immediate action. When intents are triggered, they can also contain various kinds of metadata, for example the URL of a link to be viewed, or similar. This data is also passed to the Activity when it's launched, so it can take appropriate action based on the context.

4. There's more to learn about Activities, but that's all we're going to discuss for now. You can go and read the Android developer documentation on Activities and Intents to get a fuller picture, if you want. For now, just remember that every time you're looking at an Android app, you're not just looking at an app, you're looking at one of those app's Activities. It has its own special ID, and it can be launched directly, and potentially launched via a number of different intent actions. What's great is that we can actually make all these things happen just by using Appium commands, so that we can test apps do the right things when triggered by different intents.

The main command we care about here is called <code>driver.start_activity</code>. It takes two parameters at a minimum: the package ID of the application you want to start, and the activity name or ID to launch within that app. We've already talked about how to determine the package ID of an app, but how do you find out which activities the app has available, and what their names are? Well, similarly to package ID, we can use a special tool included in the Android SDK to determine this information. This tool is called <code>aapt</code>. On Mac, you can run:

    aapt list -a ./ApiDemos.apk | grep -E "android:name.+io.appium.android.apis"

Whereas on Windows we would run:

    aapt list -a ./ApiDemos.apk | findstr /i "android:name.*io.appium.android.apis"

Whichever platform you're on, this long command starts out by using <code>aapt</code>'s <code>list</code> subcommand to list out a bunch of information from the APK. But this will again be a firehose, so we use the <code>grep</code> tool on Mac or the <code>findstr</code> tool on Windows, this time with something called a regular expression, to find any lines that match a string including <code>android:name</code> as well as our package ID, which is <code>io.appium.android.apis</code>. Obviously if you're running this command, you'd want to replace it with your app's package ID. We'll look at a demo of this in a moment, but for now just remember that this is what we can do.

Once we've got our package and activity name, we're pretty much ready to go. We don't *need* anything else in order to start an activity. But, there are a few optional keyword arguments we might want to include:

1. <code>app_wait_package</code> is a parameter that tells Appium what package it should *wait* for to be active after your activity is started. The reason we have this option is that when certain activities are launched, it's possible that, totally on their own, they cause another app and/or activity to launch. If that's the case, and if you don't tell Appium, then it might stick around trying to verify that your app and activity are active, when that is no longer the case. Basically, you should just use this option if you run into an error where Appium tells you your activity never started. If so, check to see if perhaps a new app was loaded instead, and include that app's package ID here.
2. For the same reason we have <code>app_wait_activity</code>, which is going to be used more commonly than <code>app_wait_package</code>. It tells Appium which *activity* it should wait for to be active after launching yours. Again, this is only relevant if the activity you launch somehow automatically transitions to a new activity immediately, because then Appium would think your activity never actually launched.
3. Now we come to parameters that have to do with intents. There are three main ones: <code>intent_action</code>, <code>intent_category</code>, and <code>intent_flags</code>. These correspond to the action, category, and flag concepts that relate to intents. If you happen to know that your activity can respond to a specific intent category, or if you want to send any specific flags along with the intent, then you can use these options.
4. 
There are a couple more optional parameters you can explore in the docs, but these are the only ones you're likely to need to use.

Let's talk about two other driver properties that have to do with packages and activities. The first is <code>driver.current_activity</code>, which is a property that, when retrieved, will give you the name of the currently running activity. You could use this to do different things in your script depending on where you've got to in your app, or just to use Appium itself to find out what the activity name is. And the second is <code>driver.current_package</code>, which gives you the package ID of the currently running app.

















