# GesturePlay: project explanation

## What it is

GesturePlay is a camera-based, hands-free activity app. Its landing page lets a person enter one of three modes: a retro Photo Booth, Mini Games, or Drawing. The camera reads hand gestures so people can navigate and interact without needing a keyboard or mouse. Admin controls and mouse or touch alternatives are available when needed.

## How it works

The front end is built with HTML, CSS, and JavaScript. It requests camera access through the browser and uses MediaPipe hand landmarks and gesture recognition to track the user's hand. The app maps those hand positions to screen actions and the drawing canvas.

- **Photo Booth:** Users choose one photo with an index finger or a three-photo strip with Victory. If they make no choice, it defaults to one photo. They can use the Mirror toggle and camera looks, take photos, make a strip, save it, and open the computer's print dialog.
- **Mini Games:** Speech recognition can capture the player's name when available; offline, they can type one or use the Player 1 fallback. The player points at a game card for three seconds to start one of two 30-second games. Scores and personal bests are kept in the browser on that device.
- **Drawing:** An index finger draws and Victory erases. The session lasts one minute, then the drawing is saved to `Downloads/gestureplay` and opens the computer's print dialog. Mouse, trackpad, and touch drawing also work.

A small Python server runs on the same computer. It serves the app locally and saves image files to `Downloads/gestureplay`. The browser's print dialog lets the user select a connected printer on either Mac or Windows. Use `launch.command` on Mac or `launch_windows.bat` on Windows instead of opening the HTML file directly. The camera, bundled hand/body tracking models, games, and drawing run locally. Browser speech recognition may need internet, so Mini Games also supports typed names or the Player 1 fallback.

## Short presentation script

“GesturePlay is an interactive photo booth and activity app controlled by hand gestures. On the welcome screen, an index finger opens Photo Booth, a Victory sign opens Mini Games, and three raised fingers open Drawing. In the Photo Booth, you can choose one portrait or a three-photo strip, apply a look, and save or print the result. Mini Games asks for a player name and offers two short hand-controlled games with a leaderboard. Drawing lets you sketch with your index finger and erase with Victory, then download or print your work.

I made it as a web app using HTML, CSS, and JavaScript. The browser camera and MediaPipe recognize hand positions, and the drawing and photo effects are rendered on a canvas. A small Python server runs locally to save photos in Downloads. The browser opens the computer's print dialog, so the person running GesturePlay can choose the paired YICHIP printer or another printer. That means the camera and photos are handled on the computer, while the browser provides speech recognition for player names.”
