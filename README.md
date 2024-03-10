run using the following steps:

1. change name of launchagent.plist to com.{insert your own user}.keylogger.plist

2. Edit the launch agent file for the updated file paths

3. install the launch agent

   mv com.user.keylogger.plist ~/Library/LaunchAgents/

4. load the launch agent

   launchctl load ~/Library/LaunchAgents/com.{user}.keylogger.plist
