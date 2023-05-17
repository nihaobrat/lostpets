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

// Получаем все сообщения из базы данных
$sql = "SELECT * FROM messages ORDER BY id ASC";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // Проходимся по каждому сообщению и добавляем его в массив
    $messages = array();
    while($row = mysqli_fetch_assoc($result)) {
        array_push($messages, $row["message"]);
    }
    // Возвращаем массив сообщений в JSON-формате
    $response = array("status" => "success", "messages" => $messages);
    echo json_encode($response);
} else {
    // Если нет сообщений, то возвращаем пустой массив
    $response = array("status" => "success", "messages" => array());
    echo json_encode($response);
}

mysqli_close($conn);
?>
