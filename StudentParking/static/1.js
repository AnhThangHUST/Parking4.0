function dkvcsvCheckbox() {
    var checkBox = document.getElementById("checkboxDkvcsv");
    if (checkBox.checked == true){
        $("#dkvcsvForm").append("<div class=\"form-group\" id=\"startDateDkvcsvForm\"><label>Start Date</label><input type=\"text\" class=\"form-control\" id=\"startDateDkvcsv\"></div><div class=\"form-group\" id=\"experationDateDkvcsvForm\"><label>Experation Date</label><input type=\"text\" class=\"form-control\" id=\"experationDateDkvcsv\"></div>");
    } else {
        document.getElementById("startDateDkvcsvForm").remove();
        document.getElementById("experationDateDkvcsvForm").remove();
    }
}

function dkvtCheckbox() {
    var checkBox = document.getElementById("checkboxDkvt");
    if (checkBox.checked == true){
        $("#dkvtForm").append("<div class=\"form-group\" id=\"startDateDkvtForm\"><label>Start Date</label><input type=\"text\" class=\"form-control\" id=\"startDateDkvt\"></div><div class=\"form-group\" id=\"experationDateDkvtForm\"><label>Experation Date</label><input type=\"text\" class=\"form-control\" id=\"experationDateDkvt\"></div>");
    } else {
        document.getElementById("startDateDkvtForm").remove();
        document.getElementById("experationDateDkvtForm").remove();
    }
}

// get value input
function getDkvcsvValue() {

    var checkBox = document.getElementById("checkboxDkvcsv");
    var student = {"name": $("#nameDkvcsv").val(), "studentID": $("#stuentIDDkvcsv").val(), "faculty": $("#facultyDkvcsv").val(), "birthday": $("#birthdayDkvcsv").val(), "vehicle": $("#vehicleDkvcsv").val(), "kindOfTicket": checkBox.checked, "startDate": $("#startDateDkvcsv").val(), "expirationDate": $("#expirationDateDkvcsv").val()}
    console.log("create post is working!");
    console.log(checkBox.checked);
}

$(document).ready(function(){
    $("#submitGx").click(function(){
        var json ={"student": $("#studentIDGx").val(), "numberPlate": $("#vihicleGx").val()};
        $.ajax({
            url: "/ParkingManagement/VehicleIn/",
            type: "post", // or "get"
            data: json,
            success: function(data) {
              alert(data);
            }
        });
    });
});
