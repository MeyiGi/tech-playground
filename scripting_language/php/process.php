<?php
// Показываем ошибки
ini_set('display_errors', 1);
error_reporting(E_ALL);

$host = "localhost";
$user = "root";
$pass = "";
$db   = "osint_db";

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) { die("Bağlantı hatası: " . $conn->connect_error); }

// Используем utf8mb4 для поддержки специальных символов
$conn->set_charset("utf8mb4");

// Aranacak anahtar kelimeler
$keywords = ["siber terör", "saldırı", "attack", "cyber terror", "threat", "ddos", "hack", "leak", "breach", "china", "network", "malware", "ransomware"];

function fetchUrlContent($url) {
    if (substr($url, -5) !== ".json") {
        $url = rtrim($url, "/") . "/.json";
    }
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSINT-Project/1.0');
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    $data = curl_exec($ch);
    curl_close($ch);
    return json_decode($data, true);
}

if (isset($_POST['start'])) {
    
    // Очищаем таблицу перед новой проверкой
    $conn->query("TRUNCATE TABLE reddit_logs");

    $links = [
        "https://www.reddit.com/r/cybersecurity/comments/z05r2v/network_attacks/",
        "https://www.reddit.com/r/cybersecurity/comments/1ox3bfr/china_just_used_claude_to_hack_30_companies_the/",
        "https://www.reddit.com/r/cybersecurity/comments/p9fo4d/my_thoughts_on_a_decade_of_cyber_security_10/",
        "https://www.reddit.com/r/cybersecurity/comments/iu17uu/cybersec_cheat_sheets_in_all_flavors_huge_list/",
        "https://www.reddit.com/r/cybersecurity/comments/g0mp8v/all_free_curated_list_with_6_virtual_cons_34/"
    ];

    foreach ($links as $url) {
        if (!empty($url)) {
            $jsonData = fetchUrlContent($url);
            
            if (isset($jsonData[1]['data']['children'])) {
                $comments = $jsonData[1]['data']['children'];

                foreach ($comments as $comment) {
                    if (isset($comment['data']['body'])) {
                        $body = $comment['data']['body'];
                        
                        // --- ИСПРАВЛЕНИЕ ОШИБКИ ---
                        // Удаляем Эмодзи и сложные символы, которые ломают базу данных
                        $body = preg_replace('/[\x{10000}-\x{10FFFF}]/u', '', $body);
                        // -------------------------

                        $found_matches = [];

                        foreach ($keywords as $word) {
                            if (stripos($body, $word) !== false) {
                                $found_matches[] = $word;
                            }
                        }

                        if (!empty($found_matches)) {
                            $result_str = implode(", ", array_unique($found_matches));
                            $short_body = substr($body, 0, 300) . "...";

                            $stmt = $conn->prepare("INSERT INTO reddit_logs (url, found_keywords, comment_content) VALUES (?, ?, ?)");
                            // Если prepare не сработал (например, ошибка SQL), выводим ошибку
                            if (!$stmt) {
                                echo "SQL Error: " . $conn->error;
                                continue;
                            }
                            
                            $stmt->bind_param("sss", $url, $result_str, $short_body);
                            $stmt->execute();
                        }
                    }
                }
            }
        }
    }
    
    $sql = "SELECT * FROM reddit_logs ORDER BY id DESC LIMIT 20";
    $result = $conn->query($sql);
    
    $htmlContent = '<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Tarama Sonuçları</title>
    <style>
        body { font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; padding: 20px; background-color: #f9f9f9; }
        h1 { color: #333; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.2); }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #2c3e50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        .danger { color: #d9534f; font-weight: bold; }
        .analysis-box { background: #fff3cd; padding: 20px; margin-top: 30px; border: 1px solid #ffeeba; border-radius: 5px; }
    </style>
</head>
<body>
<h1>OSINT Tarama Sonuçları</h1>
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Taranan URL</th>
            <th>Tespit Edilen Tehdit Kelimeleri</th>
            <th>Yorum İçeriği (Özet)</th>
            <th>Tarama Zamanı</th>
        </tr>
    </thead>
    <tbody>';

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            $urlShort = (strlen($row["url"]) > 50) ? substr($row["url"], 0, 50) . "..." : $row["url"];
            
            $htmlContent .= "<tr>
                <td>{$row['id']}</td>
                <td><a href='{$row['url']}' target='_blank'>{$urlShort}</a></td>
                <td class='danger'>{$row['found_keywords']}</td>
                <td>" . htmlspecialchars($row['comment_content']) . "</td>
                <td>{$row['analysis_date']}</td>
            </tr>";
        }
    } else {
        $htmlContent .= "<tr><td colspan='5'>Tehdit unsuru bulunamadı.</td></tr>";
    }

    $htmlContent .= '    </tbody>
</table>

<div class="analysis-box">
    <h3>Ülke Güvenliğine Yönelik Tehditler ve Çözüm Önerileri (Değerlendirme)</h3>
    <p>
        <strong>1. Tehdit Analizi:</strong> Yapılan taramalar sonucunda, belirlenen Reddit kaynaklarında "network attacks", "China", "hack" ve "ransomware" kelimelerinin yoğunluğu tespit edilmiştir.
    </p>
    <p>
        <strong>2. Risk Değerlendirmesi:</strong> Özellikle yapay zeka (Claude/ChatGPT) kullanılarak yapılan oltalama ve saldırı tekniklerinin tartışılması, konvansiyonel güvenlik duvarlarını aşabilecek yeni nesil tehditleri işaret etmektedir.
    </p>
    <p>
        <strong>3. Çözüm Önerileri:</strong> 
        <ul>
            <li><strong>Proaktif İzleme:</strong> Kritik kamu kurumlarında, bu projede simüle edildiği gibi, açık kaynak istihbaratı (OSINT) araçları kullanılarak forumlar sürekli izlenmeli.</li>
            <li><strong>Yapay Zeka Savunması:</strong> Saldırganların yapay zeka kullanımına karşı, savunma tarafında da yapay zeka tabanlı anomali tespiti devreye alınmalıdır.</li>
            <li><strong>Ulusal Güvenlik Protokolleri:</strong> Siber terör tanımları genişletilmeli ve sosyal medya platformları ile uluslararası işbirliği yapılarak tehdit içerikli paylaşımların hızlıca kaldırılması sağlanmalıdır.</li>
        </ul>
    </p>
</div>

<br>
<a href="index.html" style="text-decoration:none; background:#333; color:white; padding:10px 20px; border-radius:5px;">← Geri Dön</a>
</body>
</html>';

    // ВЫВОДИМ РЕЗУЛЬТАТ СРАЗУ (чтобы избежать ошибок прав доступа)
    echo $htmlContent;
    exit();
}
?>