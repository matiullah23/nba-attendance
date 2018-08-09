function initViz() {
    var containerDiv = document.getElementById("tableauViz"),
    url = "https://public.tableau.com/views/NBAAttendanceDashboard/NBAAttendanceDashboard?:embed=y&:display_count=yes&publish=yes";
        
    var viz = new tableau.Viz(containerDiv, url); 
}

function vizResize() {
    var width = document.getElementById("resizeWidth").value;
    var height = document.getElementById("resizeHeight").value;
    var sheet = viz.getWorkbook().getActiveSheet();

    sheet.changeSizeAsync(
        {"behavior": "EXACTLY", "maxSize": { "height": height, "width": width }})
        .then(viz.setFrameSize(parseInt(width, 10), parseInt(height, 10)));
}