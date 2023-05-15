
<?php

// Подключение к базе данных
$servername = "localhost";
$username = "postgres";
$password = "2110";
$dbname = "lostp";

$conn = new mysqli($servername, $username, $password, $dbname);

// Проверка соединения
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Проверка логина и пароля при отправке формы

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT id FROM users WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Перенаправление на следующую страницу при успешной авторизации
        header("Location: createprofile.html");
        exit();
    } else {
        // Вывод сообщения об ошибке при неправильном логине или пароле
        echo "Неверный логин или пароль";
    }
}

// Закрытие соединения с базой данных
$conn->close();

?>
