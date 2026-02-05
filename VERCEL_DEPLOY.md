# Vercel Deployment Guide

This guide describes how to deploy the Indegene Brainstorming Agent to Vercel. Because the project contains both a Python Backend (FastAPI) and a Next.js Frontend, we will deploy them as **two separate Vercel projects** from the same repository.

## Prerequisites

1.  A [Vercel Account](https://vercel.com/).
2.  This code pushed to a Git repository (GitHub/GitLab/Bitbucket) that Vercel can access.

---

## Part 1: Deploy the Backend

First, we deploy the backend so we can get its URL to configure the frontend.

1.  **Import Project**: Go to your Vercel Dashboard and click **"Add New..."** -> **"Project"**.
2.  **Select Repository**: Import the repository containing this code.
3.  **Configure Project**:
    *   **Project Name**: Give it a name like `indegene-agent-backend`.
    *   **Framework Preset**: Select **"Other"** (Vercel should auto-detect Python or you can leave it, but "Other" is safe if it doesn't).
    *   **Root Directory**: Click "Edit" and select `backend`. **This is crucial.**
4.  **Environment Variables**:
    Expand the "Environment Variables" section and add the following:
    *   `GEMINI_API_KEY`: Your Google Gemini API Key.
    *   `python_dotenv`: `true` (Optional, but good practice).
5.  **Deploy**: Click **"Deploy"**.

> [!WARNING]
> **Data Persistence**: This application currently uses `SQLite` for its database. On Vercel, the filesystem is **ephemeral**, meaning the database will likely reset on every new deployment or when the serverless function goes cold. For a production app, you should connect to an external database like Postgres (e.g., Vercel Postgres, Supabase, Neon) or MongoDB.

### Verify Backend
Once deployed, Vercel will give you a domain (e.g., `https://indegene-agent-backend.vercel.app`).
Visit `https://<your-backend-url>/docs` to see the Swagger UI. If it loads, your backend is live!

---

## Part 2: Deploy the Frontend

Now we deploy the frontend and connect it to the backend.

1.  **Import Project**: Go to your Vercel Dashboard and click **"Add New..."** -> **"Project"** **again**.
2.  **Select Repository**: Import the **same repository** as before.
3.  **Configure Project**:
    *   **Project Name**: Give it a name like `indegene-agent-frontend`.
    *   **Framework Preset**: Vercel should auto-detect **Next.js**.
    *   **Root Directory**: Click "Edit" and select `frontend`. **This is crucial.**
4.  **Environment Variables**:
    Add the following variable so the frontend knows where to send API requests:
    *   `NEXT_PUBLIC_API_URL`: The full URL of your backend from Part 1 (e.g., `https://indegene-agent-backend.vercel.app`). **Do not add a trailing slash.**
5.  **Deploy**: Click **"Deploy"**.

## Troubleshooting

-   **CORS Errors**: If you see CORS errors in the browser console, ensure your Backend `api/index.py` (or `data_library/api.py`) has `CORSMiddleware` configured to allow traffic from your Frontend URL. Currently, it is set to allow all origins (`*`), which should work fine.
-   **500 Errors**: Check the "Logs" tab in your Vercel Backend project dashboard. It will show Python tracebacks if something crashes.
