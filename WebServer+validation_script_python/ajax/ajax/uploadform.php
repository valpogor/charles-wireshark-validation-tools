

    <?php
    //uploadfile.php
    $tmpImageFolder = $_SERVER['DOCUMENT_ROOT'].'/assets/images/tmp';
    //$actualFileName = $_FILES['file']['name'];
    $ext = strtolower(pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION));
    //new filename based on time
    $newFileName = microtime(true).'.'.$ext;
    //retrieve uploaded file path (temporary stored by php engine)
    $source = $_FILES['file']['tmp_name'];
    $dest = $tmpImageFolder.'/'.$newFileName;
    //move uploaded file to tmp
    move_uploaded_file($source,$dest);
    //you can scale the image here with your own image functions e.g.
    //$i = new Image();
    //$i->scaleImage($dest,$dest);
    //display the new file name to be used by js/ajax success function
    echo json_encode($newFileName);
    ?>

