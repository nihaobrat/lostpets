<?php
// Подключаемся к базе данных
$servername = "localhost";
$username = "ваше_имя_пользователя_базы_данных";
$password = "ваш_пароль_пользователя_базы_данных";
$dbname = "название_вашей_базы_данных";

$conn = mysqli_connect($servername, $username, $password, $dbname);
// Проверяем успешность подключения
if (!$conn) {
    die("Ошибка подключения: " . mysqli_connect_error());
}

// Получаем значение message из запроса
$message = mysqli_real_escape_string($conn, $_POST['message']);

// Добавляем сообщение в таблицу сообщений
$sql = "INSERT INTO messages (message) VALUES ('$message')";

if (mysqli_query($conn, $sql)) {
    // Возвращаем статус "Успешно" и сохраненное сообщение
    $response = array("status" => "success", "message" => $message);
    echo json_encode($response);
} else {
    // Возвращаем статус "Ошибка" и сообщение об ошибке базы данных
    $response = array("status" => "error", "message" => mysqli_error($conn));
    echo json_encode($response);
}

mysqli_close($conn);
?>
