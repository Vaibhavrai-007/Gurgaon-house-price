@echo off
title Gurgaon House Price Predictor
cd /d "%~dp0"

echo ========================================================
echo Starting Gurgaon House Price Predictor (Streamlit App)...
echo ========================================================
echo.

if exist ".venv\Scripts\streamlit.exe" (
    ".venv\Scripts\streamlit.exe" run app.py
) else (
    echo [WARNING] .venv not found, trying global streamlit...
    streamlit run app.py
)

if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] An error occurred while running the app.
    pause
)
