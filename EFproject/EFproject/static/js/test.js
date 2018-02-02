 CanvasJS.addColorSet("greenShades", [ //colorSet Array
     "red", // high

     "#3DDB94", //low
     "yellow", // ave
 ]);

 var chart = new CanvasJS.Chart("chartContainer", {
     colorSet: "greenShades",
     interactivityEnabled: false,
     toolTip: {
         enabled: false,
     },
     data: [{
         type: "pie",
         indexLabelPlacement: "inside",
         indexLabelFontColor: "black",
         indexLabelFontSize: 20,
         colorSet: "greenShades",
         dataPoints: [
             { label: "low", y: 33 },
             { label: "average", y: 33 },
             { label: "high", y: 33 }

         ]
     }]
 });

 convertToHalfPie(chart);
 chart.render();


 function convertToHalfPie(chart) {
     var sum = 0;
     var dataPoints = chart.options.data[0].dataPoints;

     for (var i = 0; i < dataPoints.length; i++) {
         sum += dataPoints[i].y;
     }

     dataPoints.splice(0, 0, { y: sum, color: "transparent", toolTipContent: null });
 }