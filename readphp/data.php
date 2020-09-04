<?php
error_reporting(E_ALL ^ E_DEPRECATED);
$con=mysql_connect("localhost","root","");

if(!$con)
{
    die('Could not connect: '.mysql_error());
}
mysql_select_db('novels',$con);
mysql_query("SET NAMES 'utf8'");
mysql_query("SET CHARACTER_SET_CLIENT=utf8");
mysql_query("SET CHARACTER_SET_RESULTS=utf8");



if (isset($_REQUEST["Action"]) && ! empty($_REQUEST["Action"])) {
    $action = $_REQUEST["Action"];
    switch ($action) {
        case "home":
//            select_home();
            introByName('牧神记');
            break;

        default:
            break;
    }
}
//function select_home(){
//    $arr['msg']='faild';
//    $arr['status']='faild';
//
//    $sql="SELECT * FROM novels_home WHERE area='home' order by idx";
//    $res=mysql_query($sql);
//
//    if (mysql_num_rows($res)) {
//        $n = 0;
//        while ($data = mysql_fetch_array($res)) {
//            $arr["res"][$n]["area"] = $data['area'];
//            $arr["res"][$n]["idx"] = $n+1;
//            $intros= introByName($data['name']);
//
//            $arr["res"][$n]["intro"] = $intros['intro'];
//            $arr["res"][$n]["headimg"] = $intros['headimg'];
//            $arr["res"][$n]["author"] = $intros['author'];
//            $n ++;
//        }
//    }
//    $arr["status"] = 'success';
//    $arr["msg"] = 'success';
//
//    echo json_encode($arr);
//
//}
//根据name 找到intro 等详情内容
function introByName($name){
    $sql="SELECT * FROM novels_intro WHERE name=$name";
    $res=mysql_query($sql);
    $rowsnum=mysql_num_rows($res);
    $arr=[];
    if ($rowsnum > 0) {
        $data = mysql_fetch_array($res);
        $arr['intro']=$data['intro'];
        $arr['headimg']=$data['headimg'];
        $arr['author']=$data['author'];
        $arr['utime']=$data['utime'];
    }

    echo json_encode($arr);
}







?>