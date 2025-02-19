from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from chart_generator import plot_pie_chart, plot_birth_year_trend, plot_column_chart
import os

# Initialize FastAPI app
app = FastAPI()

# Serve static files (for templates)
app.mount("/templates", StaticFiles(directory="templates"), name="templates")

# Read the HTML template for rendering
def get_html_template():
    with open("templates/index.html", "r") as file:
        return file.read()

# Homepage Route (UI View)
@app.get("/", response_class=HTMLResponse)
async def home():
    return HTMLResponse(content=get_html_template(), status_code=200)

# Chart Generation Route
@app.get("/chart/")
async def get_chart(chart_type: str):
    """
    Select a chart type:
    - pie: Birth Month Distribution
    - line: Registration Year Trend
    - column: Student Count by Department
    """

    if chart_type == 'pie':
        buf = plot_pie_chart()
    elif chart_type == 'line':
        buf = plot_birth_year_trend()
    elif chart_type == 'column':
        buf = plot_column_chart()
    else:
        raise HTTPException(status_code=400, detail="Invalid chart type. Use 'pie', 'line', or 'column'.")

    return StreamingResponse(buf, media_type="image/png")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
