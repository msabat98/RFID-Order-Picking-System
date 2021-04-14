<?php
require 'common.php';
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Order Picking</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <script src="js/bootstrap.min.js"></script>
    </head>
    <body>

    <nav class="navbar navbar-dark bg-dark">
        <a class="navbar-brand" href="index.php">Order Picking System</a>
        <ul class="nav nav-pills">
            <li class="nav-item">
                <a href="itemss.php" class="nav-link active">View Items</a>
            </li>
        </ul>
    </nav>
    <div class="container">
        <div class="col-md-6 order-md-1 text-center text-md-left pr-md-5">
            <h1 class="mb-3">Welcome to the Order Picking system</h1>
            <p1>View Items stored in the warehouse</p1>
            <div class="row mx-n2">
                <div class="col-md px-2">
                    <a href="items.php" class="btn btn-lg btn-outline-secondary w-100 mb-3">Items</a>
                </div>
           
            </div>
        </div>
    </div>
</html>
