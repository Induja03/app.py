<!doctype html>
<html lang="en">
<style type='text/css'>
    * {
        padding: 0;
        margin: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
        background-image: url('download.jpg')
        background-size: cover;
        font-family: sans-serif;
        margin-top: 40px;
        height: 100vh;
        padding: 0;
        margin: 0;
    }
    table {
        border: 1px;
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 86%;
        margin: auto;
    }
    td,
    th {
        border: 1px solid black !important;
        padding: 5px;
    }
    tr:nth-child(even) {
        background-color: #dddddd;
    }
</style>

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
    <title>Face Recognition Based Attendance System</title>
</head>
<body>
    <div class='mt-3 text-center'>
        <h1 style="width: auto;margin: auto;color: white;padding: 11px;font-size: 44px;">Face Recognition Based
            Attendance System</h1>
    </div>
    {% if mess%}
    <p class="text-center" style="color: red;font-size: 20px;">{{ mess }}</p>
    {% endif %}
    <div class="row text-center" style="padding: 20px;margin: 20px;">
        <div class="col"
            style="border-radius: 20px;padding: 0px;background-color:rgb(211,211,211,0.5);margin:0px 10px 10px 10px;min-height: 400px;">
            <h2 style="border-radius: 20px 20px 0px 0px;background-color: #0b4c61;color: white;padding: 10px;">Today's
                Attendance <i class="material-icons">assignment</i></h2>
            <a style="text-decoration: none;max-width: 300px;" href="/start">
                <button
                    style="font-size: 24px;font-weight: bold;border-radius: 10px;width:490px;padding: 10px;margin-top: 30px;margin-bottom: 30px;"
                    type='submit' class='btn btn-primary'>Take Attendance <i
                        class="material-icons">beenhere</i></button>
            </a>
            <table style="background-color: white;">
                <tr>
                    <td><b>S No</b></td>
                    <td><b>Name</b></td>
                    <td><b>ID</b></td>
                    <td><b>Time</b></td>
                </tr>
                {% if l %}
                {% for i in range(l) %}
                <tr>
                    <td>{{ i+1 }}</td>
                    <td>{{ names[i] }}</td>
                    <td>{{ rolls[i] }}</td>
                    <td>{{ times[i] }}</td>
                </tr>
                {% endfor %}
                {% endif %}
            </table>
        </div>
        <div class="col"
            style="border-radius: 20px;padding: 0px;background-color:rgb(211,211,211,0.5);margin:0px 10px 10px 10px;height: 400px;">
            <form action='/add' method="POST" enctype="multipart/form-data">
                <h2 style="border-radius: 20px 20px 0px 0px;background-color: #0b4c61;color: white;padding: 10px;">Add
                    New User <i class="material-icons">control_point_duplicate</i></h2>
                <label style="font-size: 20px;"><b>Enter New User Name*</b></label>
                <br>
                <input type="text" id="newusername" name='newusername'
                    style="font-size: 20px;margin-top:10px;margin-bottom:10px;" required>
                <br>
                <label style="font-size: 20px;"><b>Enter New User Id*</b></label>
                <br>
                <input type="number" id="newusereid" name='newuserid'
                    style="font-size: 20px;margin-top:10px;margin-bottom:10px;" required>
                <br>
                <button style="width: 232px;margin-top: 20px;font-size: 20px;" type='submit' class='btn btn-dark'>Add
                    New User
                </button>
                <br>
                <h5 style="padding: 25px;"><i>Total Users in Database: {{totalreg}}</i></h5>
            </form>
        </div>
    </div>

</body>
</html>
