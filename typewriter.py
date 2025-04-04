import sys
import time

def typing(prompt_text):
    """
    Prints text with a typing effect.
    """
    for char in prompt_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")