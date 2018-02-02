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



    $(document).ready(function() {
        $('#wizard').smartWizard();

        $('#wizard_verticle').smartWizard({
            transitionEffect: 'slide'
        });

        $('.buttonNext').addClass('btn btn-success');
        $('.buttonPrevious').addClass('btn btn-primary');
        $('.buttonFinish').addClass('btn btn-default');
    });


    jQuery(document).ready(function($) {

        //initialize all
        // $('#knob').knob({
        //     'min': 0,
        //     'max': 100,
        //     'step': 20,
        //     'readOnly': false,
        //     'linecap': 'round',
        //     'displayInput': true,
        //     'displayPrevious': false,
        //     'angleOffset': -125,
        //     'angleArc': 250
        // });

        $('#knob').trigger('configure', {
            'draw': function(v) {
                v = parseInt(document.getElementById('knob').value);

                //console.log(v);
                if (v > 80) {
                    this.o.fgColor = 'red';
                    //$("#knob ").css("color ", "red ");
                    document.getElementById('r1').innerHTML = "High";
                    document.getElementById("r1").style.color = "red ";
                    //this.o.inputColor='red';
                } else if (v > 60 && v <= 80) {
                    this.o.fgColor = '#FF863B';
                    $("#knob ").css("color ", "#FF863B ");
                    document.getElementById('r1').innerHTML = "Med High";
                    document.getElementById("r1").style.color = "#FF863B ";

                    //this.o.inputColor='red';
                } else if (v > 40 && v <= 60) {
                    this.o.fgColor = '#ffe95e';
                    $("#knob ").css("color ", "#ffe95e ");
                    document.getElementById('r1').innerHTML = "Med ";
                    document.getElementById("r1").style.color = "#ffe95e ";

                    //this.o.inputColor='red';
                } else if (v > 20 && v <= 40) {
                    this.o.fgColor = '#0091FF';
                    $("#knob ").css("color ", "#0091FF ");
                    document.getElementById('r1').innerHTML = "Low Med ";
                    document.getElementById("r1").style.color = "#0091FF ";

                    //this.o.inputColor='red';
                } else if (v <= 20) {
                    this.o.fgColor = '#3DDB94';
                    $("#knob ").css("color ", "#3DDB94 ");
                    document.getElementById('r1').innerHTML = "Low ";
                    document.getElementById("r1").style.color = "#3DDB94 ";

                    //this.o.
                }
            },
            'format': function(v) {
                if (v > 80) {
                    return v + "% ";
                } else if (v > 60 && v <= 80) {
                    return v + "% ";
                } else if (v > 40 && v <= 60) {
                    return v + "% ";
                } else if (v > 20 && v <= 40) {
                    return v + "% ";
                } else if (v <= 20) {
                    return v + "% ";
                }
            }
        });
        $('#knob2').trigger('change');
    });
    jQuery(document).ready(function($) {

        //initialize all
        // $('#knob').knob({
        //     'min': 0,
        //     'max': 100,
        //     'step': 20,
        //     'readOnly': false,
        //     'linecap': 'round',
        //     'displayInput': true,
        //     'displayPrevious': false,
        //     'angleOffset': -125,
        //     'angleArc': 250
        // });

        $('#knob2').trigger('configure', {
            'draw': function(v) {
                v = parseInt(document.getElementById('knob2').value);
                //console.log(v);
                if (v > 80) {
                    this.o.fgColor = 'red';
                    $("#knob2 ").css("color ", "red ");
                    //this.o.inputColor='red';
                } else if (v > 60 && v <= 80) {
                    this.o.fgColor = '#FF863B';
                    $("#knob2 ").css("color ", "#FF863B ");
                    //this.o.inputColor='red';
                } else if (v > 40 && v <= 60) {
                    this.o.fgColor = '#ffe95e';
                    $("#knob2 ").css("color ", "#ffe95e ");
                    //this.o.inputColor='red';
                } else if (v > 20 && v <= 40) {
                    this.o.fgColor = '#0091FF';
                    $("#knob2 ").css("color ", "#0091FF ");
                    //this.o.inputColor='red';
                } else if (v <= 20) {
                    this.o.fgColor = '#3DDB94';
                    $("#knob2 ").css("color ", "#3DDB94 ");
                    //this.o.
                }
            },
            'format': function(v) {
                if (v > 80) {
                    return v + "% ";
                } else if (v > 60 && v <= 80) {
                    return v + "% ";
                } else if (v > 40 && v <= 60) {
                    return v + "% ";
                } else if (v > 20 && v <= 40) {
                    return v + "% ";
                } else if (v <= 20) {
                    return v + "% ";
                }
            }
        });
        $('#knob2').trigger('change');
    });

    <!-- know #3 -->

    jQuery(document).ready(function($) {


        $('#knob3').trigger('configure', {
            'draw': function(v) {
                v = parseInt(document.getElementById('knob3').value);
                //console.log(v);
                if (v > 80) {
                    this.o.fgColor = 'red';
                    $("#knob3 ").css("color ", "red ");
                    //this.o.inputColor='red';
                } else if (v > 60 && v <= 80) {
                    this.o.fgColor = '#FF863B';
                    $("#knob3 ").css("color ", "#FF863B ");
                    //this.o.inputColor='red';
                } else if (v > 40 && v <= 60) {
                    this.o.fgColor = '#ffe95e';
                    $("#knob3 ").css("color ", "#ffe95e ");
                    //this.o.inputColor='red';
                } else if (v > 20 && v <= 40) {
                    this.o.fgColor = '#0091FF';
                    $("#knob3 ").css("color ", "#0091FF ");
                    //this.o.inputColor='red';
                } else if (v <= 20) {
                    this.o.fgColor = '#3DDB94';
                    $("#knob3 ").css("color ", "#3DDB94 ");
                    //this.o.
                }
            },
            'format': function(v) {
                if (v > 80) {
                    return v + "% ";
                } else if (v > 60 && v <= 80) {
                    return v + "% ";
                } else if (v > 40 && v <= 60) {
                    return v + "% ";
                } else if (v > 20 && v <= 40) {
                    return v + "% ";
                } else if (v <= 20) {
                    return v + "% ";
                }
            }
        });
        $('#knob3').trigger('change');
    });

    jQuery(document).ready(function($) {
        $('#knob4').trigger('configure', {
            'draw': function(v) {
                v = parseInt(document.getElementById('knob4').value);
                //console.log(v);
                if (v > 80) {
                    this.o.fgColor = 'red';
                    $("#knob4 ").css("color ", "red ");
                    //this.o.inputColor='red';
                } else if (v > 60 && v <= 80) {
                    this.o.fgColor = '#FF863B';
                    $("#knob4 ").css("color ", "#FF863B ");
                    //this.o.inputColor='red';
                } else if (v > 40 && v <= 60) {
                    this.o.fgColor = '#ffe95e';
                    $("#knob4 ").css("color ", "#ffe95e ");
                    //this.o.inputColor='red';
                } else if (v > 20 && v <= 40) {
                    this.o.fgColor = '#0091FF';
                    $("#knob4 ").css("color ", "#0091FF ");
                    //this.o.inputColor='red';
                } else if (v <= 20) {
                    this.o.fgColor = '#3DDB94';
                    $("#knob4 ").css("color ", "#3DDB94 ");
                    //this.o.
                }
            },
            'format': function(v) {
                if (v > 80) {
                    return v + "% ";
                } else if (v > 60 && v <= 80) {
                    return v + "% ";
                } else if (v > 40 && v <= 60) {
                    return v + "% ";
                } else if (v > 20 && v <= 40) {
                    return v + "% ";
                } else if (v <= 20) {
                    return v + "% ";
                }
            }
        });
        $('#knob4').trigger('change');
    });
