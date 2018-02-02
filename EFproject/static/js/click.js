var alist = [];
Array.prototype.contains = function (v) {
    for (var i = 0; i < this.length; i++) {
        if (this[i] === v) return true;
    }
    return false;
};


if (!Array.prototype.indexOf) {
    Array.prototype.indexOf = function (searchElement /*, fromIndex */) {
        "use strict";
        if (this == null) {
            throw new TypeError();
        }
        var t = Object(this);
        var len = t.length >>> 0;
        if (len === 0) {
            return -1;
        }
        var n = 0;
        if (arguments.length > 0) {
            n = Number(arguments[1]);
            if (n != n) { // shortcut for verifying if it's NaN
                n = 0;
            } else if (n != 0 && n != Infinity && n != -Infinity) {
                n = (n > 0 || -1) * Math.floor(Math.abs(n));
            }
        }
        if (n >= len) {
            return -1;
        }
        var k = n >= 0 ? n : Math.max(len - Math.abs(n), 0);
        for (; k < len; k++) {
            if (k in t && t[k] === searchElement) {
                return k;
            }
        }
        return -1;
    }
}


Array.prototype.remove = function () {
    var what, a = arguments,
        L = a.length,
        ax;
    while (L && this.length) {
        what = a[--L];
        while ((ax = this.indexOf(what)) !== -1) {
            this.splice(ax, 1);
        }
    }
    return this;
};

Array.prototype.unique = function () {
    var arr = [];
    for (var i = 0; i < this.length; i++) {
        if (!arr.contains(this[i])) {
            arr.push(this[i]);
        }
    }
    return arr;
}


function clickRefresh(id) {


};


function clickBtn(id) {
    var titleList = ["1.Characteristics of the child's disability", "2.Characteristics of the family", "3.Availability of FSCD Resources and Information", "4.Level and intensity of FSCD approved services", "5.Other groups /programs / parties involved"];
    var d = document.getElementById(id);
    var num = id.match(/\d+/)[0];
    console.log(num - 1);
    var title = document.getElementById("title");
    document.getElementById("title").innerHTML = titleList[num - 1];
    document.getElementById("title").style.color = "black";


    for (var i = 0; i < alist.length; i++) {
        console.log(alist[i].match(/\d+/)[0]);
        if (alist[i].match(/\d+/)[0] == num) {
            alist.remove(alist[i]);
        }
    }
    alist.push(id);
    alist = alist.unique();

    //clear the background color
    var l = document.getElementById("low" + num);
    var a = document.getElementById("avg" + num);
    var h = document.getElementById("high" + num);
    var ll = document.getElementById("lowB" + num);
    var aa = document.getElementById("avgB" + num);
    var hh = document.getElementById("highB" + num);


    $(document).ready(function () {
        $("#low" + num).hover(function () {
            $(this).css("background-color", "#50F527");
        }, function () {
            if (alist.contains("lowB" + num) == true) {

                $(this).css("background-color", "#50F527");
            } else {
                if (num % 2 == 1) {
                    $(this).css("background-color", "#0f2b6d");
                } else {
                    $(this).css("background-color", "#0f2b6d");
                }
            }
        });
    });


    $(document).ready(function () {
        $("rBtn").hover(function () {
            $(this).css("background-color", "#fff842");
        }, function () {
            if (alist.contains("avgB" + num) == true) {
                console.log("green");
                $(this).css("background-color", "#fff842");
            } else {
                if (num % 2 == 1) {
                    $(this).css("background-color", "#0f2b6d");
                } else {
                    $(this).css("background-color", "#0f2b6d");
                }
            }
        });
    });


    $(document).ready(function () {
        $("#avg" + num).hover(function () {
            $(this).css("background-color", "#fff842");
        }, function () {
            if (alist.contains("avgB" + num) == true) {
                console.log("green");
                $(this).css("background-color", "#fff842");
            } else {
                if (num % 2 == 1) {
                    $(this).css("background-color", "#0f2b6d");
                } else {
                    $(this).css("background-color", "#0f2b6d");
                }
            }
        });
    });

    $(document).ready(function () {
        $("#high" + num).hover(function () {
            $(this).css("background-color", "#F56527");
        }, function () {
            if (alist.contains("highB" + num) == true) {
                console.log("green");
                $(this).css("background-color", "#f56527");
            } else {
                if (num % 2 == 1) {
                    $(this).css("background-color", "#0f2b6d");
                } else {
                    $(this).css("background-color", "#0f2b6d");
                }
            }
        });
    });


    if (num % 2 == 1) {

        l.style.backgroundColor = '#0f2b6d';
        a.style.backgroundColor = '#0f2b6d';
        h.style.backgroundColor = '#0f2b6d';
        ll.style.color = '#a7a1ae';
        aa.style.color = '#a7a1ae';
        hh.style.color = '#a7a1ae';
    } else {
        if (num != -1) {
            l.style.backgroundColor = '#0f2b6d';
            a.style.backgroundColor = '#0f2b6d';
            h.style.backgroundColor = '#0f2b6d';
            ll.style.color = '#a7a1ae';
            aa.style.color = '#a7a1ae';
            hh.style.color = '#a7a1ae';
        } else {

            l.style.backgroundColor = '#0f2b6d';
            h.style.backgroundColor = '#0f2b6d';
            ll.style.color = '#a7a1ae';
            hh.style.color = '#a7a1ae';
        }

    }


    if (id[0] == 'l') {
        var p = document.getElementById(id).parentElement;
        p.style.backgroundColor = '#50F527';
        d.style.color = "black";


    } else if (id[0] == 'a') {
        var p = document.getElementById(id).parentElement;
        p.style.backgroundColor = '#FFF842';
        d.style.color = "black";

    } else if (id[0] == 'h') {
        var p = document.getElementById(id).parentElement;
        p.style.backgroundColor = '#F56527';
        d.style.color = "black";

    }
    console.log(alist);

    //var score = document.getElementById(score);
    var c = 0;
    var total = 0;
    for (c = 0; c < alist.length; c++) {
        if (alist[c][0] == 'l') {
            var number = alist[c].match(/\d+/)[0];
            if (number == 1) {
                total = total + 0.15 * 1
            } else if (number == 2) {
                total = total + 0.10 * 1
            } else if (number == 3) {
                total = total + 0.25 * 1
            } else if (number == 4) {
                total = total + 0.20 * 1
            } else if (number == 5) {
                total = total + 0.15 * 1
            } else if (number == 6) {
                total = total + 0.15 * 1
            }
        } else if (alist[c][0] == 'a') {
            var number = alist[c].match(/\d+/)[0];
            if (number == 1) {
                total = total + 0.15 * 2
            } else if (number == 2) {
                total = total + 0.10 * 2
            } else if (number == 3) {
                total = total + 0.25 * 2
            } else if (number == 4) {
                total = total + 0.20 * 2
            } else if (number == 5) {
                total = total + 0.15 * 2
            } else if (number == 6) {
                total = total + 0.15 * 2
            }
        } else if (alist[c][0] == 'h') {
            var number = alist[c].match(/\d+/)[0];
            if (number == 1) {
                total = total + 0.15 * 3
            } else if (number == 2) {
                total = total + 0.10 * 3
            } else if (number == 3) {
                total = total + 0.25 * 3
            } else if (number == 4) {
                total = total + 0.20 * 3
            } else if (number == 5) {
                total = total + 0.15 * 3
            } else if (number == 6) {
                total = total + 0.15 * 3
            }
        }

    }
    total = total.toFixed(2)
    console.log(total);
    //document.getElementById("score").innerHTML = total;

    var rate = document.getElementById("rate");
    var rateH = document.getElementById("rateH");

    if (total <= 1.2) {
        rate.innerHTML = "Low"
        rate.style.color = "black";
        rateH.style.backgroundColor = "#50f527";
    } else if (total > 1.20 && total < 2.4) {
        rate.innerHTML = "Average"
        rate.style.color = "black";
        rateH.style.backgroundColor = "#fff842";
    } else if (total >= 2.4) {
        rate.innerHTML = "High"
        rate.style.color = "black";
        rateH.style.backgroundColor = "#f56527";
    }
}

// $('#low1').hover(
//     function(){
//         $('#d1').text('Reply!');
//     },
//     function(){
//         $.ajax({


//             success: function(){
//                 $('#d1').text("test");
//             }
//         });
//     }
// );

// first row
$(document).ready(function () {
    row1 = "1. Characteristics of the child's disability";
    $("#low1").mouseenter(function () {
        $('#d1').css("text-align", "left");
        row1 = "1. Characteristics of the child's disability";
        document.getElementById("t1").innerHTML = (row1 + ": low");
        document.getElementById("d1").innerHTML = ("<br><br>a.Unemployed <br> b.Urban <br >b.Single <br >c.Longterm housing <br>d.English speaking");
        // $('#d1').css("font-size", 14 + "px");

    });
    $("#low1").mouseleave(function () {
        $("#d1").text("");
        $("#t1").text("Description");
    });

});

$(document).ready(function () {
    $("#avg1").mouseenter(function () {
        $('#d1').css("text-align", "left");

        document.getElementById("t1").innerHTML = (row1 + ": Average");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br><br>a.Employed or attending school<br> b.Residing in shelter consistently<br> c.Housed in an urban or rural area with access to government agencies and community supports<br> d. Can communicate in English or has an interpreter <br> e.Single or steady cohabiting partner";
    });
    $("#avg1").mouseleave(function () {

        $("#d1").text("");
        $("#t1").text("Description");
        // $('#d1').css("font-size", 10 + "px");
    });

});

$(document).ready(function () {
    $("#high1").mouseenter(function () {
        $('#d1').css("text-align", "left");
        document.getElementById("t1").innerHTML = (row1 + ": High");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Unable to maintain employment or follow through with school expectations.<br>b. Transient or frequent changes in shelter<br>c.  Frequent unstable cohabiting relationships<br>d.  Cannot communicate in English and interpreter not available<br>e. Rural residency with no access to community supports or government agencies <br>f.  Family relationships, friend and social networks<br>- Difficult to track AISH benefits due to family structure or cultural reasons.<br>-  Domestic discord"
    });
    $("#high1").mouseleave(function () {
        $("#d1").text("");
        $("#t1").text("Description");

    });

});


// #2 row
$(document).ready(function () {
    $("#low2").mouseenter(function () {
        $('#d1').css("text-align", "left");
        document.getElementById("d1").innerHTML = ("<br>a.  All information supplied e.g. AB Supports compiles application information<br>b.  Documents submitted on time and as needed – usually quick response – client submits when requested<br>c.  Usually only updated information needed e.g. financials<br>");
        // $('#d1').css("font-size", 14 + "px");

    });
    $("#low2").mouseleave(function () {
        $("#d1").text("");
    });

});

$(document).ready(function () {
    $("#avg2").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Missing critical information initially but client submits when requested e.g. CRA not done but T5 slips provided in lieu<br>b.  Submits documents as requested<br>c.  Regular reporting<br>";
    });
    $("#avg2").mouseleave(function () {
        $("#d1").text("");
        // $('#d1').css("font-size", 10 + "px");
    });

});

$(document).ready(function () {
    $("#high2").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Missing critical information needed to determine eligibility (initial and ongoing) – income, assets, residence, age<br>b. Slow response from client – requires multiple requests for reasons that are in client’s control or not due to systemic factors<br>c.  Documents do not exist or are not available e.g. no ID or bank records<br>";
    });
    $("#high2").mouseleave(function () {
        $("#d1").text("");

    });

});


// #3 row
$(document).ready(function () {
    $("#low3").mouseenter(function () {
        $('#d1').css("text-align", "left");
        document.getElementById("d1").innerHTML = ("<br>a.  Primarily physical disability<br>b. Cognitive ability to fully understand process and policy.<br>c. Ability to follow through and be accountable<br>d.  Client in LTC<br>e. Financial Administrator<br>f. Community capacity<br> ");
        // $('#d1').css("font-size", 14 + "px");

    });
    $("#low3").mouseleave(function () {
        $("#d1").text("");
    });

});

$(document).ready(function () {
    $("#avg3").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Multiple diagnosis<br>b.  Primarily mental health issues<br>c.  Some capacity to make decisions<br>d. Limited understanding of rules due to lower IQ - disability based<br>e. Some ability to understand accountability<br>f. able to read and/ or write at grade level";
    });
    $("#avg3").mouseleave(function () {
        $("#d1").text("");
        // $('#d1').css("font-size", 10 + "px");
    });

});

$(document).ready(function () {
    $("#high3").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Multiple diagnosis (more than 2)<br>b.  Mental health issues not medicated or undiagnosed<br>c. Primarily mental health<br>d. Lack of ability to make decisions <br>e.  Low IQ, FASD, reoffenders (often in jail), chronic pain <br>f.  Paranoid <br>g. Violent behaviour<br>h. Addictions and transients<br>i. Lack of social skills<br>J. unable to read or write at grade level";
    });
    $("#high3").mouseleave(function () {
        $("#d1").text("");

    });

});


// #4 row
$(document).ready(function () {
    $("#low4").mouseenter(function () {
        $('#d1').css("text-align", "left");
        document.getElementById("d1").innerHTML = ("<br>a.  No Assets<br>b. No income<br>c. OPT client<br>d.  In LTC<br>e.  3rd party payments<br>f.  Financial Administrator<br>");
        // $('#d1').css("font-size", 14 + "px");

    });
    $("#low4").mouseleave(function () {
        $("#d1").text("");
    });

});

$(document).ready(function () {
    $("#avg4").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. 1-2 income types<br>b.  Assets below $3000 or steady if above<br>c. Assets not easily accessible (e.g. RRSP vs. TFSA)<br>";
    });
    $("#avg4").mouseleave(function () {
        $("#d1").text("");
        // $('#d1').css("font-size", 10 + "px");
    });

});

$(document).ready(function () {
    $("#high4").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Multiple bank accounts<br>b.  More than 2 types of income, spousal(OAS/GIS/ASB/CPP/Employment)<br>c.  Multiple or changing assets<br>d. Assets approaching $100k<br>e.  Around $3000 PB request limit<br>f. Complex assets i.e. farm, business, trusts, colonies<br>g.  Assets outside Canada<br>h. Hardship Exemption<br>";
    });
    $("#high4").mouseleave(function () {
        $("#d1").text("");

    });

});


// #5 row
$(document).ready(function () {
    $("#low5").mouseenter(function () {
        $('#d1').css("text-align", "left");
        document.getElementById("d1").innerHTML = ("<br>a.  Willingly cooperates and works with the system<br>b.  Respects established rules and regulations<br>c.  No prompting needed<br>d. Regular and appropriate check-in with life changes and financial information<br>e.  Income Support files<br>f. maintains good relationship with AISH worker");
        // $('#d1').css("font-size", 14 + "px");

    });
    $("#low5").mouseleave(function () {
        $("#d1").text("");
    });

});

$(document).ready(function () {
    $("#avg5").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Contacts regarding changes only when they happen<br>b.  Chooses to respond when requested<br>c. Follows instructions most of the times<br>d.  Mostly respectful of rules and requirements<br>e. maintains good relationship with AISH worker most of the time";
    });
    $("#avg5").mouseleave(function () {
        $("#d1").text("");
        // $('#d1').css("font-size", 10 + "px");
    });

});

$(document).ready(function () {
    $("#high5").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Intentional misrepresetation of personal or financial information<br>b. May be fraud related AISH for out of scope reasons<br>c.  Can be confrontational<br>d.  No contacts even with prompts<br>e. Frequent prompting required";
    });
    $("#high5").mouseleave(function () {
        $("#d1").text("");

    });

});


// #6 row
$(document).ready(function () {
    $("#low6").mouseenter(function () {
        $('#d1').css("text-align", "left");
        document.getElementById("d1").innerHTML = ("a.  Good participation and support from involved professionals e.g. lawyers, health professionals<br>b. Good OPGT support – information on TOI<br>c.  Good Financial Administrator – good accounting and records, no overcharging<br>d. AISH Benefit Administration Program<br>e. Supportive family, involved and helpful<br>f. Community agency/ Outreach, help with compliance<br>g.  Supportive and collaborative social worker<br>");
        // $('#d1').css("font-size", 14 + "px");

    });
    $("#low6").mouseleave(function () {
        $("#d1").text("");
    });

});

$(document).ready(function () {
    $("#avg6").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Access to appropriate supports.<br>b. Third party resources are available and supportive<br>c.  Reasonable number of third parties involved <br>";
    });
    $("#avg6").mouseleave(function () {
        $("#d1").text("");
        // $('#d1').css("font-size", 10 + "px");
    });

});

$(document).ready(function () {
    $("#high6").mouseenter(function () {
        $('#d1').css("text-align", "left");
        // $("#d1").html("a.Employed or attending school<br> ·Residing in shelter consistently \n b.Residing in shelter consistently\n c.Housed in an urban or rural area with access to government agencies and community supports\n d. Can communicate in English or has an interpreter\n e.Single or steady cohabiting partner");
        document.getElementById("d1").innerHTML = "<br>a. Non cooperative, non-compliant or unprofessional conduct from third parties e.g. doctor, lawyer, social worker, FA, Private Guardian<br>b.  Family and parties confrontational, question decisions<br>c.  Poor family and community supports<br>d.  Non guardian family <br>e.  Risk of fraud or wrong doing<br>f.  High Volume of contact required with program<br>g.  Advocacy, lobbying<br>h.  Political or media involvement<br>i.  Difficulty determining relationship. E.g. relationship of interdependence<br>";
    });
    $("#high6").mouseleave(function () {
        $("#d1").text("");

    });

});


$(function ($) {


    $(".knob").knob({
        change: function (value) {
            //console.log("change : " + value);
            if (this.val() > 20) {
                console.log(this.val() + "vvvv");
                dialColour = '#000000';
                var k = document.getElementById("knob");
                k.setAttribute('data-fgcolor', '#000000')
                var r = result()
                document.getElementById("knob").setAttribute("fgcolor", "red");

            }
        },
        release: function (value) {
            //console.log(this.$.attr('value'));
            console.log("release : " + value);
            var r = result()
            // document.getElementById("test").innerHTML = "Case Intensity Rating:    " + r;
            // document.getElementById("r1").innerHTML = "High";
            // document.getElementById("r1").style.color = "";
            // document.getElementById("knob").setAttribute("fgcolor", "red");

        },
        cancel: function () {
            console.log("cancel : ", this);
        },

    });

});


function result() {
    var v1 = parseInt(document.getElementById('knob').value);
    var v2 = parseInt(document.getElementById('knob2').value);
    var v3 = parseInt(document.getElementById('knob3').value);
    var v4 = parseInt(document.getElementById('knob4').value);
    var v5 = parseInt(document.getElementById('knob5').value);
    var v6 = parseInt(document.getElementById('knob6').value);
    if (isNaN(v1) == true) {
        v1 = 0
    }

    if (isNaN(v2) == true) {
        v2 = 0
    }

    if (isNaN(v3) == true) {
        v3 = 0
    }

    if (isNaN(v4) == true) {
        v4 = 0
    }
    if (isNaN(v5) == true) {
        v5 = 0
    }
    if (isNaN(v6) == true) {
        v6 = 0
    }


    var totle = v1 * 0.35 + v2 * 0.15 + v3 * 0.15 + v4 * 0.05 + v5 * 0.15 + v6 * 0.15;
    console.log(v1, v2, v3, v4);
    console.log(totle);
    if (totle < 20) {
        creatResult(totle);
        return "Low";
    } else if (totle >= 20 && totle < 80) {
        creatResult(totle);
        return "Average";
    } else if (totle >= 80) {
        creatResult(totle);
        return "High";
    }
}


function creatResult(num) {

    if (num > 80) {
        CanvasJS.addColorSet("greenShades", [ //colorSet Array
            "red", // high

            "#d6d6d6", //low
            "#c2c6ce", // ave
        ]);
    } else if (num < 80 && num >= 20) {
        CanvasJS.addColorSet("greenShades", [ //colorSet Array
            "#c2c6ce", // high

            "#d6d6d6", //low
            "yellow", // ave
        ]);
    } else if (num < 20) {
        CanvasJS.addColorSet("greenShades", [ //colorSet Array
            "#c2c6ce", // high

            "#3DDB94", //low
            "#d6d6d6", // ave
        ]);
    }

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
                {label: "low", y: 33},
                {label: "average", y: 33},
                {label: "high", y: 33}

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

        dataPoints.splice(0, 0, {y: sum, color: "transparent", toolTipContent: null});
    }


}

