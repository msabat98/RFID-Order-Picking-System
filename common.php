<?php
//Include medoo which is  utilized for interacting with the database
require 'Medoo.php';

//Now use Medoo's namespace
use Medoo\Medoo;

$database = new Medoo([
    'database_type' => 'mysql',
    'database_name' => 'orderpickingdb',
    'server'        => 'localhost',
    'username'      => 'picker',
    'password'      => 'pi'
]);
