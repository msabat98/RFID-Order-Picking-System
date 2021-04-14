<?php
require 'common.php';

//Grab all the items  from our database of order items
$items = $database->select("items", [
    'id',
    'name',
    'rfid_uid',
    'location',
    'created',
   
  

]);

?>
<!DOCTYPE html>
//front end webpage for displaying order data
<html lang="en">
    <head>
        <title>Order Picking System</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=2">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <script src="js/bootstrap.min.js"></script>
    </head>
    <body>



    <nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="index.php">Order Picking System</a>
        <ul class="nav nav-pills">
            <li class="nav-item">
                <a href="items.php" class="nav-link active">Items</a>
            </li>
        </ul>
    </nav>


    <div class="container">
        <div class="row">
            <h2>Order Items</h2>
        </div>
        <table class="table table-striped">
            <thead class="thead-dark">
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Name</th>
                    <th scope="col">RFID UID</th>
                    <th scope="col">Location</th>
                    <th scope="col">Log Time</th>
                </tr>
            </thead>
            <tbody>
                <?php
                //Loop through and list all the information of each user including their RFID UID
      
                foreach($items as $item) {
                    echo '<tr>';
                    echo '<td scope="row">' . $item['id'] . '</td>';
                    echo '<td>' . $item['name'] . '</td>';
                    echo '<td>' . $item['rfid_uid'] . '</td>';
                    echo '<td>' . $item['location'] . '</td>';
                    echo '<td>' . $item['created'] . '</td>';
                    echo '</tr>';
}
                ?>
            </tbody>
        </table>
    </div>
</html>


