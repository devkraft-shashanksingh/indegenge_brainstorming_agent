import os
import sys

# Add the parent directory to sys.path so we can import modules from the root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_library.api import app

# Vercel needs the variable 'app' to be available in this file.
