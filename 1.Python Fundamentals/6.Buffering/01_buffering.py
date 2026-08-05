#### Python Buffering Notes: time.sleep(), -u, flush=True

# ------------------------------------------------------------
### time.sleep(1)
# ------------------------------------------------------------
# time.sleep(1) pauses program execution for 1 second.
# It delays the next instruction but does NOT control buffering.
#
## Example:
# import time
# for i in range(5):
#     print(i)
#     time.sleep(1)
#
# Here, print(i) adds a newline automatically.
# Because newline often flushes output in terminal,
# numbers appear one by one even without -u.
#
# ------------------------------------------------------------
### Python -u (Unbuffered Mode)
# ------------------------------------------------------------
# Run script using:
# python -u script.py
#
# -u forces stdout and stderr to display immediately.
#
## Example:
# for i in range(5):
#     print(i, end=" ")
#     time.sleep(1)
#
# Without -u:
#            output may appear together after loop finishes.
#
# With -u:
#         output appears one by one every second.
#
#  Buffering: Store temporarily, then send later.
#  Unbuffering (or flushing): Don't keep it waiting—send it immediately.
#
# ------------------------------------------------------------
### flush=True
# ------------------------------------------------------------
# flush=True forces Python to empty buffer immediately after print.
#
## Example:
# print(i, end=" ", flush=True)
#
# Equivalent internal code:
# import sys
# sys.stdout.write(str(i) + " ")
# sys.stdout.flush()
# 
# 
# print()
#       │
#       ▼
# sys.stdout.write(...)
#       │
#       ▼
# Buffer
#       │
#       ▼
# flush()   ← empties the buffer immediately
#       │
#       ▼
# Screen
#
# ------------------------------------------------------------
### Difference between -u and flush=True
# ------------------------------------------------------------
# -u         -> applies to whole program
# flush=True -> applies to one print statement only
#
# ------------------------------------------------------------
### Easy Memory Trick
# ------------------------------------------------------------
# sleep() -> pauses execution
# flush() -> forces display
# -u      -> removes buffering globally
# -u disables buffering globally, while flush=True empties buffer only after a specific print statement.


# Normal Python: 
'''
Program
   │
   ▼
Tank (Buffer)
   │
(wait)
   ▼
Screen

'''

# flush=True:
'''
Program
   │
   ▼
Tank
   │
Flush Now!
   ▼
Screen
'''

# python -u:
'''
Program
   │
   ▼
Screen
'''
#   
# 

## There are three common buffering modes:

# Unbuffered – Output is sent immediately.
# Line buffered – Output is sent when a newline (\n) is encountered.
# Fully buffered – Output is sent only when the buffer is full or explicitly flushed.
# --> Most terminals use line buffering for standard output (stdout).

# Buffering mode depends on the destination of the output, not just on Python itself:

# Terminal (interactive console): Usually line buffered.
# File: Usually fully buffered.
# Running with python -u: Unbuffered for standard output and standard error.

# ------------------------------------------------------------
## Demo 1: print() with newline (newline usually flushes automatically)
# ------------------------------------------------------------

import time

print("Demo 1: print() with newline")
for i in range(5):
    print(i)
    time.sleep(1)

# ------------------------------------------------------------
## Demo 2: print without newline (buffering visible)
# ------------------------------------------------------------

print("\nDemo 2: print without newline")
for i in range(5):
    print(i, end=" ")
    time.sleep(1)

print()

# ------------------------------------------------------------
## Demo 3: print with flush=True
# ------------------------------------------------------------

print("\nDemo 3: print with flush=True")
for i in range(5):
    print(i, end=" ", flush=True)
    time.sleep(1)

print()
