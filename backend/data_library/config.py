
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model Configuration
# We use standard Flash for prompt engineering for thought traces
GEMINI_THINKING_MODEL = "gemini-3-flash-preview"
# We use standard Flash for fast File Search retrieval
GEMINI_RAG_MODEL = "gemini-3-flash-preview"
GEMINI_CORPUS_NAME = "brainstorming-research-library"

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Constants
FILE_SEARCH_STORE_NAME = "pharma-brand-library"
# Resolve paths relative to this file to ensure consistency regardless of CWD
BASE_DIR = Path(__file__).resolve().parent.parent

# Check for Vercel environment
IS_VERCEL = os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME")

if IS_VERCEL:
    # On Vercel, only /tmp is writable
    # NOTE: /tmp is ephemeral, data will be lost on function restart
    DATA_DIR = Path("/tmp/data")
else:
    DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "agents_v2.db"
SESSIONS_DB_PATH = DATA_DIR / "sessions.db"
DOCS_PATH = DATA_DIR / "documents"

# Ensure directories exist
try:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_PATH.mkdir(parents=True, exist_ok=True)
except Exception as e:
    print(f"Warning: Could not create data directories: {e}")
    # Fallback to tmp if permissions fail locally
    if not IS_VERCEL:
        print("Falling back to /tmp/data")
        DATA_DIR = Path("/tmp/indegene_agent_data")
        DB_PATH = DATA_DIR / "agents_v2.db"
        SESSIONS_DB_PATH = DATA_DIR / "sessions.db"
        DOCS_PATH = DATA_DIR / "documents"
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        DOCS_PATH.mkdir(parents=True, exist_ok=True)
