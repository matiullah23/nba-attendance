function initViz() {
    var containerDiv = document.getElementById("tableauViz"),
    url = "https://public.tableau.com/views/CitiBikeAnalysis_7/Top10StartLocations?:embed=y&:display_count=yes&publish=yes";

    var viz = new tableau.Viz(containerDiv, url);
}
