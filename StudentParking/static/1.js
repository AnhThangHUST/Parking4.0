function dkvcsvCheckbox() {
    var checkBox = document.getElementById("checkboxDkvcsv");
    if (checkBox.checked == true){
        $("#dkvcsvForm").append("<div class=\"form-group\" id=\"startDateDkvcsvForm\"><label>Ngay dang ky</label><input type=\"text\" class=\"form-control\" id=\"startDateDkvcsv\"></div><div class=\"form-group\" id=\"experationDateDkvcsvForm\"><label>Ngay het han</label><input type=\"text\" class=\"form-control\" id=\"experationDateDkvcsv\"></div>");
    } else {
        document.getElementById("startDateDkvcsvForm").remove();
        document.getElementById("experationDateDkvcsvForm").remove();
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
        var json = {"student": $("#studentIDGx").val(), "numberPlate": $("#vehicleGx").val()};
        console.log(json);

        $.ajax({
            url: "/ParkingManagement/VehicleIn/",
            type: "post", // or "get"
            data: json,
            success: function(data) {
              //alert(data);
                console.log(data);
                alert("Gui xe thanh cong");
            }
        });
    });
});

$(document).ready(function(){
    $("#submitLx").click(function(){
        var json = {"student": $("#studentIDLx").val(), "numberPlate": $("#vehicleLx").val()};
        console.log(json);

        $.ajax({
            url: "/ParkingManagement/VehicleOut/",
            type: "post", // or "get"
            data: json,
            success: function(data) {
              //alert(data);
                console.log(data);
                alert("Lay xe thanh cong");
            }
        });
    });
});


$(document).ready(function(){
    $("#submitDkvcsv").click(function(){
        var checkBox = document.getElementById("checkboxDkvcsv");
        var json = {"name": $("#nameDkvcsv").val(), "studentID": $("#studentIDDkvcsv").val(), "faculty": $("#facultyDkvcsv").val(), "birthday": $("#birthdayDkvcsv").val(), "vehicle": $("#vehicleDkvcsv").val(), "kindOfTicket": checkBox.checked, "startDate": $("#startDateDkvcsv").val(), "expirationDate": $("#expirationDateDkvcsv").val()};
        console.log(json);

        $.ajax({
            url: "/ParkingManagement/Student/",
            type: "post", // or "get"
            data: json,
            success: function(data) {
              //alert(data);
                console.log(data);
                alert("Dang ky thanh cong");
            }
        });
    });
});


$(document).ready(function(){
    $(document).on("click", "#tab4", function(){
        $.ajax({
            type: "get",
            url: "/ParkingManagement/Student/",
            dataType: "json",
            success: function(data){
                $(".rowTable").remove();
                var trHTML = '';
                $.each(data, function (i, item) {
                    trHTML += '<tr class="rowTable" style="background-color: #55d0ff; color: white;"><td>' + item.studentID + '</td><td>' + item.name + '</td><td>' + item.faculty + '</td><td>' + item.birthday + '</td> <td>' + item.vehicle + '</td> <td>' + item.kindOfTicket + '</td><td>' + item.startDate + '</td><td>' + item.expirationDate + '</td></tr>';
                });
                $('#tttcsvTable').append(trHTML);
            },
            error: function(){
                alert("error");
            }
        });
    });
});

$(document).ready(function(){
    $("#submitDkvt").click(function(){
        var json = {"studentID": $("#studentIDDkvt").val(), "startDate": $("#startDateDkvt").val(), "expirationDate": $("#experationDateDkvt").val()};
        $.ajax({
            url: "/ParkingManagement/RegisterMonthlyTicket/",
            type: "post", // or "get"
            data: json,
            success: function(data) {
              //alert(data);
                console.log(data);
                alert(data);
            }
        });
    });
});

$(document).ready(function(){
    $("#submitTdtt").click(function(){
        var json = {"studentID": $("#studentIDTdtt").val(), "name": $("#nameTdtt").val(), "faculty": $("#facultyTdtt").val(), "birthday": $("#birthdayTdtt").val(), "vehicle": $("#vehicleTdtt").val(),};
        url = "/ParkingManagement/Student/" + json["studentID"] + "/";
        console.log(json);
        $.ajax({
            url: url,
            type: "put",
            data: json,
            success: function(data) {
              //alert(data);
                alert("data");
            }
        });
    });
});

