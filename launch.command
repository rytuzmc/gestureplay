#!/bin/zsh
cd "$(dirname "$0")" || exit 1

SERVER_PID=""
PORT=""
for candidate in {8000..8010}; do
  python3 server.py "$candidate" &
  SERVER_PID=$!
  sleep 0.5
  if kill -0 "$SERVER_PID" 2>/dev/null; then
    PORT="$candidate"
    break
  fi
done
if [[ -z "$PORT" ]]; then
  echo "GesturePlay could not find a free local port. Close an old GesturePlay server and try again."
  exit 1
fi
trap 'kill "$SERVER_PID" 2>/dev/null' EXIT INT TERM
open "http://localhost:$PORT"
echo "GesturePlay is running. Photos save to Downloads/gestureplay. The browser print dialog lets you choose a printer."
echo "Keep this window open; press Control-C to stop GesturePlay."
wait "$SERVER_PID"
