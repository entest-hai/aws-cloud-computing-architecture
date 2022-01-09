<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    * {
      box-sizing: border-box;
      margin-top: 0;
    }

    h1 {
      font-size: 5rem;
    }

    label {
      font-size: 1.5rem;
      display: inline-block;
      width: 200px;
    }

    p {
      font-size: 1.5rem;
    }

    input {
      font-size: 1.5rem;
      padding: 0.2rem;
    }
  </style>
</head>

<body>
  <div>
    <h1>
      Photo uploader
    </h1>
    <p font-size: 1.5rem;">
      Student ID: 123456
    </p>
    <p font-size: 1.5rem;">
      Name: Tran Minh Hai
    </p>
    <div style="
      border-style: solid;
      border-width: 0.2rem;
      padding: 3rem 1rem;
      ">
      <form action="handle.php" method="POST" enctype="multipart/form-data">
        <label for="title">Photo title</label>
        <input type="text" id="title" name="title"> <br><br>
        <label>Select a photo</label>
        <input type="file" id="photo" name="photo"> <br><br>
        <label for="description">Description</label>
        <input type="text" id="description" name="description"> <br><br>
        <label for="date">Date</label>
        <input type="text" id="date" name="date"> <br><br>
        <p>Keywords (separated by semicolon, e.g. keyword1; keyword2; etc.)</p>
        <input type="text" id="keywords" name="keywords"> <br><br>
        <button style="font-size: 1.5rem;" type="submit">
          Upload
        </button>
      </form>
    </div>
    <div style="height: 2rem;"></div>
    <a href="/cos20019/photoalbum/getphotos.php" style="
      font-size: 1.5rem;
      padding-top: 2rem;
      ">
      Photo Album
    </a>
  </div>
</body>

</html>
