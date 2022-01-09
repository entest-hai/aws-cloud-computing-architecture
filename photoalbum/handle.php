<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      p {
          font-size: 1.0rem; 
        }
    </style>
</head>

<body>
  <div>
    <p>
    <?php
        $target_dir = "uploads/";
        $target_file = $target_dir . basename($_FILES["photo"]["name"]);
        $uploadOk = 1;
        $imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
        // Check if image file is a actual image or fake image
        if(isset($_POST["submit"])) {
          $check = getimagesize($_FILES["photo"]["tmp_name"]);
          if($check !== false) {
              echo "File is an image - " . $check["mime"] . ".";
              $uploadOk = 1;
          } else {
              echo "File is not an image.";
              $uploadOk = 0;
            }
        }
        // Check if $uploadOk is set to 0 by an error
        if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
        // if everything is ok, try to upload file
        } else {
          if (move_uploaded_file($_FILES["photo"]["tmp_name"], $target_file)) {
              echo "The file ". htmlspecialchars( basename( $_FILES["photo"]["name"])). " has been uploaded.";
          } else {
              echo "Sorry, there was an error uploading your file.";
          }
       }
    ?>
    </p>
    <p>
      Photo title:  <?php echo $_POST["title"]; ?>
    </p>
    <p>
      Description: <?php echo $_POST["description"]; ?>
    </p>
    <p>
      Date: <?php echo $_POST["date"]; ?>
    </p>
    <p>
      Keywords: <?php echo $_POST["keywords"]; ?>
    </p>
    <p>
    Photo: <?php echo "./uploads/" . basename($_FILES["photo"]["name"]); ?>
    </p>
   <?php
     $target_file = "uploads/" . basename($_FILES["photo"]["name"]);	
     echo '<img src="'.$target_file.'">';
   ?>
  </div>
</body>
</html>

