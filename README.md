# GesturePlay

GesturePlay is a local camera playground with Photo Booth, Mini Games, and Drawing. Its booth has a classic retro feel, live preview, printed keepsakes, and photos saved in `Downloads/gestureplay`.

## Start GesturePlay

On Mac, double-click `launch.command`. On Windows, double-click `launch_windows.bat`. Keep the terminal window open while using GesturePlay; press Control-C there to stop it. Both launchers open the site on localhost so the camera works.

Allow camera access when the browser asks. The hand-tracking library, hand/body models, and fonts are bundled in this folder, so those work without internet. Camera frames and photos are not uploaded by GesturePlay.

### Windows showcase

Copy the whole `photobooth` folder to the Windows computer and make sure Python 3 is installed. Connect the YICHIP printer by USB or Bluetooth, install/add its Windows printer driver beforehand, then double-click `launch_windows.bat`, allow camera access in the browser, and keep the terminal window open. GesturePlay opens the regular print dialog so you can select the YICHIP. The camera, hand tracking, games, drawing, saving, and printing all work offline. Browser speech recognition may need internet; in Mini Games, type a name or leave it blank and press **Continue** to use Player 1.

GesturePlay opens in hands-free mode by default. Hold an index finger for two seconds to open Photo Booth, Victory for two seconds for Mini Games, or three raised fingers for two seconds for Drawing. Use the **Admin** switch to show the computer controls, navigation header, and footer. The camera starts on launch so it can recognize the welcome-page gestures.

## Photo Booth

- Choose **One photo** (the default) or **Three photos** for a strip. Hands-free, hold an index finger for one photo or Victory for a three-photo strip; if there is no choice in five seconds, one photo starts.
- Three-photo mode flashes and plays a shutter sound for each shot, with the three captured frames appearing in a live strip at the side. After the third shot, the photos are assembled in a simple vertical template strip.
- The booth camera fills the screen. Use **Mirror** in the camera preview to flip both the live image and saved photos. Turn Admin on to reveal the other controls at the top.
- Show **Victory** or press **Take photo** for a three-second countdown.
- An open palm stops the current capture timer. Curl your index finger, then reopen it to confirm the next look. In three-shot mode, Victory starts or resumes the sequence; the next shots are five seconds apart until all three are taken.
- Each picture saves automatically to `Downloads/gestureplay`. A three-shot session also saves the photo strip.
- After saving, GesturePlay opens the computer's print dialog. Choose the YICHIP POS58 Bluetooth printer (or another printer) and confirm printing there. Pair the printer in Windows or macOS first and install/select its printer driver. Photo Booth returns to the main mode page five seconds after the print dialog closes; choose **Back to main page** to leave sooner.

## Mini Games

Mini Games opens a small live camera preview for hand tracking, asks the player to say their name; if no speech is heard, it assigns Player 1, Player 2, and so on. Names are confirmed automatically after four seconds unless they are repeated or edited. It then offers exactly two games. Point at **Star Catcher** or **Freeze Frame** with your index finger for three seconds to start it. Each round lasts 30 seconds: catch falling stars with your index finger, or follow and hold inside the moving ring. Scores and each player's personal best are saved separately for each game on this device; results return to the main screen after a short celebration.

## Drawing

Point with your index finger for the pencil and show Victory to erase; open your hand to lift the tool. Or draw directly on the canvas with a mouse, trackpad, or touch. Each drawing session lasts one minute. When time is up, the canvas freezes, saves to `Downloads/gestureplay`, opens the computer's print dialog, then returns to the main page. Choose a printer in the dialog to print, or cancel to skip.

## Photo booth gestures

| Gesture | Action |
| --- | --- |
| Open palm | Stop the current capture timer |
| Curl and reopen the index finger | Confirm the next filter |
| Victory | Take a photo / start or resume a strip |
