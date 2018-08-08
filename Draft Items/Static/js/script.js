function initViz() {
    var containerDiv = document.getElementById("tableauViz"),
    url = "https://public.tableau.com/profile/jt.von.seggern#!/vizhome/NBAAttendanceDashboard/NBAAttendanceDashboard?publish=yes";

    var viz = new tableau.Viz(containerDiv, url);
}
